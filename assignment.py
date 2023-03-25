dict1={"Hello": "world", 1:2}
dict2= {"zara": "john", "trisha": "sruthi"}
dict1.update(dict2)
dict3=dict([(value,key) for key,value in dict1.items()])
print(dict3)