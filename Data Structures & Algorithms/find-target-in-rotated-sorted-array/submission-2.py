class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums,target,l,r):
            if l > r:
                return -1
            m=(l+r)//2
            if nums[m]==target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    return binary(nums,target,l,m-1)
                else:
                    return binary(nums,target,m+1,r)
            else:
                if nums[m] < target <= nums[r]:
                    return binary(nums,target,m+1,r)
                else:
                    return binary(nums,target,l,m-1)

        return binary(nums,target,0,len(nums)-1)
