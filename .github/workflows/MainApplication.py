from com import your_module
import os

# Your main application logic
# ...

# Example usage:
model_size = 150
required_files = ["file1.xlsx", "file2.xlsx"]

for file in required_files:
    file_path = os.path.join("path/to/artifacts", file)
    if your_module.is_file_available(file_path):
        if your_module.is_excel_file(file_path):
            sku = your_module.determine_skus(model_size)
            print(f"SKU for {file}: {sku}")
        else:
            print(f"{file} is not a valid Excel file.")
    else:
        print(f"{file} is not available.")
