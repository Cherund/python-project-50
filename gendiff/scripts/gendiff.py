#!/usr/bin/env python3
from gendiff.genereting_difference import generate_diff
from gendiff.cli import get_args


def main():
    args = get_args()
    generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
