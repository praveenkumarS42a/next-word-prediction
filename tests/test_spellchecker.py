import unittest
from src.spellchecker_module import SpellCheckerModule

class TestSpellCheckerModule(unittest.TestCase):
    def setUp(self):
        self.spellchecker = SpellCheckerModule()

    def test_check_word(self):
        word = 'helo'
        corrected, suggestions = self.spellchecker.check_word(word)
        self.assertEqual(corrected, 'hello')
        self.assertIn('hello', suggestions)

    def test_check_sentence(self):
        sentence = 'helo wrld'
        corrected_sentence = self.spellchecker.check_sentence(sentence)
        self.assertEqual(corrected_sentence, 'hello world')

if __name__ == '__main__':
    unittest.main()

