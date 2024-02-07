class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic1 = {}
        dic2 = {}

        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
        for m in t:
            dic2[m] = dic2.get(m, 0) + 1

        
        if len(dic1) != len(dic2):
            return False

        for key, val in dic1.items():
            if dic2.get(key) != val:
                return False
        return True
    




        