from typing import Optional


class ListNode:
    def __init__(self, val: int=0, next:'ListNode' = None):
        self.val = val
        self.next = next
    def _reper__(self):
        return f"{self.val} - > {self.next}" if self.next else f"{self.next}"


class solution:
    def mergesolution(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        temp = ListNode()
        tail = temp
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return temp.next

def build_list(val: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in val:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next



if __name__ == "__main__":
    list1 = [1,2,3,4]
    list2 = [1,1,4,5]
    ans = solution().mergesolution(list1,list2)
    print(ans)
