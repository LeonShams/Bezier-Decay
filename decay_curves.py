class BezierCurve:
  # Defines constants needed for the curve
  def __init__(self, x_0=0, y_0=1, x_1=0.216, y_1=0.3, x_2=0.335, y_2=0.1, x_3=1, y_3=0.001):
    self.x_0, self.y_0, self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3 = x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3

  # Does cube root in python
  def cube_root(self, val):
    if val >= 0:
      return val**(1/3)
    else:
      return -(abs(val)**(1/3))

  # Returns y based on x
  def __call__(self, x):
    # Equation for bezier curve broken up into parts
    square_rt = math.sqrt(4*(-9*self.x_1**2 + 9*self.x_2*self.x_1 + 9*self.x_3*self.x_1 - 9*self.x_2**2 + 9*self.x_0*self.x_2 - 9*self.x_0*self.x_3)**3 + 
                          (-54*self.x_1**3 + 243*x*self.x_1**2 + 81*self.x_2*self.x_1**2 - 162*self.x_3*self.x_1**2 + 81*self.x_2**2*self.x_1 - 162*x*self.x_0*self.x_1 - 
                           486*x*self.x_2*self.x_1 + 81*self.x_0*self.x_2*self.x_1 + 162*x*self.x_3*self.x_1 + 81*self.x_0*self.x_3*self.x_1 + 81*self.x_2*self.x_3*self.x_1 - 54*self.x_2**3 + 
                           27*x*self.x_0**2 + 243*x*self.x_2**2 - 162*self.x_0*self.x_2**2 + 27*x*self.x_3**2 - 27*self.x_0*self.x_3**2 + 162*x*self.x_0*self.x_2 - 27*self.x_0**2*self.x_3 - 
                           54*x*self.x_0*self.x_3 - 162*x*self.x_2*self.x_3 + 81*self.x_0*self.x_2*self.x_3)**2)

    cube_rt = self.cube_root(-54*self.x_1**3 + 243*x*self.x_1**2 + 81*self.x_2*self.x_1**2 - 162*self.x_3*self.x_1**2 + 81*self.x_2**2*self.x_1 - 162*x*self.x_0*self.x_1 - 
                       486*x*self.x_2*self.x_1 + 81*self.x_0*self.x_2*self.x_1 + 162*x*self.x_3*self.x_1 + 81*self.x_0*self.x_3*self.x_1 + 81*self.x_2*self.x_3*self.x_1 - 54*self.x_2**3 + 
                       27*x*self.x_0**2 + 243*x*self.x_2**2 - 162*self.x_0*self.x_2**2 + 27*x*self.x_3**2 - 27*self.x_0*self.x_3**2 + 162*x*self.x_0*self.x_2 - 
                       27*self.x_0**2*self.x_3 - 54*x*self.x_0*self.x_3 - 162*x*self.x_2*self.x_3 + 81*self.x_0*self.x_2*self.x_3 + square_rt)

    t = -(self.x_0 - 2*self.x_1 + self.x_2)/(-self.x_0 + 3*self.x_1 - 3*self.x_2 + self.x_3) + cube_rt/(3*self.cube_root(2)*(-self.x_0 + 3*self.x_1 - 3*self.x_2 + self.x_3)
      ) - (self.cube_root(2)*(-9*self.x_1**2 + 9*self.x_2*self.x_1 + 9*self.x_3*self.x_1 - 9*self.x_2**2 + 9*self.x_0*self.x_2 - 9*self.x_0*self.x_3))/(3*(-self.x_0 + 3*self.x_1 - 3*self.x_2 + self.x_3)*cube_rt)

    y = (1-t)*((1-t)*((1-t)*self.y_0+t*self.y_1)+t*((1-t)*self.y_1+t*self.y_2))+t*((1-t)*((1-t)*self.y_1+t*self.y_2)+t*((1-t)*self.y_2+t*self.y_3))

    return y
