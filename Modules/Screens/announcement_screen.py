from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, OneLineListItem
from kivy.lang import Builder

KV = '''
<AnnouncementScreen>:
    name: 'announcement_screen'
    on_enter: root.load_announcements()  # Call load_announcements when the screen is entered    name: 'announcement_screen'
    
    MDScrollView:
        pos_hint: {'top': 0.9}
        MDList:
            id: announcements_list
            size_hint_y: None
            height: self.minimum_height
'''

Builder.load_string(KV)


class AnnouncementScreen(MDScreen):

    def load_announcements(self):
        # Dummy data for demonstration
        announcements = [
            "Upcoming Yoga Class on April 10th at 9:00 AM",
            "Weightlifting competition on April 15th at 5:00 PM",
            "New cardio equipment installed in the gym",
            "Group fitness classes schedule updated",
            "Upcoming Yoga Class on April 10th at 9:00 AM",
            "Weightlifting competition on April 15th at 5:00 PM",
            "New cardio equipment installed in the gym",
            "Group fitness classes schedule updated",
            "Upcoming Yoga Class on April 10th at 9:00 AM",
            "Weightlifting competition on April 15th at 5:00 PM",
            "New cardio equipment installed in the gym",
            "Group fitness classes schedule updated"
        ]

        # Access MDList by id and clear previous items
        self.ids.announcements_list.clear_widgets()

        # Add each announcement to the MDList
        for announcement in announcements:
            self.ids.announcements_list.add_widget(
                OneLineListItem(text=announcement)
            )
