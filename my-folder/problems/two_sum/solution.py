class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # stor = defaultdict(list)

        # for i in range(len(nums)):
        #     stor[nums[i]].append(i)
        # print(stor)

        # for i in range(len(nums)):
        #     complement = stor.get(target - nums[i])
        #     if complement != None:
        #         if len(complement) == 2:
        #             return complement
        #         elif target - nums[i] == nums[i]:
        #             continue
        #         else:
        #             complement.append(i)
        #             return complement
        
        preMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i]
            preMap[n] = i
        