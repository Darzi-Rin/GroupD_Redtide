from django.shortcuts import render
import logging
from django.views import generic

# Create your views here.
logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "basic/index.html"

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

class RedtidePredictionView(generic.TemplateView):
    template_name = "basic/redtide_prediction.html"

class RedtideReportView(generic.TemplateView):
    template_name = "basic/redtide_report.html"

class RedtideShareView(generic.TemplateView):
    template_name = "basic/redtide_share.html"

class SignUpView(generic.TemplateView):
    template_name = "basic/sign_up.html"