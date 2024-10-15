'''
Write a python program to find volume and surface area of cuboid.
v=l*b*h
sa=2*(l*b+b*h+h*l)

'''
l = float(input("Enter the length of the cuboid: "))
b= float(input("Enter the breadth of the cuboid: "))
h = float(input("Enter the height of the cuboid: "))

volume = l * b* h

surface_area = 2 * (l * b + b * h + h * l)

print("The volume of the cuboid =",volume)
print("The surface area of the cuboid =",surface_area)
