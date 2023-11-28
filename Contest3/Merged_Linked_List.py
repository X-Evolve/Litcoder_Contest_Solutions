class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(headA, headB):
    dummy = ListNode()  
    current = dummy

    while headA is not None and headB is not None:
        if headA.val < headB.val:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next

        current = current.next

    if headA is not None:
        current.next = headA
    elif headB is not None:
        current.next = headB

    return dummy.next

def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

countA = int(input())
arrA = [int(input()) for _ in range(countA)]
countB = int(input())
arrB = [int(input()) for _ in range(countB)]

headA = ListNode(arrA[0])
currentA = headA
for val in arrA[1:]:
    currentA.next = ListNode(val)
    currentA = currentA.next

headB = ListNode(arrB[0])
currentB = headB
for val in arrB[1:]:
    currentB.next = ListNode(val)
    currentB = currentB.next

merged_head = merge_sorted_lists(headA, headB)
print()
print_list(merged_head)

