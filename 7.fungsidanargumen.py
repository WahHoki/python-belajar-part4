# dungsi dengan argumen (input)

# def nama_fungsi(argumen/parameter):
#      badan fungsi
def nama_fungsi(nama):
       # ini adalah badan fungsinya
       # fungsi nama_fungsi akan menerima input dengan variabel
       print(f"Selamat datang wahai{nama}")

nama_fungsi("ucup")
nama_fungsi("otong")

# program tambah

def tambah(angka_1,angka_2):
       hasil = angka_1 + angka_2
       print(f"hasil dari {angka_1} + {angka_2} = {hasil}")

tambah(4,5)
tambah(3,7)

def say_hi(list_peserta):
       # ini adalah fungsi say_hi
       data_peserta = list_peserta.copy()
       for peserta in data_peserta:
              print(f"Hello {peserta}")

anggota_boyband = ["ucup","otong","budi","andi"]

say_hi(anggota_boyband)
