from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        stack = list()

        for cur_idx, temper in enumerate(temperatures):

            while stack and temper > stack[-1][1]:
                answer[stack[-1][0]] = cur_idx - stack[-1][0]
                stack.pop()
            
            stack.append((cur_idx, temper))
    
        return answer