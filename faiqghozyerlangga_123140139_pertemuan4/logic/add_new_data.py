from data.dictionary import mahasiswa
from rich.console import Console

def add_new_data():
    console = Console()

    nama = console.input("[bold magenta]Nama: ")
    nim = console.input("[bold magenta]NIM: ")
    nilai_uts = int(console.input("[bold magenta]Nilai UTS: "))
    nilai_uas = int(console.input("[bold magenta]Nilai UAS: "))
    nilai_tugas = int(console.input("[bold magenta]Nilai tugas: "))
    
    mahasiswa.append({"nama": nama, "nim": nim, "nilai_uts": nilai_uts, "nilai_uas": nilai_uas, "nilai_tugas": nilai_tugas})
