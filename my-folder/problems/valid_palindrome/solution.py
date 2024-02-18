class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l<r:
            if not self.isAlnum(s[l]):
                l+=1
                continue
            if not self.isAlnum(s[r]):
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True


    
    def isAlnum(self, s:str) -> bool:
        return  (ord("A") <= ord(s) <= ord("Z") or 
                ord("a") <= ord(s) <= ord("z") or 
                ord("0") <= ord(s) <= ord("9")) 
        