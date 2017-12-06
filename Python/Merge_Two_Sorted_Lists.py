# def mergeTwoLists(l1, l2):
#
#     if not l1:
#         return l2
#
#     if not l2:
#         return l1
#
#     l = []
#     while l1 and l2:
#         if l1[0] < l2[0]:
#             l.append(l1.pop(0))
#         else:
#             l.append(l2.pop(0))
#     return l + l1 + l2


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):

    if not l1 or not l2:
        return l1 or l2

    cur = head = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next

        cur = cur.next
    cur.next = l1 or l2
    return head.next


l1 = ListNode(1)
l1.next = ListNode(3)

l2 = ListNode(2)
l2.next = ListNode(4)

a = mergeTwoLists(l1, l2)
print (a)