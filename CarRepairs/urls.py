from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include
from accounts.views import login_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('Cars/', include('Cars.urls')),
    path('Users/', include('Users.urls')),
    path('Repairs/', include('Repairs.urls')),
    path('login.html', login_view, name='login'),

]
