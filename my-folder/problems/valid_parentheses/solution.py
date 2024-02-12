class Solution:
    def isValid(self, s: str) -> bool:
        # openBr = ["(", "[", "{"]
        # closeBr = [")", "]", "}"]

        # stack = []
        # for i in s:
        #     if len(stack)==0:
        #         stack.append(i)

        #     elif i in openBr : # in open bracket
        #         stack.append(i)

        #     else: # in closing bracket
        #         bracket = stack.pop()
        #         if bracket in closeBr or closeBr[openBr.index(bracket)] != i:
        #             return False
                    

        # return len(stack) == 0

        stack = []
        closeToOpen = {"]": "[", "}": "{",")":"(" }

        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return len(stack)==0

        


        