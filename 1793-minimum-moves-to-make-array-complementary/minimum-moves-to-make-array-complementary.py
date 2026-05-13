class Solution:
  def minMoves(self, nums: list[int], limit: int) -> int:
    n = len(nums)
    ans = n
    delta = [0] * (limit * 2 + 2)

    for i in range(n // 2):
      a = nums[i]
      b = nums[n - 1 - i]
      delta[min(a, b) + 1] -= 1
      delta[a + b] -= 1
      delta[a + b + 1] += 1
      delta[max(a, b) + limit + 1] += 1
    moves = n
    for i in range(2, limit * 2 + 1):
      moves += delta[i]
      ans = min(ans, moves)

    return ans     