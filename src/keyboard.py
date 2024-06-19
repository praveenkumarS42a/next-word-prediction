from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from spellchecker_module import SpellCheckerModule

class AutocorrectKeyboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spellchecker = SpellCheckerModule()
        
        self.text_input = TextInput(size_hint=(1, 0.8))
        self.add_widget(self.text_input)
        
        self.result_label = Label(size_hint=(1, 0.1))
        self.add_widget(self.result_label)
        
        self.correct_button = Button(text='Correct', size_hint=(1, 0.1))
        self.correct_button.bind(on_press=self.correct_text)
        self.add_widget(self.correct_button)

    def correct_text(self, instance):
        text = self.text_input.text
        corrected_text = self.spellchecker.check_sentence(text)
        self.result_label.text = f"Corrected: {corrected_text}"

class AutocorrectApp(App):
    def build(self):
        return AutocorrectKeyboard()

if __name__ == '__main__':
    AutocorrectApp().run()

