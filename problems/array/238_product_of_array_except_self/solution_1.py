from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        zero_counter = 0
        zero_idx = None

        for idx, num in enumerate(nums):

            if num == 0:
                zero_counter += 1
                zero_idx = idx

                if zero_counter > 1:
                    return [0] * len(nums)

            else:
                answer[0] *= num

        if zero_counter > 0:
            answer += [0] * (len(nums) - 1)
            answer[zero_idx], answer[0] = answer[0], answer[zero_idx]

        else:
            answer = answer * len(nums)

            for idx in range(len(nums)):
                answer[idx] //= nums[idx]
            
        return answer