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
