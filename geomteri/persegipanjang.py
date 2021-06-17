class PersegiPanjang():
    #fungsi pertama kali yang dipanggil ketika object dibuat
    def __init__(self, p, lebar):
        self.p = p
        self.lebar = lebar
    def info(self):
        return f'Ini adalah object dari persegi panjang dengan panjang {self.p} dan lebar {self.lebar}'

    def hitung_luas(self):
        return self.p * self.lebar
