# traversal

arr=[1,3,5,6,42,3]

def traversal(arrays):
    result = []
    for i in range(len(arrays)):
        result.append(arrays[i])
    return result

print(traversal(arr))


def trav(arrays):
    for i in range(len(arrays)):
        print(arrays[i])

trav(arr)

