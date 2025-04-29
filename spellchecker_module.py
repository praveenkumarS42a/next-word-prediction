from spellchecker import SpellChecker

class SpellCheckerModule:
    def __init__(self):
        self.spell = SpellChecker()

    def check_word(self, word):
        misspelled = self.spell.unknown([word])
        if misspelled:
            return self.spell.correction(word), self.spell.candidates(word)
        return word, []

    def check_sentence(self, sentence):
        words = sentence.split()
        corrected_sentence = []
        for word in words:
            corrected_word, _ = self.check_word(word)
            corrected_sentence.append(corrected_word)
        return ' '.join(corrected_sentence)
