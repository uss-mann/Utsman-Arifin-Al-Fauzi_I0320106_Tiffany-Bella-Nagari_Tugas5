nama = input('Masukkan nama: ')
jk = input('Pilih jenis kelamin (l/p): ')
if jk == 'l':
    print ('"Selamat datang Tuan %s!"' %nama)
elif jk == 'p':
    print('"Selamat datang Nyonya %s"' %nama)
else:
    pass
print()