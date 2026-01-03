from django.views import generic
from .models import Diary
# from django.urls import reverse_lazy

class ListView(generic.ListView):
    model = Diary
    template_name = 'diary/diary_list.html'

class DetailView(generic.DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html'

class CreateView(generic.edit.CreateView):
    model = Diary
    fields = ['title', 'body']
    template_name = 'diary/diary_form.html'
    # success_url = reverse_lazy('diary:list')
        # 作成後の移動先はmodels.py のほうで設定
