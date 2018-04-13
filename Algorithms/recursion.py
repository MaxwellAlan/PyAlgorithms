# 递归
'''
1.递归算法必须具有基本情况。
2.递归算法必须改变其状态并向基本情况靠近。
3.递归算法必须以递归方式调用自身。
'''
# eg1:递归求和
def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0]+listsum(numlist[1:])

# eg2:进制转换
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

# eg3: 汉诺塔
def moveTower(height,fromPole,toPole,withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


# eg4：找零
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins


if __name__ == '__main__':
    # print(toStr(10,2))
    # moveTower(3,"A","B","C")
    # print(recMC([1,5,10,25],63))
    print(recDC([1,5,10,25],63,[0]*64))