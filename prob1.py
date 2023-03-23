"""Pseudocode:
* Enter the list of numbers and sort the list
* Initialize low value as zero and high value as length minus one
* Enter the element to be searched
* Implement while loop and check if low value is less or equal to high value
 inside it give mid value as sum of lower and higher divided by two.
* check if searching element is equal to the mid value print the mid value
* And check if element is greater than the mid value change the low value by adding it with mid value else
change the high value by decrementing it by one
* If any of this is false print the current mid value
* Displays the index of the searched element
"""


lis_1=list(map(int,input("Enter the elements in the list: ").split(" ")))
for i in range(len(lis_1)):
    for j in range(i + 1, len(lis_1)):
        if lis_1[i] > lis_1[j]:
            lis_1[i], lis_1[j] = lis_1[j], lis_1[i]

print("Sorted list: ", lis_1)
low=0
high=len(lis_1)-1
element=int(input("Enter the element to search: "))
while low<=high:
    mid=(low+high)//2
    if lis_1[mid]==element:
        print(mid)
        break
    elif lis_1[mid]<element:
        low=mid+1
    else:
        high=mid-1
else:
        print("Not Found")
        print("index of closest element",mid)



