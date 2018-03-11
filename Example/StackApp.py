from DataStructure.PyStack import Stack

#括号匹配
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