class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        ans = list()

        for i, num1 in enumerate(nums):
            
            if num1 > 0: break
            if i > 0 and num1 == nums[i - 1]: continue

            j, k = i + 1, len(nums) - 1

            while j < k:

                if nums[j] + nums[k] < -num1:
                    j += 1
                
                elif nums[j] + nums[k] > -num1:
                    k -= 1
                
                else:
                    ans.append([num1, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
            
        return ans