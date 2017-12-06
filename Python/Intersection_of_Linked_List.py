# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):

    if not headA or not headB:
        return None

    pa = headA
    pb = headB

    while pa is not pb:
        if pa is None:
            pa = headB
        else:
            pa = pa.next

        if pb is None:
            pb = headA
        else:
            pb = pb.next

    return pa

