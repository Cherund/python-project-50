from gendiff.styles.get_style import style_dict
from gendiff.create_tree import create_difference_tree
from gendiff.get_extension import get_file_data


def generate_diff(file1_path, file2_path, style='stylish'):
    file1 = get_file_data(file1_path)
    file2 = get_file_data(file2_path)
    compared_dict = create_difference_tree(file1, file2)
    stringed_dict = style_dict(compared_dict, style)
    return stringed_dict
