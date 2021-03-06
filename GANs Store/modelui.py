#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#    Apr 10, 2020 08:15:18 PM IST  platform: Windows NT

import sys
import models
import base64
from ui import change, changeagain
from urllib.request import urlopen
from Animate import AnimatedGIF

from models import *
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

def vp_start_gui2():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel2 (root)
    second_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel2(rt,obj, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
        # new window definition
    newwin = tk.Toplevel(rt)
    newwin.geometry("500x400") 
    newwin.resizable(0, 0)
    global modal_obj 
    modal_obj = obj
    return Toplevel2(newwin,obj)

def destroy_Toplevel2():
    global w
    w.destroy()
    w = None

def hello():
    pass
models_d = get_models()
mylabels = []
h_line = []
frame_L = []

def rrun():
    import importlib
    import pkgutil

    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('new')
    }
    if discovered_plugins['new']:
        importlib.invalidate_caches()
        discovered_plugins['new'].run()
        importlib.invalidate_caches()
    print(discovered_plugins)

def dynamic_import(abs_module_path, class_name):
    import importlib
    module_object = importlib.import_module(abs_module_path)

    target_class = getattr(module_object, class_name)

    return target_class

def clicked_model(event,mtype:str):
    label  = event.widget
    print(label)
    frame = label.master
    bR= tk.Button(frame, text ="RUN", command = rrun)
    bR.pack(side = tk.LEFT,padx=15)
    bD= tk.Label(frame, text ="DOWNLOAD")
    bD.pack(side = tk.LEFT ,padx=15)
    bD.bind('<Button-1>',lambda event : download(event,mtype))
    b = tk.Label(frame,text ="X",padx=10)
    b.pack(side = tk.RIGHT)
    b.bind('<Button-1>',closeframe)

def download(event,mtype):
    e = (event.widget).master.winfo_children()[0]
    m_name =  e["text"]
    if mtype == "architecture" : 
        modal_obj.download_specific_model_architecture(m_name)
    elif mtype =="pretrain":
        modal_obj.download_specific_pretrained_ckpt(m_name)
def closeframe(event):
    frm = (event.widget).master
    t = True
    for child in frm.winfo_children():
        if t:
            t=False
        else : 
            child.destroy()
class Toplevel2:
    
    def __init__(self,top, model):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x700")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Model  - "+ model.name )
        top.configure(background="#444444")
        m_frame = tk.Frame(top)
        m_frame.pack()
        
        image_url = model.images
        gif64 =[]
        image_b64=[]
        for i in model.images:
            if i.endswith(".gif"):
                gif64.append(base64.encodestring(urlopen(image_url).read()))
            image_b64.append(base64.encodestring(urlopen(image_url).read()))

        photo = tk.PhotoImage(data=image_b64)
        b1= tk.Button(m_frame, text ="<", command = hello)
        b1.pack(side=tk.LEFT)
        l = AnimatedGIF(m_frame, "dcgan_downloaded.gif")
        l.pack(side=tk.LEFT)
        b1= tk.Button(m_frame, text =">", command = hello)
        b1.pack(side=tk.LEFT)
        
        frame2 = tk.Frame(top)
        frame2.pack(anchor="w",fill='x')

        name = tk.Label(frame2,text =model.name,font = 'bold 15')
        name.pack()
        
        details = tk.Label(frame2,text ="Details : " + model.details,fg = "#bebebe",font = 'bold 15' , anchor = "w",background = '#444444')
        details.pack(expand = True,fill=tk.BOTH)
        
        m_details = tk.Label(frame2,text = "More Details : " + model.more_details,fg = "#bebebe",font = 'bold 15' , anchor = "w",background = '#444444')
        m_details.pack(expand = True,fill=tk.BOTH)
        pretrained_m = []
        frame_p_a = []
        m_architecture = []
        print(model)
        if model.pretrained_model_b:
            P = tk.Label(frame2,text ="Pretrained Available Models",fg = "#bebebe",font = 'bold 15' , background = '#082c6c')
            P.pack(expand = True,fill=tk.BOTH)
            p_m = list(model.pretrained_model.keys())
            for p in range(len(p_m)):
                f = tk.Frame(top)
                f.pack(anchor="w",fill='x')
                frame_p_a.append(f)
                pretrained_m.append(tk.Label(f,text =p_m[p],padx=10))
                pretrained_m[p].pack(expand = True,fill=tk.BOTH)

                #mylabels[i].pack(expand = True,fill=tk.BOTH)
                pretrained_m[p].configure(fg = "#bebebe",font = 'bold 15' , anchor = "w",background = '#444444')
                pretrained_m[p].bind('<Enter>',lambda event : change(event))
                pretrained_m[p].bind('<Leave>',lambda event : changeagain(event))
                pretrained_m[p].bind('<Button-1>',lambda event : clicked_model(event,"pretrain"))
                
        if model.model_architecture_b:
            f = tk.Frame(top)
            f.pack(anchor="w",fill='x')
            frame_p_a.append(f)
            A = tk.Label(f,text ="Available Models Architectures",fg = "#bebebe",font = 'bold 15' , background = '#082c6c')
            A.pack(expand = True,fill=tk.BOTH)
            a_m =list(model.model_architecture.keys())
            for a in range(len(a_m)):
                f = tk.Frame(top)
                f.pack(anchor="w",fill=tk.X)

                frame_p_a.append(f)
                m_architecture.append(tk.Label(f,text =a_m[a],padx=10))
                m_architecture[a].pack(expand = True,fill=tk.BOTH)
                
                #b.pack() 
                #mylabels[i].pack(expand = True,fill=tk.BOTH)
                m_architecture[a].configure(fg = "#bebebe",font = 'bold 15' , anchor = "w",background = '#444444')
                m_architecture[a].bind('<Enter>',lambda event : change(event))
                m_architecture[a].bind('<Leave>',lambda event : changeagain(event))
                m_architecture[a].bind('<Button-1>',lambda event : clicked_model(event,"architecture"))
                #b= tk.Button(frame2, text ="Find", command = rrun)
                #b.pack()

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
