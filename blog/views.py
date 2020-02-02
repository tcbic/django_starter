from django.shortcuts import render

posts = [
    {
        'author': 'Taylor',
        'title': 'Blog Post 1',
        'content': 'Post 1 content...',
        'date_posted': 'February 1, 2020'
    },
    {
        'author': 'Lauren',
        'title': 'Blog Post 2',
        'content': 'Post 2 content...',
        'date_posted': 'February 2, 2020'
    }
]


# This is where the logic goes for how we want to handle
# certain routes.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})