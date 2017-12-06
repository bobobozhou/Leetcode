# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):

    cur = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next

        cur = cur.next
    return head






h = ListNode(1)
h.next = ListNode(1)
h.next.next = ListNode(2)
h.next.next.next = ListNode(2)
h.next.next.next.next = ListNode(3)
print (deleteDuplicates(h).next.next.val)