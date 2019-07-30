from math import pi
from math import sqrt
from math import pow

class Kwadrat :
  def __init__(self, bok) :
    self.bok = bok
  def obwod(self) :
    return 4*self.bok
  def pole(self) :
    return self.bok * self.bok
