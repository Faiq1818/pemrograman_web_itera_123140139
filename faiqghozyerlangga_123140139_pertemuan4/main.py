from logic.show_all_data import show_all_data


def main():
    while True:
        print("1. Tampilkan semua data")
        print("2. Tampilkan semua data")
        choose = input("Pilih salah satu: ")
        if choose == "1":
            show_all_data()


if __name__ == "__main__":
    main()
