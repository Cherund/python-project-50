from gendiff.generate_difference import generate_diff
from pathlib import Path


FIXTURES_DIR = f'{Path(__file__).parent}/fixtures/hexlet'


def test_nested_json_diff():
    file1_path = f'{FIXTURES_DIR}/file1.json'
    file2_path = f'{FIXTURES_DIR}/file2.json'

    with open(f'{FIXTURES_DIR}/result_stylish') as output:
        assert generate_diff(file1_path, file2_path) == output.read()

    with open(f'{FIXTURES_DIR}/result_plain') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()


def test_nested_yaml_diff():
    file1_path = f'{FIXTURES_DIR}/file1.yml'
    file2_path = f'{FIXTURES_DIR}/file2.yml'

    with open(f'{FIXTURES_DIR}/result_stylish') as output:
        assert generate_diff(file1_path, file2_path) == output.read()

    with open(f'{FIXTURES_DIR}/result_plain') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()


