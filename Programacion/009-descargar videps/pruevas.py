from pytube import YouTube, Playlist

def descarga (link_lista, quiero=""):
    playlist = Playlist (link_lista)
    # lista = YouTube (link)

    print ("1")
    # print (playlist)
    for lista in playlist.video_urls:
        print ("1.1")

        lista = YouTube (lista)
        print ("2")
        # video_completo = lista.streams.get_highest_resolution()

        videos = lista.streams.order_by("resolution").desc().filter (type = "video")
        # audios = lista.streams.order_by("abr").desc().filter (type = "audio")

        print ("3")
        print (videos)
        print ("4")
    # video_quiero = videos.filter (resolution = quiero)

        # # for video in videos :
        # #     print ("todos ",video)

    # print()

    # # for audio in audios :
    # #     print (f"audios",audio)

    # # print()

    # # for video in videos :
    # #     if video.resolution == quiero:
    # #         print ("todos ",video)

    # for videos_quiero in video_quiero:
    #     print (videos_quiero)

    # print ()
    # print ("video_completo",video_quiero)

    # print (video_completo.resolution)

    # video = videos[0]

    # if video_completo.resolution is video.resolution:
    #     print ("si")
    # else:
    #     print ("NO")

    # if quiero != "" :
    #     print ("tiene algo",quiero)
    # else:
    #     print ("esta vacio")




# link = "https://www.youtube.com/watch?v=8-bSHuiTSoM&ab_channel=DateunVlog"
# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
# link = "https://www.youtube.com/watch?v=jEugr6x2_qc&ab_channel=Bizarro"

# link = "https://www.youtube.com/watch?v=azgZ1frntYE&ab_channel=Bizarro"
# link_lista = "https://www.youtube.com/playlist?list=PL4vlU3dGym0bgQtk-MKvLFoouWHC9g7R6"
link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo"

quiero = ""

descarga (link, quiero)

