from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests



def index(request):
    return render(request,"home.html")

def result(request):
    # query= "avenger"
    # url= 'https://imdb-api.com/en/API/SearchMovie/k_pftzqnp0/'+ query
    # print(url)
    return render(request,'result.html')


def movies(request):
    return render(request, "movies.html")

def celebrities(request):
    return render(request, "celebrities.html")

def movie_details(request):
    return render(request, "movie-details.html")

def top_movies(request):
    return render(request, "top-movies.html")

def blog(request):
    return render(request, "blog.html")

def blog_details(request):
    return render(request, "blog-details.html")

def register_user(request):

    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = userInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

            return redirect('home')

        else:
            context = {'user_form.errors': user_form.errors,
                       'user_info_form.errors': user_info_form.errors}
            return render(request, 'user/register.html', context)
    else:

        user_form = userForm()
        user_info_form = userInfoForm()

        context = {'user_form': user_form,
                   'user_info_form': user_info_form}

        return render(request, 'user/register.html', context)


def searchresult(request):
    query= "avenger"
    url= 'https://imdb-api.com/en/API/SearchMovie/k_pftzqnp0/'+ query
    print(url)
    movie_data=requests.get(url).json
    context={'movie_data': movie_data}
    return render(request,'result.html',context)    