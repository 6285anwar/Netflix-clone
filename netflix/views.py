from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('admin_home')

        elif user_registration.objects.filter(username=request.POST['email'], password=request.POST['password']).exists():
            users = user_registration.objects.get(
                username=request.POST['email'], password=request.POST['password'])
            request.session['u_id'] = users
            request.session['username'] = users.username
            request.session['u_id'] = users.id
            users = user_registration.objects.filter(id=users.id)
            return render(request, 'user_index.html', {'users': users})
    return render(request, 'login.html')

# ADMIN =====================

def admin_logout(request):
    if 'Adm_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def admin_index(request):
    return render(request, 'admin_index.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_users(request):
    user = user_registration.objects.all()
    return render(request, 'admin_users.html',{'user': user})

def admin_adduser(request):
    if request.method == 'POST':
        a=user_registration()
        a.name = request.POST['n']
        a.username = request.POST['un']
        a.password = request.POST['p']
        a.photo = request.FILES['f']
        a.save()

        return redirect('admin_users')
   
    return render(request, 'admin_adduser.html')

def admin_movie(request):
    movie=movies.objects.all()
    return render(request, 'admin_movie.html',{'movie': movie})

def admin_addmovie(request):
    user = user_registration.objects.all()

    if request.method == 'POST':
        m=movies()
        m.moviename = request.POST['mn']
        m.movieurl = request.POST['mtu']
        m.movieposter = request.FILES['mp']
        su = request.POST['u']
        use=user_registration.objects.get(id=su)
        m.username=(use)  
        m.save()

        return redirect('admin_movie')
    return render(request, 'admin_addmovie.html',{'user': user})

def admin_viewuser(request,id):
    user=user_registration.objects.get(id=id)
    movie=movies.objects.filter(username_id=user)
    return render(request, 'admin_viewuser.html',{'user': user,'movie':movie})



#USER ===================

def user_logout(request):
    if 'u_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def user_index(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']

    users = user_registration.objects.filter(id=u_id)
    return render(request, 'user_index.html', {'users': users})

def user_home(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']

    users = user_registration.objects.filter(id=u_id)
    movie = movies.objects.filter(username_id=u_id)
    return render(request, 'user_home.html', {'users': users,'movie':movie})