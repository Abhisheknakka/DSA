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

import array

def inArr(arr,n,x,pos):
    for i in range(n-1,pos-1,-1):
        arr[i+1]=arr[i]

    arr[pos]=x
