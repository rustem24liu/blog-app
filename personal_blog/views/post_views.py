from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

from personal_blog.forms import PostForm, CommentForm
from personal_blog.models import Post, Author
from django.views.generic import View


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

# def index_view(request):
#     return render(request, 'index.html')



# def post_detail_view(request, *args, **kwargs):
#     try:
#         post = Post.objects.all().get(pk=kwargs.get('pk'))
#     except Post.DoesNotExist as error:
#         raise Http404('Post does not exist')
#
#     return render(request, 'posts/view.html', context={'post': post})

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        post = get_object_or_404(Post, pk = kwargs.get('pk'))
        return render(request, 'posts/view.html', context={'post':post, 'form': form})

class CommentView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post_pk = kwargs.get('post_pk')
        if form.is_valid():
            post = get_object_or_404(Post, pk=post_pk)
            post.Comments.create(
                text=request.POST.get("text"),
                author=request.POST.get("author")
                )
            return redirect('post_detail', post_pk)



def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', context={'posts': posts})


def post_create_view(request):
    print(request.POST)
    print(request.GET)
    if request.method == "GET":
        form = PostForm()
        return render(request, 'posts/create.html', context={'form':form, 'authors':Author.objects.all()})
    elif request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():
            author = Author.objects.get(pk=request.POST.get('author'))
            new_post = Post.objects.create(
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body'],
                author=author,
            )
            return redirect('post_list')

        else:
            return render(request, 'posts/create.html', context={
                'form': form
            })

    # title = request.POST.get('title')
        # body = request.POST.get('body')
        # author = request.POST.get('author')

        # errors = dict()
        #
        # if not title:
        #     errors['title'] = 'Title should not be empty'
        # elif len(title) > 50:
        #     errors['title'] = 'Title should be 50 characters long'
        # if not author:
        #     errors['author'] = 'Author should not be empty'
        # elif len(author) > 50:
        #     errors['author'] = 'Author name should not be 50 characters long'
        # if not body:
        #     errors['body'] = 'Body should not be empty'
        #
        # print(title,body,author)
        # print(len(title), len(body), len(author))


        # if errors:
        #     post = Post(title=title, body=body, author=author)
        #     return render(request, 'post_create.html', context={'errors': errors, 'post': post})
        # else:
        #
        # return redirect('home_page')


def post_update_view(request, *args, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('pk'))

    if request.method == "GET":
        form = PostForm(initial={
            'title':post.title,
            'body':post.body,
            'author':post.author
        })
        return render(request, 'posts/update.html', context={'form':form, 'post':post})

    elif request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post.title = form.cleaned_data.get('title')
            post.body = form.cleaned_data.get('body')
            post.author = form.cleaned_data.get('author')
            post.save()
            return redirect('post_detail', pk = post.pk)
        else:
            return render(request, 'posts/update.html', context={'form':form, 'post':post})
        # errors = dict()
        #
        # if not post.title:
        #     errors['title'] = 'Title should not be empty'
        # elif len(post.title) > 50:
        #     errors['title'] = 'Title should be 50 characters long'
        # if not post.author:
        #     errors['author'] = 'Author should not be empty'
        # elif len(post.author) > 50:
        #     errors['author'] = 'Author name should not be 50 characters long'

        # if errors:
        #     return render(request, 'post_update.html', context={'errors': errors, 'post': post})
        # else:
        #     post.title = request.POST.get('title')
        #     post.author = request.POST.get('author')
        #     post.body = request.POST.get('body')
        #     post.save()
        #     return redirect('post_detail', pk=post.pk)


def post_delete_view(request, *args, **kwargs):
    post = get_object_or_404(Post, pk=kwargs.get('pk'))
    if request.method == "GET":
        return render(request, 'posts/delete.html', context={'post': post})
    elif request.method == "POST":
        post.delete()
        return redirect('home_page')


