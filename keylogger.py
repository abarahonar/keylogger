#!/usr/bin/env python
import logging
import sys
import time
from pynput.keyboard import Listener
from setproctitle import setproctitle


PRESS_TEMPLATE = "{},PRESS,{}"
RELEASE_TEMPLATE = "{},RELEASE,{}"


def get_time():
    return int(round(time.time() * 1000))


def strip_quote(key):
    return key[1] if key[0] == "'" else key


def on_press(key):
    key = strip_quote(str(key))
    logging.info(PRESS_TEMPLATE.format(get_time(), key))


def on_release(key):
    key = strip_quote(str(key))
    logging.info(RELEASE_TEMPLATE.format(get_time(), key))


logging.basicConfig(stream=sys.stdout, format="%(message)s", level=logging.INFO)

if len(sys.argv) > 1:
    setproctitle(sys.argv[1])

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
