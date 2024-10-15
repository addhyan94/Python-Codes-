'''
Write a python program to find area and perimeter of circle.
area=3.14*r*r
perimeter=2*3.14*r
'''
r=eval(input("Enter R= "))
print("Press 1 for Area ")
print("Press 2 for perimeter ")
ch=eval(input())
if ch==1:
    area=3.14*r*r
    print("Area is =",area)
elif ch==2:
    perimeter=2*3.14*r
    print("perimeter is = ",perimeter)
else:
    print("ERROR :: Galat choice kiya hai be Pagal (- _ -) ")
    