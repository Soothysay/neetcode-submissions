class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher={}
        for i in range(len(nums)):
            if hasher.get(target-nums[i])!=None:
                return [hasher.get(target-nums[i]),i]
            else:
                hasher[nums[i]]=i
        return False