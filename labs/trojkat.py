from math import pi
from math import sqrt
from math import pow

class Trojkat :
  def __init__(self,bok) :
    self.bok = bok
  def obwod(self) :
    return 3*self.bok
  def pole(self) :
    return pow(self.bok,2)*sqrt(3)/4
