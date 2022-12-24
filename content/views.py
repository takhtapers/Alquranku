from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel,Kategori,Alquran,Doa
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

# def is_creator(user):
#     if user.groups.filter(name='Creator').exists():
#         return True
#     else:
#         return False

# @login_required
def dashboard(request):
    # if request.user.groups.filter(name='Creator').exists():
    #     request.session['is_creator'] = 'creator'
    
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    } 
    return render(request, template_name, context)

# @login_required
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    print(artikel)
    context = {
        'title' : 'dashboard',
        'artikel': artikel,
    }
    return render(request, template_name, context)
def alquran(request):
    template_name = "back/tabel_alquran.html"
    alquran = Alquran.objects.all()
    context = {
        'title' : 'dashboard',
        'alquran': alquran,
    }
    return render(request, template_name, context)
def doa(request):
    template_name = "back/tabel_doa.html"
    doa = Doa.objects.all()
    context = {
        'title' : 'dashboard',
        'doa': doa,
    }
    return render(request, template_name, context)



# @login_required
# @user_passes_test(is_creator)
def users(request):
    template_name = "back/table_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'dashboard',
        'list_user' : list_user
    }
    return render(request, template_name, context)

# @login_required
def tambah_surah(request):
    template_name = "back/tambah_surah.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kat = Kategori.objects.get(nama=kategori)
      
        #simpan produk karena ada relasi ke tabel kategori 
        Artikel.objects.create(
            nama = nama,
            judul = judul,
            body = body,
            kategori = kat,
        )
        return redirect (artikel)
    context = {
        'title':'Tambah surah',
        'kategori':kategori,

    }
    return render(request, template_name, context)

# @login_required
def lihat_surah(request, id):
    template_name = "back/lihat_surah.html"
    artikel = Alquran.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

def lihat_doa(request, id):
    template_name = "back/lihat_doa.html"
    doa = Doa.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'doa' :doa,
    }
    return render(request, template_name, context)


# @login_required
def edit_surah(request ,id ):
    template_name = 'back/edit_surah.html'
    a = Alquran.objects.get(id=id)
    if request.method == "POST":
        
        arti = request.POST.get('arti')
        asma = request.POST.get('asma')
        audio = request.POST.get('audio')
        ayat = request.POST.get('ayat')
        keterangan = request.POST.get('keterangan')
        nama = request.POST.get('nama')
        nomor = request.POST.get('nomor')
        rukuk = request.POST.get('rukuk')
        type = request.POST.get('type')
        urut = request.POST.get('urut')
       

        #input Kategori Dulu
        

        #simpan produk karena ada relasi ke tabel kategori 
        a.nama = nama
        a.judul = judul
        a.body = body
        a.kategori = kat
        a.save() 
        return redirect(artikel)
    context = {
        'title':'Edit Artikel',
        'kategori':kategori,
        'artikel' : artikel,

    }
    return render(request, template_name, context)


# @login_required
def delete_surah(request,id):
    Alquran.objects.get(id=id).delete()
    return redirect(alquran)

def delete_doa(request,id):
    Doa.objects.get(id=id).delete()
    return redirect(doa)

def sinkron_alquran(request):
        url = " https://al-quran-8d642.firebaseio.com/data.json?print=pretty"
        data = requests.get(url).json()
        for d in data:
            cek_berita = Alquran.objects.filter(nama=d['nama'])
            if cek_berita:
                print('data sudah ada')
                c = cek_berita.first()
                c.nama=d['nama']
                c.save()
            else: 
                #jika belum ada maka tulis baru kedatabase
                b = Alquran.objects.create(
                    arti = d['arti'],
                    asma = d['asma'],
                    audio = d['audio'],
                    ayat = d['ayat'],
                    keterangan = d['keterangan'],
                    nama = d['nama'],
                    nomor = d['nomor'],
                    rukuk = d['rukuk'],
                    type = d['type'],
                    urut = d['urut'],
                )
        return redirect(alquran)
def sinkron_doa(request):
        url = " https://doa-doa-api-ahmadramadhan.fly.dev/api"
        data = requests.get(url).json()
        for d in data:
            cek_berita = Doa.objects.filter(doa=d['doa'])
            if cek_berita:
                print('data sudah ada')
                c = cek_berita.first()
                c.doa=d['doa']
                c.save()
            else: 
                #jika belum ada maka tulis baru kedatabase
                b = Doa.objects.create(
                    id = d['id'],
                    doa = d['doa'],
                    ayat = d['ayat'],
                    latin = d['latin'],
                    artinya = d['artinya'],
                )
        return redirect(doa)