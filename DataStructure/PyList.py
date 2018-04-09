class Node:

    def __init__(self,item):
        self.data = item
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,item):
        self.data = item

    def setNext(self,next):
        self.next = next

# 无序列表
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    # 假设所要删除的项存在
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # 第一项即为查找项
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self,item):
        current = self.head
        previous = None
        temp = Node(item)
        while current != None:
            previous = current
            current = current.getNext()
        previous.setNext(temp)

    def index(self,item):
        current = self.head
        index = 0
        while current != None:
            if current.getData() == item:
                return index
            else:
                index += 1
                current = current.getNext()
        return index

    def insert(self,pos,item):
        current = self.head
        index = 0
        temp = Node(item)
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            while index < pos - 1:
                current = current.getNext()
                index += 1
            temp.setNext(current.getNext())
            current.setNext(temp)

    def pop(self,pos = None):
        if pos == None:
            current = self.head
            previous = None
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            return current.getData()
        else:
            current = self.head
            index = 0
            previous = None
            if pos == 0:
                res = self.head.getData()
                self.head = current.getNext()
                return res
            else:
                while index < pos:
                    previous = current
                    current = current.getNext()
                    index += 1
                previous.setNext(current.getNext())
            return current.getData()


    def __str__(self):
        l = []
        current = self.head
        while current != None:
            l.append(current.getData())
            current = current.getNext()
        return str(l)


# 有序列表
class OrderedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def isEmpty(self):
        return self.head == None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        # 插入点在第一个位置时
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self,item):
        current = self.head
        previous = None
        stop = False
        found = False
        while current != None and not found and not stop:
            if current.getData() > item:
                stop = True
            else:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
        temp = Node(item)
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        pass

    def index(self,item):
        current = self.head
        index = 0
        while current != None:
            if current.getData() == item:
                return index
            else:
                index += 1
                current = current.getNext()
        return index


    def pop(self,pos=None):
        current = self.head
        previous = None
        if pos == None:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            return current.getData()
        else:
            if pos == 0:
                res = self.head.getData()
                self.head = current.getNext()
                return res
            index = 0
            while current != None and index < pos:
                previous = current
                current = current.getNext()
                index += 1
            previous.setNext(current.getNext())
            return current.getData()

    def __str__(self):
        l = []
        current = self.head
        while current != None:
            l.append(current.getData())
            current = current.getNext()
        return str(l)