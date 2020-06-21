# 冒泡算法：每次把最小（或最大）值放在一端,时间复杂度：n！
# 第一步：
# 把alist[0],alist[1]比较，进行由小到大排序；
# 把alist[1],alist[2]比较，进行由小到大排序；
# 。。。
# 把alist[n-2],alist[n-1]比较，进行由小到大排序。到此，alist[n-1]为最大值，位于末端。比较n-1次
# 第二步：
# 把alist[0],alist[1]比较，进行由小到大排序；
# 把alist[1],alist[2]比较，进行由小到大排序；
# 。。。
# 把alist[n-3],alist[n-2]比较，进行由小到大排序。到此，alist[n-2]为次大值。比较n-2次
# 一共进行n-1步，完成排序。


def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


# if __name__ == '__main__':
#     alist = [1, 5, 3, 8, 4, 5]
#     bubble_sort(alist)
#     print(alist)


# 选择排序：
# 选择并定位数列最小值，放在alist[0]处（即与alist[0]互换）；（注意要定位最小值在列表中的下标）
# 选择alist[1]到alist[n-1]并定位最小值，与alist[1]互换；
# 。。。
# 选择alist[n-2]到alist[n-1]并定位最小值，与alist[n-2]互换.到此完成排序。
# 选择并定位数列最小值选择方法：将数列alist[0]与alist[1]比较，定位较小值索引min_index，用min_index先后与alist[2]。。。alist[n-1]比较，每次重新将较小值的下标重新命名为min_index。


def select_sort(alist):
    n = len(alist)
    for j in range(0, n-1):
        min_index = j                              # 此步骤很重要，每次重头排序要把min_index命名为j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[min_index], alist[j] = alist[j], alist[min_index]


# if __name__ == '__main__':
#     alist = [1, 5, 3, 8, 4, 5]
#     select_sort(alist)
#     print(alist)


# 插入算法：数列第一个元素为有序部分，依次把后面无序部分的元素插入前面有序的数列。
# 首先，alist[0]为有序数列；alist[1]。。。alist[n-1]为无序数列
# 将alist[1]与前面有序数列alist[0]比较，
# 将alist[2]与前面有序数列alist[1]，alist[0]比较，
# 将alist[3]与前面有序数列alist[2]，alist[1]，alist[0]比较，
# 。。。
# 将alist[n-1]与前面有序数列alist[n-2]，alist[n-1]。。。alist[0]比较
# 到此，排序完成。


def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        for i in range(j-1, -1, -1):         # i从大到小变化
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
                j = j-1                       # 注意j往前挪


# if __name__ == '__main__':
#     alist = [1, 5, 3, 8, 4, 5]
#     insert_sort(alist)
#     print(alist)


# 希尔排序：类似插入排序。定义一个gap，根据gap分成几个数列。
# 然后对每个数列进行插入排序。最后不断缩小gap。
def shell_sort(alist):
    n = len(alist)
    gap = n//2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:         # i从大到小变化
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i = i-gap                      # 注意j往前挪
                else:
                    break
        gap //= 2


# if __name__ == '__main__':
#     alist = [1, 5, 3, 8, 4, 5]
#     shell_sort(alist)
#     print(alist)


# 快速排序：首先定义alist[0]为min_value，指针low指向alist[1]并向右移动，指针high指向alist[n-1]并向左移动。
# 当low指向元素大于min_value，停下让high移动，当high指向元素小于min_value停下，俩元素互换，并继续移动。
# 直至low与high指针相遇，则该位置为min_value位置。
# 对min_value左侧右侧数列执行相同过程。


def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while alist[high] >= mid_value and low < high:
            high = high - 1
        alist[low] = alist[high]
        while alist[low] <= mid_value and low < high:
            low = low + 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


# if __name__ == '__main__':
#     alist = [1, 5, 3, 8, 4, 5]
#     n = len(alist)
#     quick_sort(alist, 0, n-1)
#     print(alist)


# 归并算法：把整个数列对半拆分，继续对半拆分。。。一直拆到都是一个元素
# 对相邻俩元素进行排序，得到两两有序数列，一共n/2个数列
# 对相邻两数列合并，得到n/4个有序数列。。。得到有序数列
# ##相邻两数列left和right合并方式：
# left[0]与right[0]比较（指针均指向0），将较小值放入新的结果数列，然后指针向后移，直到指针移到最右端。


def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    left_index = 0
    right_index = 0
    result = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index +=1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result


if __name__ == '__main__':
    alist = [1, 5, 3, 8, 4, 5]
    print(merge_sort(alist))













