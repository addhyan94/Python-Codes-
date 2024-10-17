# Flow control ke liye ....
'''
Write a python program to print table of given number in given format:-
2*1=2
2*2=4
2*3=6
.
.
2*10=20
'''
number = eval(input("Enter the number: "))

for i in range(1, 11):
    result = number * i
    print(number,"*",i,"=",result)
