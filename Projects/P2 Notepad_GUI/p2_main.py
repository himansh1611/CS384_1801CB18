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



def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
                ("Text file", "*.txt"), ("All files", "*.*")))
            content_2 = text_editor.get(1.0, tk.END)
            url.write(content_2)
            url.close()
    except:
        return


file.add_command(label="Save", compound=tk.LEFT,
                 accelerator="Ctrl+s", command=save_file)


def Save_as_file(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode="w", defaultextension="txt", filetypes=(
            ("Text file", "*.txt"), ("All files", "*.*")))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label="Save as", compound=tk.LEFT,
                 accelerator="Ctrl+sft+s", command=Save_as_file)
