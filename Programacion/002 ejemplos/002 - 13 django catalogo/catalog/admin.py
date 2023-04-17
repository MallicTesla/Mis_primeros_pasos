from django.contrib import admin
#   registra tus modelos aca

#   se importan todos los modelos (clases) que se crearon dentro del archibo models
from .models import Author, Genre, Book, BookInstance
#   tambien se puede hacer asi para importar todos los modelos
# from .models import *

#   despues se registran todos los modelos en el panel de administrasion


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)
