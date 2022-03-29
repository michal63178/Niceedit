import tkinter

tabs = []
files = {}
last = None
text = None
left = None
right = None


class Tab:
    def __init__(self, bar, name):
        self.tab = tkinter.Label(bar, text=name, bg='#ebebeb')
        self.active = False
        self.shown = False


def draw(bar, text_p, last_p):
    global left, right, text, last
    
    text = text_p
    last = last_p

    n = 1
    tabs_width = 0
    bar_width = bar.winfo_width()

    for tab in tabs[::-1]:
        tab_width = tab.tab.winfo_reqwidth()
        
        if tabs_width + tab_width <= bar_width:
            tabs_width += tab_width
            n += 1

        else:
            break

    index = len(tabs) - n

    for tab in tabs[index:]:
        tab.tab.pack(side=tkinter.LEFT)
        tab.shown = True

    for tab in tabs:
        if tab.active:
            tab.tab['bg'] = '#ebebeb'
            tab.active = False
            break

    left = tabs[index]
    right = tabs[-1]
    right.active = True
    right.tab['bg'] = '#ffffff'


def pick_up_event(event, v):
    if event.num == 4 or event.delta == 120:
        scroll_up(v)

    elif event.num == 5 or event.delta == -120:
        scroll_down(v)


def scroll_up(v, event=None):
    global left, right

    if v:
        if len(tabs) > 0:
            if not tabs[-1].shown:
                left.tab.pack_forget()
                left.shown = False
                left = tabs[tabs.index(left) + 1]

                right = tabs[tabs.index(right) + 1]
                right.shown = True


def scroll_down(v, event=None):
    global left, right

    if v:
        if len(tabs) > 0:
            if not tabs[0].shown:
                for tab in tabs[tabs.index(left):]:
                    tab.tab.pack_forget()

                left = tabs[tabs.index(left) - 1]

                for tab in tabs[tabs.index(left):]:
                    tab.tab.pack(side=tkinter.LEFT)

                left.shown = True

                right.shown = False
                right = tabs[tabs.index(right) - 1]


def switch(event):
    global files, text, last

    last.content = text.get(1.0, tkinter.END).strip('\n')
    last = files[event.widget]

    for tab in tabs:
        if tab.active:
            tab.tab['bg'] = '#ebebeb'
            tab.active = False
            break

    for tab in tabs:
        if tab.tab == event.widget:
            tab.tab['bg'] = '#ffffff'
            tab.active = True
            break

    text.delete(1.0, tkinter.END)
    text.insert(tkinter.INSERT, last.content)
