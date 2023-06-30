from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo, Publicasion

#   para relasionar ovjetos entre si primero se deve de crear los objetos y despues se relasionan
def crear(request):
    art1 = Articulo(linia="Articulo 1")
    art1.save()
    art2 = Articulo(linia="Articulo 2")
    art2.save()
    art3 = Articulo(linia="Articulo 3")
    art3.save()
    art4 = Articulo(linia="Articulo 4")
    art4.save()

    pub1 = Publicasion(titulo="Publicasion 1")
    pub1.save()
    pub2 = Publicasion(titulo="Publicasion 2")
    pub2.save()
    pub3 = Publicasion(titulo="Publicasion 3")
    pub3.save()
    pub4 = Publicasion(titulo="Publicasion 4")
    pub4.save()
    pub5 = Publicasion(titulo="Publicasion 5")
    pub5.save()
    pub6 = Publicasion(titulo="Publicasion 6")
    pub6.save()
    pub7 = Publicasion(titulo="Publicasion 7")
    pub7.save()
    pub8 = Publicasion(titulo="Publicasion 8")
    pub8.save()
    pub9 = Publicasion(titulo="Publicasion 9")
    pub9.save()
    pub10 = Publicasion(titulo="Publicasion 10")
    pub10.save()

#   se crea o añade una relasion colocando la variavle punto el campo punto add (la otra variavle)
    art1.publicasiones.add(pub1)
    art1.publicasiones.add(pub2)
    art1.publicasiones.add(pub3)
    art2.publicasiones.add(pub4)
    art2.publicasiones.add(pub5)
    art3.publicasiones.add(pub6)
    art3.publicasiones.add(pub7)
    art4.publicasiones.add(pub8)
    art4.publicasiones.add(pub9)
    art4.publicasiones.add(pub10)

    # # asi se borra una relacionamiento
    # art1.publicasiones.remove (pub1)

    #   asi se hace la busqueda de un campo y sus relasiones
    # resultado = art1.publicasiones.all ()

    #   asi se realisa la consulta alreves
    pub1 = Publicasion.objects.get (id = 1)
    resultado = pub1.articulo_set.all ()

    return HttpResponse (resultado)