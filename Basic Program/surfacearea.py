import math as m
r=float(input("enter radius"))
h=float(input("enter height"))
sur=2*m.pi*r*h+(m.pi*(r**2))*2
vol=m.pi*r*r*h
print("surface area ",sur)
print("volume ",vol)
