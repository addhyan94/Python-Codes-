#EH
try:
 a=eval(input("Enter first number "))
 b=eval(input("Enter second number"))
 print("Add=",a+b)
 print("Sub..=",a-b)
 print("multiply=",a*b)
 print("Divide =",a//b)
except NameError:
 print(" Number print kar pagal Kuch bhi nahi dalna hai be aapan ko (-_-)......")
except ZeroDivisionError:
 print(" Kisi bhi number ko 0 se devide nahi kiya jata hai yr pagal ")
finally:
 print("Hum to aayegebaar baar baar tere pass khikhikhikhi......")