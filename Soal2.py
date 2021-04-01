nama = input('Masukkan nama:')
nilai = float(input('Masukkan nilai:'))
if nilai < 60:
    print('Halo %s! Nilai anda setelah dikonversi adalah E' %nama)
elif 60 <= nilai <= 64:
    print('Halo %s! Nilai anda setelah dikonversi adalah C' % nama)
elif 65 <= nilai <= 69:
    print('Halo %s! Nilai anda setelah dikonversi adalah C+' % nama)
elif 70 <= nilai <= 74:
    print('Halo %s! Nilai anda setelah dikonversi adalah B' % nama)
elif 75 <= nilai <= 79:
    print('Halo %s! Nilai anda setelah dikonversi adalah B+' % nama)
elif 80 <= nilai <= 84:
    print('Halo %s! Nilai anda setelah dikonversi adalah A-' % nama)
elif 85 <= nilai <= 100:
    print('Halo %s! Nilai anda setelah dikonversi adalah A' % nama)
else:
    print('Nilai tidak valid')