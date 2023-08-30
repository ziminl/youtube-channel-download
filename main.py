


import os
import yt_dlp as youtube_dl

def download_channel_videos(channel_url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

def main():



    channel_url = 'channel url'  #https://www.youtube.com/c/name
    output_path = 'dir'




    shorts_path = os.path.join(output_path, "shorts")
    playlist_path = os.path.join(output_path, "playlist")
    video_path = os.path.join(output_path, "video")

    if not os.path.exists(shorts_path):
        os.makedirs(shorts_path)
    if not os.path.exists(playlist_path):
        os.makedirs(playlist_path)
    if not os.path.exists(video_path):
        os.makedirs(video_path)

    download_channel_videos(channel_url, shorts_path)
    download_channel_videos(channel_url + "/playlists", playlist_path)
    download_channel_videos(channel_url + "/videos", video_path)

if __name__ == "__main__":
    main()


