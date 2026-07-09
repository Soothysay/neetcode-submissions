class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i,num in enumerate(nums):
            if has.get((target-num))!=None:
                return [has[(target-num)], i]
            else:
                has[num]=i