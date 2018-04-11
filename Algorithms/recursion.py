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


if __name__ == '__main__':
    # print(toStr(10,2))
    moveTower(4,"A","B","C")