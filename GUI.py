import kivy
from kivy.app import App

#import japanese_kivy
#Builder.load_file('./autoedit.kv')

class ResultSCN(kivy.uix.widget.Widget):
    pass
class OpeSCN(kivy.uix.widget.Widget):
    pass

class Screen(kivy.uix.widget.Widget):
    pass

class AutoeditApp(kivy.app.App):
    def build(self):
        return Screen()
    

if __name__ == '__main__':
    AutoeditApp().run()