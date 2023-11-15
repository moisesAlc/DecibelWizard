from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile


def get_file_gui():
    filename = fd.askopenfilename()
    return filename


def get_save_destination_gui():
    filename = asksaveasfile()
    return filename
