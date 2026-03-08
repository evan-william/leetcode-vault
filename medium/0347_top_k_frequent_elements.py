class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        founded_num_count = {}

        # the only numbers in the array
        if nums.count(nums[0]) == len(nums):
            return [nums[0]]
        
        for num in nums:

            # if not the above
            if num not in founded_num_count:
                founded_num_count[num] = 1 
            else:
                founded_num_count[num] += 1

            angka_terurut = sorted(founded_num_count, key=founded_num_count.get, reverse=True)
        
        hasil = []
        for i in range(k):
            hasil.append(angka_terurut[i])
            
        return hasil
