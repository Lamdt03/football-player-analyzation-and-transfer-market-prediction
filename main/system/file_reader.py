def read_file_by_line(file_path):
    try:
        with open(file_path, "r") as file:
            contents = [line.strip() for line in file.readlines()]
            return contents
    except FileNotFoundError:
        print("File not found. Make sure the file exists at the specified path.")
        return []
    except PermissionError:
        print("Permission denied. Check if you have read permissions for the file.")
        return []