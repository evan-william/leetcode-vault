class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary_history = {}
    
        for current_index, current_num in enumerate(nums): # [2,7,11,15], target = 9
            
            target_partner = target - current_num # 9 - 2 = 7, 9 - 7 = 2, 9 - 11 = -2, 9 - 15 = -6
            
            if target_partner in dictionary_history:
                partner_index = dictionary_history[target_partner]
            
                return [partner_index, current_index]
    
            dictionary_history[current_num] = current_index # [key] = value
            
        return []

