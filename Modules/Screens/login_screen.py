from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton, MDIconButton, MDTextButton
from kivymd.uix.dialog import MDDialog
import psycopg2

KV = '''
<LoginScreen>:
    Image:
        source: '10thPlanetPoway.png'
        size_hint_y: None #allows setting a fixed height
        height: dp(250)
        pos_hint: {"top": 1.0} #aligns top of image to top

    ClickableTextFieldRound:
        id: clickable_text_field_round
        size_hint: None, None
        width: "300dp"
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .35}
        
<ClickableTextFieldRound>:
    id: clickable_text_field_round
    MDGridLayout:
        cols: 1
        size_hint_y: None
        height: username_field.height + text_field.height + dp(20)

        MDTextField:
            id: username_field
            hint_text: "Username"
            helper_text: "or click on forgot username"
            helper_text_mode: "on_focus"
            text: root.username
            icon_left: "account"

        MDTextField:
            id: text_field
            hint_text: root.hint_text
            text: root.text
            password: True
            icon_left: "key-variant"

    MDIconButton
        id: login-variant
        icon: "login-variant"
        pos_hint: {"center_y": 1.20}
        pos: username_field.width - self.width + dp(8), 0
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        on_press: root.login_dialog()

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True

    MDTextButton:
        id: forgot_password
        text: "Forgot Password"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_size: 15
        pos_hint: {"center_x": 0.18}
        on_press: root.show_data() #change later, testing purposes for now

    MDTextButton:
        id: create_account
        text: "Create Account"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        font_size: 15
        pos_hint: {"center_x": 0.83}
        on_press: root.show_data() #change later, testing purposes for now
'''
Builder.load_string(KV)


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    username = StringProperty()
    username_hint_text = StringProperty()

    def show_data(self):
        # Retrieve the text from the username field and print it
        username_text = self.ids.username_field.text
        password_text = self.ids.text_field.text
        print(f'Username: {username_text}, Password: {password_text}')

    def login_dialog(self):
        username_text = self.ids.username_field.text
        password_text = self.ids.text_field.text
        if username_text != "":
            user_error = f"{username_text} user does not exist."
        else:
            if password_text == "":  # Replace with the actual correct password
                user_error = "Username and password correct. Login success!"
                self.parent.parent.current = 'main_menu'  # Access parent of parent (LoginScreen) to reach screen_manager
            else:
                user_error = "Incorrect password."

        dialog = MDDialog(title='Username check',
                          text=user_error, size_hint=(0.8, 1),
                          buttons=[MDFlatButton(text='Close', on_release=lambda *args: self.close_dialog(dialog)),
                                   MDFlatButton(text='More')]
                          )
        dialog.open()

    def close_dialog(self, dialog_instance):
        dialog_instance.dismiss()
        # do stuff after closing the dialog


class LoginScreen(MDScreen):
    pass


