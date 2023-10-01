from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

def descarga (link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida):
    lista = YouTube (link)

    video_completo = lista.streams.get_highest_resolution()

    videos = lista.streams.order_by("resolution").desc().filter (type = "video")
    audios = lista.streams.order_by("abr").desc().filter(type = "audio")

    videos_quiero = videos.filter (resolution = quiero)

    # for video in videos :
    #     print ("todas ",video)
    # print ()
    # for audio in audios :
    #     print ("audios", audio)

    print()

    # video_quiero = videos_quiero [0]
    video = videos[0]
    audio = audios[0]

    # print (f"video quiero {video_quiero}")
    # print (f"video_completo.resolution {video_completo.resolution}")
    # print (f"primer video {video}")
    # print (f"primer audio {audio}")

    if descarga_rapida or video_completo.resolution is video.resolution:
        print ("video_completo")
        try:
        #     # video_completo.download(final, filename = 'prueva')
            video_completo.download(final)

        except:
            print ("fallo descarga")

    else:
        if lo_mejor and quiero == "":
            print (f"lo mejor {video}")
        else:
            video = videos_quiero [0]
            print (f"quiero {video}")

        try:
            video.download (ruta_video)
            audio.download (ruta_audio)

            print ("descarga completa")

            try:
                video = VideoFileClip (f"{ruta_video}/{video.default_filename}")
                audio = AudioFileClip (f"{ruta_audio}/{audio.default_filename}")

                fusion = video.set_audio (audio)

                fusion.write_videofile (f"{final}\\final.mp4", codec="libx264", audio_codec="aac")

            except Exception as e:
                print ("Fallo la fusion", str(e))
        except:
            print ("fallo descarga")
        print (f"Proseso terminado")
    print ("Descarga completa")

def descargar_audio (link_audio, ruta_audio):
    lista = YouTube (link_audio)
    audios = lista.streams.order_by("abr").desc().filter(type = "audio")

    for audio in audios :
        print (f"audio {audio}")

    audio = audios[0]

    audio.download (ruta_audio)



# --------------------------------------------------------------------------------------------------------
# RUTAS DE DESTINO

ruta_video = "C:\\Users\\Mallic\\Downloads\\YouTube\\video"
ruta_audio = "C:\\Users\\Mallic\\Downloads\\YouTube\\audio"
final = "C:\\Users\\Mallic\\Downloads\\YouTube\\pronto"

# --------------------------------------------------------------------------------------------------------
# DESCARGAR AUDIO

# link_audio = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro"
link_audio = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo"

# descomenta esto para descargar audio y comenta el de DESCARGAR VIDEOS
descargar_audio (link_audio, ruta_audio)

# --------------------------------------------------------------------------------------------------------
# DESCARGAR VIDEOS

# link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog" #1080
# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley" #1080
link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo" #720
# link = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro" # 2160

lo_mejor = True
quiero = ""

descarga_rapida = lo_mejor is False and quiero == ""

# descomenta esto para descargar videos y comenta el de DESCARGAR AUDIO
# descarga (link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida)


# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------





