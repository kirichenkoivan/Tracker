from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login  # Добавьте импорт для входа пользователя

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('task_list')  # Перенаправление на страницу задач после успешной регистрации
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Вход пользователя после успешной регистрации
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        user = request.user  # Получаем текущего пользователя
        Task.objects.create(title=title, user=user)  # Создаем задачу с текущим пользователем
        return redirect('task_list')

    tasks = Task.objects.filter(user=request.user)  # Фильтруем задачи по текущему пользователю
    return render(request, 'task_tracker/task_list.html', {'tasks': tasks})
