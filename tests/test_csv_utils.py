
from devtoolkit.csv_utils import read_csv, csv_info, csv_head


def test_read_csv_returns_headers_and_rows(tmp_path):
    csv_file = tmp_path / "employees.csv"
    csv_file.write_text(
        "name,department\nAnas,Engineering\nSara,Finance\n",
        encoding="utf-8",
    )

    headers, rows = read_csv(csv_file)

    assert headers == ["name", "department"]
    assert len(rows) == 2
    assert rows[0]["name"] == "Anas"
    assert rows[1]["department"] == "Finance"


def test_csv_info_displays_row_and_column_counts(tmp_path, capsys):
    csv_file = tmp_path / "employees.csv"
    csv_file.write_text(
        "name,salary\nAnas,50000\nSara,58000\n",
        encoding="utf-8",
    )

    csv_info(csv_file)

    output = capsys.readouterr().out

    assert "Rows: 2" in output
    assert "Columns: 2" in output
    assert "name" in output
    assert "salary" in output


def test_csv_head_displays_limited_rows(tmp_path, capsys):
    csv_file = tmp_path / "employees.csv"
    csv_file.write_text(
        "name,department\nAnas,Engineering\nSara,Finance\nRahul,Marketing\n",
        encoding="utf-8",
    )

    csv_head(csv_file, limit=2)

    output = capsys.readouterr().out

    assert "Anas" in output
    assert "Sara" in output
    assert "Rahul" not in output

