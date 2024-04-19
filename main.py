import re
from utils.tokenizer_class import Tokenizer
from utils.sample_c_codes import sample_1


def main():
    c_lite_code = sample_1

    tok = Tokenizer(c_lite_code)

    print(tok)


if __name__ == '__main__':
    main()
