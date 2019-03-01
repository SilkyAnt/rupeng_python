# 快速排序 的思路
# 1.选取一个数字座位基准，可选取末位数字
# 2.将数列第一位开始，依次与此数字比较，如果小于此数，将小数交换到左边，
# 最后达到小于基准数的在左边，大于基准数的在右边，分为两个数组
# 3.分别对两个数组重复上述步骤
import time

arr1 = [23, 45, 5, 67, 1, 3, 8, 10]


def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        fn(*args, **kwargs)
        print
        "%s cost %s second" % (fn.__name__, time.clock() - start)

    return _wrapper


# arr是数组，firstIndex是排序的第一个下标,lastIndex排序的最后一个下标
# 以最后的数值为基准，小的排在左边，大的排在右边
def Partition(arr, firstIndex, lastIndex):
    print("firstIndex", firstIndex, "lastindex", lastIndex)
    # 左边列表下标值的初始值
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        # 如果arr[j]下于基准，即最后一个值，即arr[j]要放在左边的序列
        if arr[j] < arr[lastIndex]:
            # 左边的下标值 ，用于存arr[j]
            i = i + 1
            # arr[j]和arr[i]交换 ，即j位置上的数放在i位置上，而原来i位置上的数放在j位置上
            arr[i], arr[j] = arr[j], arr[i]
            # 分组完毕以后，把最后基准数放在i位置上，原来i位置上的数放在最后
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i


@time_me
def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
    else:
        return


QuickSort(arr1, 0, len(arr1) - 1)
print(arr1)
