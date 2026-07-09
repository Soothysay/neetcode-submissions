class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n, n1 = 0, len(nums) - 1
        while n <= n1:
            middle = (n + n1) // 2
            if nums[middle] < target:
                n = middle + 1
            elif nums[middle] > target:
                n1 = middle - 1
            else:
                return middle
        return -1
