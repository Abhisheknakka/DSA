#delete element

def delete_element(arr,value):
    arr.remove(value)
    return arr

myarr = [1, 2, 3, 4, 5]
print(delete_element(myarr, 3))


# traversal in array

def traversal_array(arr):
    for num in arr:
        print(num)

    return arr

print(traversal_array(myarr))

