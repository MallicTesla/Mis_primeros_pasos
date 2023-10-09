from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

def lista (link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida):
    lista = YouTube (link)

    titulo = lista.title

    video_completo = lista.streams.get_highest_resolution()
    print (video_completo)

    videos = lista.streams.order_by("resolution").desc().filter (type = "video")
    audios = lista.streams.order_by("abr").desc().filter (type = "audio")

    videos_quiero = videos.filter (resolution = quiero)

    # for video in videos :
    #     print ("todas ",video)
    # print ()
    # for audio in audios :
    #     print ("audios", audio)

    video = videos[0]
    audio = audios[0]

    # print (titulo)
    # print (f"video quiero {videos_quiero}")
    # print (f"video_completo.resolution {video_completo.resolution}")
    # print (f"primer video {video}")
    # print (f"primer audio {audio}")

    descarga (video_completo, videos_quiero, video, audio, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, titulo)


def descarga (video_completo, videos_quiero, video, audio, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida, titulo):
    if descarga_rapida or video_completo.resolution is video.resolution or video_completo.resolution is videos_quiero[0].resolution:
        print ("descarga rapida", {video_completo})
        try:
        #     # video_completo.download(final, filename = 'prueva')
            video_completo.download(final)

            print ("descarga completa")
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

            fusionar (video, audio, ruta_video, ruta_audio, final, titulo)

        except:
            print ("fallo descarga")


def fusionar (video, audio, ruta_video, ruta_audio, final, titulo):
    try:
        video = VideoFileClip (f"{ruta_video}/{video.default_filename}")
        audio = AudioFileClip (f"{ruta_audio}/{audio.default_filename}")

        fusion = video.set_audio (audio)

        fusion.write_videofile (f"{final}\\{titulo}.mp4", codec="libx264", audio_codec="aac")

    except Exception as e:
        print ("Fallo la fusion", str(e))

    print (f"Proseso terminado")



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
# descargar_audio (link_audio, ruta_audio)

# --------------------------------------------------------------------------------------------------------
# DESCARGAR VIDEOS

# link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog" #1080
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley" #1080
# link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo" #720
# link = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro" # 2160

lo_mejor = False
quiero = "1080p"

descarga_rapida = False

# descomenta esto para descargar videos y comenta el de DESCARGAR AUDIO
lista (link, quiero, ruta_video, ruta_audio, final, lo_mejor, descarga_rapida)


# --------------------------------------------------------------------------------------------------------
# DESCARGAR VIDEOS DE LISTA DE REPRODUCCION

link_lista = "sda"
# --------------------------------------------------------------------------------------------------------






