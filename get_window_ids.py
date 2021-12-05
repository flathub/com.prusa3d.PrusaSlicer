#!/usr/bin/env python3

import Xlib
import Xlib.display
import time
import subprocess
import os
import sys

disp = Xlib.display.Display()
root = disp.screen().root

NET_CLIENT_LIST = disp.intern_atom('_NET_CLIENT_LIST')


def set_theme_variant(window_titles, variant):
    winids = []
    win_ids = root.get_full_property(NET_CLIENT_LIST, Xlib.X.AnyPropertyType)
    if win_ids:
        win_ids = win_ids.value
        try:
            for win_id in win_ids:
                win = disp.create_resource_object('window', win_id)
                win_name = win.get_wm_name()
                if win_name and window_titles in win_name:
                    winids.append(str(win_id))
        except:
            pass

    return winids


if os.environ.get('PRUSA_SLICER_DARK_THEME') != 'true':
    sys.exit(0)

start = time.time()
root.change_attributes(event_mask=Xlib.X.PropertyChangeMask)
window_titles = ('PrusaSlicer')
variant = 'dark'

if time.time() - start <= 2:
    disp.next_event()
    time.sleep(1)
    l = list(set(set_theme_variant(window_titles, variant)))
    for i in l:
        print(i)
else:
    l = list(set(set_theme_variant(window_titles, variant)))
    for i in l:
        print(i)
