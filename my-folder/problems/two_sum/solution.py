class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(0, len(nums)):
            compliment = target - nums[i]
            if compliment in dict.keys():
                return[i, dict.get(compliment)]
            else:
                dict[nums[i]] = i
