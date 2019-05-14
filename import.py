# Basics of importing modules into your file.

You want to calculate sin(5) + cos(90) * tan(2)

# Lesson 1
import math

math.sin(5) + math.cos(90) * math.tan(2)

# Lesson 2
import math

sin = math.sin
cos = math.cos
tan = math.tan

sin(5) + cos(90) * tan(2)

# Lesson 3
from math import sin, cos, tan 


sin(5) + cos(90) * tan(2)
