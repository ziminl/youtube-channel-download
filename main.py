


import yt_dlp
import os

def download_youtube_shorts(channel_url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    yt_dlp_options = {
        'format': 'best',
        'outtmpl': os.path.join(output_dir, 'TradingLabOfficial', 'shorts', '%(playlist)s', '%(upload_date)s_%(title)s.%(ext)s'),
        'max_duration': 60,
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'quiet': False,
        'verbose': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'cookiefile': 'path/to/your/cookies.txt',  
        'ratelimit': '500K',  
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate'
        }
    }
    with yt_dlp.YoutubeDL(yt_dlp_options) as ydl:
        shorts_url = f"{channel_url}/shorts"
        ydl.download([shorts_url])

if __name__ == "__main__":
    channel_url = input("Paste YouTube channel link: ").strip()
    output_dir = r'C:\dir' ##C:\Users\noway\OneDrive\사진\test
    download_youtube_shorts(channel_url, output_dir)
