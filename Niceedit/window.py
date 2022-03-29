import tkinter


class Window(tkinter.Tk):
    def __init__(self, title='Window', stat='normal'):
        super().__init__()
        self.title = tkinter.Tk.title(self, title)
        self.state = tkinter.Tk.state(self, stat)
