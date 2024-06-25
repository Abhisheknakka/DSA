# Q1- sum of array


arr = [1,2,3,4,5,6,7,8,9,10]

def sum_array(array):
    sum = 0
    for i in range(0,len(arr)):
        sum= sum+arr[i]
    return sum


print(sum_array(arr))
