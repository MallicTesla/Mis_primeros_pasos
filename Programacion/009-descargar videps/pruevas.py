from pytube import YouTube

def descarga (link):
    lista = YouTube (link)

    comparar = lista.streams.get_highest_resolution()




link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"



