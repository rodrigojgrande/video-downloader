from pytube import YouTube

def download_youtube_video(url, save_path="."):
    try:
        # Cria um objeto YouTube
        yt = YouTube(url)
        
        # Exibe informações do vídeo
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Views: {yt.views}")
        print(f"Duration: {yt.length} seconds")
        
        # Seleciona o stream de maior resolução
        video_stream = yt.streams.get_highest_resolution()
        
        # Baixa o vídeo
        print("Downloading...")
        video_stream.download(output_path=save_path)
        print(f"Download complete! Video saved at {save_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Insira o URL do vídeo e o caminho de destino
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    destination_path = input("Enter the destination folder (leave blank for current directory): ") or "."
    download_youtube_video(video_url, destination_path)
