# Flow control ke liye ....
'''
    Write a python program to calculate electricity bill based on following parameters:
      Units                      Bill/unit
      1-150                          2.40
   For next 151-300                  3.00
   For next more than 300            3.20
'''
units = eval(input("Enter the number of units consumed: "))

if units <= 150:
    bill = units * 2.40
elif units <= 300:
    bill = (150 * 2.40) + (units - 150) * 3.00
else:
    bill = (150 * 2.40) + (150 * 3.00) + (units - 300) * 3.20

print("The electricity bill is: ₹",bill)
