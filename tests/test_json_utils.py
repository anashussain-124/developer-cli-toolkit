
import json

from devtoolkit.json_utils import read_json, json_info, json_keys


def test_read_json_returns_python_data(tmp_path):
    json_file = tmp_path / "config.json"
    expected = {
        "app": "Developer CLI Toolkit",
        "debug": True,
    }
    json_file.write_text(
        json.dumps(expected),
        encoding="utf-8",
    )

    data = read_json(json_file)

    assert data == expected
    assert data["app"] == "Developer CLI Toolkit"


def test_json_info_displays_object_details(tmp_path, capsys):
    json_file = tmp_path / "config.json"
    json_file.write_text(
        '{"name": "Anas", "active": true}',
        encoding="utf-8",
    )

    json_info(json_file)

    output = capsys.readouterr().out

    assert "Root type: Object" in output
    assert "Top-level items: 2" in output


def test_json_keys_displays_top_level_keys(tmp_path, capsys):
    json_file = tmp_path / "config.json"
    json_file.write_text(
        '{"name": "Anas", "language": "Python"}',
        encoding="utf-8",
    )

    json_keys(json_file)

    output = capsys.readouterr().out

    assert "- name" in output
    assert "- language" in output
