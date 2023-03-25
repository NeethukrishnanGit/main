# CODE FOR INPUT  STRING IS PALINDROM OR NOT

input_string=input("enter the string: \n")
reversed_string= input_string[::-1]
if input_string == reversed_string:
    print(f"the given string \"{input_string}\" is palindrom")
else:
    print(f"the given string \"{input_string}\" is not palindrom")

#CODE WHICH IS WRITTEN BY NEETHU MAM
dict1={"Hello": "world", 1:2}
dict2= {"zara": "john", "trisha": "sruthi"}
dict1.update(dict2)
dict3=dict([(value,key) for key,value in dict1.items()])
print(dict3)