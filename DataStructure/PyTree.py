class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # 内部方法实现树的前序遍历
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

# 外部函数实现树的前序遍历
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    # 堆插入
    # 子结点与父结点交换
    def percUp(self,i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[i // 2]
                self.heaplist[i // 2] = tmp
            i = i // 2

    # 每次插入时在列表最后添加数据，之后进行堆的维护,保证父结点小于子结点
    def insert(self,k):
        self.heaplist.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # 删除元素
    # 为了维护堆顺序属性，我们所需要做的是将根节点和最小的子节点交换。
    # 在初始交换之后，我们可以将节点和其子节点重复交换，直到节点被交换到正确的位置，使它小于两个子节点。
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return  i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retual = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heaplist.pop()
        self.percDown(1)
        return retual

    # 构建二叉堆
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while(i > 0):
            self.percDown(i)
            i = i - 1



if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())