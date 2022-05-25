"""
Filename: FK_SMMV.py
Created on Wednesday 25/05/2022
Title: Forward Kinematics of Spherical Manipulator - MV - Robotics Toolbox
Author: Aaron Joshua M. Apolonia
Team: Group 12-Block C
"""
import roboticstoolbox as rtb
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3

a1 = float(input("a1 = ")) # For testing, 100 mm
a2 = float(input("a2 = ")) # For testing, 70 mm
a3 = float(input("a3 = ")) # For testing, 40 mm

def mm_to_meter(a):
    m = 1000
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)

lm = float(input("lm1 = "))
lm = mm_to_meter(lm)

Sphe_MV = DHRobot([
    RevoluteDH(a1,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a2,(90/180)*np.pi,(90/180)*np.pi,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    PrismaticDH(0,0,0,a3,qlim=[0,lm]),
], name='Spherical')

print(Sphe_MV)

T1 = float(input("T1 = ")) # For testing, -50 degrees
T2 = float(input("T2 = ")) # For testing, -20 degrees
d3 = float(input("d3 = ")) # For testing, 60mm

T1 = (T1/180.0)*np.pi # Theta 1 in radians
T2 = (T2/180.0)*np.pi # Theta 2 in radians

FK = Sphe_MV.fkine([T1,T2,d3])
print('Forward Kinematics = ')
print(FK)