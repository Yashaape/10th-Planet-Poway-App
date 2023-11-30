from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineAvatarListItem
from ListsMD_Helper import list_helper

class DemoListApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
        # Code below has been moved to the builder method because it's preferred
        # scroll = ScrollView()
        # list_viewer = MDList()
        # scroll.add_widget(list_viewer)
        #
        # for i in range(20):
        #     icon = IconLeftWidget(icon="account")
        #     items = ThreeLineIconListItem(text='Membership #P' + str(i), secondary_text='First & Last Name',
        #                               tertiary_text='Email Address')
        #     items.add_widget(icon)
        #     list_viewer.add_widget(items)
        #
        # screen.add_widget(scroll)
        return screen

    def on_start(self): #called when application starts
        for i in range(20):
            items = ThreeLineAvatarListItem(text='Member #P' + str(i), secondary_text='First & Last Name',
                                           tertiary_text='Email Address')
            self.root.ids.container.add_widget(items) #Important, self.root.ids. used to add items to container variable in ListsMD_Helper
DemoListApp().run()