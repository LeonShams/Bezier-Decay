import matplotlib.pyplot as plt
import numpy as np

default_start_x = 0
default_start_y = 1
default_x_1 = 0.216
default_y_1 = 0.3
default_x_2 = 0.335
default_y_2 = 0.1
default_final_x = 1
default_final_y = 0.001

class BezierCurve:
  # Defines constants needed for the curve
  def __init__(self, 
               start_x=default_start_x, 
               start_y=default_start_y, 
               x_1=default_x_1, 
               y_1=default_y_1, 
               x_2=default_x_2, 
               y_2=default_y_2, 
               final_x=default_final_x, 
               final_y=default_final_y, 
               adaptive=True):
    
    if adaptive:
      if not start_x < final_x:
        raise ValueError("The starting x value must be less than the final x value when using adaptive mode.")
      if start_y < final_y:
        raise ValueError("The starting y value must be less than the final y value when using adaptive mode.")
      
      horizontal_shift = (start_x-default_start_x)/2 + (final_x-default_final_x)/2
      vertical_shift = (start_y-default_start_y)/2 + (final_y-default_final_y)/2
      
      self.x_0, self.y_0, self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3 = start_x, start_y, x_1+horizontal_shift, y_1+vertical_shift, x_2+horizontal_shift, y_2+vertical_shift, final_x, final_y
    else:
      self.x_0, self.y_0, self.x_1, self.y_1, self.x_2, self.y_2, self.x_3, self.y_3 = start_x, start_y, x_1, y_1, x_2, y_2, final_x, final_y

  # Does cube root in python
  def cube_root(self, val):
    if val >= 0:
      return val**(1/3)
    else:
      return -(abs(val)**(1/3))
    
  def get_y(self, x):
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

  # Returns y based on x
  def __call__(self, x):
    return self.get_y(x)
  
  # Graphs the bezier curve
  def graph(self, start=0, stop=1, smoothing=1_000):
    x = np.linspace(start, stop, num=smoothing)
    y = [get_y(i) for i in x]
    
    plt.plot(x, y)
    plt.show()
