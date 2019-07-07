from django.shortcuts import render

posts = [
    {
        'author':'Viks',
        'title':'post 1',
        'content':'content 1',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'James Bond',
        'title':'post 2',
        'content':'content 2',
        'date_posted':'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})