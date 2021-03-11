import PySimpleGUI


class UIElement:
    STANDARD_SIZE = (20, 1)

    def __init__(self, _id, size=None):
        self._id = _id
        self._size = size if size else self.__class__.STANDARD_SIZE

    def create(self):
        pass


class Input(UIElement):
    STANDARD_SIZE = (30, 1)

    def __init__(self, _id, size=None):
        super().__init__(_id, size)

    def create(self):
        return PySimpleGUI.Input(key=self._id, size=self._size)


class Text(UIElement):
    STANDARD_SIZE = (19, 1)

    def __init__(self, _id, text, size=None, justification='left', visible=True):
        super().__init__(_id, size)
        self.__text = text
        self.__justification = justification
        self.__visible = visible

    def create(self):
        return PySimpleGUI.Text(key=self._id, text=self.__text, size=self._size, justification=self.__justification,
                                visible=self.__visible)


class DropDownList(UIElement):
    STANDARD_SIZE = (28, 1)

    def __init__(self, _id, choices, size=None):
        super().__init__(_id, size)
        self.__choices = choices

    def create(self):
        return PySimpleGUI.Combo(values=self.__choices, key=self._id, size=self._size, enable_events=False,
                                 default_value=self.__choices[0], readonly=True)


class CheckBox(UIElement):
    STANDARD_SIZE = (28, 1)

    def __init__(self, _id, default_value, text, size=None):
        super().__init__(_id, size)
        self.__default_value = default_value
        self.__text = text

    def create(self):
        return PySimpleGUI.Checkbox(text=self.__text, default=self.__default_value, key=self._id, size=self._size,
                                    enable_events=False)


class Button(UIElement):
    STANDARD_SIZE = (20, 1)

    def __init__(self, _id, text, size=None):
        super().__init__(_id, size)
        self.__text = text

    def create(self):
        return PySimpleGUI.Button(button_text=self.__text, key=self._id, size=self._size)


class Image(UIElement):
    STANDARD_SIZE = (100, 100)

    def __init__(self, _id, filepath, size=None):
        super().__init__(_id, size)
        self.__filepath = filepath

    def create(self):
        return PySimpleGUI.Image(filename=self.__filepath, key=self._id, size=self._size)


class Column:
    def __init__(self, layout, justification):
        self.__layout = layout
        self.__justification = justification

    def create(self):
        return PySimpleGUI.Column(self.__layout, justification=self.__justification)
