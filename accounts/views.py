from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('store:all_products')
    template_name = 'registration/signup.html'


