class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
    
        for m in range(len(strs[0])):
            character = strs[0][m]
            
            for n in range (1,len(strs)):
                if len(strs[n]) == m or strs[n][m] != character:
                    return prefix
            
            prefix += character
            
        return prefix
                
       