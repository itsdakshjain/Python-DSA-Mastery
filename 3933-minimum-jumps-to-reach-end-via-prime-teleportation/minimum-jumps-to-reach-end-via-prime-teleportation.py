MAX_VAL = 1000001
min_prime = [0] * MAX_VAL
for i in range(2, int(MAX_VAL**0.5) + 1):
    if min_prime[i] == 0:
        for j in range(i*i, MAX_VAL, i):
            if min_prime[j] == 0:
                min_prime[j] = i
for i in range(2, MAX_VAL):
    if min_prime[i] == 0:
        min_prime[i] = i

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        prime_to_indices = {}
        for i, val in enumerate(nums):
            temp = val
            factors = set()
            while temp > 1:
                p = min_prime[temp]
                factors.add(p)
                while temp % p == 0:
                    temp //= p
            for p in factors:
                if p not in prime_to_indices:
                    prime_to_indices[p] = []
                prime_to_indices[p].append(i)

        queue = deque([(0, 0)])
        visited_indices = {0}
        visited_primes = set()
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            if curr_idx == n - 1:
                return steps
            
            for next_idx in [curr_idx - 1, curr_idx + 1]:
                if 0 <= next_idx < n and next_idx not in visited_indices:
                    visited_indices.add(next_idx)
                    queue.append((next_idx, steps + 1))
            
            val = nums[curr_idx]
            if val > 1 and min_prime[val] == val:
                if val not in visited_primes:
                    if val in prime_to_indices:
                        for target_idx in prime_to_indices[val]:
                            if target_idx not in visited_indices:
                                visited_indices.add(target_idx)
                                queue.append((target_idx, steps + 1))
                    visited_primes.add(val)
        
        return 1