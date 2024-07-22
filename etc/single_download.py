import yt_dlp

def download_1080p_mp4(url, output_path='.'):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',   #MP4 see docs for more
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video
            ydl.download([url])
            print(f'Download completed! The video is saved to {output_path}')
    
    except Exception as e:
        print(f'An error occurred: {e}')

# Example usage
if __name__ == "__main__":
    video_url = '<yt link>' ##https://youtu.be/WaZHX6RhGLs?si=fdPAT9UoT5PjwVv1
    download_1080p_mp4(video_url)
