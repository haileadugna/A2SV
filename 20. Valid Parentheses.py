class Solution:
    def isValid(self, s: str) -> bool:
        dict1={'}':'{',']':'[',')':'('}
        list1 =list(s)
        stack = [list1[0]]
        if list1[0] in dict1:
                return False
        for i in range(1,len(list1)):
            if list1[i] in dict1.values():
                stack.append(list1[i])
            else:
                if stack and stack[-1] == dict1[list1[i]]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
        