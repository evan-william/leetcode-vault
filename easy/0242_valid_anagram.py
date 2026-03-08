class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_distinct = {}
        
        # instant stop
        if len(s) != len(t):
            return False
        
        for each in s:

            # if not distinct
            if each not in count_distinct:
                count_distinct[each] = s.count(each)

                if s.count(each) != t.count(each):
                    return False

        return True