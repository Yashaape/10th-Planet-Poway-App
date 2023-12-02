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
            
"""