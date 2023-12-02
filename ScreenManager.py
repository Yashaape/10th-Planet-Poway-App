from kivymd.app import MDApp
from kivy.lang import Builder
from ScreenManager_Helper import screen_helper
from kivy.uix.screenmanager import Screen, ScreenManager


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class AnnouncementScreen(Screen):
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(name='menu'))  # assosiates our menu screen to our kivyproperty of menu screen
screen_manager.add_widget(ProfileScreen(name="profile"))
screen_manager.add_widget(AnnouncementScreen(name='announcement'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
