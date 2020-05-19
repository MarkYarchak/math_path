from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.properties import ObjectProperty

with open('markup.kv') as f:
    KV = f.read()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    side_nav_drawer = ObjectProperty()


class Tab(FloatLayout, MDTabsBase):
    pass


class Bootstrap(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change_theme_root(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    def build(self):
        return Builder.load_string(KV)


    def on_start(self):
        # for subject in self.subjects:
        #     self.root.ids.drawer_list.add_widget(OneLineListItem(text=subject.title))  # Tab(text=f"Tab {i}")
        pass

    def on_tab_switch(
       self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print("on_tab_switch")


Bootstrap().run()
