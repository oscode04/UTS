print('Selamat data di aplikasi parkir')
print('Created by : Gaos')
print('==================================')

# input untuk menanyakan lama parkir
print('Berapa lama anda akan parkir?')
print('Biaya Parkir :' '\n' '1. Jika kurang dari 60 menit untuk motor Rp. 5.000 dan mobil Rp. 10.000' '\n' '2. Jika lebih dari atau sama dengan 60 menit untuk motor Rp. 15.000 dan Mobil Rp. 25.000')
lamaParkir = int(input('masukan lama parkir (dalam menit): '))

# input untuk menanyakan jenis kendaraan
print('Tekan A jika anda memakai mobil dan Tekan B jika anda memakai motor')
jenisKendaraan = input('Pilih A atau B : ')

# ketentuan parkir
if lamaParkir < 60:
    if (jenisKendaraan == 'A'):
        print('Total biaya parkir anda adalah Rp. 10.000')
    else:
        print('Total Total biaya parkir anda adalah Rp. 5.000')
else:
    if (jenisKendaraan == 'A'):
        print('Total biaya parkir anda adalah Rp. 25.000')
    else:
        print('Total Total biaya parkir anda adalah Rp. 15.000')