from tkinter import filedialog
import tkinter
import tab


class File:
    def __init__(self):
        self.directory = None
        self.content = None
        self.name = None
        self.path = None

    def file_info(self):
        index = self.path.rfind('/')
        self.directory = self.path[:index]
        self.name = self.path[index + 1:]

    def open(self, path):
        self.path = path

        with open(self.path, encoding='utf-8') as f:
            self.content = f.read()

        self.file_info()

    def save_as(self, txt):
        keep_path = self.path
        self.content = txt
        self.path = \
            filedialog.asksaveasfilename(initialfile=self.name, initialdir=None,
                                         title='Choose a directory',
                                         filetypes=(('All files', '*.*'),
                                                    ('Text files', '*.txt')))

        if self.path:
            with open(self.path, 'w', encoding='utf-8') as f:
                f.write(txt)

            self.file_info()

        else:
            self.path = keep_path

    def save(self, txt):
        self.content = txt

        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(txt)


def file_tab(f, bar, txt):
    to_draw = tab.Tab(bar, f.name)
    tab.tabs.append(to_draw)
    tab.files[to_draw.tab] = f
    tab.draw(bar, txt, f)


def open_wrapper(txt, bar):
    files = filedialog.askopenfilenames(initialdir=None, title='Browse files',
                                        filetypes=(('All files', '*.*'),
                                                   ('Text file', '*.txt')))

    if files:
        obj = None

        for el in files:
            obj = File()
            obj.open(el)
            to_draw = tab.Tab(bar, obj.name)
            to_draw.tab.bind('<Button-1>', tab.switch)
            tab.tabs.append(to_draw)
            tab.files[to_draw.tab] = obj

        txt.delete(1.0, tkinter.END)
        txt.insert(tkinter.INSERT, obj.content)
        tab.draw(bar, txt, obj)


def save_as_wrapper(txt, bar):
    if tab.last.path:
        tab.last.save_as(txt.get(1.0, tkinter.END).strip('\n'))

    else:
        obj = File()
        obj.save_as(txt.get(1.0, tkinter.END).strip('\n'))

        if obj.path:
            file_tab(obj, bar, txt)


def save_wrapper(txt, bar):
    if tab.last.path:
        tab.last.save(txt.get(1.0, tkinter.END).strip('\n'))

    else:
        obj = File()
        obj.save_as(txt.get(1.0, tkinter.END).strip('\n'))

        if obj.path:
            file_tab(obj, bar, txt)
