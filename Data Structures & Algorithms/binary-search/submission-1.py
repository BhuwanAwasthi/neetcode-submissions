class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1


        while left<=right:
            if nums[left]==target:
                return left
            elif nums[right]==target:
                return right
        
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid
                left+=1
            elif nums[mid]<target:
                left=mid
                right-=1
        return -1
            
        