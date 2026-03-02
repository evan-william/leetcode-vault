class Solution:
    def isValid(self, s: str) -> bool:
        stack_parentheses = []
        pair_parentheses = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for current_parentheses in s:
            if current_parentheses in pair_parentheses: # Check open parentheses -> Cause only check keys
                stack_parentheses.append(current_parentheses)
            else: # Happends if not open Bracket
                if not stack_parentheses: # If next loop, stack still have closed brackets but empty stacked          
                    return False
                
                last_open_parentheses = stack_parentheses.pop() # (

                if pair_parentheses[last_open_parentheses] != current_parentheses: #
                    return False

        return len(stack_parentheses) == 0 # -> returns True if empty
                
            
                
                
    