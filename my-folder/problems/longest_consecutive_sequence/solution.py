class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        maxNum = 0

        for num in nums:
            if num-1 not in store: # this is starting point of a seq
                length = num+1
                while length in store:
                    length+=1
                if length - num > maxNum:
                    maxNum = length -num
        
        return maxNum
                    


        
        