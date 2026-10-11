
from pathlib import Path


def get_file_info(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: '{file_path}' does not exist.")
        return

    if not path.is_file():
        print(f"Error: '{file_path}' is not a file.")
        return

    try:
        print(f"Name: {path.name}")
        print(f"Extension: {path.suffix or '(none)'}")
        print(f"Size: {path.stat().st_size} bytes")
    except OSError as error:
        print(f"Error accessing file: {error}")


def list_files(directory):
    path = Path(directory)

    if not path.exists():
        print(f"Error: '{directory}' does not exist.")
        return

    if not path.is_dir():
        print(f"Error: '{directory}' is not a directory.")
        return

    try:
        items = sorted(path.iterdir(), key=lambda item: item.name.lower())

        if not items:
            print("Directory is empty.")
            return

        for item in items:
            kind = "DIR " if item.is_dir() else "FILE"
            print(f"{kind}  {item.name}")

    except OSError as error:
        print(f"Error listing directory: {error}")


def count_text(file_path):
    path = Path(file_path)

    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: '{file_path}' does not exist.")
        return
    except IsADirectoryError:
        print(f"Error: '{file_path}' is a directory, not a file.")
        return
    except UnicodeDecodeError:
        print("Error: File is not valid UTF-8 text.")
        return
    except OSError as error:
        print(f"Error reading file: {error}")
        return

    print(f"Lines: {len(text.splitlines())}")
    print(f"Words: {len(text.split())}")
    print(f"Characters: {len(text)}")
