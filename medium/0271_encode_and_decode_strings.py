class Solution:
    def encode(self, strs: List[str]) -> str: # [cats,dog,123]
        s = "" 
        for word in strs:
            current_word_long = len(word)
            current_part = str(current_word_long) + "#" + word
            s += current_part
        return s # -> 4#cats3#dog3#123"
        
    def decode(self, s: str) -> List[str]:
        decoded_msg = []
        current_index = 0

        while current_index < len(s):
            
            # 1. Cari di mana posisi '#' terdekat dari tempat kita berdiri
            # Ini akan otomatis membaca mau angkanya 4, 10, atau 999
            posisi_pagar = s.find("#", current_index)
            
            # 2. Ambil angka panjang kata utuhnya (dari current_index sampai SEBELUM pagar)
            times = int(s[current_index : posisi_pagar])
            
            # 3. Kata aslinya pasti dimulai tepat SETELAH pagar
            mulai_kata = posisi_pagar + 1
            
            # 4. Potong kata aslinya
            current_part = s[mulai_kata : mulai_kata + times]
            decoded_msg.append(current_part)

            # 5. Lompat! Geser index ke ujung kata yang barusan dipotong
            current_index = mulai_kata + times

        return decoded_msg