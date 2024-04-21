import sys
import argparse
from random import randint


def arg_manager():
    """Function that creates the CLI interface with different arguments"""
    description = (
        "🛠️ Command line utility for handling input.\n"
        "For larger codebases we recommend the --file option.\n"
        "⛔️ Don't use empty lines in the --cli mode"
    )
    manager = argparse.ArgumentParser(description=description)
    manager.add_argument('--cli', action='store_true', help='Prompt for multiline input from the CLI.')
    manager.add_argument('--file', type=str, help='Read data from a file specified by the user. The file has to be stored in the inputs folder')
    return manager


def handle_cli_input():
    print("Enter your multiline input (end with a blank line):")
    user_input = []
    while True:
        line = input()
        if line:
            user_input.append(line)
        else:
            break
    doc_string = "\n".join(user_input)
    
    return doc_string


def handle_file_input(file_name):
    try:
        with open(f"inputs/{file_name}", 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def generate_random_name(file_name):
    """Generates a random name for the tokenized output file"""
    return f"{file_name.split(".")[0]}{randint(1000, 10000)}_tokenized"
