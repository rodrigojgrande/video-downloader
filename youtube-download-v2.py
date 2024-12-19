import yt_dlp

def download_youtube_video(url, save_path="."):
    try:
        ydl_opts = {
            'outtmpl': f"{save_path}/%(title)s.%(ext)s",
            'format': 'bestvideo+bestaudio/best',  # Baixa a melhor qualidade
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Insira o URL do vídeo e o caminho de destino
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    destination_path = input("Enter the destination folder (leave blank for current directory): ") or "."
    download_youtube_video(video_url, destination_path)
