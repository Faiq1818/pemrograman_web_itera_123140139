from data.dictionary import mahasiswa
from summary import summary
from rich.console import Console
from rich.table import Table


def show_all_data():
    table = Table(title="Tabel Data Mahasiswa")

    table.add_column("Nama", justify="left", style="cyan", no_wrap=True)
    table.add_column("NIM", justify="left", style="magenta")
    table.add_column("Nilai UTS", justify="left", style="green")
    table.add_column("Nilai UAS", justify="left", style="green")
    table.add_column("Nilai Tugas", justify="left", style="green")

    for mhs in mahasiswa:
        table.add_row(
            mhs["nama"],
            mhs["nim"],
            str(mhs["nilai_uts"]),
            str(mhs["nilai_uas"]),
            str(mhs["nilai_tugas"])
        )
    summary()

    console = Console()
    console.print(table)

