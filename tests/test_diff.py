from gendiff.generate_difference import generate_diff
from pathlib import Path
import pytest

FIXTURES_DIR = f'{Path(__file__).parent}/fixtures'


@pytest.mark.parametrize(
    ('file1', 'file2'),
    [
        ('file1.json', 'file2.json'),
        ('file1.yml', 'file2.yml'),
    ]
)
def test_flat_diff(file1, file2):
    file1_path = f'{FIXTURES_DIR}/{file1}'
    file2_path = f'{FIXTURES_DIR}/{file2}'

    with open(f'{FIXTURES_DIR}/flat_result') as output:
        assert generate_diff(file1_path, file2_path) == output.read()

    with open(f'{FIXTURES_DIR}/flat_plain_result') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()

    with open(f'{FIXTURES_DIR}/flat_json_result') as output:
        assert generate_diff(file1_path, file2_path, 'json') == output.read()


@pytest.mark.parametrize(
    ('file1', 'file2'),
    [
        ('nested_file1.json', 'nested_file2.json'),
        ('nested_file1.yml', 'nested_file2.yml'),
    ]
)
def test_nested_json_diff(file1, file2):
    file1_path = f'{FIXTURES_DIR}/{file1}'
    file2_path = f'{FIXTURES_DIR}/{file2}'

    with open(f'{FIXTURES_DIR}/nested_result') as output:
        assert generate_diff(file1_path, file2_path) == output.read()

    with open(f'{FIXTURES_DIR}/nested_plain_result') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()

    with open(f'{FIXTURES_DIR}/nested_json_result') as output:
        assert generate_diff(file1_path, file2_path, 'json') == output.read()
