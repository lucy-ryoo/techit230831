from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, DetailView

from articleapp.forms import ArticleForm
from articleapp.models import Article


# Create your views here.

class TempView(TemplateView):
    template_name = 'articleapp/temp.html'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articleapp/create.html'

    def get_success_url(self):
        return reverse('articleapp:detail',
                       kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'tqrget_article'
    template_name = 'articleapp/detail.html'