'''

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = ListNode(0)
        head = res
        # 判断特殊情况
        if not l1:
            return l2
        if not l2:
            return l1

        while l1 or l2:
            if l1 and l2:
                temp = l1.val + l2.val + carry
                if temp > 9:
                    temp = temp - 10
                    carry = 1
                else:
                    carry = 0
                tmp = ListNode(temp)
                res.next = tmp
                l1 = l1.next
                l2 = l2.next
                res = res.next
            elif l1 and not l2:
                temp = l1.val + carry
                if temp > 9:
                    temp = temp - 10
                    carry = 1
                else:
                    carry = 0
                tmp = ListNode(temp)
                res.next = tmp
                l1 = l1.next
                res = res.next
            elif not l1 and l2:
                temp = l2.val + carry
                if temp > 9:
                    temp = temp - 10
                    carry = 1
                else:
                    carry = 0
                tmp = ListNode(temp)
                res.next = tmp
                l2 = l2.next
                res = res.next
        if carry > 0:
            res.next = ListNode(carry)
        return head.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    s = Solution()
    l3 = s.addTwoNumbers(l1,l2)
    while l3:
        print(l3.val)
        l3 = l3.next