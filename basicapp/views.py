from django.shortcuts import render
import logging
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Share
from .forms import CreateForm

from basicapp.observation_AI import hantei
# from basicapp.observation_AI import image

# Create your views here.
logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "basic/index.html"
    # success_url = reverse_lazy('basicapp:index')

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

class RedtideReportView(generic.CreateView):
    model = Share
    template_name = "basic/redtide_report.html"
    form_class = CreateForm
    success_url = reverse_lazy('basicapp:share_mail')

    def form_valid(self, form):
        create = form.save(commit=False)
        create.user = self.request.user
        create.save()
        messages.success(self.request, '報告を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "報告の作成に失敗しました。")
        return super().form_invalid(form)

class ShareListView(generic.ListView):
    model = Share
    template_name = "basic/share_list.html"
    paginate_by = 2

    def get_queryset(self):
        creates = Share.objects.order_by('-created_at')
        return creates

class ShareDetailView(generic.DetailView):
    model = Share
    template_name = "basic/share_detail.html"

class ShareDeleteView(generic.DeleteView):
    model = Share
    template_name = "basic/share_delete.html"
    success_url = reverse_lazy('basicapp:share_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "赤潮情報を削除しました。")
        return super().delete(request, *args, **kwargs)

class SharePlaceView(generic.TemplateView):
    template_name = "basic/share_place.html"

class ShareMailView(generic.TemplateView):
    template_name = "basic/share_mail.html"

class SignUpView(generic.TemplateView):
    template_name = "basic/sign_up.html"