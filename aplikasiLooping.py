print('Selamat datang di aplikasi PEMBUATAN TABEL PERKALIAN')
print('Created by : Gaos')
print('Aplikasi ini di buat untuk membuat sebuah tabel perkalian, tabel perkalian ini biasa dipakai oleh murid SD untuk membantu mereka dalam menghapalkan perkalian.')
print('Cara kerja aplikasi ini yaitu' '\n' 'pertama anda memasukan angka untuk nanti nya di buatkan tabel perkaliannya' '\n' 'setelah itu anda tinggal memasukan awal perkalian dan akhir dari perkalian')
print('Contoh hasilnya seperti ini seperti ini')
print('======================================================================================================================================')
print('Perkalian 5')
# contoh input untuk perkalian berapa
contohAngka = 5
# contoh nilai awal, nilai ini di pakai sebagai awal dari tabel perkalian
contohAwal = 1
# contoh nilai akhir, nilai ini di pakai sebagai akhir dari tabel perkalian
contohAkhir = 10
# looping untuk membuat tabel perkalian
# di lakukan looping dengan bantuan range untuk menentukan rentang angka angka nya, nilai range diambil dari contohAwal sebagai nilai minimal nya dan contohAkhir sebagai nilai maksimal nya.
# contohAkhir ditambah dengan satu agar hasilnya sesuai dengan permintaan karena default dari range itu selalu dikurangi 1, jadi jiak contohAwal 1 dan contohAkhir nya 10 maka rentang nilai nya adalah 1 - 9. Lalu ditambah dengan 1 agar sesuai dengan input dari user
# setelah range nya di ketahui, maka range ini akan di inisialisasi ke dalam nilai i, lalu nilai i ini akan masuk kedalam baris print beserta contohAngka, string 'x', i (nilai range), string '=' dan contohAngka * i untuk hasil perkalian nya
for i in range(contohAwal, (contohAkhir+1)):
    print(contohAngka, 'x', i, '=', contohAngka*i)
print('=======================================================================================================================================')
print('Silahkan di coba')
# input perkalian berapa
angka = int(input("Mau perkalian berapa? : "))
# input awal perkalian nya mau mulai dari angka berapa
awal = int(input("Mulai dari berapa : "))
# input akhir perkalian nya mau berakhir di angka berapa
akhir = int(input("Sampai berapa : "))

print('=======================================================================================================================================')
# baris kode di bawah berfungsi untuk mengecek input dari user. Jika nilai awal yang di kirim user lebih besar dari angka sampai maka blok if akan di jalankan
if awal > akhir:
    print('angka mulai harus lebih kecil dari angka sampai')
# namun jika user menginput nilai awal lebih kecil dari nilai sampai maka blok else ini akan di jalankan
else:
    print('Ini hasilnya')
    print('Perkalian ', angka)
    # hasil input user masuk ke dalam looping di bawah, untuk cara kerjanya sama seperti contoh di atas
    for j in range(awal, (akhir+1)):
        print(angka, 'x', j, '=', angka*j)