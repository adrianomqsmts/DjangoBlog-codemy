from django.shortcuts import render, get_object_or_404
from django.views import generic
from myblog.models import Profile, Category
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfileForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.


class ProfileCreateView(generic.CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/create_user_profile_page.html"
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdateView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('home')


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        users = Profile.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class UserCreateView(generic.CreateView):
    # model = User
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    # model = User
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    """
    docstring
    """
    template_name = "registration/change-password.html"
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    # success_url = reverse_lazy("home")
    success_url = reverse_lazy("password_success")


class PasswordSuccessView(generic.TemplateView):
    template_name = "registration/password_success.html"
