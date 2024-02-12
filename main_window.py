import customtkinter as sck
import tkinter as tk
import screeninfo
import keyboard
from Scripts import (
    get_jsondata, write_monitor_info, write_userinfo
)
from tkinter import *
from datetime import datetime
from tkinter.filedialog import (askopenfile, askdirectory, asksaveasfilename, asksaveasfile)
from tkinter import messagebox

hour = datetime.now().hour

class Application_Files_Functions:
    def newfile(content):
        confirm = messagebox.askyesno('Create new document', 'Are u sure u want to create a new text document?')
        if confirm == TRUE:
            content.delete('1.0', 'end')
        elif confirm == FALSE:
            pass
        
    def save(content): 
        file = asksaveasfile(mode="w", filetypes=[('Document', '*.*')])
        tosave = content.get("1.0", "end")
        file.write(tosave)
        file.close()
        
    def saveas(content): ...
    
    def open_(content) -> None: 
        file = askopenfile(mode="r", filetypes=[('Document', '*.*')])
        content.delete("1.0", "end")
        content.insert("1.0", file.read())
        file.close()
        
    def copy(content) -> None: ...
    
    def paste(content) -> None: ...

class Application:
    def menubar(self, window, textentry) -> None:
        menus = tk.Menu()
        
        # ______Configure functions______
        FileFunctions_Class = Application_Files_Functions
        save_file, open_file = lambda: FileFunctions_Class.save(textentry), lambda: FileFunctions_Class.open_(textentry)
        newfile = lambda: FileFunctions_Class.newfile(textentry)
        
        def kbtrigger_filefunctions():
            keyboard.add_hotkey('Ctrl+N', newfile)
            keyboard.add_hotkey('Ctrl+O', open_file)
            keyboard.add_hotkey('Ctrl+S', save_file)
        
        kbtrigger_filefunctions()
        
        # __________File__________
        filefunctions = Application_Files_Functions
        menu_files = tk.Menu(menus, tearoff=0)
        menu_files.add_command(label="New", accelerator="Ctrl+N", command=newfile, font=('Helvetica', 9))
        menu_files.add_command(label="Save", command=save_file, accelerator="Ctrl+S", font=('Helvetica', 9))
        menu_files.add_command(label="Save as ", command=any, accelerator="Ctrl+E", font=('Helvetica', 9))
        menu_files.add_command(label="Open", accelerator="Ctrl+O", command=open_file, font=('Helvetica', 9))
        
        # __________UTILS__________
        menu_utils = tk.Menu(menus, tearoff=0)
        menu_utils.add_command(label="Compress", font=('Helvetica', 9))
        menu_utils.add_command(label="Download", font=('Helvetica', 9))
        
        # __________AI__________
        menu_ai = tk.Menu(menus, tearoff=0)
        menu_ai.add_command(label="Assistant", font=('Helvetica', 9))
        menu_ai.add_command(label="Chat-GPT", font=('Helvetica', 9))
        
        # _____Configuring menu_____
        menus.add_cascade(label="File", menu=menu_files)
        menus.add_cascade(label="Utils", menu=menu_utils)
        menus.add_cascade(label="AI", menu=menu_ai)
        window.config(menu=menus)

    def __init__(self)-> None:
        window = sck.CTk()
        
        # ________Configuring sizes________
        text_ = Text(window, font=('Helvetica', 10))
        text_.pack(side="top", fill="both", expand=True)
        window.geometry("800x550")
        
        # ________Configuring window________
        window.title('Aether')
        self.menubar(window, text_)
        window.mainloop()

if __name__ == "__main__":
    
    # Honestly idk why font size gets shorter If deleting `write_monitor_info`
    # Mood: confused (¿?)
    write_monitor_info()
    write_userinfo()
    Application()