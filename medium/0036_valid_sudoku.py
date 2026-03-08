class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # input = board
        pos_baris = defaultdict(set)  
        pos_kolom = defaultdict(set)  
        pos_kotak = defaultdict(set)  

        for r in range(9): # row
            for c in range(9): # column

                angka = board[r][c]

                if angka == ".":
                    continue

                koordinat_kotak = (r // 3, c // 3)

                if angka in pos_baris[r]:
                    return False
                if angka in pos_kolom[c]:
                    return False
                if angka in pos_kotak[koordinat_kotak]:
                    return False

                pos_baris[r].add(angka)
                pos_kolom[c].add(angka)
                pos_kotak[koordinat_kotak].add(angka)

        return True
