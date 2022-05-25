# Forward Kinematics-SMMV
 To find HTM and Position Vector

 Property From Aaron Joshua M. Apolonia
 
 HTM = 
[[ 0.242  0.707  0.664 62.831]
 [ 0.242 -0.707  0.664 62.831]
 [ 0.94   0.    -0.342 20.226]
 [ 0.     0.     0.     1.   ]]
Position Vector
X = 62.831
Y = 62.831
Z = 20.226
 
 In RTB:
 ┏━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━┓
┃   θⱼ     ┃     dⱼ     ┃  aⱼ  ┃  ⍺ⱼ   ┃   q⁻   ┃  q⁺   ┃
┣━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━╋━━━━━━━╋━━━━━━━━╋━━━━━━━┫
┃ q1       ┃       0.01 ┃    0 ┃ 90.0° ┃ -90.0° ┃ 90.0° ┃
┃ q2 + 90° ┃          0 ┃ 0.04 ┃ 90.0° ┃ -90.0° ┃ 90.0° ┃
┃0.0°      ┃  q3 + 0.04 ┃    0 ┃  0.0° ┃    0.0 ┃  0.04 ┃
┗━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━━━┻━━━━━━━┻━━━━━━━━┻━━━━━━━┛

Forward Kinematics =
   0.2418    0.7071    0.6645    26.61
   0.2418   -0.7071    0.6645    26.61
   0.9397    0        -0.342    -13.65
   0         0         0         1
 
 Robotics Toolbox Python
![FK_SMMV](https://user-images.githubusercontent.com/57609815/170194847-7743b63e-1208-4f8a-a41e-d8a43f76f4e3.jpg)

Robotics Toolbox Matlab

![Spherical Manipulator Modern Variant Inverse](https://user-images.githubusercontent.com/104018603/170195661-e676672d-885d-4038-bbfa-6651d421a561.png)
