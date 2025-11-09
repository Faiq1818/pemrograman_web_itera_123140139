from data.dictionary import mahasiswa
from logic.summary import summary
from rich.console import Console
from rich.table import Table

def biggest_smallest_point():
    table = Table(title="Nilai terbesar dan terkecil")
    biggest = 0
    smallest = 99999999
    for mhs in mahasiswa:
        nilai_akhir = summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])
        if nilai_akhir > biggest:
            biggest = nilai_akhir
        if nilai_akhir < smallest:
            smallest = nilai_akhir

    table.add_column("Terbesar", justify="left", style="cyan")
    table.add_column("Terkecil", justify="left", style="cyan")

    table.add_row(str(biggest), str(smallest))

    console = Console()
    console.print(table)
