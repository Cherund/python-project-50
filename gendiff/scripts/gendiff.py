#!/usr/bin/env python3
from gendiff.generate_difference import generate_diff
from gendiff.cli import get_args


def main():
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
