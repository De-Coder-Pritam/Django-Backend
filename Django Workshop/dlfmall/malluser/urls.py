from django.http import HttpRequest
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/',views.userSignup.as_view()),
    path('getmembership/<email>',views.userMembership.as_view()),

]