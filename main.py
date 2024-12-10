from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

from kivy.graphics import Color, Rectangle
from kivy.graphics import RoundedRectangle
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

import datetime
import json

class App(App):
    def build(self):
        self.layout = FloatLayout()

        with open("system/img/slide/data_slides.json", 'r', encoding="utf-8") as slide_data:
            slides = json.load(slide_data)

            slide_1_data = slides['slide1']

            slide_1_path = slide_1_data['path']
            slide_1_upload = slide_1_data['content']['upload_data']
            slide_1_title = slide_1_data['content']['message']['title']
            slide_1_desc = slide_1_data['content']['message']['description']

            slide_2_data = slides['slide2']

            slide_2_path = slide_2_data['path']
            slide_2_upload = slide_2_data['content']['upload_data']
            slide_2_title = slide_2_data['content']['message']['title']
            slide_2_desc = slide_2_data['content']['message']['description']

        menu_main = Widget(size_hint=(1, 0.2), pos_hint={"x": 0, "y": -.1})
        background = Widget(size_hint=(1, 1))

        slide_1_bg = Widget()

        with background.canvas:
            Color(1, 1, 1, 1)
            self.background = Rectangle(size=background.size)

        with menu_main.canvas:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = RoundedRectangle(size=menu_main.size, pos=menu_main.pos)

        def update_rect(instance, value):
            self.rect.size = instance.size
            self.rect.pos = instance.pos

        def background_update(instance, value):
            self.background.size = instance.size
            self.background.pos = instance.pos

        calendar_menu_button = Image(source="system/files/icons/calendar_icon_64x64.png", size_hint=(None, None), size=(25, 25), pos_hint={"x": 0.05, "y": 0.035})
        chat_menu_button = Image(source="system/files/icons/chat_icon_64x64.png", size_hint=(None, None), size=(25, 25), pos_hint={"x": 0.25, "y": 0.035})
        database_menu_button = Image(source="system/files/icons/database_icon_64x64.png", size_hint=(None, None), size=(25, 25), pos_hint={"x": 0.45, "y": 0.035})
        notification_menu_button = Image(source="system/files/icons/notification_icon_64x64.png", size_hint=(None, None), size=(25, 25), pos_hint={"x": 0.65, "y": 0.035})
        todo_menu_button = Image(source="system/files/icons/todo_icon_64x64.png", size_hint=(None, None), size=(25, 25), pos_hint={"x": 0.85, "y": 0.035})

        label_main = Label(text="Лицей-Connect", font_name="system/files/fonts/NimbusSanL-Bol.otf", font_size="20px", color=(0,0,0,1), pos_hint={"x": 0, "y": .4})

        menu_main.bind(pos=update_rect, size=update_rect)
        background.bind(size=background_update, pos=background_update)

        # Slide 1
        slide1 = Image(source=slide_1_path, size_hint=(0.8, 0.8), pos_hint={"x": 0.1, "y": 0.0}, size=(100, 100))

        self.layout.add_widget(background)

        self.layout.add_widget(slide1)

        self.layout.add_widget(label_main)

        self.layout.add_widget(menu_main)
        self.layout.add_widget(calendar_menu_button)
        self.layout.add_widget(chat_menu_button)
        self.layout.add_widget(database_menu_button)
        self.layout.add_widget(notification_menu_button)
        self.layout.add_widget(todo_menu_button)

        return self.layout

if __name__ == "__main__":
    App().run()
