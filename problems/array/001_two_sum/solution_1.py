from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for num_idx, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], num_idx]
        
            else:
                seen[num] = num_idx
        
        return [-1, -1]