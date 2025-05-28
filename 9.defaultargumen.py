# default argument

# def fungsi(argument):
# def fungsi(argument = nilai default):


def say_hello(nama = "bro"):
       # fungsi dengan default argument
       print(f"hallo {nama}")

say_hello("ucup")
say_hello()

def sapa_dia(nama,pesan = "apa kabar?"):
       # fungsi dengan satu inpur biasa dan satu input default
       print(f"{pesan} {nama}")

sapa_dia("ucup","gimana kabarmu?")
sapa_dia("ucup")


# contoh 3

def hitung_pangkat(angka, pangkat):
       hasil = angka**pangkat
       return hasil

print(hitung_pangkat(2,3))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh 4

def fungsi(input1=1, input2=2, input3=3, input4=4):
       hasil = input1 + input2 + input3 + input4
       return hasil

print(fungsi())
print(fungsi(input3=10))
