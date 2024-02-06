from django.shortcuts import render, redirect

from personal_blog.forms import AuthorForm
from personal_blog.models import Author
from django.views.generic import View


def author_create_view(request):
    if request.method == 'GET':
        form = AuthorForm()
        return render(request, 'authors/create.html', context={'form': form})
    elif request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            author = Author.objects.create(name=request.POST.get('name'))
            return redirect('author_list')
        else:
            return render(request, 'authors/create.html', context={'form': form})


def author_list_view(request):
    return render(request, 'authors/list.html', context={'authors': Author.objects.all()})


class AuthorView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.get(request, *args, **kwargs)
        elif request.method == 'POST':
            return self.post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = AuthorForm()
        return render(request, 'authors/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)

        if form.is_valid():
            author = Author.objects.create(name=request.POST.get('name'))
            return redirect('author_list')
        else:
            return render(request, 'authors/create.html', context={'form': form})
