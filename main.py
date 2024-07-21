import os
import yt_dlp

def download_channel_videos(channel_url, output_path, max_duration=None):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_path, '%(upload_date)s_%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'quiet': False,
        'verbose': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'ratelimit': 500 * 1024,  # Setting rate limit as an integer in bytes
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate'
        },
        'compat_opts': set()
    }

    if max_duration:
        ydl_opts['max_duration'] = max_duration

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

def main():
    print("Paste YouTube channel link:")
    ytlink = input().strip()

    parts = ytlink.split("@")
    if len(parts) > 1:
        username = parts[1]
    else:
        print("Error: Invalid YouTube channel link format.")
        return

    channel_url = f'https://www.youtube.com/@{username}'

    main_path = "C:\\Users\\noway\\OneDrive\\사진\\test"
    output_path = os.path.join(main_path, username)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    shorts_path = os.path.join(output_path, "shorts")
    playlists_path = os.path.join(output_path, "playlists")
    video_path = os.path.join(output_path, "video")

    for path in [shorts_path, playlists_path, video_path]:
        if not os.path.exists(path):
            os.makedirs(path)
    download_channel_videos(channel_url + "/shorts", shorts_path, max_duration=60)
    download_channel_videos(channel_url + "/playlists", playlists_path)
    download_channel_videos(channel_url + "/videos", video_path)

if __name__ == "__main__":
    main()
