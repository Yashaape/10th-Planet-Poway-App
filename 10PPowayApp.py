from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from Modules.Screens.login_screen import LoginScreen
from Modules.Screens.schedule_screen import ScheduleScreen
from Modules.Screens.main_menu import MainMenuScreen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.factory import Factory
from kivy.core.window import Window

Window.size = (325, 580)


class MyScreenManager(MDScreenManager):
    pass


class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        screen_manager = MDScreenManager()

        Factory.register('LoginScreen', module='Modules.Screens.login_screen')
        Factory.register('ClickableTextFieldRound', module='Modules.Widgets.clickable_text_field_round')
        Factory.register('MainMenuScreen', module='Modules.Screens.main_menu')
        Factory.register('ContentNavigationDrawer', module='Modules.Widgets.content_navigation_drawer')
        Factory.register('ScheduleScreen', module='Modules.Screens.schedule_screen')
        # Add other screens to the ScreenManager
        screen_manager.add_widget(LoginScreen(name='login'))
        screen_manager.add_widget(MainMenuScreen(name='main_menu'))
        screen_manager.add_widget(ScheduleScreen(name='schedule_screen'))
        return screen_manager

    def show_data(self):
        # Retrieve the text from the username field and print it
        username_text = self.root.current_screen.ids.clickable_text_field_round.ids.username_field.text
        password_text = self.root.current_screen.ids.clickable_text_field_round.ids.text_field.text
        print(f'Username: {username_text}, Password: {password_text}')

    def login_dialog(self):
        username_text = self.root.current_screen.ids.clickable_text_field_round.ids.username_field.text
        password_text = self.root.current_screen.ids.clickable_text_field_round.ids.text_field.text
        if username_text != "":
            user_error = f"{username_text} user does not exist."
        else:
            if password_text == "":  # Replace with the actual correct password
                user_error = "Username and password correct. Login success!"
                self.root.current = 'main_menu'
            else:
                user_error = "Incorrect password."

        self.dialog = MDDialog(title='Username check',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='More')]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog

    def logout(self):
        # Switch back to the login screen
        self.root.current = 'login'
        # Clear the text in the username and password fields
        self.root.current_screen.ids.clickable_text_field_round.ids.username_field.text = ''
        self.root.current_screen.ids.clickable_text_field_round.ids.text_field.text = ''


if __name__ == '__main__':
    MyApp().run()
