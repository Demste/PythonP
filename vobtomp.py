import moviepy.editor
from tkinter.filedialog import askopenfilenames, askdirectory, asksaveasfilename
import os

# Kullanıcıya birden çok video dosyası seçtir
video_files = askopenfilenames(filetypes=[("Video files", "*.mp4;*.avi;*.vob;*.mkv")])

# Kaydedilecek konumu bir kere seç, ardından tüm dosyaları o konuma kaydet
save_directory = askdirectory()
if save_directory:  # Eğer kullanıcı iptal etmezse
    for vid_path in video_files:
        # Seçilen dosyayı VideoFileClip nesnesine çevir
        video = moviepy.editor.VideoFileClip(vid_path)

        # Ses dosyasını oluştur
        audio = video.audio

        # Video dosyasının adını al ve uzantısını kaldır
        video_filename = os.path.splitext(os.path.basename(vid_path))[0]

        # Kaydedilecek konumu ve dosya adını birleştir
        save_path = os.path.join(save_directory, f"{video_filename}.mp3")

        # Ses dosyasını belirtilen konuma kaydet
        audio.write_audiofile(save_path)

        print(f"Ses dosyası {save_path} konumuna kaydedildi.")
else:
    print("Kayıt konumu seçilmedi. İşlem iptal edildi.")
