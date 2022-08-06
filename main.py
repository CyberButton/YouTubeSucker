# importing the module
from pytube import YouTube
from pytube.cli import on_progress

urlLink = input("please enter Youtube link: ")
placeToSave = input("where to store the video: ")


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


yt = YouTube(urlLink, on_progress_callback=on_progress)

# yt.streams there is a feature to choose quality, but for now following will do fine
video = yt.streams.get_highest_resolution()

video.download(placeToSave)