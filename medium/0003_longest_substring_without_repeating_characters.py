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