import yt_dlp

def baixar_video(url, caminho_salvar='./'):
    try:
        ydl_opts = {
            'outtmpl': f'{caminho_salvar}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print('✅ Download concluído com sucesso!')
    except Exception as e:
        print(f'\n❌ Ocorreu um erro: {e}')

if __name__ == '__main__':
    url = input('Cole a URL do vídeo do YouTube: ').strip()
    caminho = input('Digite o caminho para salvar (pressione Enter para salvar na pasta atual): ').strip() or './'
    baixar_video(url, caminho)