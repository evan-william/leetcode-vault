class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary_history = {}
    
        for i, current_num in enumerate(nums):
            
            target_partner = target - current_num
            
            if target_partner in dictionary_history:
                partner_index = dictionary_history[target_partner]
            
                return [partner_index, i]
    
            dictionary_history[current_num] = i
            
        return []