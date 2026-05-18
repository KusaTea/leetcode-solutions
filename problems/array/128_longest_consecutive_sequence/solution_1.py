from typing import List
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        results = defaultdict(int)
        mx_len = 0

        for num in nums:
            if results[num]: continue

            results[num] = results[num - 1] + 1 + results[num + 1]
            results[num - results[num - 1]] = results[num]
            results[num + results[num + 1]] = results[num]

            mx_len = max(mx_len, results[num])

        return mx_len
            