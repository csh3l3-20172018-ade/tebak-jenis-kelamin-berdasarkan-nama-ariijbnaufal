#Program tebak jenis kelamin berdasarkan nama

#function lelaki bertujuan untuk menghitung berapa jumlah huruf yang mengidentifikasikan nama laki-laki pada variabel nama
def lelaki(nama):
    poin = 0
    for i in range(len(nama)):
        if nama[i] == 'b':
            poin = poin + 1
        elif nama[i] == 'B':
            poin = poin + 1
        elif nama[i] == 'd':
            poin = poin + 1
        elif nama[i] == 'D':
            poin = poin + 1
        elif nama[i] == 'o':
            poin = poin + 1
        elif nama[i] == 'O':
            poin = poin + 1
        elif nama[i] == ' ':
            break
    return poin

#function perempuan bertujuan untuk menghitung berapa jumlah huruf yang mengidentifikasikan nama perempuan pada variabel nama
def perempuan(nama):
    poin = 0
    for i in range(len(nama)):
        if nama[i] == 'i':
            poin = poin + 1
        elif nama[i] == 'I':
            poin = poin + 1
        elif nama[i] == 'a':
            poin = poin + 1
        elif nama[i] == 'A':
            poin = poin + 1
        elif nama[i] == 'u':
            poin = poin + 1
        elif nama[i] == 'U':
            poin = poin + 1
        elif nama[i] == 'e':
            poin = poin + 1
        elif nama[i] == 'E':
            poin = poin + 1
        elif nama[i] == 't':
            poin = poin + 1
        elif nama[i] == 'T':
            poin = poin + 1
        elif nama[i] == 'l':
            poin = poin + 1
        elif nama[i] == 'L':
            poin = poin + 1
        elif nama[i] == ' ':
            break
    return poin


print('PROGRAM TEBAK JENIS KELAMIN BERDASARKAN NAMA')
print('')
nama = (input('Silakan masukkan nama: ')) #data masukan

x = lelaki(nama) #variabel x menampung jumlah huruf yang mengidentifikasikan nama laki-laki
y = perempuan(nama) #variabel y menampung jumlah huruf yang mengidentifikasikan nama perempuan

if y > x : #rule pertama
    print('Nama Tersebut Adalah: PEREMPUAN')
elif x > y : #rule kedua
    print('Nama Tersebut Adalah: LAKI-LAKI')
else: #rule ketiga
    print('Nama Tersebut Adalah: LAKI-LAKI')

#Percobaan:
#1. Ariij = Perempuan
#2. Faisal = Perempuan
#3. Robi = Laki-laki

#Analisis:
#Nama saya sendiri Ariij dan nama teman saya Faisal yang notabene adalah nama yang biasanya digunakan oleh laki-laki
#ternyata teridentifikasi sebagai perempuan, sedangkan contoh ketiga nama Robi berhasil teridetifikasi sebagai laki-laki
#hal tersebut dapat terjadi karena masih sangat sederhana nya rule dan parameter penentu dalam program ini
#sehingga masih banyak celah program untuk mengalami kesalahan saat mengidentifikasi nama
#penentuan hanya berdasarkan jumlah kemunculan huruf saya nilai terlalu subjektif
#mengingat sangat beragam nya bahasa, budaya dan tatacara penamaan yang ada