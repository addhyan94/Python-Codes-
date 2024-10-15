'''
Write a python program to find simple interest.
si=(p*n*r)/100
'''
p= float(input("Enter the principal amount: "))
t = float(input("Enter the time period (in years): "))
r = float(input("Enter the rate of interest: "))

simple_interest = (p * t * r) / 100
print("The simple interest = ",simple_interest)