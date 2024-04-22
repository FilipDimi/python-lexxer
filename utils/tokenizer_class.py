import re
from .helpers import write_list_to_file

# List of tuple that containt the tokens with their regex
# Tuple: (Token, regex) -> follow this grammar for the token_specs list
token_specs = [
    ('Inline-comment-',      r'(?s)//.*?$|/\*.*?\*/'),
    ('Open-multiline-comment',  r'/\*'),
    ('Close-multiline-comment',  r'\*/'),
    ('Keyword-',             r'\bint|float|double|boolean|String|char|if|while|for|do\b'),
    ('Integer-',             r'[1-9]+'),
    ('Open-paren',           r'\('),
    ('Close-paren',          r'\)'),
    ('Open-bracket',         r'{'),
    ('Close-bracket',        r'}'),
    ('Semi-Colon',           r';'),
    ('Assignment',           r'='),
    ('Comparison',           r'==|!=|>=|=<|<|>'),
    ('Operator-',             r'\+|-|/|\b\*\b'),
    ('Identifer-',           r'\b[a-zA-z]+\b'),
    # TODO (Finish tokens) Fill out all of the missing tokens
    # TODO (Appropriate token names) make sure the token names match with the hw instruction
    # ! NOONE TOUCH THE COMMENT REGEX
]


class Tokenizer:
    """Lexical Analyzer Class"""
    def __init__(self, c_code):
        """Constructor"""
        self.c_code = c_code

    def __str__(self):
        """Show cat and tail of c lite code"""
        return f"{self.c_code[:20]}\n{self.c_code[-30::]}"

    def convert_doc_to_list(self, temp):
        """Doc String to list converter"""
        return temp.splitlines()

    def parser(self, file_name='cli_input'):
        """Parse that convers the c lite code to tokens"""
        token_lines = []
        # ! HIGHLY EXPERIMENTAL Method. For now it's working good, but we have to test it better
        c_code = self.convert_doc_to_list(self.c_code)
        for line in c_code:
            for token in token_specs:
                #Assigning match to if a regular expression is found
                match = re.search(token[1], line)
                    # These print statements are just to test the program flow
                    # so far the program behaves the way it should
                #checking if there is a match printing out the token name and the found object
                if match:
                    token_lines.append(f"{token[0]} {match.group()}")
        

        write_list_to_file(token_lines, file_name)
