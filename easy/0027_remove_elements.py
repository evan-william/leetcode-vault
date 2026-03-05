class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        # instantly returns 0 if the value that wanna be removed isn't found
        if val not in nums:
            return len(nums)

        for num in range(len(nums)):
            if nums[num] != val:
                nums[k] = nums[num]

                k += 1

        return k
