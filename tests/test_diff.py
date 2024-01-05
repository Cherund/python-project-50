from gendiff.genereting_difference import generate_diff
from pathlib import Path



FIXTURES_DIR = f'{Path(__file__).parent}/fixtures'
def test_flat_json_diff():
    file1_path = f'{FIXTURES_DIR}/file1.json'
    file2_path = f'{FIXTURES_DIR}/file2.json'
    with open(f'{FIXTURES_DIR}/result') as output:
        assert generate_diff(file1_path, file2_path) == output.read()


def test_flat_yml_diff():
    file1_path = f'{FIXTURES_DIR}/file1.yml'
    file2_path = f'{FIXTURES_DIR}/file2.yml'

    with open(f'{FIXTURES_DIR}/result') as output:
        assert generate_diff(file1_path, file2_path) == output.read()
