from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

def descarga (link, quiero, ruta_video, ruta_audio, final):
    lista = YouTube (link)
    directo = lista.streams.get_highest_resolution()
    print ("mas resolusion ", directo)

    es_este = lista.streams.filter(res=quiero, mime_type="video/webm").order_by("resolution").desc().first()
    print ("resolusion quiero ", es_este)

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

    video_descargado = videos[0]
    audio_descargado = audios[0]


    print (f"primer video {video_descargado}")
    print (f"primer audio {audio_descargado}")


    try:
        print ("descargo ",es_este)
        video_descargado.download (ruta_video)
        audio_descargado.download (ruta_audio)

        print ("descarga completa")

        try:
            print ("0")
            video = VideoFileClip (f"{ruta_video}/{video_descargado.default_filename}")
            print ("1")
            audio = AudioFileClip (f"{ruta_audio}/{audio_descargado.default_filename}")

            print ("2")
            fusion = video.set_audio (audio)
            print ("3")
            # video_with_audio.write_videofile(f"{ruta_descarga}/{yt.title}_final.mp4", codec="libx264")
            fusion.write_videofile (f"{final}/{lista.title}_final.mp4", codec="libx264", audio_codec="aac")
        except Exception as e:
            print ("Fallo la fusion", str(e))
    except:
        print ("fallo descarga")

    print ("pronto")


link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog"
quiero = "1080p"

ruta_video = "C:\\Users\\Mallic\\Downloads\\YouTube\\video"
ruta_audio = "C:\\Users\\Mallic\\Downloads\\YouTube\\audio"
final = "C:\\Users\\Mallic\\Downloads\\YouTube\\pronto"

descarga (link, quiero, ruta_video, ruta_audio, final)