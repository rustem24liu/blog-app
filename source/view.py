from django.shortcuts import render
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html')

