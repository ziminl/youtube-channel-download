


import os
import yt_dlp as youtube_dl

def download_channel_videos(channel_url, output_path, max_duration=None):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_path, '%(playlist)s', '%(upload_date)s_%(title)s.%(ext)s'),
        'max_duration': max_duration,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

def main():

    ytlink = input()

    parts = ytlink.split("@")
    if len(parts) > 1:
        username = parts[1]
        print(username)
    else:
        print("error")

    channel_url = r'https://www.youtube.com/c/' + username        # https://www.youtube.com/c/name
    #print(channel_url)

    main_path = "C:\\Users\\noway\\OneDrive\\사진\\test" # C:\\
    output_path = main_path +"\\" +  username      
    out_gen = os.path.join(main_path, username)

    if not os.path.exists(out_gen):
        os.makedirs(out_gen)

    shorts_path = os.path.join(output_path, "shorts")

    if not os.path.exists(shorts_path):
        os.makedirs(shorts_path)
    
    playlists_path = os.path.join(output_path, "playlists")

    if not os.path.exists(playlists_path):
        os.makedirs(playlists_path)

    # ytshorts(videos that are 60 seconds or less)
    download_channel_videos(channel_url + "/shorts", shorts_path, max_duration=60)

    download_channel_videos(channel_url + "/playlists", playlists_path)

    video_path = os.path.join(output_path, "video")
    if not os.path.exists(video_path):
        os.makedirs(video_path)
    download_channel_videos(channel_url + "/videos", video_path)

if __name__ == "__main__":
    main()


