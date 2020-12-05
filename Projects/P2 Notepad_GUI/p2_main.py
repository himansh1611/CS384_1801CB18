import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter.messagebox import showinfo
import datetime
import time
import os
os.system('cls')

main_app = tk.Tk()
main_app.geometry("800x600")
main_app.title("Our Notepad")

menu = tk.Menu()
# file menu

file = tk.Menu(menu, tearoff=False)

menu.add_cascade(label="File", menu=file)

url = ""


def new_file(event=None):
    global url
    url = " "
    text_editor.delete(1.0, tk.END)


file.add_command(label="New", compound=tk.LEFT,
                 accelerator="Ctrl+N", command=new_file)


def Open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="select file", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
    try:
        with open(url, "r") as for_read:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))


file.add_command(label="Open", compound=tk.LEFT,
                 accelerator="Ctrl+o", command=Open_file)