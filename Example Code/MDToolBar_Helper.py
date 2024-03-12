#BoxLayout info is in kivy
    #Stack elements vertically or horizontally
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Toolbar App'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["10thPlanetPoway.png", lambda x: app.navigation_draw()]]
            elevation: 4
            
        MDLabel:
            text: 'Hello World'
            halign: 'center' 
            
        MDBottomAppBar:
            MDTopAppBar:
                icon: '10thPlanetPoway.png'
                type: "bottom"
                left_action_items: [["menu", lambda x: app.navigation_draw()]]  
                mode: 'end'          
                on_action_button: app.navigation_draw()   #app.navigation_draw() is just for testing purposes     
"""