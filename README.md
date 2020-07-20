# Info
**Bezier-Decay is a package for quickly creating and implementing complex decay curves.** This package can easily be implemented into any existing code that is using python 3.6 or newer and is very lightweight since it is based on complex mathematical equation rather than loops. There are domain restrictions because of this so not all curves will work, but most should work fine and will run quickly even on slower machines.

# Installation
Copy and paste the following command into the shell
```
pip install --upgrade git+https://github.com/schaall/Bezier-Decay.git
```
# Usage
The default initialization of the bezier curve assumes that all inputs will be in the range of 0-1, so the first step is to initialize the decay curve based on how many steps will be taken.
```
from bezier_decay import bezier_curve

total_steps = 100
decay_curve = bezier_curve(final_x=total_steps)
 ```

Then to confirm that the curve is correct, a graph can be created to visualize it.
```
decay_curve.graph()
```

Then the loop can be created and when given the current step the value at that step will be returned.
```
for step in range(total_steps+1):
 current_val = decay_curve(step)
```

If the default curve is not the desired curve it can be changed by modifying the x_1, y_1, x_2, and y_2 values.
```
x_1 = 0.275
y_1 = 0.1
x_2 = 0.5
y_2 = 0.001
```
By default an adaptive mode is turned on which automatically scales the x_1 - y_2 values based on the staring x and ys and final x and ys. So if changes to the x_1 - y_2 values are undesired the this mode can be toggled off.
```
# Adaptive mode on implementation (given x_1 - y_2s above)
steps = 1000
decay_curve = bezier_curve(x_1=x_1, y_1=y_1, x_2=x_2, y_2=y_2, final_x=steps)

for step in range(steps+1):
 current_val = decay_curve(step)
 
# Adaptive mode off implementation (given x_1 - y_2s above)
steps = 1000
decay_curve = bezier_curve(x_1=x_1*steps, y_1=y_1, x_2=x_2*steps, y_2=y_2, final_x=steps)

for step in range(steps+1):
 current_val = decay_curve(step)
 
# or

steps = 1000
decay_curve = bezier_curve(x_1=x_1, y_1=y_1, x_2=x_2, y_2=y_2, final_x=steps)

for step in range(steps+1):
 current_val = decay_curve(step/steps)
```

For an interactive curve visit https://www.desmos.com/calculator/cd99jvsggg. Once the desired curve has been created then input the values on the left side of the screen.
```
x_0 = 0 # Staring x
y_0 = 1 # Staring y
x_1 = 0.275
y_1 = 0.1
x_2 = 0.5
y_2 = 0.001
x_3 = 1 # Final x
y_3 = 0.001 # Final y

curve = bezier_curve(x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3, adaptive=False)
```
