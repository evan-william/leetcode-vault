class MinStack:
    def __init__(self):
        # Dua list utama: satu buat data, satu buat rekor min
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Trik: Kalau min_stack kosong, lgsg isi val.
        # Kalau ada isinya, ambil yang terkecil antara val baru VS rekor lama.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # Bandingin val baru sama angka paling atas di min_stack
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        # Dua-duanya harus dibuang bareng biar sejarahnya sinkron
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]