import os
def add(x, y):
    return x + y

def is_file_available(file_path):
    return os.path.exists(file_path)

def is_excel_file(file_path):
    return file_path.lower().endswith(('.xls', '.xlsx'))

def determine_skus(model_size):
    # Example logic to determine Skus based on model size
    if model_size < 100:
        return 'small_sku'
    elif 100 <= model_size < 500:
        return 'medium_sku'
    else:
        return 'large_sku'