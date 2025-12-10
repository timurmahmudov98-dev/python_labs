import argparse
from pathlib import Path

import sys

sys.path.append(r"C:\Users\user\Desktop\python_labs\src")
from lib_with_funcs_from_lab05.csv_xlsx import *
from lib_with_funcs_from_lab05.json_csv import *


def main():
    parser = argparse.ArgumentParser(description="CLI для конвертации файла")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # подкоманда json2csv
    json2csv_parser = subparsers.add_parser("json2csv", help="JSON -> CSV")
    json2csv_parser.add_argument(
        "--in", required=True, dest="input_file", help="Входной JSON"
    )
    json2csv_parser.add_argument(
        "--out", required=True, dest="output_file", help="Выходной CSV"
    )

    # подкоманда csv2json
    csv2json_parser = subparsers.add_parser("csv2json", help="CSV -> JSON")
    csv2json_parser.add_argument(
        "--in", required=True, dest="input_file", help="Вхдной CSV"
    )
    csv2json_parser.add_argument(
        "--out", required=True, dest="output_file", help="Выходной JSON"
    )

    # подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="CSV -> XLSX")
    csv2xlsx_parser.add_argument(
        "--in", required=True, dest="input_file", help="Входной CSV"
    )
    csv2xlsx_parser.add_argument(
        "--out", required=True, dest="output_file", help="Выходной XLSX"
    )

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input_file, args.output_file)
        elif args.command == "csv2json":
            csv_to_json(args.input_file, args.output_file)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input_file, args.output_file)
    except Exception as e:
        parser.error


if __name__ == "__main__":
    main()
