from gendiff.genereting_difference import generate_diff
from pathlib import Path


output = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_diff():
    current_dir = Path(__file__).parent

    paths = [f'{current_dir}/fixtures/file1.json',
             f'{current_dir}/fixtures/file2.json']
    assert generate_diff(paths) == output
