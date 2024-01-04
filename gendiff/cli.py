def get_paths(args):
    if isinstance(args, list):
        return {'first_file': args[0], 'second_file': args[1]}

    return {'first_file': args.first_file, 'second_file': args.second_file}
