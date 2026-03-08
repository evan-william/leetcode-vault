# O(n) Solution - Initial Solution -> Copied from Two Sum I and modified just a bit
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary_history = {}
    
        for current_index, current_num in enumerate(nums): # [2,7,11,15], target = 9
            
            target_partner = target - current_num # 9 - 2 = 7, 9 - 7 = 2, 9 - 11 = -2, 9 - 15 = -6
            
            if target_partner in dictionary_history:
                partner_index = dictionary_history[target_partner]
            
                return [partner_index + 1, current_index + 1]
    
            dictionary_history[current_num] = current_index # [key] = value
            
        return []


# O(1) Solution using pointer since the array is sorted
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            total = numbers[l] + numbers[r]
            
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1
