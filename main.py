from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from Modules.Screens.login_screen import LoginScreen
from Modules.Screens.main_menu import MainMenuScreen
from Modules.Screens.schedule_screen import ScheduleScreen
from Modules.Screens.profile_screen import ProfileScreen
from Modules.Screens.announcement_screen import AnnouncementScreen
from Modules.Screens.chat_screen import ChatScreen

# from kivy.core.window import Window


class MyScreenManager(MDScreenManager):
    pass


class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        screen_manager = MDScreenManager()

        # Add other screens to the ScreenManager
        screen_manager.add_widget(LoginScreen(name='login'))
        screen_manager.add_widget(MainMenuScreen(name='main_menu'))
        screen_manager.add_widget(ProfileScreen(name='profile_screen'))
        screen_manager.add_widget(ScheduleScreen(name='schedule_screen'))
        screen_manager.add_widget(ChatScreen(name='chat_screen'))
        screen_manager.add_widget(AnnouncementScreen(name='announcement_screen'))

        return screen_manager

    def logout(self):
        # Switch back to the login screen
        self.root.current = 'login'
        # Clear the text in the username and password fields
        self.root.current_screen.ids.clickable_text_field_round.ids.username_field.text = ''
        self.root.current_screen.ids.clickable_text_field_round.ids.text_field.text = ''


if __name__ == '__main__':
    MyApp().run()
