'''
删除链表的结点
请编写一个函数，使其可以删除某个链表中给定的（非末尾的）节点，您将只被给予要求被删除的节点。

比如：假设该链表为 1 -> 2 -> 3 -> 4  ，给定您的为该链表中值为 3 的第三个节点，那么在调用了您的函数之后，该链表则应变成 1 -> 2 -> 4 。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if not head:
        #     return None
        #
        # p = head
        # while p.next:
        #     if p.next.val == val:
        #         p.next = p.next.next
        #     else:
        #         p = p.next
        # return head.next if head.val == val else head

        if head == None:
            return head
        head.next = self.removeElements(head.next,val)
        if head.val == val:
            return head.next
        else:
            return head

if __name__ == '__main__':
    l0 = ListNode(0)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l62 = ListNode(6)
    l0.next = l1
    l1.next = l2
    l2.next = l6
    l6.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l62
    s = Solution()
    s.removeElements(l0,6)
