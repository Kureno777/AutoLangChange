from pythainlp.tokenize import word_tokenize

def is_thai(text):
    return any('\u0E00' <= ch <= '\u0E7F' for ch in text)

class DictionaryChecker:
    def __init__(self, en_path='data/dictionary_en.txt', th_path='data/dictionary_th.txt'):
        self.en_words = set()
        self.th_words = set()
        self.load_dictionaries(en_path, th_path)

    def load_dictionaries(self, en_path, th_path):
        with open(en_path, 'r', encoding='utf-8') as f:
            self.en_words = set(line.strip().lower() for line in f if line.strip())

        with open(th_path, 'r', encoding='utf-8') as f:
            self.th_words = set(line.strip() for line in f if line.strip())

    def is_valid_word(self, word):
        word = word.strip()
        if not word:
            return False

        if is_thai(word):
            # Exact match
            if word in self.th_words:
                return True

            # Word segmentation match
            segments = word_tokenize(word, engine="newmm")
            return all(segment in self.th_words for segment in segments)

        else:
            # English logic (lowercase match only)
            return word.lower() in self.en_words

