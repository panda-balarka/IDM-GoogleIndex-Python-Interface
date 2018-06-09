''' 
Tkinter interface to download files from the main index link from google search

- panda_inline4
'''

# import the required libraries
import tkinter as tk
from tkinter import ttk
from idm_dwn import *


# Gui class
class Gui_Main(tk.Frame):
    
    def __init__(self,parent):
        self.parent = parent
        parent.geometry("450x200")
        parent.title("Google_Index-IDM Downloader Interface")
        parent.resizable(0,0)
        
        mainStyle_V = ttk.Style()
        mainStyle_V.theme_use("xpnative")
        
        #self.frameStlye_V = ttk.Style("TFrame")
        
        self.widgets_F()
    
    def widgets_F(self):
        
        addressFrame_V = ttk.Frame(self.parent,height=50,width=450)
        addressFrame_V.pack(side='top',anchor='center')
        addressFrame_V.pack_propagate(False)
        
        pathFrame_V = ttk.Frame(self.parent,height=50,width=450)
        pathFrame_V.pack(side='top',anchor='center')
        pathFrame_V.pack_propagate(False)
        
        specFileName_V = ttk.Frame(self.parent,height=50,width=450)
        specFileName_V.pack(side='top',anchor='center')
        specFileName_V.pack_propagate(False)        
        
        buttonFrame_V = ttk.Frame(self.parent,height=50,width=450)
        buttonFrame_V.pack(side='top',anchor='center')        
        
        urlLabel_V = ttk.Label(addressFrame_V,text='Index URL : ')
        urlLabel_V.pack(side='left',padx = 5,pady = 5,anchor = 'w')
              
        urlString_V = tk.StringVar()
        urlEntry_V = ttk.Entry(addressFrame_V,textvariable=urlString_V,width = 50)
        urlEntry_V.pack(side='left',padx = [34,5], pady = 5)
        
        filePathLabel_V = ttk.Label(pathFrame_V,text='Download Path : ')
        filePathLabel_V.pack(side='left',padx = 5,pady = 5)
        
        filePathString_V = tk.StringVar()
        filePathEntry_V = ttk.Entry(pathFrame_V,textvariable=filePathString_V,width = 50)
        filePathEntry_V.pack(side='left',padx = 5, pady = 5)
        
        fileNameLabel_V = ttk.Label(specFileName_V,text='FileName Series : ')
        fileNameLabel_V.pack(side='left',padx = 5,pady = 10)
        
        fileNameString_V = tk.StringVar()
        FileNameEntry_V = ttk.Entry(specFileName_V,textvariable=fileNameString_V,width = 50)
        FileNameEntry_V.pack(side='left',padx = 3, pady = 5)

        launchIdmButton_V = ttk.Button(buttonFrame_V,text = 'Download',command = lambda : \
                                       self.launchInterface_F(urlString_V.get(),
                                                              filePathString_V.get(),
                                                              fileNameString_V.get()))
        launchIdmButton_V.pack(side = 'left' ,anchor = 'center' , padx = 5, pady = 10)
        
        quitButton_V = ttk.Button(buttonFrame_V,text = 'Quit',command = self.parent.destroy)
        quitButton_V.pack(side = 'left' ,anchor = 'center' , padx = 5, pady = 10)
        
    def launchInterface_F(self,urlString_V,filePathString_V,fileNameString_V):
        get_links(urlString_V,filePathString_V,fileNameString_V)        
        
        
tk_Obj = tk.Tk()
application_Obj = Gui_Main(tk_Obj)
tk_Obj.mainloop()
