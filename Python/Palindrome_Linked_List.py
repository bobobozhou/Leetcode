# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    val = []
    while head:
        val.append(head.val)
        head = head.next

    return val == val[::-1]

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(1)

print (isPalindrome(a))