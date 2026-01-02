from django.views import generic
from .models import Diary

class ListView(generic.ListView):
    model = Diary

class DetailView(generic.DetailView):
    model = Diary
