"""
Filename: FK_SMMV.py
Created on Wednesday 25/05/2022
Title: Forward Kinematics of Spherical Manipulator - Modern Variant
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
"""

import numpy as np
import math

a1 = float(10)
a2 = float(40)
a3 = float(40)
T1 = float(45)
T2 = float(-20)
d3 = float(40)

T1= (T1/180.0)*np.pi
T2 = (T2/180.0)*np.pi   

DHPT = [[T1, (90.0/180.0)*np.pi, 0, a1],
       [T2+(90.0/180.0)*np.pi, (90.0/180.0)*np.pi, a2, 0],
       [(0.0/180.0)*np.pi, (0.0/180.0)*np.pi,0, a3+d3]]

i = 0
H0_1 = [[np.cos(DHPT[i][0]),-np.sin(DHPT[i][0])*np.cos(DHPT[i][1]),np.sin(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.cos(DHPT[i][0])],
      [np.sin(DHPT[i][0]),np.cos(DHPT[i][0])*np.cos(DHPT[i][1]),-np.cos(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.sin(DHPT[i][0])],
      [0,np.sin(DHPT[i][1]),np.cos(DHPT[i][1]),DHPT[i][3]],
      [0,0,0,1]]

i = 1
H1_2 = [[np.cos(DHPT[i][0]),-np.sin(DHPT[i][0])*np.cos(DHPT[i][1]),np.sin(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.cos(DHPT[i][0])],
      [np.sin(DHPT[i][0]),np.cos(DHPT[i][0])*np.cos(DHPT[i][1]),-np.cos(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.sin(DHPT[i][0])],
      [0,np.sin(DHPT[i][1]),np.cos(DHPT[i][1]),DHPT[i][3]],
      [0,0,0,1]]

i = 2
H2_3 = [[np.cos(DHPT[i][0]),-np.sin(DHPT[i][0])*np.cos(DHPT[i][1]),np.sin(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.cos(DHPT[i][0])],
      [np.sin(DHPT[i][0]),np.cos(DHPT[i][0])*np.cos(DHPT[i][1]),-np.cos(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.sin(DHPT[i][0])],
      [0,np.sin(DHPT[i][1]),np.cos(DHPT[i][1]),DHPT[i][3]],
      [0,0,0,1]]

H0_1 = np.matrix(H0_1)
H1_2 = np.matrix(H1_2)
H2_3 = np.matrix(H2_3)
H0_2 = np.dot(H0_1, H1_2)
H0_3 = np.dot(H0_2, H2_3)

print("HTM = ")
print(np.matrix(np.around(
      H0_3,3)))

print("Position Vector")
X0_3 = H0_3[0,3]
print('X =',np.around(X0_3,3))

Y0_3 = H0_3[1,3]
print('Y =',np.around(Y0_3,3))

Z0_3 = H0_3[2,3]
print('Z =',np.around(Z0_3,3))