# folder_sort

A tiny Python script that organizes your **Downloads** folder into subfolders by file type

wrote this in 30 min honestly pretty helpful idk why i never wrote this
## Usage

```
git clone https://github.com/seraph27/folder_sort.git
cd folder_sort
python3 main.py --dir ~/Downloads
`--dir` is optional (defaults to `~/Downloads`).
```

## Auto-run (WSL)

If you want it to run automatically while WSL is open:
```
sudo apt install -y inotify-tools
chmod +x watch.sh
./watch.sh
```
## File Type Mapping

| Folder    | Extensions |
|-----------|------------|
| Pictures  | .png .jpg .jpeg .gif .bmp .tiff |
| Documents | .pdf .docx .txt .xlsx .pptx |
| Music     | .mp3 .wav .aac .flac |
| Videos    | .mp4 .mkv .avi .mov |
| Archives  | .zip .rar .tar .gz |
| Code      | .py .js .java .cpp .html .css |
| Scripts   | .sh .bat .ps1 |
| Misc      | everything else |
