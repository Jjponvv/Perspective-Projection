# Perspective projection
<img src="img/Screenshot.png" alt="Screenshot" width="600">

## How it works?
In my project I used 5 functions: 
- 2D to 3D conversion
- rotate x, y, z
- drawing

## 2D to 3D conversion

For this function I used this formula:

`x / (z * tan(angle / 2))`
Where:
**x** - cordinate (I can use **y** also)
**z** - z cordinate
**angle** - it's a field of view (**FOV**)

**tan()** function is tangent

## rotating (**x**, **y** and **z**)

To rotate shapes in 3D space, I used a **rotation matrix**  
<img src="img/RotationMatrices.png" alt="matrix example">
