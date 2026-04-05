class Solution:
    def isValid(self, s: str) -> bool:
       # the last thing you ee before the closed parantehses is 
       # the open brcket of teh closed parantheses 
       map = {'}':'{',')':'(',']':'['}
       stack = []
       for c in s :
        if c in map:
            if stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
       return True if not stack else False




