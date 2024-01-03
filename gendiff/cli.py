def get_paths(args):
    if isinstance(args, list):
        return args
    return [args.first_file, args.second_file]