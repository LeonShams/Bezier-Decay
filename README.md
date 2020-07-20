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
from bezier_curve import bezier_curve

total_steps = 100

starting_val = 1 # Value returned at step 0
x_1 = # Point that defines shape of curve
x_2 = # Point that defines shape of curve
final_val = 0.1 # Value returned at final step

 bezier_curve = bezier_curve()
 ```
