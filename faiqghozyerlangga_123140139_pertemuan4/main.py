from logic.show_all_data import show_all_data
from logic.add_new_data import add_new_data
from logic.biggest_smallest_point import biggest_smallest_point
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def main():
    console = Console()
    while True:
        title = Text("Menu Utama", style="bold cyan")
        menu_text = (
            "1. Tampilkan semua data\n"
            "2. Tambah mahasiswa\n"
            "3. Cari mahasiswa dengan nilai tertinggi atau terendah\n"
            "4. Filter mahasiswa berdasarkan grade\n"
            "5. Selesai"
        )

        console.print(Panel(menu_text, title=title, border_style="bright_blue"))

        choose = input("Pilih salah satu: ")

        if choose == "1":
            show_all_data()
        elif choose == "2":
            add_new_data()
        elif choose == "3":
            biggest_smallest_point()
        elif choose == "4":
            biggest_smallest_point()
        elif choose == "5":
            break


if __name__ == "__main__":
    main()
