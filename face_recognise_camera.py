from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--haar-cascade", required=True,
        help = "path to where the face cascade resides")
    parser.add_argument("-f", "--face-encodings", required=True,
        help="path to serialized db of facial encodings")
    args = vars(parser.parse_args())

    haar_cascade_path = args["haar_cascade"]
    face_encodings_filepath = args["face_encodings"]

    # Load the known faces and embeddings along with OpenCV's Haar
    # cascade classifier for face detection
    binary_data = None
    with open(face_encodings_filepath, "rb") as file:
        binary_data = file.read()
    data = pickle.loads(binary_data)

    classifier = cv2.CascadeClassifier(haar_cascade_path)

    # Initialize the video stream and allow the camera sensor to warm up
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    while True:
        # Get frame from camera stream
        image = vs.read()
        image = imutils.resize(image, width=500)

        # Convert the input image from  BGR to grayscale (for face detection - Haar cascade classifier)
        # and from BGR to RGB (for face recognition - face_recognition package)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect faces in the grayscale image using Haar cascade classifier
        locations = classifier.detectMultiScale(gray_image, scaleFactor=1.1,
                                                minNeighbors=5, minSize=(30, 30),
                                                flags=cv2.CASCADE_SCALE_IMAGE)

        # Translate OpenCV coordinates from (x, y, w, h) to (top, right, bottom, left)
        # Translation formula: (top, right, bottom, left) = (y, x + w, y + h, x)
        face_locations = [(y, x + w, y + h, x) for (x, y, w, h) in locations]

        # Compute the facial embeddings for each face using translated coordinates and
        # RGB image. Be aware that face_recognition.face_encodings() function returns
        # returns a list!
        face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

        names = []
        # Loop over the facial embeddings
        for face_encoding in face_encodings:
            # Attempt to match each face in the input image to our known encodings
            known_encodings = data["encodings"]
            matches = face_recognition.compare_faces(known_encodings, face_encoding)

            # Find the indexes of all matched faces then count how many times each person was matched
            # to detected face - assign their name to the face. If nothing was matched, assign "unknown"
            # to the face.
            recognized_name = "unknown"
            if True in matches:
                known_faces = data["names"]
                matched_faces = {}
                index = 0
                for match in matches:
                    if match:
                        name = known_faces[index]
                        matched_faces[name] = matched_faces.get(name, 0) + 1
                    index += 1
                recognized_name = max(matched_faces, key=matched_faces.get)

            names.append(recognized_name)

        # Loop over the recognized faces
        # 'face_encodings' are locations of faces detected by Haar classifier and translated
        # to different format and names are the corresponding names assigned in the previous step
        for ((top, right, bottom, left), name) in zip(face_locations, names):
            # Draw rectangles around the detected faces and display a person's name
            cv2.rectangle(image, (left, top), (right, bottom),
                          (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.75, (0, 255, 0), 2)

        # Display the image to the screen
        cv2.imshow("image", image)
        key_pressed = cv2.waitKey(1)

        # If any key was pressed, break from the loop
        if key_pressed != -1:
            break

    # Clean up after script
    cv2.destroyAllWindows()
    vs.stop()
