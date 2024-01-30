from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    # Other URL patterns...
    path('journal_entries/', views.journal_entries, name='journal_entries'),
    path('login_view/', views.login_view, name='login_view'),
    path("accounts/", include("django.contrib.auth.urls")),
]
