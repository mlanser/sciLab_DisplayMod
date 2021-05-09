import time
import copy

from sense_hat import SenseHat

from .display_base import _DisplayBase


# =========================================================
#                      G L O B A L S
# =========================================================
# Misc. defaults
_DEFAULT_HOLD_TIME_: int = 0         # 0 sec
_DEFAULT_STYLE_:     str = ''        # Blank string
_DEFAULT_SPEED_:     float = 0.1     # Default speed for scrolling msg

# Screen resolution for SenseHat 8x8 16bit LED
_SCRN_RES_X_:        int = 8
_SCRN_RES_Y_:        int = 8
_SCRN_COLORS_:       int = 16
_SCRN_TYPE_:         str = 'led8x8'

_ROTATE_N_:          int = 0         # North -   0 degrees
_ROTATE_E_:          int = 90        # East  -  90 degrees
_ROTATE_S_:          int = 180       # South - 180 degrees
_ROTATE_W_:          int = 270       # West  - 270 degrees

# Core color definitions
_BLK_:               tuple = (0, 0, 0)        # Black
_WHT_:               tuple = (255, 255, 255)  # White
_RED_:               tuple = (255, 0, 0)      # Red
_ORN_:               tuple = (255, 127, 0)    # Orange
_YEL_:               tuple = (255, 255, 0)    # Yellow
_GRN_:               tuple = (0, 255, 0)      # Green
_BLU_:               tuple = (0, 0, 255)      # Blue
_PUR_:               tuple = (159, 0, 255)    # Purple


# =========================================================
#        M A I N   C L A S S   D E F I N I T I O N
# =========================================================
class Display(_DisplayBase):
    def __init__(self):
        super().__init__(_SCRN_RES_X_, _SCRN_RES_X_, _SCRN_COLORS_, _SCRN_TYPE_)
        self._display = SenseHat()
        self._image = [_BLK_ for i in range(256)]

    def _init_display(self, attribs):
        rotation = self._parse_attribs(attribs, 'rotation', _ROTATE_N_)
        doDim = (self._parse_attribs(attribs, 'doDim', False) is True)

        self._display.set_rotation(rotation)
        self._display.low_light = doDim

    def clear(self, attribs=None):
        clearColor = self._parse_attribs(attribs, 'clearColor', _BLK_)
        holdTime = self._parse_attribs(attribs, 'holdTime', _DEFAULT_HOLD_TIME_)
        time.sleep(holdTime)
        self._display.clear(clearColor)

    def display_log(self, data=None):
        """The SenseHat 8x8 LED can obviously not show log messages. So we'll simply do nothing :-)"""
        pass

    def display_msg(self, msg='', attribs=None):
        speed = self._parse_attribs(attribs, 'speed', _DEFAULT_SPEED_)
        fgColor = self._parse_attribs(attribs, 'fgColor', _WHT_)
        bgColor = self._parse_attribs(attribs, 'bgColor', _BLK_)

        self._init_display(attribs)

        if len(msg) == 1:
            self._display.show_letter(msg, text_colour=fgColor, back_colour=bgColor)
        elif len(msg) > 1:
            self._display.show_message(msg, scroll_speed=speed, text_colour=fgColor, back_colour=bgColor)

    def display_table(self, data=None, columns=None, attribs=None):
        """The SenseHat 8x8 LED can obviously not show tables. So we'll simply do nothing :-)"""
        pass

    def display_status(self, tasks=None, msg=None, attribs=None):
        work = copy.deepcopy(tasks)
        defaultMsg = msg if msg is not None else "Processing ..."
        finishedMsg = "Finished!"
        speed = self._parse_attribs(attribs, 'speed', _DEFAULT_SPEED_)
        fgColor = self._parse_attribs(attribs, 'fgColor', _WHT_)
        bgColor = self._parse_attribs(attribs, 'bgColor', _BLK_)

        self._init_display(attribs)

        while work:
            task = work.pop(0)
            msg = "{}...".format(task['title']) if task['title'] is not None else defaultMsg
            self._display.show_message(msg, scroll_speed=speed, text_colour=fgColor, back_colour=bgColor)
            task['action'](task['params'])

        self._display.show_message(finishedMsg, scroll_speed=speed, text_colour=fgColor, back_colour=bgColor)

    def display_progress(self, data):
        pass
        # def do_step(step):
        #     time.sleep(1)
        #
        # for step in track(range(len(data)*5)):
        #     do_step(step)
