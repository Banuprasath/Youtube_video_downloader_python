# You can use this app in command line also for using this is in command line just remove the comments and run in command line you can also see the video title as well as thumbnail

"""

from pytube import YouTube
url = input("Enter the Url:")
SAVE_PATH = input("Enter the location as text like (D:/youtube): ")
my_video = YouTube(url)

print("*********************Video Title************************")
#get Video Title
print(my_video.title)

print("********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)

print("********************Download video*************************")
#get all the stream resolution for the
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

my_video.download(SAVE_PATH)
"""



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube


# Function to handle the download button click
def download_video():
    url = url_entry.get()
    save_path = save_path_entry.get()

    try:
        my_video = YouTube(url)
        stream = my_video.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create the main application window
app = tk.Tk()
app.title("YouTube Video Downloader")

# Set the window size
app.geometry("600x400")

# Create and place widgets
url_label = ttk.Label(app, text="Enter the URL:")
url_label.pack()

url_entry = ttk.Entry(app, width=70)  # Increase the width of the text box
url_entry.pack()

save_path_label = ttk.Label(app, text="Enter the save path:")
save_path_label.pack()

save_path_entry = ttk.Entry(app, width=70)  # Increase the width of the text box
save_path_entry.pack()

download_button = ttk.Button(app, text="Download Video", command=download_video)
download_button.pack()

app.mainloop()
