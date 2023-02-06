from pytube import YouTube

#Getting video details

def video_info(video_url):
    yt = YouTube(video_url)
    title = yt.title
    views = yt.views
    return(f"Title: {title}\n\nViews: {views}")

# audio requests
def audio_dl(video_url):
    audio_file = YouTube(video_url)

    audio_file.streams.filter(only_audio=True)
    audio_to_send = audio_file.streams.get_by_itag(140)
    song = audio_to_send.download()
    return(song)

# video in 360p
def video_dl_360(video_url):
    video_file = YouTube(video_url)

    video_file_to_send = video_file.streams.get_by_itag(18)
    video_360 = video_file_to_send.download()
    return(video_360)


# video in 720p
def video_dl_720(video_url):
    video_file = YouTube(video_url)

    video_file_to_send = video_file.streams.get_by_itag(22)
    video_720 = video_file_to_send.download()
    return(video_720)

# video in 1080p
def video_dl_1080(video_url):
    video_file = YouTube(video_url)

    video_file_to_send = video_file.streams.get_by_itag(137)
    video_1080 = video_file_to_send.download()
    return(video_1080)

def title_finder(video_url):
    vid = YouTube(video_url)

    title_of_video = vid.title
    return(title_of_video)

# replace "|" and "," from the title without this function everything crashes ;_;
def replace_characters(string):
    string = string.replace("|", "")
    string = string.replace(",", "")
    return string
