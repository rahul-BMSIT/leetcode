class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            k=0
            i=0
            j=0
            while j<len(needle) and i<len(haystack):
                if needle[j]!=haystack[i]:
                    i=i-j+1
                    j=k
                else:
                    i+=1
                    j+=1
            return i-j
            


        