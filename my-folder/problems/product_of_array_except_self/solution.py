class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        #two iterations 

        # prefix
        prefix = 1
        for i in range(len(nums)-1):
            prefix *= nums[i]
            output[i+1] = prefix

        postfix = 1
        for i in range(len(nums)-1, 0, -1):
            postfix *= nums[i]
            output[i-1] *= postfix
        
        return output
        