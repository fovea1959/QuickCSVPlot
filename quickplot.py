import csv

import numpy as np

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar2Wx
import wx

import quickplot_wx

matplotlib.use('WXAgg')

class PlotCanvasPanel(wx.Panel):
    def __init__(self, parent, x, y):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()

        self.x = x
        self.y = y

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()

    def Draw(self):
        self.axes.plot(self.x, self.y)


class PlotFrame(wx.Frame):
    def __init__(self, parent, title, x, y):
        wx.Frame.__init__(self, parent, -1,
                          title,
                          size=(620, 620))
        self.SetMinSize((620, 620))
        self.panel = PlotCanvasPanel(self, x, y)
        self.panel.Draw()


class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window : QuickPlotFrame = window

    def OnDropFiles(self, x, y, filenames):
        message = f"{len(filenames)} file(s) dropped at ({x}, {y})"
        print(message)
        self.window.handle_dropped_files(filenames)
        return True


class QuickPlotFrame(quickplot_wx.QuickplotFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.checkboxes = {}
        self.data = {}
        self.fn = None

        self.drop_target = MyFileDropTarget(self)
        self.SetDropTarget(self.drop_target)

    def handle_dropped_files(self, filenames):
        self.data.clear()
        self.fn = None
        for file in filenames:
            self.fn = file
            with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                labels = reader.fieldnames
                for label in labels:
                    self.data[label] = []
                for row in reader:
                    if row['time'] is not None and row['time'] != '':
                        for label in labels:
                            v = row[label]
                            if v is not None:
                                try:
                                    v = float(v)
                                except:
                                    pass
                            self.data[label].append(v)
            break

        changed_checkboxes = False
        for label in self.data.keys():
            if label not in ['meta', 'time', 'timeSinceStart']:
                if label not in self.checkboxes.keys():
                    checkbox = wx.CheckBox(self.cb_window, label=label)
                    self.cb_sizer.Add(checkbox)
                    self.checkboxes[label] = checkbox
                    changed_checkboxes = True

        if changed_checkboxes:
            self.plot_button.Enable(True)
            self.Layout()
            pass
        else:
            self.do_plot()

    def on_plot_button_pressed(self, event):
        self.do_plot()
        event.Skip()

    def do_plot(self):
        pf = PlotFrame(self, self.fn, self.data['time'], self.data['main.rpm.actual'])
        pf.Show()
        self.plot_button.Enable(False)

if __name__ == '__main__':
    app = wx.App()

    frm1 = QuickPlotFrame(None)
    frm1.Show()

    app.MainLoop()