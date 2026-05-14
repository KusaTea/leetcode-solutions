class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = dict()
        for let in s:
            if let not in counter:
                counter[let] = 0
            counter[let] += 1
        
        for let in t:
            if let not in counter:
                return False
            counter[let] -= 1
            if counter[let] < 1:
                del counter[let]
        
        return not bool(counter)