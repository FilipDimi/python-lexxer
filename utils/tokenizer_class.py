import re

# List of tuple that containt the tokens with their regex
# Tuple: (Token, regex) -> follow this grammar for the token_specs list
token_specs = [
    ('COMMENT',     r'(?s)//.*?$|/\*.*?\*/'),
    ('INT',         r'\bint\b'),
    ('MAIN',        r'\bmain\b'),
    ('Open (',      r'\('),
    ('Close )',     r'\)'),
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

    def parser(self):
        """Parse that convers the c lite code to tokens"""
        # ! HIGHLY EXPERIMENTAL Method. For now it's working good, but we have to test it better
        c_code = self.convert_doc_to_list(self.c_code)

        for line in c_code:
            for token in token_specs:
                if re.search(token[1], line):
                    # These print statements are just to test the program flow
                    # so far the program behaves the way it should
                    print(token[0], end='')
                    print(line)
