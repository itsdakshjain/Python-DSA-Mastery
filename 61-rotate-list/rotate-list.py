class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        current_node = head
        list_size = 1
        
        while current_node.next:
            current_node = current_node.next
            list_size += 1
        
        last_node = current_node
        
        effective_rotations = k % list_size
        if effective_rotations == 0:
            return head
        
        last_node.next = head
        
        steps_to_new_tail = list_size - effective_rotations
        new_tail = head
        
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head