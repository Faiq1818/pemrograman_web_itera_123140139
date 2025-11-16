import json
from rich.console import Console
from rich.table import Table
from .library_item import Book, Magazine

class Library:
    @staticmethod
    def load_items():
        try:
            with open("data/data.json") as f:
                raw = json.load(f)
        except:
            return []

        items = []
        for i in raw:
            if i["categories"] == "b":
                items.append(Book(i["name"], int(i["year"])))
            else:
                items.append(Magazine(i["name"], int(i["year"])))

        return items

    @staticmethod
    def Add():
        print("Simpan buku atau magazine")

        item_name = input("Masukan nama item: ")
        item_categories = input("Masukan kategori (jika buku b, jika magazine m): ")

        while True:
            item_year = input("Masukan tahun rilis: ")
            if item_year.isdigit():
                item_year = int(item_year)
                break
            else:
                print("Tahun harus berupa angka!")

        if item_categories == "m":
            categories = "Magazine"
        elif item_categories == "b":
            categories = "Buku"
        else:
            print("Kategori tidak sesuai!")
            return

        new_data = {
            "name": item_name,
            "year": str(item_year),
            "categories": categories 
        }

        try:
            with open("data/data.json") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_data)

        with open("data/data.json", "w") as f:
            json.dump(data, f, indent=4)


    @staticmethod
    def Show():
        table = Table(title="Tabel Data Perpustakaan")

        table.add_column("Nama", justify="left", style="cyan")
        table.add_column("Kategori", justify="left", style="magenta")
        table.add_column("Tahun", justify="left", style="magenta")

        with open("data/data.json") as f:
            data = json.load(f)

        for item in data:
            table.add_row(
                item["name"],
                item["categories"],
                item["year"]
            )

        console = Console()
        console.print(table)
    
    @staticmethod
    def Find(keyword):
        keyword = keyword.lower()
        hasil = []

        items = Library.load_items()

        for item in items:
            if keyword in item._name.lower():
                hasil.append(item)

        if not hasil:
            print("Tidak ditemukan.")
            return

        table = Table(title="Hasil Pencarian")
        table.add_column("Judul")
        table.add_column("Kategori")
        table.add_column("Tahun")

        for item in hasil:
            info = item.get_info()
            table.add_row(info["name"], info["category"], str(info["year"]))

        Console().print(table)
