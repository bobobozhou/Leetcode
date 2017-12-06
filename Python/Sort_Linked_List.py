# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def merge(h1, h2):
    if not h1 or not h2:
        return h2 or h1

    root = p = ListNode(0)
    while h1 and h2:
        if h1.val < h2.val:
            p.next = h1
            h1 = h1.next
            p = p.next
        else:
            p.next = h2
            h2 = h2.next
            p = p.next

    while h1:
        p.next = h1
        h1 = h1.next
        p = p.next

    while h2:
        p.next = h2
        h2 = h2.next
        p = p.next

    return root.next

def sortList(head):

    if not head or not head.next:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    head1 = head
    head2 = slow.next
    slow.next = None

    head1 = sortList(head1)
    head2 = sortList(head2)

    head = merge(head1, head2)

    return head



a = ListNode(2)
a.next = ListNode(1)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)

res = sortList(a)

c = 1