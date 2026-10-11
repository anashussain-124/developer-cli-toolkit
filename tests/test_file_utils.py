
from devtoolkit.file_utils import (
    get_file_info,
    count_text,
)


def test_get_file_info_prints_file_details(tmp_path, capsys):
    test_file = tmp_path / "example.txt"
    test_file.write_text("Hello Python", encoding="utf-8")

    get_file_info(test_file)

    output = capsys.readouterr().out

    assert "Name: example.txt" in output
    assert "Extension: .txt" in output
    assert "Size: 12 bytes" in output


def test_get_file_info_handles_missing_file(tmp_path, capsys):
    missing_file = tmp_path / "missing.txt"

    get_file_info(missing_file)

    output = capsys.readouterr().out

    assert "does not exist" in output


def test_count_text_counts_lines_words_and_characters(
    tmp_path,
    capsys,
):
    test_file = tmp_path / "notes.txt"
    test_file.write_text(
        "Hello Python\nLearn testing\n",
        encoding="utf-8",
    )

    count_text(test_file)

    output = capsys.readouterr().out

    assert "Lines: 2" in output
    assert "Words: 4" in output
    assert "Characters: 27" in output
