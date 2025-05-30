from typing import Optional


class solution:
    '''
    Technique : Brute force
    Time Complexity : O(n*2)
    Space Complexity :O(1)
    Remarks: Not an efficent method it will work
    '''
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev
    

    '''
    Technique : Brute force
    Time Complexity : O(n*2)
    Space Complexity :O(1)
    Remarks: Not an efficent method it will work
    '''    
    def reverseLinkedListRC(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        nhead = head
        if head.next:
            nhead = self.reverseLinkedListRC(head.next)
            head.next.next = head
        head.next = None





if __name__ =="__main__":
    head = [0,1,2,3,4,5]
    list_ouput = solution.reverseLinkedList(head)
    print(list_ouput)
 