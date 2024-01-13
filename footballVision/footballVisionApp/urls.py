from django.urls import path
from .views import uploadpage, loginView, register, success_page, logoutView, dashboard, uploadpageML

urlpatterns = [
    path('upload/', uploadpage, name='upload_page'),
    path('uploadML/', uploadpageML, name='upload_pageML'),
    path('register/', register, name='register'),
    path('success/', success_page, name='success_page'),
    path('', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('dashboard/', dashboard, name='dashboard')
]