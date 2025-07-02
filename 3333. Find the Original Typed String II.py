import math


class Solution(object):
    def countPossibleOriginals(self, word, k):
        MOD = 10**9 + k
        reducible_groups = 0
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            if j - i >= 2:
                reducible_groups += 1
            i = j

        total_length = len(word)
        total_ways = 0

    # Step 2: Try reducing 0 to all possible reducible groups
        for reduction_count in range(0, reducible_groups + 1):
            reduced_length = total_length - reduction_count
            if reduced_length >= k:
                ways = math.comb(reducible_groups, reduction_count)
                total_ways = (total_ways + ways) % MOD

        return total_ways

A = Solution()

print(A.countPossibleOriginals("aabbccdd", 7))