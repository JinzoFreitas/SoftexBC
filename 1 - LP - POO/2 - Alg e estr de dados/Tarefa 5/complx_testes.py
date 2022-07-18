#
#

class complx:
  def __init__(self, real=0, imag=0, value=0):
    self.real = real
    self.imag = imag
    self.value = (real + imag*1j)
      
n1 = complx(1,1)
n2 = complx(2,1)

help(complex)
