#Helper file for Navigation_Drawer

Nav_helper = """
MDScreen:
    MDNavigationLayout:
        MDScreenManager: #Very important, it's how each button will switch to a new screen
            MDScreen:
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: 'Navigation Drawer Demo'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 4
                        
                    Widget:
                    
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            
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
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'account'
                                
                        OneLineIconListItem:
                            text: 'Announcements'
                            IconLeftWidget:
                                icon: 'bullhorn'
                                
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
                
"""