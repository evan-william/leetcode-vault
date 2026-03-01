# Initial Solution -> Submitted
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        inverted_digit_list = []
        digit_list = list(map(int, str(x)))
 
        for numbers in reversed(digit_list):
            inverted_digit_list.append(numbers)

        for i in range(len(digit_list)):
            if digit_list[i] == inverted_digit_list[i]:
                pass  
            else:
                return False 

        return True
    
# Optimized Solution -> Found on Internet
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        teks_asli = str(x)
        teks_terbalik = teks_asli[::-1]
        return teks_asli == teks_terbalik
