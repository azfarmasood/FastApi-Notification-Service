from flet import Page, Column, Text, AlertDialog, ElevatedButton, app  # type: ignore
from database.db import PUSHER_CLUSTER, PUSHER_KEY
import logging
import pysher  # type: ignore
import pusher  # type: ignore
import json
import sys
import time


root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

def main_flet(page: Page):
    page.window.width = 300
    global pusher

    def close_dialog(e):
        notifi.open = False
        page.update()

    notifi = AlertDialog(
        title=Text("new notification", size=15, weight='medium'),
        content=Text(size=10, weight='medium'),
        actions=[
            ElevatedButton(
                "close",
                on_click=close_dialog
            )
        ]
    )

    def my_event(data: str):
        page.dialog = notifi
        parsed_data = json.loads(data)
        message = parsed_data['message']
        notifi.content.value = message
        notifi.open = True
        page.update()

    def connect_handler():
        channel = pusher.subscribe("my-channel")
        channel.bind("my-event", my_event)

    key = str(PUSHER_KEY)
    cluster = str(PUSHER_CLUSTER)
    pusher = pysher.Pusher(key = key, cluster = cluster)
    pusher.connection.bind("pusher:connection_established", connect_handler)
    pusher.connect()

    page.add(
        Column([
            Text('This is Html Page', size=15, weight='medium')
        ])
    )
    while True:
        time.sleep(1)

app(target=main_flet)
