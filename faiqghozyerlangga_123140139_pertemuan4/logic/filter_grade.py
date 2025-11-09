from data.dictionary import mahasiswa
from logic.summary import summary
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text


def filter_grade():

    title = Text("Pilih grade yang ingin di filter", style="bold cyan")
    menu_text = (
        "A\n"
        "B\n"
        "C\n"
        "D\n"
        "E"
    )

    console = Console()
    console.print(Panel(menu_text, title=title, border_style="red"))

    choose = input("Pilih grade: ")

    table = Table(title="Tabel data mahasiswa yang telah di filter")

    table.add_column("Nama", justify="left", style="cyan", no_wrap=True)
    table.add_column("NIM", justify="left", style="magenta")
    table.add_column("Nilai UTS", justify="left", style="green")
    table.add_column("Nilai UAS", justify="left", style="green")
    table.add_column("Nilai Tugas", justify="left", style="green")
    table.add_column("Nilai Akhir", justify="left", style="green")
    table.add_column("Grade", justify="left", style="green")

    for mhs in mahasiswa:
        nilai_akhir = summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])
        
        if choose == "A":
            if nilai_akhir >= 80:
                table.add_row(
                    mhs["nama"],
                    mhs["nim"],
                    str(mhs["nilai_uts"]),
                    str(mhs["nilai_uas"]),
                    str(mhs["nilai_tugas"]),
                    str(summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])),
                    "A"
                )
        elif choose == "B":
            if nilai_akhir >= 70 and nilai_akhir < 80:
                table.add_row(
                    mhs["nama"],
                    mhs["nim"],
                    str(mhs["nilai_uts"]),
                    str(mhs["nilai_uas"]),
                    str(mhs["nilai_tugas"]),
                    str(summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])),
                    "B"
                )
        elif choose == "C":
            if nilai_akhir >= 60 and nilai_akhir < 70:
                table.add_row(
                    mhs["nama"],
                    mhs["nim"],
                    str(mhs["nilai_uts"]),
                    str(mhs["nilai_uas"]),
                    str(mhs["nilai_tugas"]),
                    str(summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])),
                    "C"
                )
        elif choose == "D":
            if nilai_akhir >= 50 and nilai_akhir < 60:
                table.add_row(
                    mhs["nama"],
                    mhs["nim"],
                    str(mhs["nilai_uts"]),
                    str(mhs["nilai_uas"]),
                    str(mhs["nilai_tugas"]),
                    str(summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])),
                    "D"
                )
        elif choose == "E":
            if nilai_akhir < 50:
                table.add_row(
                    mhs["nama"],
                    mhs["nim"],
                    str(mhs["nilai_uts"]),
                    str(mhs["nilai_uas"]),
                    str(mhs["nilai_tugas"]),
                    str(summary(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])),
                    "E"
                )

    console = Console()
    console.print(table)
