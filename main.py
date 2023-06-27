from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
# import random
# from kivy.config import Config
# from kivymd.color_definitions import colors
# from kivy.uix.button import Button
# from kivy.uix.image import Image
# from kivy.core.audio import SoundLoader
# import json
from kivy.uix.screenmanager import WipeTransition
from kivy.animation import Animation

width, height = Window.size # application body
# Window.size = (350,650)

class Homescreen(Screen):
    Builder.load_file('screens/home_screen.kv')
    
class Flashtiming(Screen):
    Builder.load_file('screens/flashtiming.kv')
    
class Header(Screen):
    Builder.load_file('screens/header.kv')
    
class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.accent_palette = 'DeepPurple'
        self.theme_cls.accent_hue = '400'
        sm = ScreenManager(transition=WipeTransition(duration=0.3))
        sm.add_widget(Homescreen(name="Homescreen"))
        sm.add_widget(Flashtiming(name="Flashtiming"))
        # sm.add_widget(Count_screen(name="Countscreen"))
        # sm.add_widget(Input_screen(name="Inputscreen"))
        # sm.add_widget(Lose_screen(name="Losescreen"))
        # sm.add_widget(Information_screen(name="Informationscreen"))
        self.sm = sm
        return sm
    
    def ChangeMode(self):
        if self.theme_cls.theme_style == 'Light':
            animation = Animation(duration=0.5, opacity=0) + Animation(opacity=1, duration=0.5)
            animation.start(self.sm)
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Orange'
            self.theme_cls.accent_palette = 'Orange'
        else:
            animation = Animation(duration=0.5, opacity=0) + Animation(opacity=1, duration=0.5)
            animation.start(self.sm)
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.primary_palette = 'DeepPurple'
            self.theme_cls.accent_palette = 'DeepPurple'

    
if __name__ == "__main__":
    App().run()