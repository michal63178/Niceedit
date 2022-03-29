import tkinter
import window
import file
import tab


class Main(window.Window):
    def __init__(self):
        super().__init__('Niceedit', 'zoomed')

        self.menu_bar = tkinter.Menu(self)
        self.menu = tkinter.Menu(self)
        tkinter.Tk.config(self, menu=self.menu)

        self.task = tkinter.Menu(self.menu)
        self.menu.add_cascade(label='Task', menu=self.task)
        self.task.add_command(label='Open', command=lambda: file.open_wrapper(self.text_field, self.files_bar))
        self.task.add_command(label='Save', command=lambda: file.save_wrapper(self.text_field, self.files_bar))
        self.task.add_command(label='Save as', command=lambda: file.save_as_wrapper(self.text_field, self.files_bar))
        self.task.add_separator()
        self.task.add_command(label='Quit program', command=self.quit)

        self.files_bar = tkinter.Frame(self, height=21)

        self.scroll_bar_x = tkinter.Scrollbar(self, orient=tkinter.HORIZONTAL)
        self.scroll_bar_y = tkinter.Scrollbar(self)

        self.text_field = tkinter.Text(self, xscrollcommand=self.scroll_bar_x.set,
                                       yscrollcommand=self.scroll_bar_y.set,
                                       wrap=tkinter.NONE)

        self.files_bar.pack(fill=tkinter.X)

        self.scroll_bar_x.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.scroll_bar_x.config(command=self.text_field.xview)
        self.scroll_bar_y.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scroll_bar_y.config(command=self.text_field.yview)

        self.text_field.pack(expand=True, fill=tkinter.BOTH)

        self.files_bar_focus = False

        self.files_bar.bind('<Enter>', lambda event: self.turn_files_bar_focus(True))
        self.files_bar.bind('<Leave>', lambda event: self.turn_files_bar_focus(False))

        if tkinter.sys.platform == 'win32':
            self.bind('<MouseWheel>', lambda event: tab.pick_up_event(event, self.files_bar_focus))

        else:
            self.bind('<Button-4>', lambda event: tab.scroll_up(self.files_bar_focus, event))
            self.bind('<Button-5>', lambda event: tab.scroll_down(self.files_bar_focus, event))

    def turn_files_bar_focus(self, v):
        self.files_bar_focus = v
