from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)



class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategori','date')

admin.site.register(Artikel, ArtikelAdmin)


class AlquranAdmin(admin.ModelAdmin):
    list_display = ('arti','asma','audio','ayat','keterangan','nama','nomor','rukuk','type','urut')

admin.site.register(Alquran, AlquranAdmin)

class DoaAdmin(admin.ModelAdmin):
    list_display = ('id','doa','ayat','latin','artinya')

admin.site.register(Doa, DoaAdmin)

