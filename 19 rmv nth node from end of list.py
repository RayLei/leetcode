# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    tmp1 = tmp2 = head

    # count the total nodes
    total_node = 0
    while head:
        total_node += 1
        head = head.next

    if total_node - n - 1 < 0:
        tmp2 = tmp2.next
    else:
        for i in range(total_node - n - 1):
            tmp2 = tmp2.next

        tmp2.next = tmp2.next.next
    return tmp1

head, n = [1], 1
removeNthFromEnd(head, n)
