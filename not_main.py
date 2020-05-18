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
    '''Class implementing content for a tab.'''
    pass


class SubjectItem:
    def __init__(self, title, content, action):
        self.title = title
        self.content = content
        self.action = action
        pass


class SubjectContent:
    def __init__(self, text, diagram_plt, input_field):
        self.text = text
        self.diagram_plt = diagram_plt
        self.input_field = input_field
        pass


class MatplotDiagram:
    def __init__(self):
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

    subjects = [
        SubjectItem(
            "Лінійна діаграма",
            SubjectContent("Description of subject 1", MatplotDiagram(), ""),
            "src 1"
            ),


        SubjectItem(
            "Гістограми",
            SubjectContent("Description of subject 2", MatplotDiagram(), ""),
            "src 2"
            ),

        SubjectItem(
            "Кругові діаграми",
            SubjectContent("Description of subject 3", MatplotDiagram(), ""),
            "src 3"
            )
        ]

    def on_start(self):
        for subject in self.subjects:
            self.root.ids.drawer_list.add_widget(OneLineListItem(text=subject.title))  # Tab(text=f"Tab {i}")
        pass

    def on_tab_switch(
       self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print("on_tab_switch")


Bootstrap().run()
