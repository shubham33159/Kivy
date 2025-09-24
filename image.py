from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage

class MyImageApp(App):
    def build(self):
        img = Image(source="deer.jpg", size_hint=(None, None), width=700, height=500, pos_hint={"center_x":0.5, "center_y":0.5})
        # imgAsync = AsyncImage(source="https://media.istockphoto.com/id/1064128576/photo/young-woman-running-on-mountain.jpg?s=1024x1024&w=is&k=20&c=RAAD-kekpdRuANX_I7PdYRYbYXQKzdLzq_EbXxku9I4=", size_hint=(0.5, 0.5), pos_hint={"center_x":0.5, "center_y":0.5})
        return img
MyImageApp().run()