from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.http import urlencode
from django.views.generic import View, TemplateView, FormView, ListView
from personal_blog.forms import CommentForm, SearchForm, PostForm
from personal_blog.helpers.views import CustomListView, CustomFormView
from personal_blog.models import Post, Author

''' Just by using View class'''
# class PostDetailView(View):
#     def get(self, request, *args, **kwargs):
#         form = CommentForm()
#         post = get_object_or_404(Post, pk=kwargs.get('pk'))
#         return render(request, 'posts/view.html', context={'post': post, 'form': form})

''' By using templateView'''


class PostDetailView(TemplateView):
    template_name = 'posts/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post']  = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context


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


class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts'
    form = SearchForm
    #
    def get_objects(self):
        return super().get_objects()

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return self.form(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")
        return None
    def get_context_data(self, object_list = None ,**kwargs):
        context = super().get_context_data(object_list = object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['search'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(author__name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset
class PostCreateView(CustomFormView):
    form_class = PostForm
    template_name = 'posts/create.html'

    def form_valid(self, form):
        """
        data = {}
        tags = form.cleaned_data.pop('tags')

        for key, value in form.cleaned_data.items():  # полагаю что здесь все наши данные к примеру { title : Crime and Punishment, author: Dostoevsky, body: such a great book}
            if value is not None:  # key = name, value = Crime and Punishment, key = author , value = Dostoevsky
                data[key] = value
        self.post = Post.objects.create(**data)  # и наша пост будет записать все эти данные в себе
        self.post.tags.set(tags)
        """

        self.post = form.save()
        return super().form_valid(form)  # мы должны переопределять redirect_url потому что джанго не знает куда отправлять данные

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context

    def get_redirect_url(self):
        return reverse('post_list')


class PostUpdateView(FormView):
    template_name = 'posts/update.html'
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        self.post = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)
        return Post.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post
        return context

    # def get_initial(self):
    #     initial = {} # для начала пустой словарик
    #
    #     for key in ['title', 'body', 'author', 'tags']:
    #         initial[key] = getattr(self.post, key)
    #     initial['tags'] = self.post.tags.all()
    #     return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.post
        return kwargs

    def form_valid(self, form):
        # tags = form.cleaned_data.pop('tags')
        # for key, value in form.cleaned_data.items():
        #     if value:
        #         setattr(self.post, key, value)
        # self.post.save()
        # self.post.tags.set(tags)
        self.post = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.pk})
