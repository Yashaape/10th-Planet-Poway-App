from kivy.lang import Builder
from kivy.properties import StringProperty
from Login_Helper import Login_helper
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.window import Window

Window.size = (325, 580)


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    username = StringProperty()
    username_hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]


class Login(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(Login_helper)
        return screen

    def show_data(self):
        username_field = self.root.ids.username_field
        password_field = self.root.ids.text_field
        username = username_field.text
        password = password_field.text
        print(f"Username: {username}, Password: {password}")



Login().run()