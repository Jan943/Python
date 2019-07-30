from math import pi
from math import sqrt
from math import pow

class Kolo :
  def __init__(self,promien) :
    self.promien = promien
  def obwod(self) :
    return 2*pi*self.promien
  def pole(self) :
    return pi*pow(self.promien,2) # self.promien**2
