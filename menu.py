from nicegui import ui


def menu() -> None:
    ui.link('Home', '/').classes(replace='text-white')
    ui.link('Subpage', '/subpage').classes(replace='text-white')