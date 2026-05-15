from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        most_freq = None

        for num in nums:
            if num not in counter:
                counter[num] = 0
            
            counter[num] += 1

            if most_freq == None or counter[num] > counter[most_freq]:
                most_freq = num
        
        return list(dict(sorted(counter.items(), key=lambda x: x[1], reverse=True)).keys())[:k]