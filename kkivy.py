from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import Screen

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
        for subjectIndex in range(len(subjects)):
            self.root.ids.screen_manager.add_widget(
                Screen(id=f'screen {str(subjectIndex)}', name=subjects[subjectIndex].title)
            )
            self.root.ids.screen_manager.current = subjects[0].title
            # iterable_screen = 'screen ' + str(subjectIndex)
            # self.root.ids[iterable_screen].add_widget(
            #     MDTabs=MDTabs(
            #         on_tab_switch=self.on_tab_switch,
            #         Tab=Tab(
            #             name='theory',
            #             text="Теорія"
            #         ),
            #         AnotherTab=Tab(
            #             name='practice',
            #             text="Практика",
            #             BoxLayout(
            #                 MDLabel=MDLabel(
            #                     text="Title",
            #                     halign="center",
            #                 )
            #             )
            #         )
            #     )
            # )
            self.root.ids.drawer_list.add_widget(
                OneLineListItem(text=subjects[subjectIndex].title, on_press=self.change_subject)
            )
        pass

    def change_subject(self, list_item):
        # list_item.
        self.root.ids.nav_drawer.set_state("close")
        self.root.ids.screen_manager.current = list_item.text
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
