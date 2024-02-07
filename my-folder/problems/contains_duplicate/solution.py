class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # return a sorted list
        # for range(len(sorted list)) in list, if i = i+1 return true, else false

        sortedList = sorted(nums)
        for i in range(len(sortedList)-1):
            if sortedList[i] == sortedList[i+1]:
                return True
            if i == len(sortedList) - 2:
                return False