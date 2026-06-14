class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        max_sum = 0
        first_half = head
        second_half = prev
        
        while second_half:
            current_twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, current_twin_sum)
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum