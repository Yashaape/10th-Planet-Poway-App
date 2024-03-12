screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    AnnouncementScreen:
    
<MenuScreen>: #Define what we want in the MenuScreen
    name: 'menu'
    
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile' #takes us to our profile screen
        
    MDRectangleFlatButton:
        text: 'Announcements'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'announcement' 
        
<ProfileScreen>:
    name: 'profile'
    
    MDLabel:
        text: 'Welcome Brandon'
        halign: 'center'
        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'
        
<AnnouncementScreen>:
    name: 'announcement'
        
    MDLabel:
        text: 'Stay up to date with gym announcements here'
        halign: 'center'
        
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu' 
"""
