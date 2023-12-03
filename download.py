import threading
from pytube import YouTube
from win10toast import ToastNotifier


def show_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=1)


def download_video(url, selected_quality, folder_path):
    try:
        print("Скачивание видео началось в отдельном потоке")
        print(f"Выбранное качество: {selected_quality}")

        youtube = YouTube(url)

        video_streams = youtube.streams.filter(progressive=True, resolution=selected_quality)

        if video_streams:
            video_stream = video_streams[0]
            video_duration = youtube.length
            video_size = video_stream.filesize
            video_size_mb = round(video_size / (1024 * 1024))
            print(video_size_mb, video_duration)
            video_stream.download(output_path=folder_path)
            show_notification("Скачивание завершено", "Ваше видео успешно скачано, приятного просмотра")
            print("Скачивание завершено")
        else:
            show_notification("Скачивание не удалось", "Данное разрешение не поддерживанься на этом видео")
            print(f"Видео с выбранным качеством '{selected_quality}' недоступно.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


def main(url, hd, folder_path):

    thread = threading.Thread(target=download_video, args=(url, hd, folder_path))
    thread.start()

    for i in range(10):
        print(i)
