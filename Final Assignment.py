""" This file contains contributions of members of the team and a practice to perform resolving conflicts"""

if __name__ == '__main__':
    print("Demo Program")

# CODE FOR INPUT  STRING IS PALINDROM OR NOT

input_string=input("enter the string: \n")
reversed_string= input_string[::-1]
if input_string == reversed_string:
    print(f"the given string \"{input_string}\" is palindrom")
else:
    print(f"the given string \"{input_string}\" is not palindrom")

#CODE FOR SUM OF TEN NUMBERS
a=[1,2,3,4,5,6,7,8,9,10]
total=sum(a)
print("sum of ten numbers",total)

#factorial of a number
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# Code for sum of 10 odd numbers
c = 0
for i in range(1, 20):
    if i % 2 != 0:
        c += i
print("Sum of first 10 odd number is ", c)
