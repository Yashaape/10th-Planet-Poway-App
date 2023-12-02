from kivymd.app import MDApp
from kivy.lang import Builder
from MDToolBar_Helper import screen_helper
from kivy.core.window import Window

Window.size = (300, 500) #Note this  needs to be removed once we create the app, this is for testing

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")

DemoApp().run()
