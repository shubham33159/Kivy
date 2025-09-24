from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)


class MyApp(App):
    def build(self):
        label = Label(text="Hello World", font_size="120sp", bold=True, italic=True, color=(0,1,0,0.5))
        return label
    
MyApp().run()