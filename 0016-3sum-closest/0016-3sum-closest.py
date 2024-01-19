class Solution:
       def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        mn=inf
        ans=0
        for i in range(n):
            s=i+1
            e=n-1
            while s<e:
                sm=nums[i]+nums[s]+nums[e]
                if sm==target:
                    return sm
                if abs(target-sm)<mn:
                    mn=abs(target-sm)
                    ans=sm
                if sm<target:
                    s+=1
                else:
                    e-=1
       
        return ans