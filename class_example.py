import theme
from message import message

from nicegui import app, ui


class ClassExample:

    def __init__(self) -> None:
        """The page is created as soon as the class is instantiated.

        This can obviously also be done in a method, if you want to decouple the instantiation of the object from the page creation.
        """
        @ui.page('/subpage')
        def page_subpage():
            with theme.frame('- Subpage -'):
                message('Subpage')
                ui.label('This is a subpage')
                ui.label().bind_text_from(app.storage.general, 'number', backward=lambda a: f'Latest Value: {a}')