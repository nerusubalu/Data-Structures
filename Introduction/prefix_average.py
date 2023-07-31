'''
Write a program to calculate the prefix average
Eg: 
[1,2,3,4,5]
[1, 3, 6, 10, 15]

We can use the same logic to solve prefix sum
'''

#O(n^2) Solution
def prefix_average(arr):
    n = len(arr)
    sum_list = []
    for i in range(n):
        temp = 0
        for j in range(i+1):
            temp+=arr[j]
        sum_list.append(temp/(i+1))
    
    return sum_list

#O(n) Solution
def prefix_average_v2(arr):
    n = len(arr)
    sum_list = []
    sum = 0
    for i in range(n):
        sum+=arr[i]
        sum_list.append(sum/(i+1))

    return sum_list

arr = [1,2,3,4,5]
print(prefix_average_v2(arr))