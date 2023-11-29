from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang.builder import Builder

username_helper = """
MDTextField:
    hint_text: "Enter Username: "
    helper_text: "Forgot Username?"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
    size_hint_x:None
    width:300
"""

class PowayApp(MDApp):
    def build(self):
        username = Builder.load_string(username_helper)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='login: ', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        screen.add_widget(username)
        return screen

PowayApp().run()