# Helper file for Navigation_Drawer
Nav_helper = """
<ContentNavigationDrawer>
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
                    root.screen_manager.current = "profile"
                IconLeftWidget:
                    icon: 'account'
     
            OneLineIconListItem:
                text: 'Announcements'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "announcements"
                IconLeftWidget:
                    icon: 'bullhorn'  
            
            OneLineIconListItem:
                text: 'Live Schedule'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "announcements"
                IconLeftWidget:
                    icon: 'calendar-clock' 
                    
            OneLineIconListItem:
                text: 'Chat'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "announcements"
                IconLeftWidget:
                    icon: 'message-text'
             
            OneLineIconListItem:
                text: 'Logout'
                IconLeftWidget:
                    icon: 'logout'

MenuScreen:
    name:'menu'      
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Navigation Drawer Demo'
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
                name: 'profile'
                MDLabel:
                    text: 'Welcome Brandon'
                    halign: 'center'
                         
            AnnouncementsScreen:
                name: 'announcements'
                MDLabel:
                    text: 'Stay Up-to-date Here'
                    halign: 'center'             
                    
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                        
                
"""
