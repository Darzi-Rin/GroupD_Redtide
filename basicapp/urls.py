from django.urls import path
from . import views

app_name = 'basicapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('p_poricy', views.PoricyView.as_view(), name="p_poricy"),
    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('redtide_observe/', views.RedtideObserveView.as_view(), name="redtide_observe"),
    path('redtide_prediction/', views.RedtidePredictionView.as_view(), name="redtide_prediction"),
    path('redtide_report/', views.RedtideReportView.as_view(), name="redtide_report"),
    path('share_list/', views.ShareListView.as_view(), name="share_list"),
    path('share_detail/<int:pk>/', views.ShareDetailView.as_view(), name="share_detail"),
    path('share_delete/<int:pk>/', views.ShareDeleteView.as_view(), name="share_delete"),
    path('share_place/', views.SharePlaceView.as_view(), name="share_place"),
    path('share_mail/', views.ShareMailView.as_view(), name="share_mail"),
    path('sign_up/', views.SignUpView.as_view(), name="sign_up"),
    path('redtide_observe/ans/', views.ans, name="redtide_observe_ans"),
]
