#!/usr/bin/env python3

import Xlib
import Xlib.display
import time
import subprocess
import os
import sys


disp = Xlib.display.Display()
root = disp.screen().root
inspection_list = [root]

NET_CLIENT_LIST = disp.intern_atom('_NET_CLIENT_LIST')


def set_theme_variant_by_window_id(id):
    try:
        subprocess.call(['xprop', '-f', '_GTK_THEME_VARIANT', '8u', '-set', '_GTK_THEME_VARIANT', 'dark', '-id', str(id)],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False


def set_theme_variant():

    start = time.time()
    root.change_attributes(event_mask=Xlib.X.PropertyChangeMask)

    while True:

        if time.time() - start <= 3:
            disp.next_event()

        for win_id in root.get_full_property(NET_CLIENT_LIST, Xlib.X.AnyPropertyType).value:
            try:
                win = disp.create_resource_object('window', win_id)
                if not win.get_wm_transient_for():
                    win_class = win.get_wm_class()
                    if win_id and 'prusa-slicer' in win_class:
                        if set_theme_variant_by_window_id(win_id):
                            return True

            except Xlib.error.BadWindow:
                pass

    if time.time() - start <= 10:
        return False


if __name__ == '__main__':
    root.change_attributes(event_mask=Xlib.X.PropertyChangeMask)
    set_theme_variant()
