class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    flag = 0
    root = n = ListNode(0)

    while l1 or l2 or flag:
        v1 = v2 = 0

        if l1:
            v1 = l1.val
            l1 = l1.next

        if l2:
            v2 = l2.val
            l2 = l2.next

        flag, num = divmod(v1 + v2 + flag, 10)
        n.next = ListNode(num)
        n = n.next

    return root.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

k  = addTwoNumbers(l1, l2)
print (k.next.val)