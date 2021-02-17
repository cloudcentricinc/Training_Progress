# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    temp = ListNode(0)
    head = temp
    while l1 != None and l2 != None:
        print(l1.val)
        print(l2.val)
        if l1.val <= l2.val:
            temp.next = l1
            temp = temp.next
            l1 = l1.next
        else:
            temp.next = l2
            temp = temp.next
            l2 = l2.next
    if l1 == None:
        temp.next = l2
        return head.next
    if l2 == None:
        temp.next = l1
        return head.next


class Solution:
    pass
