# 顺序查找
def sequentialSearch(alist,item):
    index = 0
    found = False
    while index < len(alist) and not found:
        if alist[index] == item:
            found = True
        else:
            index += 1
    return found

def orderedSequentialSearch(alist,item):
    index = 0
    found = False
    stop = False
    while index < len(alist) and not found and not stop:
        if alist[index] == item:
            found = True
        else:
            if alist[index] > item:
                stop = True
            else:
                index += 1
    return found

# 二分查找
def binarySearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        mid = (first + last)//2
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
# 递归实现二分查找
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)


if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))
    print("binary search")
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
