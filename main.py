from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.stacklayout import StackLayout
from not_useful_text import more_text
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.list import OneLineListItem
# from kivy.uix.image import Image, AsyncImage
from kivy.core.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
import matplotlib.pyplot as plt
from kivy.uix.widget import Widget
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from subjects import subjects

plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')

with open('index.kv') as f:
    KV = f.read()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()
    pass


class Tab(FloatLayout, MDTabsBase):
    pass


class MyWidget(Widget):
    pass


class GraphMath(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for subjectIndex in range(len(subjects)):
            subject = subjects[subjectIndex]
            iterable_screen_id = f'screen {str(subjectIndex)}'
            iterable_screen = Screen(id=iterable_screen_id, name=subject.title)
            self.root.ids.screen_manager.add_widget(iterable_screen)

            # theory page description
            theory_header_wrapper = BoxLayout()
            theory_header = MDLabel(font_style='H6', text=subject.title)
            theory_header_wrapper.add_widget(theory_header)
            theory_content = MDLabel(text=more_text, font_style='Body1')
            theory_content_wrapper = MDBoxLayout()
            theory_content_wrapper.add_widget(theory_content)
            theory_page_layout = GridLayout(cols=1, adaptive_height=True, spacing='10dp', padding='10dp')
            theory_page_layout.add_widget(theory_header_wrapper)
            theory_page_layout.add_widget(theory_content_wrapper)

            # practice page description
            simple_label = MDLabel(
                text=f"iterable_screen_id: {iterable_screen_id} {more_text}",
                halign="center",
                size_hint_y=None
            )
            simple_label.height = simple_label.texture_size[1]
            practice_page_layout = MDBoxLayout(
                size_hint_y=None,
                adaptive_height=True,
                orientation="vertical"
            )
            # practice_page_layout.cols = 1
            # practice_page_layout.add_widget(simple_label)
            btn0 = MDRaisedButton(text="Btlkawe")
            practice_page_layout.add_widget(btn0)
            wid = MyWidget()
            print(MyWidget)

            imageA = Image("pexels-photo-2335126.jpeg")
            # wid.add_widget(imageA)
            # practice_page_layout.add_widget(wid)
            box_graph_layout = MDBoxLayout(
                adaptive_height=True
            )
            graph = FigureCanvasKivyAgg(plt.gcf())
            box_graph_layout.add_widget(graph)
            # practice_page_layout.add_widget(box_graph_layout)

            # add pages to tabs and layouts
            screen_tabs = MDTabs(default_tab=0)
            screen_tabs.on_tab_switch = self.on_tab_switch
            # ...theory
            theory_tab = Tab(text="Теорія")  # name='theory',
            theory_scroll_view = ScrollView()
            theory_scroll_view.add_widget(theory_page_layout)
            theory_tab.add_widget(theory_scroll_view)
            # ...practice
            practice_tab = Tab(text="Практика")  # name='practice',
            practice_scroll_view = ScrollView(do_scroll_y=True)
            practice_scroll_view.add_widget(practice_page_layout)
            practice_tab.add_widget(practice_scroll_view)
            # ...both
            screen_tabs.add_widget(theory_tab)
            screen_tabs.add_widget(practice_tab)
            iterable_screen.add_widget(screen_tabs)

            # add items to navigation drawer
            self.root.ids.drawer_list.add_widget(
                OneLineListItem(
                    text=subjects[subjectIndex].title,
                    on_press=self.change_subject
                )
            )
        # set default screen on application start
        self.root.ids.screen_manager.current = subjects[0].title
        pass

    def change_subject(self, list_item):
        self.root.ids.nav_drawer.set_state("close")
        self.root.ids.screen_manager.current = list_item.text
        pass

    def change_theme_root(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )

    def on_tab_switch(
       self, instance_tabs, instance_tab, instance_tab_label
    ):
        pass
        # print(instance_tabs)
        # screen = Screen()
        # screen.add_widget(MDLabel(text=instance_tab_label))
        # instance_tabs.add_widget(screen)

        # print(instance_tab_label)
        # instance_tab.add_widget(MDLabel(text=instance_tab.text))

        # x = np.linspace(-10, 9, 20)
        #
        # y = x ** 3

        # plt.plot(x, y, 'b')
        # plt.xlabel('X axis')
        # plt.ylabel('Y axis')
        # plt.title('Cube Function')
        # plt.show()
        # print("on_tab_switch")


GraphMath().run()
