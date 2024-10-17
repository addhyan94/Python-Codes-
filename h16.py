# Flow control ke liye ....
'''
    Write a python program to find factorial of given number.
'''
n = eval(input("Enter a number: "))

factorial = 1
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        factorial = factorial*i
    print("The factorial of ",n," is=",factorial)
