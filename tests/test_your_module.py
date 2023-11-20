from com import your_module

def test_add():
    assert your_module.add(2, 3) == 5
def test_is_file_available(tmp_path):
    file_path = tmp_path / "test_file.txt"
    file_path.touch()

    # Test if the file is available
    assert your_module.is_file_available(file_path)

    # Test with a non-existing file
    non_existing_file = tmp_path / "non_existing_file.txt"
    assert not your_module.is_file_available(non_existing_file)