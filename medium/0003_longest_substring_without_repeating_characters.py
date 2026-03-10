class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_train = []
        longest_record = 0

        for huruf in s:
            while huruf in string_train:
                string_train.pop(0) 

            string_train.append(huruf)

            if len(string_train) > longest_record:
                longest_record = len(string_train)

        return longest_record
    

# More Optimized Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        output = 0

        for r in range(len(s)):
            # found dupe
            while s[r] in char_set:
                # remove the farther left 
                char_set.remove(s[l])
                l += 1
            
            # add new word to set
            char_set.add(s[r])
            
            # update longest sliding window (r - l + 1)
            output = max(output, r - l + 1)
            
        return output