from pytube import YouTube

def descarga (link):
    lista = YouTube (link)

    video_completo = lista.streams.get_highest_resolution()

    videos = lista.streams.order_by("resolution").desc().filter (type = "video")
    audios = lista.streams.order_by("abr").desc().filter(type = "audio")

    for video in videos :
        print ("todos ",video)
    print ()
    print (video_completo)

    print (video_completo.resolution)

    video = videos[0]

    if video_completo.resolution is video.resolution:
        print ("si")
    else:
        print ("NO")





# link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
link = "https://www.youtube.com/watch?v=GVkiFP71n_c&ab_channel=LaMomiadelHugo"

descarga (link)

