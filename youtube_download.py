from pytube import YouTube
link = input("Enter URL video: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
