# Flow control ke liye ....
'''
Write a python program to compute gross salary based on following parameters:
Basic Salary  -    HRA     DA
1-4000        -    10%     50%
4001-8000     -    15%     60%
8001-12000     -   20%     70%
More than 12000 -   25%     80%
'''
salary = eval(input("Enter the salary= "))
if salary <= 4000:
    HRA = 0.10 * salary
    DA = 0.50 * salary
elif salary <= 8000:
    HRA = 0.15 * salary
    DA = 0.60 * salary
elif salary <= 12000:
    HRA = 0.20 * salary
    DA = 0.70 * salary
else:
    HRA = 0.25 * salary
    DA = 0.80 * salary
total = salary + HRA + DA

print("The gross salary is=",total)
