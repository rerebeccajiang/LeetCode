class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = [[x, y] for x, y in zip(position, speed)]
        stack = []

        for x, y in sorted(lst)[::-1]:
            if stack and (target-x)/y <= (target - stack[-1][0])/stack[-1][1]:
                continue
            else:
                stack.append((x,y))

        return len(stack)