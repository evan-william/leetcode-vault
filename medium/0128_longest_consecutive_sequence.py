class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: 
            return 0

        current_consecutive_form = []
        best_consecutive_form = []

        # nums [2,20,4,10,3,4,5]
        # nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
        # nums = [0,3,2,5,4,6,1,1]
        sorted_nums = sorted(set(nums)) # [-1, 0, 1, 3, 4, 5, 6, 7, 8, 9] 
                                        # [2,3,4,5,5,10,20]
                                        # [0,1,1,2,3,4,5,6]

        for index, num in enumerate(sorted_nums): 
            # if still going correctly or first index
            if num - sorted_nums[index - 1] == 1 or index == 0:
                current_consecutive_form.append(num) # [-1,0,1]

            # already wrong
            else:
                if len(current_consecutive_form) > len(best_consecutive_form):
                    best_consecutive_form = current_consecutive_form.copy()
                    
                current_consecutive_form = [num]

        if len(best_consecutive_form) > 0 and len(best_consecutive_form) > len(current_consecutive_form):
            return len(best_consecutive_form)
        else:
            return len(current_consecutive_form)
