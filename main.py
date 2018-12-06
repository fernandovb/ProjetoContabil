# -*- coding: utf-8 -*-

import wx.xrc
from _telas.mn01 import MN01


class App(wx.App):

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        frame = MN01(None)
        frame.Show()


if __name__ == '__main__':
    App().MainLoop()
