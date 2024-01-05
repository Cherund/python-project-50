from gendiff.genereting_difference import generate_diff
from pathlib import Path


def test_diff():
    current_dir = Path(__file__).parent

    file1_path = f'{current_dir}/fixtures/file1.json'
    file2_path = f'{current_dir}/fixtures/file2.json'
    with open(f'{current_dir}/fixtures/result') as output:
        assert generate_diff(file1_path, file2_path) == output.read()
