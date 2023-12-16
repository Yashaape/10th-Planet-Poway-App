from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from Modules.Screens.login_screen import LoginScreen
from kivy.properties import StringProperty
from kivy.factory import Factory
from kivy.core.window import Window

Window.size = (325, 580)


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        #sm = MDScreenManager()
        #sm.add_widget(LoginScreen(name='login', kv_file=LoginScreen_kv_path))
        Factory.register('LoginScreen', module='Modules.Screens.login_screen')
        Factory.register('ClickableTextFieldRound', module='Modules.Widgets.clickable_text_field_round')
        # Add other screens to the ScreenManager
        return LoginScreen()

    def show_data(self):
        # Retrieve the text from the username field and print it
        username_text = self.root.ids.clickable_text_field_round.ids.username_field.text
        password_text = self.root.ids.clickable_text_field_round.ids.text_field.text
        print(f'Username: {username_text}, Password: {password_text}')


if __name__ == '__main__':
    MyApp().run()
