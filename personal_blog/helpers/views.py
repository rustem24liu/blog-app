from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView


class CustomFormView(View):  # мы импортируем здесь generic view и с этого и мы построили свой FormView
    form_class = None  # передаем туда класс формы например у нас есть формы: PostForm, CommentForm, AuthorForm вот этих то мы и передаем здесь
    template_name = None  # мы будем сюда передовать путь шаблона -> html страница
    redirect_url = ''  # ссылка для перенапровление

    def get(self, request, *args, **kwargs):  # метод для обработки get запросов
        form = self.form_class()  # наша форма -> PostForm, AuthorForm ...
        context = self.get_context_data(
            form=form)  # контекст функция getter должны передовать форму чтоб мы в шоблоне могли работать
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):  # для работы с post запросами
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(
                form)  # это метод который мы сами будем создать для того чтоб если форма валидна выполнялась эта функция
        else:
            return self.form_invalid(
                form)  # это точно также если у нас форма не валидна то есть есть ошибки в форме то мы будем вызвать этот мутод инвалид

    def form_valid(self, form):
        return redirect(self.get_redirect_url())  # перенаправляем на url адрес если наша форма валидна

    def form_invalid(self,
                     form):  # форма не прошел валидацию в этом случае мы должны render to smt like this { return render(request, 'posts/create.html', context = context) }
        context = self.get_context_data(form=form)
        return render(self.request, self.template_name, context=context)

    def get_context_data(self, **kwargs):  # **kwargs это именованный аргумент, словарь с аргументами key and value
        return kwargs

    def get_redirect_url(
            self):  # просто геттер для url - ну например с помощью этого мы можем брать 'home_page', 'post_create'-> вот такие url имена мы можем брать
        return self.redirect_url


class CustomListView(TemplateView):
    model = None  # даем имя модели
    context_key = 'objects'  # имя шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.model.objects.all()
        return context

    def get_objects(self):
        return self.model.objects.all()
