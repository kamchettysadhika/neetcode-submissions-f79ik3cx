class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c not in closeToOpen: 
                stack.append(c)
                #not a closing bracket  
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
                # if its a closing bracket 
        return True if not stack else False


    #     #1) order 
    #     #2) if it exsists or not 
    #     #3) within the order we need to see if its teh same type of close bracet 
    #     ([{}()])
    #     ([])
    
    # so when we go through teh string we stop when we see a closing bracket and check f its teh closing bracket of the last opening bracket that we saw 
