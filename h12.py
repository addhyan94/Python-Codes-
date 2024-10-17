# Flow control ke liye ....
'''
Write a python program to take coordinates of a point as input and determine its 
quadrant.
'''
a = eval(input("Enter the x-coordinate: "))
b = eval(input("Enter the y-coordinate: "))
if a > 0 and b > 0:
    print("The point lies in the First quadrant.")
elif a < 0 and b > 0:
    print("The point lies in the Second quadrant.")
elif a < 0 and b < 0:
    print("The point lies in the Third quadrant.")
elif a > 0 and b < 0:
    print("The point lies in the Fourth quadrant.")
elif a == 0 and b > 0:
    print("The point lies on the y-axis.")
elif b == 0 and a > 0:
    print("The point lies on the x-axis.")
else:
    print("tu pagal hai aache se dal na kya kar raha hai be tu..........")
