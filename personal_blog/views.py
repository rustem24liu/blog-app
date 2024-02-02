from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

from personal_blog.models import Post


# posts_list = [
#     {
#         'pk':1,
#         'title':'rustem',
#         'description':'post description1',
#         'body':'lorem ipsum dolor sit',
#         'image_url':'https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg'
#     },
# {
# 'pk':2,
#         'title':'I love',
#         'description':'post description2',
#         'body':'lorem ipsum dolor sit',
#         'image_url':'https://cdn.britannica.com/99/197999-050-D22B29F0/Leopard-cat.jpg'
#     },
# {
# 'pk':4,
#         'title':'I just died in your arms to night',
#         'description':'post description3',
#         'body':'lorem ipsum dolor sit',
#         'image_url':'https://cdn.britannica.com/25/7125-050-67ACEC3C/Abyssinian-sorrel.jpg'
#     },
# {
# 'pk':5,
#         'title':'How I wish, how i wish you were here',
#         'description':'post description4',
#         'body':'lorem ipsum dolor sit',
#         'image_url':'https://cdn.britannica.com/53/155253-050-642F3524/Egyptian-cat-statue-Bastet.jpg'
#     },
# {
# 'pk':6,
#         'title':'I will see you on the dark side of the moon',
#         'description':'post description5',
#         'body':'lorem ipsum dolor sit',
#         'image_url':'https://cdn.britannica.com/62/5162-004-E7F758CE/Dick-Whittington-portrait-cat-engraving-Renold-Elstracke.jpg?w=300'
#     }
# ]

def index_view(request):
    return render(request, 'index.html')


def post_detail_view(request, *args, **kwargs):
    try:
        post = Post.objects.all().get(pk=kwargs.get('pk'))
    except Post.DoesNotExist as error:
        raise Http404('Post does not exist')

    return render(request, 'post_view.html', context={'post': post})


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', context={'posts': posts})


def post_create_view(request):
    print(request.POST)
    print(request.GET)
    if request.method == "GET":
        return render(request, 'post_create.html')
    elif request.method == "POST":

        title = request.POST.get('title'),
        body = request.POST.get('body'),
        author = request.POST.get('author')

        errors = dict()

        if len(title) ==  1:
            errors['title'] = 'Title should not be empty'
        elif len(title) > 50:
            errors['title'] = 'Title should be 50 characters long'
        elif not author:
            errors['author'] = 'Author should not be empty'
        elif len(author) > 50:
            errors['author'] = 'Author name should not be 50 characters long'

        print(title,body,author)
        print(len(title), len(body), len(author))
        if errors:
            post = Post(title=title, body=body, author=author)
            return render(request, 'post_create.html', context={'errors': errors, 'post': post})
        else:
            new_post = Post.objects.create(
                title=title,
                body=body,
                author=author,
            )
        return redirect('home_page')


def post_update_view(request, *args, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('pk'))

    if request.method == "GET":
        return render(request, 'post_update.html', context={'post': post})

    elif request.method == "POST":
        post.title = request.POST.get('title')
        post.author = request.POST.get('author')
        post.body = request.POST.get('body')
        post.save()
        return redirect('post_detail', pk=post.pk)


def post_delete_view(request, *args, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('pk'))
    if request.method == "GET":
        return render(request, 'post_delete.html', context={'post': post})
    elif request.method == "POST":
        post.delete()
        return redirect('home_page')
