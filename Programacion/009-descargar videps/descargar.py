from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

def descarga (link, quiero, ruta_video, ruta_audio, final, lo_mejor, defecto):
    lista = YouTube (link)

    video_completo = lista.streams.get_highest_resolution()

    videos = lista.streams.order_by("resolution").desc().filter (type = "video")
    audios = lista.streams.order_by("abr").desc().filter(type = "audio")

    # for video in videos :
    #     print ("todas ",video)
    # print ()
    # for audio in audios :
    #     print ("audios", audio)

    print()

    video = videos[0]
    audio = audios[0]

    print (f"video_completo.resolution {video_completo.resolution}")
    print (f"primer video {video}")
    # print (f"primer audio {audio}")

    if defecto or video_completo.resolution is video.resolution:
        print ("video_completo")
        # try:
        #     video_completo.download(final)

        # except:
        #     print ("fallo descarga")

    else:
        print ("lo mejor")
        # try:
        #     video.download (ruta_video)
        #     audio.download (ruta_audio)

        #     print ("descarga completa")

        #     try:
        #         print ("1")
        #         video = VideoFileClip (f"{ruta_video}/{video.default_filename}")
        #         print ("2")
        #         audio = AudioFileClip (f"{ruta_audio}/{audio.default_filename}")
        #         print ("3")

        #         fusion = video.set_audio (audio)

        #         # titulo = str (lista.title)
        #         # print (f"({titulo})")
        #         print ("4")
        #         fusion.write_videofile (f"{final}\\final.mp4", codec="libx264", audio_codec="aac")
        #         print ("5")

        #     except Exception as e:
        #         print ("Fallo la fusion", str(e))
        # except:
        #     print ("fallo descarga")
        # print (f"Proseso terminado")





# link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog"
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
# link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo"

lo_mejor = True
defecto = False
quiero = "1080p"

ruta_video = "C:\\Users\\Mallic\\Downloads\\YouTube\\video"
ruta_audio = "C:\\Users\\Mallic\\Downloads\\YouTube\\audio"
final = "C:\\Users\\Mallic\\Downloads\\YouTube\\pronto"

descarga (link, quiero, ruta_video, ruta_audio, final, lo_mejor, defecto)