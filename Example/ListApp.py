from DataStructure.PyList import UnorderedList,OrderedList

if __name__ == '__main__':
    #UnorderedList Test
    # uList = UnorderedList()
    #
    # uList.add(10)
    # uList.add(11)
    # uList.add(13)
    # uList.add(14)
    # uList.add(15)
    # uList.add(16)
    # uList.add(17)
    # uList.add(18)
    # uList.add("a")
    # uList.add("b")
    #
    # print(uList)
    # print(uList.isEmpty())
    # print(uList.size())
    # uList.remove(15)
    # print(uList)
    # print(uList.index(11))
    # print(uList.search('a'))
    # print(uList.search(15))
    # uList.append(15)
    # print(uList)
    # uList.insert(0,"c")
    # print(uList)
    # uList.pop()
    # print(uList)
    # uList.pop(1)
    # print(uList)

    # OrderedList Test
    uList = OrderedList()

    uList.add(10)
    uList.add(11)
    uList.add(13)
    uList.add(14)
    uList.add(15)
    uList.add(6)
    uList.add(17)
    uList.add(18)

    print(uList)
    print(uList.isEmpty())
    print(uList.size())
    uList.remove(15)
    print(uList)
    print(uList.index(6))
    print(uList.search(17))
    print(uList)
    uList.pop()
    print(uList)
    uList.pop(0)
    print(uList)

    '''
    线性数据结构以有序的方式保存它们的数据。
    栈是维持 LIFO，后进先出，排序的简单数据结构。
    栈的基本操作是 push，pop和 isEmpty。
    队列是维护 FIFO（先进先出）排序的简单数据结构。
    队列的基本操作是 enqueue，dequeue 和 isEmpty。
    前缀，中缀和后缀都是写表达式的方法。
    栈对于设计计算解析表达式算法非常有用。
    栈可以提供反转特性。
    队列可以帮助构建定时仿真。
    模拟使用随机数生成器来创建真实情况，并帮助我们回答“假设”类型的问题。
    Deques 是允许类似栈和队列的混合行为的数据结构。
    deque 的基本操作是 addFront，addRear，removeFront，removeRear 和 isEmpty。
    列表是项的集合，其中每个项目保存相对位置。
    链表实现保持逻辑顺序，而不需要物理存储要求。
    修改链表头是一种特殊情况。
    '''