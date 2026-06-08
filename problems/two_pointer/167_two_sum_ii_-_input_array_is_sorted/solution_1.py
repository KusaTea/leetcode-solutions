from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, first in enumerate(numbers):
            l, r = idx + 1, len(numbers) - 1
            pretarget = target - first

            while l <= r:
                m = int((l + r) / 2)

                if numbers[m] == pretarget:
                    return [idx + 1, m + 1]
                
                elif numbers[m] > pretarget:
                    r = m - 1
                
                else:
                    l = m + 1
        
        return [-1, -1]