from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'