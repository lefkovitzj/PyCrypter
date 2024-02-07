"""
    Author: AaronTook (https://AaronTook.github.io)
    Version: 1.0.0
    Version Launch Date: 2/6/2024
    File Last Modified: 2/6/2024
    Project Name: PyCrypter
    File Name: app.py
"""

# Python Standard Library Imports
from tkinter import *
from tkinter import filedialog
import os

def gui_get_file(initial_directory="", limit_filetypes=[]):
    """ Open file explorer (using tkinter) to select a file. """
    root = Tk()
    root.withdraw()
    complete_file_path = filedialog.askopenfilename(title="Encrypt - File Select", initialdir = os.getcwd() + "/" + initial_directory, filetypes = limit_filetypes)
    root.destroy()
    file_path, file_name = os.path.split(complete_file_path)
    return complete_file_path, file_name
def gui_get_files(initial_directory="", limit_filetypes=[]):
    """ Open file explorer (using tkinter) to select multiple files. """
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="Encrypt - File Select", initialdir = os.getcwd() + "/" + initial_directory, filetypes = limit_filetypes)
    root.destroy()
    file_paths_full = []
    file_paths_partial = []
    for file_path in file_paths:
        file_paths_full.append(file_path)
        file_paths_partial.append(os.path.split(file_path))
    return file_paths_full, file_paths_partial
