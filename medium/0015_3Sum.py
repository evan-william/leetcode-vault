class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        output = []

        # [-1,0,1,2,-1,-4]
        nums.sort() # [-4, -1, -1, 0, 1, 2]
       
        # if len is 3 and wrong instantly:
        if len(nums) == 3:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        
        # Main Part
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # if dupe
                continue

            l, r = i + 1, len(nums) - 1
            # Main Part 2
            while l < r:
                answer = a + nums[l] + nums[r]

                if answer > target:
                    r -= 1
                elif answer < target:
                    l += 1
                elif answer == target:
                    output.append([a,nums[l],nums[r]])

                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return output


