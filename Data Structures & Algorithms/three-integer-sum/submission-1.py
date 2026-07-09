class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        out=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                summer=nums[i]+nums[l]+nums[r]
                if summer>0:
                    r-=1
                elif summer<0:
                    l+=1
                else:
                    out.append([nums[i],nums[l],nums[r]])
                    # skip duplicates for nums[l]
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    # skip duplicates for nums[r]
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return out