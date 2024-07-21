import yt_dlp

def download_youtube_shorts(channel_url, username):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'C:\\Users\\noway\\OneDrive\\사진\\test\\{username}\\%(upload_date)s_%(title)s.%(ext)s',
        'max_duration': 60,
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'quiet': False,
        'verbose': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        # Remove the 'cookiefile' line if you don't have a cookies.txt file
        # 'cookiefile': 'path/to/your/cookies.txt',
        'ratelimit': 500 * 1024,  # Setting rate limit as an integer in bytes
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate'
        },
        'compat_opts': set()
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

if __name__ == "__main__":
    channel_url = input("Paste YouTube channel link: ")
    username = input("Enter the username: ")
    download_youtube_shorts(channel_url, username)
 
