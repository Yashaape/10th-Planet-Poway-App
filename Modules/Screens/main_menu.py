from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.lang import Builder
import psycopg2

# Dictionary to map screen names to formatted titles
SCREEN_TITLES = {
    'profile_screen': 'Profile',
    'schedule_screen': 'Schedule',
    'announcement_screen': 'Announcements',
    'chat_screen': 'Chat'
}

KV = '''
<MainMenuScreen>:
    name:'main_menu'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: top_app_bar
            title:  root.get_screen_title(root.ids.screen_manager.current) # Bind title to formatted title
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            elevation: 4
        Widget:
            
    MDNavigationLayout:
        MDScreenManager: #Very important, it's how each button will switch to a new screen
            id: screen_manager
            MDScreen:
                MDLabel:
                    text: "Welcome to the 10P Poway App"
                    halign: 'center'

            ProfileScreen:
                name: 'profile_screen'

            ScheduleScreen:
                name: 'schedule_screen'

            AnnouncementScreen: #Might need to change later
                name: 'announcement_screen'

            ChatScreen: #Might need to change later
                name: 'chat_screen'

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                
<ContentNavigationDrawer>:
    name: 'content_nav_drawer'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        padding: '8dp'
        Image:
            source: '10thPlanetPoway.png'
        MDLabel:
            id: first_name_label
            font_style: 'Subtitle1'
            size_hint_y: None
            height: self.texture_size[1]
        MDLabel:
            id: email_label
            font_style: 'Caption'
            size_hint_y: None
            height: self.texture_size[1]
        MDList:
            OneLineIconListItem:
                text: 'Profile'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "profile_screen"
                IconLeftWidget:
                    icon: 'account'

            OneLineIconListItem:
                text: 'Announcements'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "announcement_screen"
                IconLeftWidget:
                    icon: 'bullhorn'

            OneLineIconListItem:
                text: 'Live Schedule'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "schedule_screen"
                IconLeftWidget:
                    icon: 'calendar-clock'

            OneLineIconListItem:
                text: 'Chat'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "chat_screen"
                IconLeftWidget:
                    icon: 'message-text'

            OneLineIconListItem:
                text: 'Logout'
                on_press:
                    root.nav_drawer.set_state("close")
                    app.logout()
                IconLeftWidget:
                    icon: 'logout'
'''
Builder.load_string(KV)


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainMenuScreen(MDScreen):
    user_info = {}  # Initialize an empty dictionary to hold user info
    first_name_label = StringProperty()
    email_label = StringProperty()

    # Method to set user info retrieved from login
    def set_user_info(self, info):
        self.user_info = info  # Set user_info dictionary

        # Access MDLabel widgets and set their text to user info
        self.ids.first_name_label.text = self.user_info.get('first_name', '')
        self.ids.email_label.text = self.user_info.get('email', '')

    # Method to get formatted title based on screen name
    def get_screen_title(self, screen_name):
        return SCREEN_TITLES.get(screen_name, '')


