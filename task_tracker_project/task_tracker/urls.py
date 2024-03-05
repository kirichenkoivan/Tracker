from django.urls import path
from .views import task_list
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from .views import SignUpView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('login')), name='index'),
    path('tasks/', task_list, name='task_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
