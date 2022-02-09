from django.shortcuts import render,redirect
import logging
from django.views import generic
from django.urls import reverse_lazy
from basicapp.forms import UserCreateForm

from basicapp.observation_AI import hantei

from . forms import UserCreateForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

# Create your views here.
logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "basic/index.html"
    success_url = reverse_lazy('basicapp:index')

class InquiryView(generic.TemplateView):
    template_name = "basic/inquiry.html"

class LoginView(generic.TemplateView):
    template_name = "basic/login.html"

class LogoutView(generic.TemplateView):
    template_name = "basic/logout.html"

class PoricyView(generic.TemplateView):
    template_name = "basic/p_poricy.html"

class PasswordResetView(generic.TemplateView):
    template_name = "basic/password_reset.html"

class PasswordResetCompleteView(generic.TemplateView):
    template_name = "basic/password_reset_complete.html"

class RedtideObserveView(generic.TemplateView):
    template_name = "basic/redtide_observe.html"

def ans(request):
        return hantei(request)

class RedtidePredictionView(generic.TemplateView):
    template_name = "basic/redtide_prediction.html"

class RedtideReportView(generic.TemplateView):
    template_name = "basic/redtide_report.html"

class SharePlaceView(generic.TemplateView):
    template_name = "basic/share_place.html"

class ShareMailView(generic.TemplateView):
    template_name = "basic/share_mail.html"

# class SignUpView(generic.TemplateView):
#     template_name = "basic/sign_up.html"

class SignUpView(CreateView):
    template_name = "basic/sign_up.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("basicapp:sign_up")
#     def post(self, request, *args, **kwargs):
#         form = UserCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             #フォームから'username'を読み取る
#             username = form.cleaned_data.get('username')
#             #フォームから'password1'を読み取る
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         return render(request, 'basic/sign_up.html', {'form': form,})

#     def get(self, request, *args, **kwargs):
#         form = UserCreateForm(request.POST)
#         return  render(request, 'basic/sign_up.html', {'form': form,})

# create_account = Create_account.as_view()