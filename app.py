from pytube import YouTube

def video_info(video_url):
    yt = YouTube(video_url)

    title = yt.title
    channel = yt.author
    views = yt.views
    date = yt.publish_date

    return(f"Title: {title} \n\nChannel name: {channel} \n\nViews: {views} \n\nPublished on: {date}")

def audio_dl(video_url):
    audio_file = YouTube(video_url)

    audio_file.streams.filter(only_audio=True)
    audio_to_send = audio_file.streams.get_by_itag(140)
    audio_to_send.download()


def title_finder(video_url):
    vid = YouTube(video_url)

    title_of_video = vid.title
    return(title_of_video)




#audio_dl("https://youtu.be/dU8ZSWck7KQ")