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

ui.label().bind_text_from(app.storage.general, 'number', backward=lambda a: f'Latest Value: {a}')
line_plot = ui.line_plot(n=1, limit=25, figsize=(10, 4))

app.on_startup(read_loop)

ui.run()
