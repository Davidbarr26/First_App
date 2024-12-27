import zipfile
import pathlib

def make_archieve(filepaths, destin_dir):
    destin_path = pathlib.Path(destin_dir, 'compressed.zip')
    with zipfile.ZipFile(destin_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == '__main__':
    make_archieve(filepaths=["file_compressor.py"], destin_dir='destin')