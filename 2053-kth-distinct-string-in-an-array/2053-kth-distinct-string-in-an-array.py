class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for val,c in Counter(arr).items():
            if c==1:
                k-=1
            if k==0: return val
        return ""