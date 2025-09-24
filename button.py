from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn = Button(text="Click Me!", size_hint=(0.5, 0.5), pos_hint={"center_x":0.5, "center_y":0.5}
                , font_size="14sp", on_press=self.btn_click, on_release=self.btn_release)
        return btn
    def btn_click(self, btn):
        print("Button Clicked!")
        
    def btn_release(self, btn):
        print("Button Release")

ButtonApp().run()