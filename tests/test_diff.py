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


def test_nested_json_diff():
    file1_path = f'{FIXTURES_DIR}/nested_file1.json'
    file2_path = f'{FIXTURES_DIR}/nested_file2.json'

    with open(f'{FIXTURES_DIR}/nested_result') as output:
        assert generate_diff(file1_path, file2_path) == output.read()
#

def test_nested_yaml_diff():
    file1_path = f'{FIXTURES_DIR}/nested_file1.yml'
    file2_path = f'{FIXTURES_DIR}/nested_file2.yml'

    with open(f'{FIXTURES_DIR}/nested_result') as output:
        assert generate_diff(file1_path, file2_path) == output.read()


def test_flat_json_diff_plain():
    file1_path = f'{FIXTURES_DIR}/file1.json'
    file2_path = f'{FIXTURES_DIR}/file2.json'

    with open(f'{FIXTURES_DIR}/plain_result') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()


def test_flat_yml_diff_plain():
    file1_path = f'{FIXTURES_DIR}/file1.yml'
    file2_path = f'{FIXTURES_DIR}/file2.yml'

    with open(f'{FIXTURES_DIR}/plain_result') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()


def test_nested_json_diff_plain():
    file1_path = f'{FIXTURES_DIR}/nested_file1.json'
    file2_path = f'{FIXTURES_DIR}/nested_file2.json'

    with open(f'{FIXTURES_DIR}/plain_nested_result') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()


def test_nested_yaml_diff_plain():
    file1_path = f'{FIXTURES_DIR}/nested_file1.yml'
    file2_path = f'{FIXTURES_DIR}/nested_file2.yml'

    with open(f'{FIXTURES_DIR}/plain_nested_result') as output:
        assert generate_diff(file1_path, file2_path, 'plain') == output.read()


def test_flat_json_diff_jdumps():
    file1_path = f'{FIXTURES_DIR}/file1.json'
    file2_path = f'{FIXTURES_DIR}/file2.json'

    with open(f'{FIXTURES_DIR}/json_result') as output:
        assert generate_diff(file1_path, file2_path, 'json') == output.read()


def test_flat_yml_diff_jdumps():
    file1_path = f'{FIXTURES_DIR}/file1.yml'
    file2_path = f'{FIXTURES_DIR}/file2.yml'

    with open(f'{FIXTURES_DIR}/json_result') as output:
        assert generate_diff(file1_path, file2_path, 'json') == output.read()


def test_nested_json_diff_jdumps():
    file1_path = f'{FIXTURES_DIR}/nested_file1.json'
    file2_path = f'{FIXTURES_DIR}/nested_file2.json'

    with open(f'{FIXTURES_DIR}/json_nested_result') as output:
        assert generate_diff(file1_path, file2_path, 'json') == output.read()


def test_nested_yaml_diff_jdumps():
    file1_path = f'{FIXTURES_DIR}/nested_file1.yml'
    file2_path = f'{FIXTURES_DIR}/nested_file2.yml'

    with open(f'{FIXTURES_DIR}/json_nested_result') as output:
        assert generate_diff(file1_path, file2_path, 'json') == output.read()
