import os
import sys
import argparse


_VALID_MODULES_ = ['console', 'led8x8sh']
_LED8x8_ATTRIBS_ = {
    'doClear': True,
    'doDim': True,
    'clearColor': (0, 0, 0),
    'rotation': 270,
    'speed': 0.1,
    'fgColor': (128, 0, 0),
    'bgColor': (0, 0, 0),
    'holdTime': 1,
    'style': 'bold blue',
}

parser = argparse.ArgumentParser(description="Try displaying content via 'DisplayMod' module",
                                 epilog="NOTE: Only call a module if the corresponding hardware/driver is installed")
parser.add_argument('--mod',
                    action='store',
                    type=str,
                    required=True,
                    help="Display module to use")
parser.add_argument('--msg',
                    action='store',
                    type=str,
                    help="Text to display")

args = parser.parse_args()
display = None

if args.mod not in _VALID_MODULES_:
    print("ERROR: '{}' is not a valid display module!".format(args.mod))
    exit(1)

if args.mod == 'console':
    from .display_console import Display

if args.mod == 'led8x8sh':
    from .display_LED8x8SH import Display

display = Display()

if args.msg is None:
    text = "Hello world!"
else:
    text = args.msg

display.display_msg(text, _LED8x8_ATTRIBS_)
display.display_progress(['apple', 'banana', 'orange'])
display.display_log(['apple', 'banana', 'orange'])

columns, lines = display.resolution
colors = display.colors

print("COLS: {} - LINES: {} - COLORS: {}".format(columns, lines, colors))

display.clear()

