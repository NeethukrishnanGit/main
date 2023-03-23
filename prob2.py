"""
Pseudocode:
* In this we do two functions one is for accessing the ascii values and other for accessing the string characters
* First create an empty dictionaru
* Implement for loop for accessing the number. Inside it give chr function and update the numbers and characters to the
dictionary
* Input the string and create a empty list for storing the numbers
* Implement for loop for accessing the string and inside it access through the dictionary and add the numbers to the
list
* Display the output
"""
y={}
for i in range(123):
    ab=chr(i)
    y.update({ab:i})
a=input("Enter the String: ")
b=[]
for j in a:
    x=y[j]
    b.append(x)
print(b)



