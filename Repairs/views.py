from django.views.generic import ListView
from django.views.generic import DetailView
from .models import User  # Проверете дали моделът е правилно указан


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'repairs/user_detail.html'