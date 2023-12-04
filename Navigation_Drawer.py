from kivymd.app import MDApp
from kivy.lang import Builder
from Navigation_Drawer_Helper import Nav_helper
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window

Window.size = (300, 500) #Note this  needs to be removed once we create the app, this is for testing

class NavDemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(Nav_helper)
        return screen

NavDemoApp().run()