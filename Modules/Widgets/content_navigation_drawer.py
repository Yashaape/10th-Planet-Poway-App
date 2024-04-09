from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView

KV = '''
<ContentNavigationDrawer>
    name: 'content_nav_drawer'
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        padding: '8dp'
        Image:
            source: '10thPlanetPoway.png'
        MDLabel:
            text: 'Brandon'
            font_style: 'Subtitle1'
            size_hint_y: None
            height: self.texture_size[1]
        MDLabel:
            text: 'brasgaitis97@gmail.com'
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
