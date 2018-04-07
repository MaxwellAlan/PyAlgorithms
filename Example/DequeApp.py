from DataStructure.PyDeque import Deque

# Eg1:回文检查
def palchecker(cString):
    chardeque = Deque()

    for c in cString:
        chardeque.addFront(c)

    result = True

    while chardeque.size() >= 2 and result:
        if chardeque.removeFront() != chardeque.removeRear():
            result = False

    return result

if __name__ == '__main__':
    print(palchecker("abcdedcba"))
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))