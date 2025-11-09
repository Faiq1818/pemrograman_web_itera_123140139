from data.dictionary import mahasiswa

def summary():
    for mhs in mahasiswa:
        nilai_akhir = mhs["nilai_uts"]
        print(nilai_akhir)
