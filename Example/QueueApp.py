from DataStructure.PyQueue import Queue

def hotPotato(nameList,num):
    queue = Queue()
    for name in nameList:
        queue.enqueue(name)

    while queue.size()>1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()


if __name__ == '__main__':
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],3))
