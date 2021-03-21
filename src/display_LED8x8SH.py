import os
import time

from sense_hat import SenseHat

from .display_base import _DisplayBase

_BLK_ = (0, 0, 0)           # Black
_WHT_ = (255, 255, 255)     # White
_RED_ = (255, 0, 0)         # Red
_ORN_ = (255, 127, 0)       # Orange
_YEL_ = (255, 255, 0)       # Yellow
_GRN_ = (0, 255, 0)         # Green
_BLU_ = (0, 0, 255)         # Blue
_PUR_ = (159, 0, 255)       # Purple


class Display(_DisplayBase):
    def __init__(self):
        super().__init__(8, 8, 16, 'led8x8')
        self._display = SenseHat()
        self._image = [_BLK_ for i in range(256)]

    def _init_display(self, attribs):
        rotation = self._parse_attribs(attribs, 'rotation', 0)
        doDim = (self._parse_attribs(attribs, 'doDim', False) is True)

        self._display.set_rotation(rotation)
        self._display.low_light = doDim

    def clear(self, attribs=None):
        clearColor = self._parse_attribs(attribs, 'clearColor', _BLK_)
        self._display.clear(clearColor)

    def display_msg(self, msg='', attribs=None):
        doClear = (self._parse_attribs(attribs, 'doClear', False) is True)
        clearColor = self._parse_attribs(attribs, 'clearColor', _BLK_)
        speed = self._parse_attribs(attribs, 'speed', 0.1)
        fgColor = self._parse_attribs(attribs, 'fgColor', _WHT_)
        bgColor = self._parse_attribs(attribs, 'bgColor', _BLK_)
        holdTime = self._parse_attribs(attribs, 'holdTime', 1)

        if doClear:
            self._display.clear(clearColor)

        self._init_display(attribs)

        if len(msg) == 1:
            self._display.show_letter(msg, text_colour=fgColor, back_colour=bgColor)
            if holdTime > 0:
                time.sleep(holdTime)
                self._display.clear(clearColor)

        elif len(msg) > 1:
            self._display.show_message(msg, scroll_speed=speed, text_colour=fgColor, back_colour=bgColor)

    def display_table(self, data=None, columns=None, attribs=None):
        """The SenseHat 8x8 LED can obviously not show tables. So we'll simply do nothing :-)"""
        pass

    def display_status(self, tasks=None, msg=None):
        statusMsg = msg if msg is not None else "Processing ..."
        self._display.show_message(statusMsg)

        # with self._console.status(statusMsg):
        #     while tasks:
        #         task = tasks.pop(0)
        #         task['action']()
        #         self._console.log("{} complete.".format(task['title']))

    def display_log(self, data):
        """The SenseHat 8x8 LED can obviously not show log messages. So we'll simply do nothing :-)"""
        pass

    def display_progress(self, data):
        pass
        # def do_step(step):
        #     time.sleep(1)
        #
        # for step in track(range(len(data)*5)):
        #     do_step(step)
