class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary(nums,l,r):
            m=(l+r)//2
            if l==r:
                return nums[l]
            if nums[m]>nums[r]:
                return binary(nums,m+1,r)
            else:
                return binary(nums,l,m)
        return binary(nums,0,len(nums)-1)
            
        