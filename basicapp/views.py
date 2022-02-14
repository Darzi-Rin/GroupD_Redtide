# mainに元からあるモジュール
from django.shortcuts import render,redirect #qiitaにもある
import logging
from django.views import generic
from django.urls import reverse_lazy

# sotoをコピペしたもの
# from django.contrib.auth.models import CustomUser #importエラーの原因
from django.contrib.auth import login, authenticate # qiitaにもあり
from django.views.generic import CreateView
# from . forms import UserCreateForm

# qiitaのサイトから参考にしたもの
# from django.contrib.auth.models import User #問題点だと思われるもの
from django.contrib.auth import get_user_model #代替え案
# from django.contrib.auth import login, authenticate #すでにsatoあり
from django.views.generic import CreateView, TemplateView #不明

#追加した理由は不明
from django.views import View
# from basicapp.forms import CustomUser #importエラー原因
from . forms import LoginForm

# Create your views here.
logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "basic/index.html"
    success_url = reverse_lazy('basicapp:index')

class InquiryView(generic.TemplateView):
    template_name = "basic/inquiry.html"

# class LoginView(generic.TemplateView):
#     template_name = "basic/login.html"

#ログイン
class LoginView(generic.TemplateView):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'basic/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'basic/login.html', {'form': form,})


# account_login = Account_login.as_view()


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

class RedtidePredictionView(generic.TemplateView):
    template_name = "basic/redtide_prediction.html"

class RedtideReportView(generic.TemplateView):
    template_name = "basic/redtide_report.html"

class SharePlaceView(generic.TemplateView):
    template_name = "basic/share_place.html"

class ShareMailView(generic.TemplateView):
    template_name = "basic/share_mail.html"

class SignUpView(generic.TemplateView):
    template_name = "basic/sign_up.html"



# # 修正前
# from django.shortcuts import render,redirect 修正後もある
# import logging　ある
# from django.views import generic　ある
# from django.urls import reverse_lazy　ある
# from django.contrib.auth import login, authenticate　ある
# from django.views.generic import CreateView, TemplateView　ある
# from django.views import View　ある
# from django.contrib.auth.models import User　消してる
# from . forms import LoginForm　ある


