class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, num_of_letters = [], [], 0
        
        for w in words:
            # CEK LENGTH: total huruf + kata baru + minimal 1 spasi tiap kata
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # JUSTIFICATION
                for i in range(maxWidth - num_of_letters):
                    # Bagi spasi ke slot yang tersedia secara merata dari kiri
                    cur[i % (len(cur) - 1 or 1)] += ' '
                
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
                
            cur.append(w)
            num_of_letters += len(w)
        
        # LAST LINE: rata kiri, sisa spasi ditaruh di paling kanan
        last_line = ' '.join(cur)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return res