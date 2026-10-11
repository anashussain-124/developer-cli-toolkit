
import json
from pathlib import Path


def read_json(file_path):
    """Read and parse a JSON file."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"JSON file not found: {file_path}"
        )

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def json_info(file_path):
    """Display information about a JSON file."""
    try:
        data = read_json(file_path)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return
    except json.JSONDecodeError as error:
        print(f"Invalid JSON at line {error.lineno}: {error.msg}")
        return
    except OSError as error:
        print(f"Error reading file: {error}")
        return

    if isinstance(data, dict):
        root_type = "Object"
        count = len(data)
    elif isinstance(data, list):
        root_type = "Array"
        count = len(data)
    else:
        root_type = type(data).__name__
        count = 1

    print(f"File: {file_path}")
    print(f"Root type: {root_type}")
    print(f"Top-level items: {count}")


def json_pretty(file_path):
    """Print JSON with indentation."""
    try:
        data = read_json(file_path)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return
    except json.JSONDecodeError as error:
        print(f"Invalid JSON at line {error.lineno}: {error.msg}")
        return
    except OSError as error:
        print(f"Error reading file: {error}")
        return

    print(json.dumps(data, indent=4, ensure_ascii=False))


def json_keys(file_path):
    """Display top-level keys in a JSON object."""
    try:
        data = read_json(file_path)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return
    except json.JSONDecodeError as error:
        print(f"Invalid JSON at line {error.lineno}: {error.msg}")
        return
    except OSError as error:
        print(f"Error reading file: {error}")
        return

    if not isinstance(data, dict):
        print("Error: JSON root must be an object to list keys.")
        return

    if not data:
        print("JSON object contains no keys.")
        return

    print("JSON keys:")
    for key in data:
        print(f"- {key}")
