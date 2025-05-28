# multi keys dan nesting dictionary
import datetime

mahasiswa1 ={
       'nama':'ucup',
       'nim':'220010101',
       'sks':'130',
       'beasiswa':False,
       'lahir':datetime.datetime(2004,4,10)
}
mahasiswa2 ={
       'nama':'cecep',
       'nim':'220010102',
       'sks':'127',
       'beasiswa':False,
       'lahir':datetime.datetime(2000,1,30)
}
mahasiswa3 ={
       'nama':'ucup cecep',
       'nim':'220010101',
       'sks':'135',
       'beasiswa':True,
       'lahir':datetime.datetime(2002,2,16)
}

data_mahasiswa = {
       'MAH001':mahasiswa1,
       'MAH002':mahasiswa2,
       'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("="*50)

for mahasiswa in data_mahasiswa:
       KEY = mahasiswa
       NAMA = data_mahasiswa[KEY]['nama']
       NIM = data_mahasiswa[KEY]['nim']
       SKS = data_mahasiswa[KEY]['sks']
       BEASISWA = data_mahasiswa[KEY]['beasiswa']
       LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

       print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
       
