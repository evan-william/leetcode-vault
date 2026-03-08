class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        long = len(nums)
        
        # if nums = [1, 2, 4, 6], output = [1, 1, 1, 1]
        output = [1] * long
        
        # prefix (multiply from left)
        prefix = 1
        for i in range(long):
            # put prefix in output from left
            output[i] = prefix
            # update prefix for next position
            prefix = prefix * nums[i]
            
        # postfix (multiply from right)
        postfix = 1
        # loop from end to start with -1
        # stop in -1 so index 0 is counted
        for i in range(long - 1, -1, -1):
            # multiply output that is product of prefix with postifx
            output[i] = output[i] * postfix
            # update postfix for enxt position
            postfix = postfix * nums[i]
            
        return output