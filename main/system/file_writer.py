import os
from pathlib import Path


def write_file_by_line(file_path, contents: [], mode):
    try:
        filepath = Path(file_path)
        if not os.path.exists(filepath.parent):
            os.makedirs(filepath.parent)
        with open(file_path, mode) as file:
            for content in contents:
                file.write(content + "\n")
        return True
    except Exception as e:
        print("write ", file_path, " failed: ", e)
        return False
