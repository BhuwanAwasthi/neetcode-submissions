class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in enumerate(nums):
            for x,y in enumerate(nums):
                if (nums[i]+nums[x]==target) and i!=x:
                    return [i,x]