class Solution:
    def romanToInt(self, s: str) -> int:
        kamus = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0

        i = 0 
        while i < len(s): # s = [] misal , loop1

            angka_sekarang = kamus[s[i]] # loop1 = 10, loop2 = 1
            
            if i + 1 < len(s) and angka_sekarang < kamus[s[i + 1]]: # loop1 = y & n,  loop2 = y & y,  
                angka_next = kamus[s[i+1]]

                if angka_next == 5 or angka_next == 10:
                    total += angka_next - 1
                elif angka_next == 50 or angka_next == 100:
                    total += angka_next - 10
                else:
                    total += angka_next - 100
                i += 2

            else:
                total += angka_sekarang
                i += 1
                
        return total
