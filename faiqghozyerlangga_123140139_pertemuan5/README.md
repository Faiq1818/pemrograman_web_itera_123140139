# Sistem Manajemen Perpustakaan Sederhana

## Fitur Utama

- Menambahkan data buku atau magazine
- Mengecek item yang ada
- Mencari data item berdasarkan nama

## Screenshot Aplikasi
#### Tampilan Help
![Screenshot 1](./screenshots/screenshot1.png)

#### Menambahkan data dan menampilkan data
![Screenshot 2](./screenshots/screenshot2.png)

#### Mencari data
![Screenshot 3](./screenshots/screenshot3.png)

## Cara Menjalankan Aplikasi

1. Clone repository:
   ```
   git clone https://github.com/Faiq1818/pemrograman_web_itera_123140139.git
   ```
2. Masuk ke folder tugasnya
   ```
   cd pemrograman_web_itera_123140139/faiqghozyerlangga_123140139_pertemuan5
   ```
3. Install dependensi (Pastikan poetry telah terinstall untuk management dependency, jika belum, silahkan install di dokumentasi resminya)
   ```
   poetry install --no-root
   ```
4. Jalankan localhost
   ```
   poetry run python main.py -h
   ```

## Pengguanan fitur OOP
1. Penggunaan argparse dan pengeksekusian methode oop

Ini adalah kode main.py saya sebagai entry file dan entry point, akan mengeksekusi methode dari class Library berdasarkan argumen dan flag yg dimasukan
#### main.py
```py
import argparse
from src.library import Library

def main():
    parser = argparse.ArgumentParser(description="Sistem Manajemen Perpustakaan Sederhana")

    parser.add_argument(
        '-a', '--add',
        action='store_true',
        help='Add new book or magazine'
    )
    parser.add_argument(
        '-s', '--show',
        action='store_true',
        help='Show collection of book and magazine'
    )
    parser.add_argument(
        '-f', '--find',
        type=str,
        help='Find an item using name'
    )
    args = parser.parse_args()

    if args.add:
        Library.Add()

    if args.show:
        Library.Show()

    if args.find:
        Library.Find(args.find)

if __name__ == "__main__":
    main()

```

2. Static methode dan penggunaan protected attribute dari class lain

Kode ini berfungsi untuk menampilkan dan mencari data, fungsi ini adalah sebuah staticmethode dari class Library, terlihat bahwa salah satu fungsi ini juga menggunakan protected attribute dari objek lain
#### src/library.py
```py
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

```
3. Abstract methode, inheritance, private dan protected attribute

Kode ini memiliki abstract methode class yg bernama LibraryItem, class ini memiliki private dan protected attribute serta methode dan property, class Book dan Magazine menginheritance class Library items
#### src/library_item.py
```py
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, name: str, year: int):
        self._name = name
        self.__year = year

    @property
    def year(self):
        return self.__year

    @abstractmethod
    def get_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, name, year):
        super().__init__(name, year)
        self.category = "Book"

    def get_info(self):
        return {
            "name": self._name,
            "year": self.year,
            "category": self.category
        }

class Magazine(LibraryItem):
    def __init__(self, name, year):
        super().__init__(name, year)
        self.category = "Magazine"

    def get_info(self):
        return {
            "name": self._name,
            "year": self.year,
            "category": self.category
        }

```
