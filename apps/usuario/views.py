from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateUserForm
from .models import User

# Create your views here.


@method_decorator(login_required(), name='dispatch')
class UserProfile(DetailView):
   model = User
   template_name = 'user_profile/profile.html'
   slug_field = 'username'
   slug_url_kwarg = 'username'
   context_object_name = 'user'


@method_decorator([login_required(), never_cache], name='dispatch')
class UserUpdate(UpdateView):
   model = User
   form_class = UpdateUserForm
   template_name = 'user_profile/update_profile.html'
   context_object_name = 'user'
   slug_field = 'username'
   slug_url_kwarg = 'username'

   def form_valid(self, form):
      if self.object.check_password(self.kwargs['password']):
         return super().form_valid(form)
      return super().form_invalid(form)


class SignUp(CreateView):
   template_name = 'authentication/sign_up.html'
   form_class = SignUpForm
   success_url = reverse_lazy('usuario:login')

   def dispatch(self, request, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('index:index')
      return super().dispatch(request, *args, **kwargs)

   def form_valid(self, form):
      form.save()
      user = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      credentials = authenticate(username=user, password=password)
      login(self.request, credentials)
      return super().form_valid(form)
