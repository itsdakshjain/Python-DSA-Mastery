class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        halfCount = [0] * 26
        midLetter = ''
        
        for c, freq in count.items():
            halfCount[ord(c) - ord('a')] = freq // 2
            if freq % 2 == 1:
                midLetter = c

        MAX_K = k + 1

        def nCr(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        def count_permutations(counts: list) -> int:
            total_items = sum(counts)
            ways = 1
            for freq in counts:
                if freq > 0:
                    ways *= nCr(total_items, freq)
                    if ways >= MAX_K:
                        return MAX_K
                    total_items -= freq
            return ways

        if count_permutations(halfCount) < k:
            return ""

        half_len = sum(halfCount)
        left_half = []

        for _ in range(half_len):
            for i in range(26):
                if halfCount[i] == 0:
                    continue

                halfCount[i] -= 1
                ways = count_permutations(halfCount)

                if k <= ways:
                    left_half.append(chr(ord('a') + i))
                    break
                else:
                    k -= ways
                    halfCount[i] += 1

        first_half = "".join(left_half)
        return first_half + midLetter + first_half[::-1]