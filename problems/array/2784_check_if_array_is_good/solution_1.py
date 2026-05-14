from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        last_num = len(nums) - 1
        last_num_counter = 2
        target = set(range(1, last_num))

        for num in nums:
            if num in target:
                target.remove(num)
            elif num == last_num and last_num_counter > 0:
                last_num_counter -= 1
            else:
                return False

        return True