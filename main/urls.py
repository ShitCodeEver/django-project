from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('error/', views.ErrorView.as_view(), name='error'),
]
