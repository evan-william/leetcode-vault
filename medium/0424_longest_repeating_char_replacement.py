# Solution 1
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # count dictionary
       L = 0
       output = 0
       frequency_dict = {}

       for R in range(len(s)):
            frequency_dict[s[R]] = 1 + frequency_dict.get(s[R], 0)

            # valid or not (R-L + 1 -> Banyak Huruf di Window)
            while (R - L + 1) - max(frequency_dict.values()) > k:

                frequency_dict[s[L]] -= 1
                L += 1

            output = max(output, R - L + 1)

       return output

# Solution 2 (Optimized)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # count dictionary
       L = 0
       output = 0
       frequency_dict = {}
       max_f = 0

       for R in range(len(s)):
            frequency_dict[s[R]] = 1 + frequency_dict.get(s[R], 0)

            max_f = max(max_f, frequency_dict[s[R]])

            # valid or not (R-L + 1 -> Banyak Huruf di Window)
            while ((R - L + 1) - max_f) > k:

                frequency_dict[s[L]] -= 1
                L += 1

            output = max(output, R - L + 1)

       return output

        
        