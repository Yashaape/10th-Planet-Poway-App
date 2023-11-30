from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang.builder import Builder
from Login_Helper import username_helper

class PowayApp(MDApp):
    def build(self):
        self.username = Builder.load_string(username_helper)
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='login: ', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                         on_release=self.show_data)
        screen.add_widget(btn_flat)
        screen.add_widget(self.username)
        return screen

    def show_data(self, obj):

        if self.username.text is "":
            check_string = "Please enter a Username"
        else:
            check_string = self.username.text + 'Does not exist'

        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog_box = MDDialog(title= 'Username Check', text=check_string, size_hint=(0.7, 1),
                              buttons=[close_button, more_button])
        print(self.username.text) #Prints text to terminal, for testing purposes
        self.dialog_box.open()

    def close_dialog(self, obj):
        self.dialog_box.dismiss()


PowayApp().run()