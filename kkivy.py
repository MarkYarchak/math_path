from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import Screen
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import numpy as np

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
            iterable_screen_id = f'screen {str(subjectIndex)}'
            iterable_screen = Screen(id=iterable_screen_id, name=subjects[subjectIndex].title)
            self.root.ids.screen_manager.add_widget(iterable_screen)
            self.root.ids.screen_manager.current = subjects[0].title
            screen_tabs = MDTabs(on_tab_switch=self.on_tab_switch)
            theory_tab = Tab(text="Теорія")  # name='theory',
            practice_tab = Tab(text="Практика")  # name='practice',
            practice_page = BoxLayout()
            simple_label = MDLabel(text=f"iterable_screen_id: {iterable_screen_id}", halign="center")
            practice_page.add_widget(simple_label)
            practice_tab.add_widget(practice_page)
            screen_tabs.add_widget(theory_tab)
            screen_tabs.add_widget(practice_tab)
            screen_tabs.default_tab = 0
            iterable_screen.add_widget(screen_tabs)

            self.root.ids.drawer_list.add_widget(
                OneLineListItem(text=subjects[subjectIndex].title, on_press=self.change_subject)
            )
        self.root.ids.screen_manager.current = subjects[0].title
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

        x = np.linspace(-10, 9, 20)

        y = x ** 3

        plt.plot(x, y, 'b')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.title('Cube Function')
        plt.show()
        print("on_tab_switch")


GraphMath().run()
