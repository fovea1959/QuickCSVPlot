# https://stackoverflow.com/a/24261464/17887564


# Used to guarantee to use at least Wx2.8
#import wxversion

#wxversion.ensureMinimal('2.8')

import numpy as np
import wx
import csv

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window, canvas_panel):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.canvas_panel = canvas_panel
        print('mydropwindow', window)
        print('mydropwindow.canvaspanel', canvas_panel)


    def OnDropFiles(self, x, y, filenames):
        fig = self.window.figure
        inaxes = fig.get_axes()[0]
        h_pix = int(fig.get_figheight() * fig.get_dpi()) # fig height in pixels
        message = "%d file(s) dropped at (%d,%d):\n" % (len(filenames), x, y)
        data = {}
        for file in filenames:
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                labels = reader.fieldnames
                for label in labels:
                    data[label] = []
                for row in reader:
                    if row['time'] is not None and row['time'] != '':
                        for label in labels:
                            v = row[label]
                            if v is not None:
                                try:
                                    v = float(v)
                                except:
                                    pass
                            data[label].append(v)
            break
        print(data)
        inaxes.annotate(message, (x, h_pix-y), xycoords='figure pixels')
        self.canvas_panel.setXY(data['time'], data['main.rpm.actual'])
        self.canvas_panel.draw()
        self.window.draw()
        return True

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.add_toolbar()
        self.Fit()

        self.xseries = np.linspace(0.0, 6., 100)
        self.yseries = np.sin(2 * np.pi * self.xseries)

        win_target = self.canvas
        dt = MyFileDropTarget(win_target, self)
        win_target.SetDropTarget(dt)

        print('canvaspanel', self)

    def setXY(self, x, y):
        self.xseries = x
        self.yseries = y

    def draw(self):

        print("axes", type(self.axes))
        self.axes.clear()
        min_x = int(min(self.xseries) - 1)
        max_x = int(max(self.xseries) + 1)
        self.axes.set_xticks(np.arange(min_x, max_x + 1, 1.0))
        rv = self.axes.plot(self.xseries, self.yseries)
        print(rv)
        print(self.axes)

    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        if wx.Platform == '__WXMAC__':
            # Mac platform (OSX 10.3, MacPython) does not seem to cope with
            # having a toolbar in a sizer. This work-around gets the buttons
            # back, but at the expense of having the toolbar at the top
            self.SetToolBar(self.toolbar)
        else:
            # On Windows platform, default window size is incorrect, so set
            # toolbar width to figure width.
            tw, th = self.toolbar.GetSize()
            fw, fh = self.canvas.GetSize()
            # By adding toolbar in sizer, we are able to put it at the bottom
            # of the frame - so appearance is closer to GTK version.
            # As noted above, doesn't work for Mac.
            self.toolbar.SetSize(wx.Size(fw, th))
            self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        # update the axes menu on the toolbar
        self.toolbar.update()

if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, title='File drop test')
    panel = CanvasPanel(frame)
    panel.draw()
    frame.Show()
    app.MainLoop()