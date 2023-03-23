#binary search


# print("enter the elements of the list")
# arr =list(map(int,input().split()))
# for i in range(0,len(arr)):
#     for j in range(i+1):
#         if arr[i] < arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
# print(arr)
# print("enter the input number:")
# x =int(input())
# m={}
# low = 0
# high = len(arr) - 1
# mid = 0
# if x in arr:
#     for i in range(len(arr)):
#         mid = (low + high) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             result=mid
#     print("Element is present at index", str(result))
# else:
#     for i in arr:
#         y = abs(float(x) - float(i))
#         m.update({y: i})
#         z = [v for k, v in m.items() if k == min(m.keys())]
#         ab=(z[0])
#     print("the closest index,number is:",arr.index(ab),",",ab)