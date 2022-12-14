# importing the module
import os
import tkinter as tk
from threading import *
from tkinter import filedialog as fd
from tkinter import messagebox

from pytube import YouTube


# defining a function that will ask for mp3/mp4
def submit():
    ask = messagebox.askyesno("mp3/mp4", "Do you want to download a whole vide or just sound? "
                                         "click 'yes' for video 'no' for audio only")

    change_while_dlading()
    yt = YouTube(link_var.get())

    # yt.streams there is a feature to choose quality, but for now following will do fine
    if ask:
        video = yt.streams.get_highest_resolution()
        # 720p
        video.download(address)
    else:
        video = yt.streams.get_audio_only()
        out_file = video.download(output_path=address)
        # highest audio quality is chosen
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    complete_func()
    change_after_dlading()
    link_var.set("")


def change_while_dlading():
    sub_btn.config(text='WAIT PLEASE!')
    address_label.config(text='DONT TOUCH ANYTHING WHILE FILE IS BEING DOWNLOADED!')
    link_label.config(text='DOWNLOAD STARTED')


def change_after_dlading():
    sub_btn.config(text='Download')
    address_label.config(text='Choose where to download')
    link_label.config(text='Put Youtube link here ->')


# info that download completed
def complete_func():
    messagebox.showinfo("Done", "Download completed")


# # download started
# def progress_func():
# could figure out how to make this work)

# to get address
def get_address():
    global address
    address = fd.askdirectory()


def threading():
    t1 = Thread(target=submit)
    t1.start()


root = tk.Tk()

# setting the windows size
root.geometry("600x400")

root.title("YouTubeSucker(mp3/mp4)")

# declaring string variable
# for storing name and password
link_var = tk.StringVar()
address_var = tk.StringVar()
address = ""

# creating a label for
# link using widget Label
link_label = tk.Label(root, text='Put Youtube link here ->', font=('calibre', 10, 'bold'))

# creating an entry for input
# link using widget Entry
link_entry = tk.Entry(root, textvariable=link_var, font=('calibre', 10, 'normal'))

# creating a label for address
address_label = tk.Button(root, text='Choose where to download', font=('calibre', 10, 'bold'), command=get_address)

# creating an entry for address
# address_entry = tk.Entry(root, textvariable=address_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Download', command=threading)

# placing the label and entry in
# the required position using grid
# method
link_label.grid(row=0, column=0)
link_entry.grid(row=0, column=1)
address_label.grid(row=1, column=0)
# address_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
