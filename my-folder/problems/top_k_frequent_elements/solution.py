class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # dict1 = {}
        # for num in nums:
        #     dict1[num] = dict1.get(num,0) + 1
        # sortedLst = sorted(dict1, key=lambda x:dict1[x],reverse=True)

        # return sortedLst[0:k]

        result = []
        freq = [[] for i in range(len(nums)+1)] # each bucket holds list of nums that have the same frequency (index)
        print(freq)
        print(nums)
        output=[]

        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num,0) + 1

        for key,val in dict1.items():
            freq[val].append(key)

        for i in range(len(freq)-1, 0, -1):
            print(i)
            for m in freq[i]:
                output.append(m)
            if len(output) == k:
                return output





        