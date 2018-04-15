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

class HashTable:
    def __init__(self):
        self.size = 11 #一般用质素
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        hashvalue = self.hashfunc(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            #如果已经存在则替换
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
    def get(self,key):
        startslot = self.hashfunc(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key,value)

    def hashfunc(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

def listtest():
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))
    print("binary search")
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))

def hashtest():
    h = HashTable()
    h[54]="cat"
    h[26]="dog"
    h[93]="lion"
    h[17]="tiger"
    h[77]="bird"
    h[31]="cow"
    h[44]="goat"
    h[55]="pig"
    h[20]="chickent"
    print(h.slots)
    print(h.data)
    h[20]='duck'
    print(h.slots)
    print(h.data)

if __name__ == '__main__':
    # listtest()
    hashtest()
