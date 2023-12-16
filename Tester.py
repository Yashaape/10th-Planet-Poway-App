from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog

username_input = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    width:250
"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(username_input)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is not "hi":
            user_error = self.username.text + " user does not exist."
        else:
            user_error = "Please enter a username"
        self.dialog = MDDialog(title='Username check',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='More')]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog


DemoApp().run()