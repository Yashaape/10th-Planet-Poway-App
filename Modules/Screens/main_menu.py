from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

# Dictionary to map screen names to formatted titles
SCREEN_TITLES = {
    'profile_screen': 'Profile',
    'schedule_screen': 'Schedule',
    'announcement_screen': 'Announcements',
    'chat_screen': 'Chat'
}

KV = '''
<MainMenuScreen>:
    name:'menu'
    BoxLayout:
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
'''
Builder.load_string(KV)


class MainMenuScreen(MDScreen):

    # Method to get formatted title based on screen name
    def get_screen_title(self, screen_name):
        return SCREEN_TITLES.get(screen_name, '')
