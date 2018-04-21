def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        #当列表本身是有序时提前终止
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i],alist[i+1] = alist[i+1],alist[i]
        passnum -= 1

# 选择排序：遍历时寻找最大值，最后进行交换
def selectSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionMax = 0
        for loaction in range(1,fillslot+1):
            if alist[loaction] > alist[positionMax]:
                positionMax = loaction
        alist[fillslot],alist[positionMax] = alist[positionMax],alist[fillslot]

def insertSort(alist):
    for index in range(1,len(alist)-1):
        for position in range(index,-1,-1):
            if alist[position] > alist[position+1]:
                alist[position],alist[position+1] = alist[position+1],alist[position]

def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentvalue

def mergeSort(alist):
    print('splitting',alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j <len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i <len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
        print("merging",alist)
def bubbleSortTest():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(alist)

def shortBubbleSortTest():
    alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    shortBubbleSort(alist)
    print(alist)

def selectSortTest():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectSort(alist)
    print(alist)

def insertSortTest():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertSort(alist)
    print(alist)

def shellSortTest():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    print(alist)

def mergeSortTest():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)

if __name__ == '__main__':
    # bubbleSortTest()
    # shortBubbleSortTest()
    # selectSortTest()
    # insertSortTest()
    # shellSortTest()
    mergeSortTest()