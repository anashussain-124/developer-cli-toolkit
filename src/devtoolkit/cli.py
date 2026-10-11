
import argparse

from devtoolkit.file_utils import (
    get_file_info,
    list_files,
    count_text,
)
from devtoolkit.csv_utils import (
    csv_info,
    csv_head,
    csv_summary,
)
from devtoolkit.json_utils import (
    json_info,
    json_pretty,
    json_keys,
)
from devtoolkit.api_utils import api_get


def main():
    parser = argparse.ArgumentParser(
        prog="devtoolkit",
        description="A collection of useful developer utilities.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="devtoolkit 0.1.0",
    )
    parser.add_argument(
        "--author",
        action="store_true",
        help="Display the developer's name",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    # FILE COMMANDS
    files_parser = subparsers.add_parser(
        "files",
        help="File management utilities",
    )
    files_subparsers = files_parser.add_subparsers(
        dest="files_command"
    )

    info_parser = files_subparsers.add_parser(
        "info",
        help="Display file information",
    )
    info_parser.add_argument("path")

    list_parser = files_subparsers.add_parser(
        "list",
        help="List directory contents",
    )
    list_parser.add_argument(
        "path",
        nargs="?",
        default=".",
    )

    count_parser = files_subparsers.add_parser(
        "count",
        help="Count lines, words and characters",
    )
    count_parser.add_argument("path")

    # CSV COMMANDS
    csv_parser = subparsers.add_parser(
        "csv",
        help="CSV data processing utilities",
    )
    csv_subparsers = csv_parser.add_subparsers(
        dest="csv_command"
    )

    csv_info_parser = csv_subparsers.add_parser(
        "info",
        help="Display CSV information",
    )
    csv_info_parser.add_argument("path")

    csv_head_parser = csv_subparsers.add_parser(
        "head",
        help="Preview CSV rows",
    )
    csv_head_parser.add_argument("path")
    csv_head_parser.add_argument(
        "--limit",
        type=int,
        default=5,
    )

    csv_summary_parser = csv_subparsers.add_parser(
        "summary",
        help="Summarize CSV columns",
    )
    csv_summary_parser.add_argument("path")

    # JSON COMMANDS
    json_parser = subparsers.add_parser(
        "json",
        help="JSON data processing utilities",
    )
    json_subparsers = json_parser.add_subparsers(
        dest="json_command"
    )

    json_info_parser = json_subparsers.add_parser(
        "info",
        help="Display JSON information",
    )
    json_info_parser.add_argument("path")

    json_pretty_parser = json_subparsers.add_parser(
        "pretty",
        help="Print formatted JSON",
    )
    json_pretty_parser.add_argument("path")

    json_keys_parser = json_subparsers.add_parser(
        "keys",
        help="List top-level JSON keys",
    )
    json_keys_parser.add_argument("path")

    # API COMMANDS
    api_parser = subparsers.add_parser(
        "api",
        help="HTTP API utilities",
    )
    api_subparsers = api_parser.add_subparsers(
        dest="api_command"
    )

    api_get_parser = api_subparsers.add_parser(
        "get",
        help="Send an HTTP GET request",
    )
    api_get_parser.add_argument(
        "url",
        help="URL to request",
    )
    api_get_parser.add_argument(
        "--timeout",
        type=float,
        default=10,
        help="Request timeout in seconds (default: 10)",
    )

    args = parser.parse_args()

    if args.author:
        print("Developer: Anas")
        return

    if args.command == "files":
        if args.files_command == "info":
            get_file_info(args.path)
        elif args.files_command == "list":
            list_files(args.path)
        elif args.files_command == "count":
            count_text(args.path)
        else:
            files_parser.print_help()

    elif args.command == "csv":
        if args.csv_command == "info":
            csv_info(args.path)
        elif args.csv_command == "head":
            if args.limit < 1:
                parser.error("--limit must be at least 1")
            csv_head(args.path, args.limit)
        elif args.csv_command == "summary":
            csv_summary(args.path)
        else:
            csv_parser.print_help()

    elif args.command == "json":
        if args.json_command == "info":
            json_info(args.path)
        elif args.json_command == "pretty":
            json_pretty(args.path)
        elif args.json_command == "keys":
            json_keys(args.path)
        else:
            json_parser.print_help()

    elif args.command == "api":
        if args.api_command == "get":
            if args.timeout <= 0:
                parser.error("--timeout must be greater than zero")
            api_get(args.url, args.timeout)
        else:
            api_parser.print_help()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
