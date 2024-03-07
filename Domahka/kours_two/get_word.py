from utils import load_web_dictionary
random_word = load_web_dictionary()


class BasicWord:

    def __init__(self, random_dict):
        self.word = random_dict["word"]
        self.subwords = random_dict['subwords']

    def quantity_short_words(self):
        return len(self.subwords)

    def get_main_word(self):
        return self.word

    def try_chek(self, inp_word):

        if inp_word in self.subwords:
            return True
        else:
            return False
