#insert

import array

def insertElement(arr,ele,pos):
    if pos>= len(arr):
        return False
    else:
        arr.insert(pos,ele)

    return arr

myarr = [1,2,3,4,5]
num = 14
index=2

print(insertElement(myarr,num,index))
    


### methods 2

