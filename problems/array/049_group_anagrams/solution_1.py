from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        
        seen = dict()
        for strr in strs:
            strr_sorted = ''.join(sorted(strr))
            if strr_sorted in seen:
                seen[strr_sorted].append(strr)
            else:
                seen[strr_sorted] = [strr]
        
        return list(seen.values())
