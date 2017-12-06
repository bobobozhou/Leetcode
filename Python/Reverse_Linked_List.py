# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # 3 pointers: prev, cur, cur.next and draw a long graph!!!!
    prev = None
    curr = head

    while curr is not None:
        tmp = curr.next
        curr.next = prev

        prev = curr
        curr = tmp

    return prev


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

res = reverseList(a)
