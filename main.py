#!/usr/bin/env python3
from datetime import datetime

import zmq
import zmq.asyncio

from nicegui import app, ui

import class_example
import home_page
import theme


context = zmq.asyncio.Context()
socket = context.socket(zmq.PULL)
socket.connect('tcp://localhost:5555')

poller = zmq.asyncio.Poller()
poller.register(socket, zmq.POLLIN)

# This function reads a value from the zeromq socket and stores it in the app storage for use in 
# multiple tabs.
async def read_loop() -> None:
    while not app.is_stopped:
        events = await poller.poll()
        if socket in dict(events):
            data = await socket.recv()
            number = float(data)
            print(f'Received number {number}')

            # Save number in app.storage.general
            app.storage.general['number'] = number

# Example 1: use a custom page decorator directly and putting the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        home_page.content()

# Example 3: use a class to move the whole page creation into a separate file
class_example.ClassExample()

app.on_startup(read_loop)

ui.run()
