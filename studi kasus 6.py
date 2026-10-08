import json
import os

def lihat_barang():
    print("=" * 30)
    print("Daftar Barang")
    print("=" * 30)
    with open("barang.json", "r", encoding="utf-8") as file:
        barang = json.load(file)

        for item in barang:
            print(f"Nama: {item['nama']}, Stok: {item['stok']}")

def tambah_barang():
    with open("barang.json", "r", encoding="utf-8") as file:
        barang = json.load(file)

        print("=" * 30)
        print("Tambah Barang")
        print("=" * 30)
        nama_barang = input("Nama Barang: ")
        stok_barang = int(input("Stok Barang: "))
        data_baru = {
            "nama": nama_barang,
            "stok": stok_barang
        }
        barang.append(data_baru)

        with open (r"barang.json", "w", encoding="utf-8") as file:
            json.dump(barang, file, indent=4)

def main():
    while True:
        print("=" * 30)
        print("MENU")
        print("=" * 30)
        print("1. Lihat Barang")
        print("2. Tambah Barang")
        print("3. Keluar")
        pilihan = input("\nPilih menu: ")

        os.system("cls" if os.name == "nt" else "clear")
        if pilihan == "1":
            lihat_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program ini.")
            break
        else:
            print("\nPilihan tidak valid. Silahkan coba lagi.")

main()