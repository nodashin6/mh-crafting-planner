#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

BACKEND_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BACKEND_DIR / "src"
CACHE_DIR = BACKEND_DIR / ".cache"

LINE = "=" * 12


def get_parser():
    parser = argparse.ArgumentParser(description="Code to Text")
    parser.add_argument(
        "-t", "--target", type=str, required=True, help="Path to input file"
    )
    return parser


def create_output_text_file(output_path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = CACHE_DIR / f"{timestamp}.txt"
    output_path.touch()
    return output_path


def code_to_text(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        code = f.read()
    return code


def output_text(output_path, text, py_file: Path):
    with open(output_path, "a", encoding="utf-8") as f:
        f.write("# " + str(py_file))
        f.write("\n")
        f.write(text)
        f.write(f"\n{LINE}\n")


def main(args):
    target_path = SRC_DIR / args.target
    output_path = create_output_text_file(target_path)
    if target_path.is_file():
        py_file = target_path
        code = code_to_text(py_file)
        output_text(output_path, code, py_file)

    elif target_path.is_dir():
        py_files = target_path.glob("**/*.py")
        for py_file in py_files:
            code = code_to_text(py_file)
            output_text(output_path, code, py_file)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    main(args)
