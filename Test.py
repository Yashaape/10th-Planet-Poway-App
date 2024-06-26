from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


KV = """


"""

Builder.load_string(KV)


class MyScreenManager(MDScreenManager):
    pass


class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        screen_manager = MDScreenManager()
        #Factory.register('ProfileScreen', module='Modules.Screens.profile_screen')
        #screen_manager.add_widget(ProfileScreen(name='profile_screen'))

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
