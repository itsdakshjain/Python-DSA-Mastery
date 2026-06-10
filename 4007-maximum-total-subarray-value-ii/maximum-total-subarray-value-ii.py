class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        def count_valid(X):
            total_count = 0
            max_q = deque()
            min_q = deque()
            left = 0
            
            for right in range(n):
                while max_q and nums[max_q[-1]] <= nums[right]:
                    max_q.pop()
                max_q.append(right)
                
                while min_q and nums[min_q[-1]] >= nums[right]:
                    min_q.pop()
                min_q.append(right)
                
                while max_q and min_q and (nums[max_q[0]] - nums[min_q[0]] >= X):
                    if max_q[0] == left:
                        max_q.popleft()
                    if min_q[0] == left:
                        min_q.popleft()
                    left += 1
                total_count += left
            return total_count

        low, high = 0, max(nums) - min(nums)
        threshold_X = 0
        
        while low <= high:
            mid = (low + high) // 2
            if count_valid(mid) >= k:
                threshold_X = mid
                low = mid + 1
            else:
                high = mid - 1
                
        total_ans = 0
        items_added = 0
        
        max_q, min_q = deque(), deque()
        left = 0
        
        for right in range(n):
            while max_q and nums[max_q[-1]] <= nums[right]: 
                max_q.pop()
            max_q.append(right)
            while min_q and nums[min_q[-1]] >= nums[right]: 
                min_q.pop()
            min_q.append(right)
            
            while max_q and min_q and (nums[max_q[0]] - nums[min_q[0]] >= threshold_X + 1):
                if max_q[0] == left: 
                    max_q.popleft()
                if min_q[0] == left: 
                    min_q.popleft()
                left += 1
            
            if left > 0:
                current_max_q = deque()
                current_min_q = deque()
                l_ptr = 0
                
                for r_ptr in range(right + 1):
                    while current_max_q and nums[current_max_q[-1]] <= nums[r_ptr]:
                        current_max_q.pop()
                    current_max_q.append(r_ptr)
                    while current_min_q and nums[current_min_q[-1]] >= nums[r_ptr]:
                        current_min_q.pop()
                    current_min_q.append(r_ptr)
                
                for l in range(left):
                    while current_max_q and current_max_q[0] < l:
                        current_max_q.popleft()
                    while current_min_q and current_min_q[0] < l:
                        current_min_q.popleft()
                    
                    total_ans += (nums[current_max_q[0]] - nums[current_min_q[0]])
                    items_added += 1

        if items_added < k:
            total_ans += (k - items_added) * threshold_X
            
        return total_ans