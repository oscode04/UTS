print('Aplikasi NILAI MATA KULIAH')
print('Created by : Gaos')
print('=============================')
# kode untuk memasukin inputan dari user
nama = input('Masukan nama anda : ')
jurusan = input('Masukan Jurusan anda : ')
nilai_uts = int(input('Masukan Nilai UTS anda : '))
nilai_tugas = int(input('Masukan Nilai Tugas anda : '))
nilai_uas = int(input('Masukan Nilai UAS anda : '))

def hitung_nilai_akhir(uts, tugas, uas):
    hasil_akhir_uts = uts * 0.3
    hasil_akhir_tugas = tugas * 0.2
    hasil_akhir_uas = uas * 0.5
    total = hasil_akhir_uts + hasil_akhir_tugas + hasil_akhir_uas
    return total

# baris untuk memasukan input user ke dalam Fungsi
nilai_akhir = hitung_nilai_akhir(uts=nilai_uts, tugas=nilai_tugas, uas=nilai_uas)

# pengecekan nilai user, Jika nilai akhir lebih ari 80 maka berikan ucapan “ Selamat Anda lulus “, jika di bawah 80 “
# Maaf, silahkan belajar lagi “
print('===========================')
if nilai_akhir >= 80:
    print('Nama : ', nama)
    print('Jurusan : ', jurusan)
    print('Nilai Akhir Anda Adalah', nilai_akhir)
    print('Selamat Anda Lulus')
else:
    print('Nama : ', nama)
    print('Jurusan: ', jurusan)
    print('Nilai Akhir Anda Adalah', nilai_akhir)
    print('Maaf, silahkan belajar lagi')