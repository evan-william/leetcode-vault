# Initial Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []

        # cleaning
        for huruf in s:
            if huruf.isalnum():
                clean_s.append(huruf.lower())

        first_pointer = 0
        second_pointer = len(clean_s) - 1 # 18

        # wasitacaroracatisaw
        while len(clean_s) > 1: # wasitacaroracatisaw
            if clean_s[first_pointer] == clean_s[second_pointer]: 
                clean_s.pop(second_pointer)
                clean_s.pop(first_pointer)

                first_pointer = 0 
                second_pointer = len(clean_s) - 1
                
            else:
                return False

        return True
    

# Faster Solution Learned from Internet

"""
1. 
return clean_s == clean_s[::-1]
2. 

# change the while loop to two pointers:
        l, r = 0, len(clean_s) - 1
        
        while l < r:
            if clean_s[l] == clean_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

Note: Problem with the first initial solution is that after pop it has to move the whole list to the left so it takes alot of time on long string
"""