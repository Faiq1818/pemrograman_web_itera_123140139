from data.dictionary import mahasiswa
from logic.summary import summary
from rich.console import Console
from rich.table import Table


def show_all_data():
    table = Table(title="Tabel Data Mahasiswa")

    table.add_column("Nama", justify="left", style="cyan", no_wrap=True)
    table.add_column("NIM", justify="left", style="magenta")
    table.add_column("Nilai UTS", justify="left", style="green")
    table.add_column("Nilai UAS", justify="left", style="green")
    table.add_column("Nilai Tugas", justify="left", style="green")
    table.add_column("Nilai Akhir", justify="left", style="green")
    table.add_column("Grade", justify="left", style="green")

    for mhs in mahasiswa:
        nilai_akhir = summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])

        if nilai_akhir >= 80:
            grade = "A"
        elif nilai_akhir >= 70:
            grade = "B"
        elif nilai_akhir >= 60:
            grade = "C"
        elif nilai_akhir >= 50:
            grade = "D"
        else:
            grade = "E"

        table.add_row(
            mhs["nama"],
            mhs["nim"],
            str(mhs["nilai_uts"]),
            str(mhs["nilai_uas"]),
            str(mhs["nilai_tugas"]),
            str(summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])),
            grade
        )

    console = Console()
    console.print(table)

