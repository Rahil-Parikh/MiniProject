#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#    Apr 10, 2020 08:15:18 PM IST  platform: Windows NT
import sys
import models
from models import *
from modelui import *
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import second_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    second_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    second_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def entrystyle():
    data = open("pic.dat").read()
    global s1, s2
    s1 = tk.PhotoImage("search1", data=data, format="gif -index 0")
    style = ttk.Style()
    style.element_create("Search.field", "image", "search1",
         border=[22, 7, 14], sticky="ew")
    style.layout("Search.entry", [
        ("Search.field", {"sticky": "nswe", "border": 5, "children":
            [("Entry.padding", {"sticky": "nswe", "children":
                [("Entry.textarea", {"sticky": "nswe"})]
            })]
        })]
    )
    style.configure("Search.entry", background="#444444")

models_d = get_models()
mylabels = []
h_line = []
frame_L = []

def get_all_models():
    return models_d.keys()

def getmodels(str):
    result = []
    for i in All_models:
        if str in i:
            result.append(i)
    return result

def change(event):
    label = event.widget
    label.configure(bg = "#FFFFFF",fg = "black")

def changeagain(event):
    label = event.widget
    label.configure(bg = "#444444" , fg = "#bebebe")

def clicked_model(event):
    label = event.widget 
    print("hah", models_d,"aaha")
    m = label['text']
    model_id = models_d[m]
    obj = Model(model_id)
    obj.load_id()
    print(obj)
    tw = create_Toplevel2(root,obj)

def dynamicSearch(sv):
    print(sv)
    models = getmodels(sv)
    if mylabels:
        for i in range(len(mylabels)):
            h_line[i].destroy()
            mylabels[i].destroy()
            frame_L[i].destroy()

        del mylabels[:]
        del h_line [:]
        del frame_L[:]
    for i in range(len(models)):
        frame_L.append(tk.Frame(root))
        frame_L[i].pack(side=tk.TOP, anchor="w",fill='x')

        mylabels.append(tk.Label(frame_L[i],text=models[i] ,padx=10))
        mylabels[i].pack(expand = True,fill=tk.BOTH)
        mylabels[i].configure(fg = "#bebebe",font = 'bold 15' , anchor = "w",background = '#444444')
        #if i%2 :
        #    mylabels[i].configure(background = "#878683")
        mylabels[i].bind('<Enter>',lambda event : change(event))
        mylabels[i].bind('<Leave>',lambda event : changeagain(event))
        mylabels[i].bind('<Button-1>',lambda event : clicked_model(event))

        h_line.append(ttk.Separator(frame_L[i], orient='horizontal'))
        h_line[i].pack(fill='x')
        
class Toplevel1:
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("GANS Store")
        top.configure(background="#444444")
        entrystyle()
        global All_models 
        All_models = get_all_models()
        sv = tk.StringVar()
        
        entry1 = ttk.Entry(root, style="Search.entry", width=70,textvariable=sv)
        entry1.pack()

        separator = ttk.Separator(root, orient='horizontal')
        separator.pack(side='top', fill='x')

        dynamicSearch("")

        sv.trace("w", lambda name, index, mode, sv=sv: dynamicSearch(sv.get()))
   
    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="-family {Segoe UI} -size 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()
