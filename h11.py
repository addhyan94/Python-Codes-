# Flow control ke liye ....
'''
    Write a python program to find roots of quadratic equation ax2+bx+c=0.
root1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
root2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
'''
import math
a = eval(input("Enter the value of a: "))
b = eval(input("Enter the value of b: "))
c = eval(input("Enter the value of c: "))

d = b * b - 4 * a * c
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("The roots are real and different: ",root1, root2)
elif d == 0:
    root1 = root2 = -b / (2 * a)
    print("The roots are real and the same:",root1)
else:
    r = -b / (2 * a)
    i = math.sqrt(-d) / (2 * a)
    print("The roots are complex:",r,i)
