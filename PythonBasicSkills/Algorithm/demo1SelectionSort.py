#选择排序 的思路
'''
1、首先在未排序中找到最小元素，存放到排序序列的起始位置，然后，
再从剩余未排序元素中寻找最二小元素，然后放到排序的第二个位置
'''
arr = [12,45,67,3,5,9,10,23,90,78]
for t in range(len(arr)-1):
    for j in range(t+1,len(arr)):
        if(arr[j] < arr[t]):
            swap = arr[t]
            arr[t] = arr[j]
            arr[j] = swap
    print(arr)

