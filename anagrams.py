from collections import defaultdict
import threading
import unittest

PATH = 'ENTER_YOUR_PATH'

class Anagrams:
    def __init__(self, file_path):
        self.dictionary = defaultdict(list)
        self.lock = threading.Lock()
        self.build_dictionary(file_path)

    def get_anagrams(self, word):
        with self.lock:
            if not word.isalnum() or any(c.isdigit() for c in word):
                return ["Invalid Word"]
            
            lower_case_word = word.lower()
            key = ''.join(sorted(lower_case_word))
            if str(key) in self.dictionary.keys():
                return self.dictionary[key]
        
        return ["Not Found"]
    
    def build_dictionary(self, file_path):
        words = open(file_path).readlines()
        for word in words:
            word = word.strip()
            lower_case_word = word.lower()
            key = ''.join(sorted(lower_case_word))
            self.dictionary[key].append(word)
        


class TestAnagrams(unittest.TestCase):
    def setUp(self):
        self.anagrams = Anagrams(PATH)

    def test_anagrams(self):
        self.assertEqual(self.anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(self.anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEqual(self.anagrams.get_anagrams('repeals'), ['relapse', 'repeals'])
        self.assertEqual(self.anagrams.get_anagrams('reigns'), ['reigns', 'resign', 'signer', 'singer'])
        self.assertEqual(self.anagrams.get_anagrams('resign'), ['reigns', 'resign', 'signer', 'singer'])
        self.assertEqual(self.anagrams.get_anagrams('signer'), ['reigns', 'resign', 'signer', 'singer'])

    def test_not_found(self):
        self.assertEqual(self.anagrams.get_anagrams('poplopsdf'), ['Not Found'])
        self.assertEqual(self.anagrams.get_anagrams('loprl'), ['Not Found'])
        self.assertEqual(self.anagrams.get_anagrams('lfasdraer'), ['Not Found'])
        self.assertEqual(self.anagrams.get_anagrams('asfgg'), ['Not Found'])
    
    def test_invalid_word(self):
        self.assertEqual(self.anagrams.get_anagrams(''), ['Invalid Word'])
        self.assertEqual(self.anagrams.get_anagrams('eat@'), ['Invalid Word'])
        self.assertEqual(self.anagrams.get_anagrams('*f@'), ['Invalid Word'])
        self.assertEqual(self.anagrams.get_anagrams('7459'), ['Invalid Word'])
        self.assertEqual(self.anagrams.get_anagrams('ad@7459'), ['Invalid Word'])


if __name__ == '__main__':
    unittest.main()