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
        else:
            current = self.head
            index = 0
            previous = None
            if pos == 0:
                self.head = current.getNext()
            else:
                while index < pos:
                    previous = current
                    current = current.getNext()
                    index += 1
                previous.setNext(current.getNext())


    def __str__(self):
        l = []
        current = self.head
        while current != None:
            l.append(current.getData())
            current = current.getNext()
        return str(l)
