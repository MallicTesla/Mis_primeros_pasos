from pytube import YouTube

def descarga (link, quiero=""):
    lista = YouTube (link)

    video_completo = lista.streams.get_highest_resolution()

    videos = lista.streams.order_by("resolution").desc().filter (type = "video")
    audios = lista.streams.order_by("abr").desc().filter (type = "audio")

    video_quiero = videos.filter (resolution = quiero)

    # for video in videos :
    #     print ("todos ",video)

    print()

    # for audio in audios :
    #     print (f"audios",audio)

    # print()

    # for video in videos :
    #     if video.resolution == quiero:
    #         print ("todos ",video)

    for videos_quiero in video_quiero:
        print (videos_quiero)

    print ()
    print ("video_completo",video_quiero)

    print (video_completo.resolution)

    video = videos[0]

    if video_completo.resolution is video.resolution:
        print ("si")
    else:
        print ("NO")

    if quiero != "" :
        print ("tiene algo",quiero)
    else:
        print ("esta vacio")




# link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog"
# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
# link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo"
link = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro"

quiero = ""

descarga (link, quiero)

