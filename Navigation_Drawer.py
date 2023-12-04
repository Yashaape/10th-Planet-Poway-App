from kivymd.app import MDApp
from kivy.lang import Builder
from Navigation_Drawer_Helper import Nav_helper
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

Window.size = (325, 580) #Note this  needs to be removed once we create the app, this is for testing

# Create Profile screen
class ProfileScreen(MDScreen):
    pass

# Create Announcements screen
class AnnouncementsScreen(MDScreen):
    pass

# Create Menu screen
class MenuScreen(MDScreen):
    pass

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


screen_manager = MDScreenManager()
screen_manager.add_widget(MenuScreen(name='menu'))  # assosiates our menu screen to our kivyproperty of menu screen
screen_manager.add_widget(ProfileScreen(name="profile"))
screen_manager.add_widget(AnnouncementsScreen(name='announcements'))

class NavDemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(Nav_helper)
        return screen

NavDemoApp().run()