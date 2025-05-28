# Fungsi kuadrat
def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

# Fungsi tambah
def tambah(angka_1, angka_2):
    return angka_1 + angka_2

# Fungsi dengan return banyak
def operasi_matematika(operasi):
    if operasi == "+":
        return angka_1 + angka_2
    elif operasi == "-":
        return angka_1 - angka_2
    elif operasi == "*":
        return angka_1 * angka_2
    elif operasi == "/":
        return angka_1 / angka_2
    else:
        return "Operasi tidak dikenal"

# Input angka dan operasi
angka_1 = int(input("Masukkan angka pertama: "))
angka_2 = int(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi (+,-,*,/): ")

# Cetak hasil operasi
hasil = operasi_matematika(operasi)
print(f"Hasil dari {operasi} adalah: {hasil}")
