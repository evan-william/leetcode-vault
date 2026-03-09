class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max values got from pairs:
        max_water = 0

        # setting up 2 pointers
        l, r = 0 , len(heights) - 1

        while l < r:
            
            # r - l is the distance difference
            current_water = (r - l) * min(heights[l], heights[r])

            # jika lebih besar
            if current_water > max_water:
                max_water = current_water
            
            # jika kiri lebih kecil dari kanan
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water