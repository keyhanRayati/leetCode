from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        it = len(min(strs, key=len))
        
        for i in range(it):
            p = strs[0][i]
            for s in strs:
                if s[i] == p:
                    pass
                else:
                    return result 
            result += p
        
        return result
            

class __main__():
    instance = Solution()
    print(instance.longestCommonPrefix(["a"]))
