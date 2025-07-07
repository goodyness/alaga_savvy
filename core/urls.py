from django.urls import path
from . import views, admin_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ping/', views.ping),
    path('about/', views.about, name='about'),
    path('rate-us/', views.rate_us, name='rate_us'),
    path('admin-dashboard/', admin_views.dashboard, name='admin_dashboard'),
    path('request-service/', views.request_service, name='request_service'),
    path('clients/', admin_views.client_list, name='client_list'),
    path('clients/<int:pk>/', admin_views.client_detail, name='client_detail'),
    path('messages/', admin_views.contact_message_list, name='contact_message_list'),
    path('messages/<int:pk>/', admin_views.contact_message_detail, name='contact_message_detail'),
    path('recent-works/', admin_views.recent_work_list, name='recent_work_list'),
    path('recent-work/', views.all_recent_works, name='all_recent_works'),
    path('recent-works/<int:work_id>/', views.work_detail, name='work_detail'),
    path('add-video/', admin_views.add_video, name='add_video'),
    path('all-videos/', views.all_work_videos, name='all_work_videos'),
    path('videos/', admin_views.admin_all_videos, name='admin_all_videos'),
    path('videos/edit/<int:video_id>/', admin_views.edit_video, name='edit_video'),
    path('videos/delete/<int:video_id>/', admin_views.delete_video, name='delete_video'),

    path('recent-works/edit/<int:work_id>/', admin_views.edit_recent_work, name='edit_recent_work'),
    path('recent-works/delete/<int:work_id>/', admin_views.delete_recent_work, name='delete_recent_work'),



]
