# THIS FILE FOR FUNCTION BASED VIEWS FOR POSTS

from django.shortcuts import render, redirect, reverse, get_object_or_404
from personal_blog.models import Post, Author, Comment, Tag
from django.http import HttpResponse, Http404
from personal_blog.forms import PostForm, AuthorForm, CommentForm, Tag


def index_view(request):
    return render(request, 'index.html')


def post_detail_view(request, *args, **kwargs):
    try:
        post = Post.objects.all().get(pk=kwargs.get('pk'))
    except Post.DoesNotExist as error:
        raise Http404('Post does not exist')

    return render(request, 'posts/view.html', context={'post': post})


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', context={'posts': posts})


def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'posts/create.html', context={'form': form, 'authors': Author.objects.all()})

    elif request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():
            author = Author.objects.get(pk=request.POST.get('author'))
            tags = form.cleaned_data.pop('tags')
            new_post = Post.objects.create(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                author=author,
            )
            new_post.tags.set(tags)
            return redirect('post_list')

        else:
            return render(request, 'posts/create.html', context={
                'form': form
            })


'''
    title = request.POST.get('title')
    body = request.POST.get('body')
    author = request.POST.get('author')

    errors = dict()

    if not title:
        errors['title'] = 'Title should not be empty'
    elif len(title) > 50:
        errors['title'] = 'Title should be 50 characters long'
    if not author:
        errors['author'] = 'Author should not be empty'
    elif len(author) > 50:
        errors['author'] = 'Author name should not be 50 characters long'
    if not body:
        errors['body'] = 'Body should not be empty'

    print(title,body,author)
    print(len(title), len(body), len(author))

    if errors:
        post = Post(title=title, body=body, author=author)
        return render(request, 'post_create.html', context={'errors': errors, 'post': post})
    else:

    return redirect('home_page')
'''


def post_update_view(request, *args, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('pk'))

    if request.method == "GET":
        form = PostForm(initial={
            'title': post.title,
            'body': post.body,
            'author': post.author,
            'tags': post.tags.all()
        })
        return render(request, 'posts/update.html', context={'form': form, 'post': post})

    elif request.method == "POST":
        form = PostForm(data=request.POST, initial={'tags': post.tags.all()})
        if form.is_valid():
            tags = form.cleaned_data.pop('tags')
            post.title = form.cleaned_data.get('title')
            post.body = form.cleaned_data.get('body')
            post.author = form.cleaned_data.get('author')
            post.save()
            post.tags.set(tags)
            return redirect('post_detail', pk=post.pk)
        else:
            return render(request, 'posts/update.html', context={'form': form, 'post': post})


'''
        errors = dict()

        if not post.title:
            errors['title'] = 'Title should not be empty'
        elif len(post.title) > 50:
            errors['title'] = 'Title should be 50 characters long'
        if not post.author:
            errors['author'] = 'Author should not be empty'
        elif len(post.author) > 50:
            errors['author'] = 'Author name should not be 50 characters long'

        if errors:
            return render(request, 'post_update.html', context={'errors': errors, 'post': post})
        else:
            post.title = request.POST.get('title')
            post.author = request.POST.get('author')
            post.body = request.POST.get('body')
            post.save()
            return redirect('post_detail', pk=post.pk)
'''


def post_delete_view(request, *args, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('pk'))
    if request.method == "GET":
        return render(request, 'posts/delete.html', context={'post': post})
    elif request.method == "POST":
        post.delete()
        return redirect('home_page')
