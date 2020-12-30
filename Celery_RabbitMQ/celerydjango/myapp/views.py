from django.shortcuts import render
from django.shortcuts import HttpResponse
from .tasks import celery_task

from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


def celery_view(request):
    for counter in range(2):
        celery_task.delay(counter)
    return HttpResponse("FINISH PAGE LOAD")


class UsersListView(ListView):
    template_name = 'myapp/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'myapp/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')