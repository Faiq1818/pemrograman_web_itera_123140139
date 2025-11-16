import json
from rich.console import Console
from rich.table import Table

class Library:
    @staticmethod
    def Add():
        print("Simpan buku atau magazine")

        item_name = input("Masukan nama item: ")
        item_year = input("Masukan tahun rilis: ")
        item_categories = input("Masukan kategori (jika buku b, jika magazine m): ")

        new_data = {
            "name": item_name,
            "year": item_year,
            "categories": item_categories
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
