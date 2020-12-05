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

def Exit_fun(event=None):
    global url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel(
                "warning", " Do you want to save this file")
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        main_app.destroy()
                else:
                    content_2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(
                        ("Text file", "*.txt"), ("All files", "*.*")))
                    url.write(content_2)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return


file.add_command(label="Exit", compound=tk.LEFT,
                 accelerator="Ctrl+", command=Exit_fun)
# Edit menu
Edit = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=Edit)
Edit.add_command(label="Copy", compound=tk.LEFT, accelerator="Ctrl+C",
                 command=lambda: text_editor.event_generate("<Control c>"))
Edit.add_command(label="Cut", compound=tk.LEFT, accelerator="Ctrl+X",
                 command=lambda: text_editor.event_generate("<Control x>"))
Edit.add_command(label="Paste", compound=tk.LEFT, accelerator="Ctrl+v",
                 command=lambda: text_editor.event_generate("<Control v>"))


def find_fun(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0

        if word:
            start_position = "1.0"
            while True:
                start_position = text_editor.search(
                    word, start_position, stopindex=tk.END)
                if not start_position:
                    break
                end_position = f"{start_position}+{len(word)}c"
                text_editor.tag_add("match", start_position, end_position)
                matches += 1
                start_position = end_position
                text_editor.tag_config(
                    'match', foreground="red", background="blue")

    find_popup = tk.Toplevel()
    find_popup.geometry("300x150")
    find_popup.title("find word")
    find_popup.resizable(0, 0)

    find_fram = ttk.Labelframe(find_popup, text="Find")
    find_fram.pack(pady=20)

    text_find = ttk.Label(find_fram, text="Find")
    find_input = ttk.Entry(find_fram, width=30)
    find_button = ttk.Button(find_fram, text="Find", command=find)
    text_find.grid(row=0, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    find_button.grid(row=2, column=0, padx=8, pady=4)


Edit.add_command(label="Find", compound=tk.LEFT,
                 accelerator="Ctrl+f", command=find_fun)


def find_and_replace_fun(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove("match", "1.0", tk.END)
        matches = 0
        if word:
            start_position = "1.0"
            while True:
                start_position = text_editor.search(
                    word, start_position, stopindex=tk.END)
                if not start_position:
                    break
                end_position = f"{start_position}+{len(word)}c"
                text_editor.tag_add("match", start_position, end_position)
                matches += 1
                start_position = end_position
                text_editor.tag_config(
                    'match', foreground="red", background="blue")

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_popup = tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("find word")
    find_popup.resizable(0, 0)
    # frame
    find_fram = ttk.Labelframe(find_popup, text="Find and Replace Word")
    find_fram.pack(pady=20)

    text_find = ttk.Label(find_fram, text="Find")
    text_replace = ttk.Label(find_fram, text="Replace")

    find_input = ttk.Entry(find_fram, width=30)
    replace_input = ttk.Entry(find_fram, width=30)

    find_button = ttk.Button(find_fram, text="Find", command=find)
    replace_button = ttk.Button(find_fram, text="Replace", command=replace)

    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)
