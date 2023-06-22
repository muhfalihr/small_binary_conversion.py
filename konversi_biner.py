# Belajar Logika Konversi Bilangan Biner

binary = []
b = int(input('Masukkan Angka Bilangan Desimal: '))

while b > 0:
    h = b%2
    if h == 0 or h == 1:
        binary.append(h)
    b//=2

binary.reverse()
print('Result:')
for i in binary:
    print(f'{i} ', end='')
