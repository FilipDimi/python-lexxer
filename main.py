# #############################################
# AUTHORS:
# Austin Kite
# Filip Dimitrievski
# CPS450 Homework
# https://github.com/FilipDimi/python-lexxer
# #############################################

import sys
from utils.helpers import arg_manager, handle_cli_input, handle_file_input, generate_random_name
from utils.tokenizer_class import Tokenizer

def main():
    manager = arg_manager()
    args = manager.parse_args()

    if len(sys.argv) == 1:
        manager.print_help(sys.stderr)
        sys.exit(1)

    if args.cli:
        print("CLI mode activated. Please enter your input. 💻")
        user_input = handle_cli_input()
    elif args.file:
        print(f"Reading from file: {args.file} 📂")
        generate_random_name(args.file)
        user_input = handle_file_input(args.file)
    else:
        manager.print_help()

    tok = Tokenizer(user_input)
    tok.parser(args.file)

if __name__ == '__main__':
    main()
