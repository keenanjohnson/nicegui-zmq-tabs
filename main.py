#!/usr/bin/env python3
from datetime import datetime

import zmq
import zmq.asyncio

from nicegui import app, ui

context = zmq.asyncio.Context()
socket = context.socket(zmq.PULL)
socket.connect('tcp://localhost:5555')

poller = zmq.asyncio.Poller()
poller.register(socket, zmq.POLLIN)


async def read_loop() -> None:
    while not app.is_stopped:
        events = await poller.poll()
        if socket in dict(events):
            data = await socket.recv()
            number = float(data)
            print(f'Received number {number}')
            line_plot.push([datetime.now()], [[number]])

            # Save number in app.storage.general
            app.storage.general['number'] = number

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs() as tabs:
        ui.tab('A')
        ui.tab('B')
        ui.tab('C')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.label('Content of A')
        ui.label().bind_text_from(app.storage.general, 'number', backward=lambda a: f'Latest Value: {a}')
        line_plot = ui.line_plot(n=1, limit=25, figsize=(10, 4))
    with ui.tab_panel('B'):
        ui.label('Content of B')
        ui.label().bind_text_from(app.storage.general, 'number', backward=lambda a: f'Latest Value: {a}')
    with ui.tab_panel('C'):
        ui.label('Content of C')
        ui.label().bind_text_from(app.storage.general, 'number', backward=lambda a: f'Latest Value: {a}')

app.on_startup(read_loop)

ui.run()
