class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair (index, height)
        ret = 0

        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                i, h = stack.pop()
                ret = max(ret, (index-i) * h)
                start = i
            stack.append([start, height])

        for item in stack:
            ret = max(ret, (len(heights)-item[0])*item[1])

        print(stack)

        return ret


        