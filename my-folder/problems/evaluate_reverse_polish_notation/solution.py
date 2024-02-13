class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in ["+", "/", "*", "-"]:
                stack.append(i)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                result = 0
                if i == "+":
                    result = num2+num1
                elif i == "-":
                    result = num2-num1
                elif i == "/":
                    result = int(num2/num1)
                elif i == "*":
                    result = num2*num1
                stack.append(str(result))

        return int(stack[0])

            