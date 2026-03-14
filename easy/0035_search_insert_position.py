class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2 # FIND MIDDLE
            
            if nums[mid] == target:
                return mid # Found Return Index
            
            if target > nums[mid]:
                L = mid + 1 # TARGET RIGHT SIDE
            else:
                R = mid - 1 # TARGET LEFT SIDE
                
        # If the target is not found, L will stop at the correct insertion position.
        return L