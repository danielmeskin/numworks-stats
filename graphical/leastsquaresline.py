from math import *
x=float(input("x-bar: "))
y=float(input("y-bar: "))
sx=float(input("Sx: "))
sy=float(input("Sy: "))
r=float(input("r: "))
b=((r*sy)/sx)
a=y-b*x
print("---")
print("a: "+str(a))
print("b: "+str(b))
