from logic.show_all_data import show_all_data
from logic.add_new_data import add_new_data

def main():
    while True:
        print("1. Tampilkan semua data")
        print("2. Tambah mahasiswa")
        print("5. Selesai")
        choose = input("Pilih salah satu: ")

        if choose == "1":
            show_all_data()
        elif choose == "2":
            add_new_data()
        elif choose == "5":
            break


if __name__ == "__main__":
    main()
