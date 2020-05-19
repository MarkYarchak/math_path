
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