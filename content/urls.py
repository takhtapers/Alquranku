from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('artikel/', artikel, name='artikel'),
    path('tabel_alquran/', alquran, name='tabel_alquran'),
    path('tabel_doa', doa, name='tabel_doa'),
    path('sinkron_doa', sinkron_doa, name='sinkron_doa'),
    path('sinkron_alquran', sinkron_alquran, name='sinkron_alquran'),
    path('users/',users , name='users'),
    path('artikel/tambah',tambah_surah, name='tambah_surah'),
    path('artikel/lihat/<str:id>',lihat_surah, name='lihat_surah'),
    path('artikel/edit/<str:id>',edit_surah, name='edit_surah'),
    path('artikel/delete/<str:id>',delete_surah, name='delete_surah'),
    path('doa/lihat/<str:id>',lihat_doa, name='lihat_doa'),
    path('doa/delete/<str:id>',delete_doa, name='delete_doa'),
]