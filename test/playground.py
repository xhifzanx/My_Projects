array = []
n = int(input())
for i in range(0, n):
    ele = int(input())
    array.append(ele)
array2 = []
def operation1(arr):
    arr.remove(arr[0])
    return arr
def operation2(arr):
    for i in arr:
        array2.append(i / 2)
    return array2


if sum(array) % 2 == 0:
    result1 = operation1(array)
    result2 = operation2(array)
    print(result1)
    print(result2)
    if sum(result1) % 2 == 1:
        print(1)
    elif sum(result2) % 2 == 1:
        print(2)




