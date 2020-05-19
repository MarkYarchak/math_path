from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import OneLineListItem

from subjects import subjects

with open('index.kv') as f:
    KV = f.read()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass


class Tab(FloatLayout, MDTabsBase):
    pass


class GraphMath(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        print(self)
        for subject in subjects:  # , on_press=change_subject
            self.root.ids.drawer_list.add_widget(OneLineListItem(text=subject.title))  # Tab(text=f"Tab {i}")
        pass

    def change_subject(self):
        # print(data)
        self.root.nav_drawer.set_state("close")
        self.root.screen_manager.current = "scr 2"
        pass

    def change_theme_root(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

    def on_tab_switch(
       self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print("on_tab_switch")


GraphMath().run()
