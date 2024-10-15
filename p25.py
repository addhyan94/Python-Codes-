#WAP to check greatest number among three
a=eval(input("Enter first number=  "))
b=eval(input("Enter second number="))
c=eval(input("Enter Third number="))
if a>b and a>c:
    print(a,"Is a Greastest Number ")
elif b>c and b>a:
    print(b,"Is Greastest Number ")
else:
    print(c,"Is Greastest Number ")