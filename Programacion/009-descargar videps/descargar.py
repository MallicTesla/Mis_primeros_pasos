from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

def descarga (link, quiero, ruta_video, ruta_audio, final):
    lista = YouTube (link)
    # directo = lista.streams.get_highest_resolution()
    # print ("mas resolusion ", directo)

    # es_este = lista.streams.filter(res=quiero, mime_type="video/webm").order_by("resolution").desc().first()
    # print ("resolusion quiero ", es_este)

    videos = lista.streams.order_by("resolution").desc().filter (type = "video")
    audios = lista.streams.order_by("abr").desc().filter(type = "audio")

    # for video in videos :
    #     print ("todas ",video)
    #     # if quiero in str (video):
    #     #     print ("print2",video)

    # print ()

    # for audio in audios :
    #     print ("audios", audio)

    # print()

    video = videos[0]
    audio = audios[0]

    print (f"primer video {video}")
    print (f"primer audio {audio}")

    try:
        video.download (ruta_video)
        audio.download (ruta_audio)

        print ("descarga completa")

        try:
            print ("0")
            video = VideoFileClip (f"{ruta_video}/{video.default_filename}")
            print ("1")
            audio = AudioFileClip (f"{ruta_audio}/{audio.default_filename}")

            print ("2")
            fusion = video.set_audio (audio)
            print ("3")

            # titulo = str (lista.title)
            # print (f"({titulo})")
            fusion.write_videofile (f"{final}\\final", codec="libx264", audio_codec="aac")

        except Exception as e:
            print ("Fallo la fusion", str(e))
    except:
        print ("fallo descarga")
    print (f"Proseso terminado")


link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog"
quiero = "1080p"

ruta_video = "C:\\Users\\Mallic\\Downloads\\YouTube\\video"
ruta_audio = "C:\\Users\\Mallic\\Downloads\\YouTube\\audio"
final = "C:\\Users\\Mallic\\Downloads\\YouTube\\pronto"

descarga (link, quiero, ruta_video, ruta_audio, final)