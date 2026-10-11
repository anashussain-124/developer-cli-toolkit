
import csv
from pathlib import Path


def read_csv(file_path):
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"CSV file not found: {file_path}"
        )

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError(
                "CSV file is empty or has no header row."
            )

        headers = reader.fieldnames

        if any(not header.strip() for header in headers):
            raise ValueError(
                "CSV contains an empty column name."
            )

        if len(headers) != len(set(headers)):
            raise ValueError(
                "CSV contains duplicate column names."
            )

        rows = list(reader)

        for row_number, row in enumerate(rows, start=2):
            if None in row:
                raise ValueError(
                    f"CSV row {row_number} has extra columns."
                )

            if any(value is None for value in row.values()):
                raise ValueError(
                    f"CSV row {row_number} has missing columns."
                )

        return headers, rows


def csv_info(file_path):
    try:
        headers, rows = read_csv(file_path)

    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")
        return

    print(f"File: {file_path}")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(headers)}")
    print("Column names:")

    for header in headers:
        print(f"- {header}")


def csv_head(file_path, limit=5):
    if limit < 1:
        print("Error: limit must be at least 1.")
        return

    try:
        headers, rows = read_csv(file_path)

    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")
        return

    print(" | ".join(headers))
    print("-" * 40)

    for row in rows[:limit]:
        print(
            " | ".join(
                str(row.get(header, ""))
                for header in headers
            )
        )

    if not rows:
        print("No data rows found.")


def csv_summary(file_path):
    try:
        headers, rows = read_csv(file_path)

    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")
        return

    print(f"Total records: {len(rows)}")
    print(f"Total columns: {len(headers)}")

    for header in headers:
        non_empty = sum(
            1
            for row in rows
            if row.get(header) is not None
            and row[header].strip() != ""
        )

        print(f"{header}: {non_empty} non-empty values")
