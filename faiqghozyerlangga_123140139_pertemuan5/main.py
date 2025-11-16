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
    args = parser.parse_args()

    if args.add:
        Library.Add()

    if args.show:
        Library.Show()

if __name__ == "__main__":
    main()
