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

if __name__ == '__main__':
    bubbleSortTest()
    shortBubbleSortTest()
    selectSortTest()
    insertSortTest()