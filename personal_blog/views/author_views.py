from django.shortcuts import render, redirect

from personal_blog.forms import AuthorForm
from personal_blog.models import Author


def author_create_view(request):
    if request.method == 'GET':
        form = AuthorForm()
        return render(request, 'authors/create.html', context={'form':form})
    elif request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            author = Author.objects.create(name = request.POST.get('name'))
            return redirect('author_list')
        else:
            return render(request, 'authors/create.html', context={'form':form})


def author_list_view(request):
    return render(request, 'authors/list.html', context={'authors':Author.objects.all()})