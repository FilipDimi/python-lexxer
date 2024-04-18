class Tokenizer:
    """Lexical Analyzer Class"""
    def __init__(self, c_code):
        """Constructor"""
        self.c_code = c_code

    def __str__(self):
        """Show cat and tail of c lite code"""
        return f"{self.c_code[:20]}\n{self.c_code[-30::]}"

    
    # TODO (Planning and Implementing Methods)
    # .
    # .
    # .