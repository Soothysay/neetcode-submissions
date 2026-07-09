class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        i=0
        ans=[]
        while i<len(nums)-2:
            if i > 0 and nums[i]==nums[i-1]:
                i+=1
                continue
            l=i+1
            #if nums[l]==nums[l+1]:
            #    l+=1
            r=len(nums)-1
            #if nums[r]==nums[r-1]:
            #    r-=1
            while l<r:
                summer=nums[i]+nums[l]+nums[r]
                if summer==0:
                    if l!=i and r!=i:
                        ans.append([nums[i],nums[l],nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r-=1
                elif summer<0:
                    l+=1
                elif summer>0:
                    r-=1
            i+=1
        return ans