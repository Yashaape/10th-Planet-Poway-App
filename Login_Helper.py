Login_helper = '''
<ClickableTextFieldRound>:
    GridLayout:
        cols: 1
        size_hint_y: None
        height: username_field.height + text_field.height + dp(20)
    
        MDTextField:
            id: username_field
            hint_text: "Username"
            helper_text: "or click on forgot username"
            helper_text_mode: "on_focus"
            text: root.username
            icon_left: "account"
        
        MDTextField:
            id: text_field
            hint_text: root.hint_text
            text: root.text
            password: True
            icon_left: "key-variant"
            
    MDIconButton
        id: login-variant
        icon: "login-variant"
        pos_hint: {"center_y": 1.20}
        pos: username_field.width - self.width + dp(8), 0
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color
        on_press: root.show_data()
        
    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True
    
    MDTextButton:
        id: forgot_password
        text: "Forgot Password"
        theme_text_color: "Custom" 
        text_color: app.theme_cls.primary_color
        font_size: 15
        pos_hint: {"center_x": 0.18}
          
    MDTextButton:
        id: create_account
        text: "Create Account"
        theme_text_color: "Custom" 
        text_color: app.theme_cls.primary_color
        font_size: 15
        pos_hint: {"center_x": 0.83}

MDScreen:
    name: 'login_screen'                
    Image:
        source: '10thPlanetPoway.png'    
        size_hint_y: None #allows setting a fixed height
        height: dp(250)
        pos_hint: {"top": 1.0} #aligns top of image to top
        
    ClickableTextFieldRound:
        size_hint: None, None
        width: "300dp"
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .35}
'''
