from utils.tokenizer_class import Tokenizer
from utils.sample_c_codes import sample_2


def main():
    c_lite_code = sample_2

    tok = Tokenizer(c_lite_code)
    tok.parser()


if __name__ == '__main__':
    main()
