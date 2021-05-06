#metode dengan mode "w"

print("Selamat datang di Program Biodata")
print("=================================")

print("Isilah Biodata di bawah ini dengan benar!")
nama = input("Nama : ")
nim = input("NIM : ")
jenis_kelamin = input("Jenis Kelamin : ")
tempat_lahir = input("Tempat Lahir :")
tanggal_lahir = input("Tanggal Lahir :")
umur = input("Umur: ")
jurusan = input("Jurusan :")
alamat = input("Alamat : ")

#format teks
teks = "Nama: {}\nNIM: {}\nJenis Kelamin: {}\nTempat Lahir: {}\nTanggal Lahir: {}\nUmur: {}\nJurusan: {}\nAlamat: {}\n".format(nama, nim, jenis_kelamin, tempat_lahir, tanggal_lahir, umur, jurusan, alamat)

#buka file untuk ditulis
file_bio = open("biodata.txt", "w")

#tulis teks ke file
file_bio.write(teks)

#tutup file
file_bio.close()
