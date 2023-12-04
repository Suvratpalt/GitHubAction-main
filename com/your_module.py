import os
def add(x, y):
    return x + y

def is_file_available(file_path):
    return os.path.exists(file_path)

def is_excel_file(file_path):
    return file_path.lower().endswith(('.xls', '.xlsx'))