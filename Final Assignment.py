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

# CODE FOR INPUT  NUMBER IS PRIME OR NOT
num = int(input("enter the number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Print odd and even number

# Print odd or even
n = int(input("enter number of elements: "))
numbers = [int(input(f"enter the number {i} : ")) for i in range(1, n + 1)]
odd = []
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"odd numbers: {odd}")
print(f"even numbers: {even}")



#factorial of a number
#by ajay
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#CODE FOR SUM OF TEN NUMBERS
a=[1,2,3,4,5,6,7,8,9,10]
total=sum(a)
print("sum of ten numbers",total)



