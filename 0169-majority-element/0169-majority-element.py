class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = Counter(nums)
        return mp.most_common(1)[0][0]