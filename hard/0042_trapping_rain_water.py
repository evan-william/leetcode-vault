class Solution:
    def trap(self, height: List[int]) -> int:
        # inputs nothing
        if not height: return 0
        
        # setting up 2 pointer
        L, R = 0, len(height) - 1
        leftMax, rightMax = height[L], height[R]
        answer = 0

        # starts pointer  
        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                answer += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                answer += rightMax - height[R]
        
        return answer
            