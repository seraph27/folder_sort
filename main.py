"""
proj 1.
local file sorter
python3 main.py --dir "/mnt/c/Users/rexch/Downloads" (on wsl2) 
"""

from pathlib import Path
import argparse

mapping = {
    "Pictures" : [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music"    : [".mp3", ".wav", ".aac", ".flac"],
    "Videos"   : [".mp4", ".mkv", ".avi", ".mov"],
    "Archives" : [".zip", ".rar", ".tar", ".gz"],
    "Code"  : [".py", ".js", ".java", ".cpp", ".html", ".css"],
    "Scripts"  : [".sh", ".bat", ".ps1"],
    "Misc"     : []
}

def sort_file(file: Path, base: Path):
    ext = file.suffix.lower()
    for folder, extensions in mapping.items():
        if ext in extensions:
            return move(file, base / folder)
    return move(file, base / "Misc")

def move(file: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True)
    dest = target_folder / file.name
    base = file.stem
    ext = file.suffix
    count = 1
    while dest.exists():
        dest = target_folder / f"{base}({count}){ext}"
        count += 1
    file.rename(dest)
    return dest

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=str(Path.home() / "Downloads"), help="Directory to sort, default=Downloads")
    args = ap.parse_args()

    base = Path(args.dir).expanduser()
    for f in base.iterdir():
        if f.is_file():
            new_path = sort_file(f, base)
            print(f"Moved: {f.name} -> {new_path}")


if __name__ == "__main__":
    main()
