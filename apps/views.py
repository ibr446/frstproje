from django.contrib.auth import authenticate,login
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from .forms import LoginForm, SignupForm, ContactForm
from django.urls import reverse_lazy
from .models import service, Contact
# from utils.bot_main import send_msg




class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)




class IndexView(TemplateView):
    template_name = 'index.html'
    context_object_name = 'index'



class ServiceView(ListView):
    model = service
    context_object_name = 'service'
    template_name = 'services.html'



class ContactView(CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/"


