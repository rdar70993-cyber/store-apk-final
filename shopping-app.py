from kivy.app import App
from kivy.uix.label import Label

class StoreApp(App):
    def build(self):
        return Label(text="Welcome to Store AP")

if __name__ == '__main__':
    StoreApp().run()
