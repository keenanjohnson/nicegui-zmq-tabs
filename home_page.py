from message import message


from nicegui import app, ui


def content() -> None:
    message('This is the home page.').classes('font-bold')
    ui.label('Use the menu on the top right to navigate.')

    ui.label().bind_text_from(app.storage.general, 'number', backward=lambda a: f'Latest Value: {a}')
    ui.line_plot(n=1, limit=25, figsize=(10, 4))
