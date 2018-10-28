#冒泡排序 的思路
'''
外层循环 n 次，内层循环 n-1 次，相邻两个进行比较
'''
arr = [23,12,6,9,70,45,24,57,78,10]


for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

    print(arr)
