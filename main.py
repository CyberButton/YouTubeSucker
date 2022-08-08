# importing the module

import tkinter as tk

from pytube import YouTube
from pytube.cli import on_progress

# urlLink = input("please enter Youtube link: ")
# placeToSave = input("where to store the video: ")


# def progress_callback(stream, data_chunk, left_bytes):
#     size = stream.filesize
#     p = 0
#     while p <= 100:
#         progress = p
#         print(str(p) + '%')
#         p = percent(left_bytes, size)
#
#
# def percent(tem, total):
#     perc = (float(tem) / float(total)) * float(100)
#     return perc


root = tk.Tk()

# setting the windows size
root.geometry("600x400")

root.title("YouTubeSucker(mp3/mp4)")

# declaring string variable
# for storing name and password
link_var = tk.StringVar()
address_var = tk.StringVar()


# defining a function that will
# get the link and address and
# print them on the screen
def submit():
    # name = link_var.get()
    # password = address_var.get()
    #
    # print("The name is : " + name)
    # print("The password is : " + password)
    #
    # link_var.set("")
    # address_var.set("")

    yt = YouTube(link_var.get(), on_progress_callback=on_progress)

    # yt.streams there is a feature to choose quality, but for now following will do fine
    video = yt.streams.get_highest_resolution()

    video.download(address_var.get())


 # creating a label for
# link using widget Label
link_label = tk.Label(root, text='Put Youtube link here ->', font=('calibre', 10, 'bold'))

# creating an entry for input
# link using widget Entry
link_entry = tk.Entry(root, textvariable=link_var, font=('calibre', 10, 'normal'))

# creating a label for address
address_label = tk.Label(root, text='Where to download ->', font=('calibre', 10, 'bold'))

# creating an entry for address
address_entry = tk.Entry(root, textvariable=address_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
link_label.grid(row=0, column=0)
link_entry.grid(row=0, column=1)
address_label.grid(row=1, column=0)
address_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
