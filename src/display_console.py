import os
import time

from rich.console import Console
from rich.table import Table
from rich.progress import track

from .display_base import _DisplayBase


class Display(_DisplayBase):
    def __init__(self):
        self._cols, self._lines = os.get_terminal_size()
        super().__init__(self._cols, self._lines, 2, 'console')
        self._console = Console()

    def clear(self, attribs=None):
        goHome = (self._parse_attribs(attribs, 'goHome', True) is True)
        self._console.clear(goHome)

    def display_msg(self, msg='', attribs=None):
        style = self._parse_attribs(attribs, 'style', '')
        self._console.print(msg, style=style)

    def display_table(self, data=None, columns=None, attribs=None):
        style = self._parse_attribs(attribs, 'style', '')
        hasHeader = (columns is not None)

        table = Table(show_header=hasHeader, style=style)
        for col in columns:
            table.add_column(col['title'], style=col['style'], width=col['width'], justify=col['justify'])

        for row in data:
            table.add_row(*row)

        self._console.print(table)

    def display_status(self, tasks=None, msg=None):
        statusMsg = msg if msg is not None else "Processing ..."

        with self._console.status(statusMsg):
            while tasks:
                task = tasks.pop(0)
                task['action']()
                self._console.log("{} complete.".format(task['title']))

    def display_log(self, data):
        self._console.log(data)

    def display_progress(self, data):
        def do_step(step):
            time.sleep(1)

        for step in track(range(len(data)*5)):
            do_step(step)
