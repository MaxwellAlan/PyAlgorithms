from DataStructure.PyStack import Stack

#简单括号匹配
def parMatch(inputString):
    index=0
    s=Stack()
    balance=True
    while index<len(inputString) and balance:
        symbol = inputString[index]
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.is_empty():
                balance=False
            else:
                s.pop()
        index += 1
    if balance and s.is_empty():
        return True
    else:
        return False

# print(parMatch('(()()()()'))

def comParMatch(inputString):
    s=Stack()
    index=0
    balance=True
    while index<len(inputString) and balance:
        symbol=inputString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balance=False
            else:
                symbol2=s.pop()
                if not match(symbol,symbol2):
                    balance=False
        index +=1
    if balance and s.is_empty():
        return True
    else:
        return False

#比较下标是否相等
def match(symbol1,symbol2):
    open='([{'
    close=')]}'
    return open.index(symbol1) == close.index(symbol2)


#十进制转二进制
def divideBy2(decNumber):
    s=Stack()
    temp=decNumber
    while temp!=0:
        s.push(temp%2)
        temp=temp//2
    binNum=''
    while not s.is_empty():
        binNum=binNum+str(s.pop())

    return binNum

#扩展：除任意基数
def baseConverter(decNumber,base):
    s=Stack()
    digits="0123456789ABCDEF"

    temp=decNumber
    while temp>0:
        s.push(temp%base)
        temp=temp//base
    baseNum=''
    while not s.is_empty():
        baseNum+=digits[s.pop()]
    return baseNum



if __name__ == '__main__':
    print(divideBy2(233))
    print(baseConverter(25,16))