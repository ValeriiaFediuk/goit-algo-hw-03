from pathlib import Path
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів за їхнім розширенням")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--destination", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dst)
            else:
                extension = item.suffix[1:]
                if extension:
                    extension_dir = dst / extension
                    extension_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy(item, extension_dir)
    except Exception as error:
        print(f"Помилка при копіюванні файлів: {error}")

def main():
    args = parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    copy_files(args.source, args.destination)

if __name__ == "__main__":
    main()
