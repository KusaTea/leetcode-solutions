class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False


        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = list()

        for br in s:
            if br in brackets:
                if not stack or brackets[br] != stack[-1]:
                    return False
                
                stack.pop()
            
            else:
                stack.append(br)
        
        return len(stack) == 0