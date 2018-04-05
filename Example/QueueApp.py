from DataStructure.PyQueue import Queue
import random

# eg1:烫手山芋
def hotPotato(nameList,num):
    queue = Queue()
    for name in nameList:
        queue.enqueue(name)

    while queue.size()>1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()

# eg2:模拟打印机

'''
    打印机：
    1.打印机打印的速率
    2.当前任务
    3.当前任务完成还需多少时间
'''
class Printer:

    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    #当前任务时间完成时间
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    #开始新的任务，重新赋值timeRemaing
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

'''
    任务：
    1.创建的时间
    2.页数
    3.计算等待时间
'''
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime-self.timestamp

# 模拟打印机运行过程
def simulation(numSeconds,pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

#随机创建新任务
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False



if __name__ == '__main__':
    # print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],3))
    for i in range(10):
        simulation(3600,10)