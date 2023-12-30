class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)        
        if shortest == "": return ""

        for ind, ch in enumerate(shortest):
            for s in strs:
                if s[ind] != ch:
                    return shortest[:ind]

        return shortest