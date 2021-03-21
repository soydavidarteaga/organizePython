import os 
import shutil
import sys

def directory(file_extension: str) -> str :
    if not file_extension:
        return

    folders_by_extension = {
        "exe": "Software",
        "txt": "Texts",
        "pdf": "PDF Documents",
        "epub": "Books",
        "jpg": "Images",
        "jpeg": "Images",
        "png": "Images",
        "raw": "Images",
        "mp3": "Music",
        "mp4": "Videos",
        "mkv": "Videos",
        "xlsx": "Excel Files",
        "ppt": "Slides",
        "doc": "Documents",
        "rar": "Compressed Files",
        "zip": "Compressed Files"
    }
    return folders_by_extension.get(file_extension, 'Extras')

def organize(path:str):
    if not os.path.exists(path):
        print(f"ERROR. Not found {path} or not exixsts.")
        return 
    files = os.listdir(path)
    extensions = [os.path.splitext(file)[1].strip(".") for file in files]

    for ext in extensions:
        dir = directory(ext) or ""
        new_directory = os.path.join(path, dir)
        if dir and not os.path.exists(new_directory):
            os.makedirs(new_directory)

    for file in files:
        ext = os.path.splitext(file)[1].strip(".")
        _dir = directory(ext)
        if not _dir:
            continue

        source_filepath = os.path.join(path, file)
        destination_filepath = os.path.join(path, _dir, file)

        if not os.path.exists(destination_filepath):
            shutil.move(source_filepath, destination_filepath)
            print(f"Se ha movido {file} en {_dir} directorio \n")
            print(f"Todos los archivos se han organizado correctamente en  {path}")

if __name__ == "__main__":
    try:
        directory_location = sys.argv[1]
        organize(directory_location)
    except Exception as e:
        print(f"Hemos detectado un error: {str(e)}")