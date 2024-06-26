# array operations

import array

arr1 = array.array('i',[1,2,3])
print(arr1)


for i in range (0, 3):
    print (arr1[i], end=" ")
print("\r")

 
# using append() to insert new value at end
arr1.append(43);
 
# printing appended array
print("The appended array is : ", end="")
for i in range (len(arr1)):
    print (arr1[i], end=" ")


#######

import array

arr2= array.array('i',[1,2,3,4,5])
print(arr2)
