from django.urls import path,include

from . import views

urlpatterns = [
path('',views.HomeView.as_view(),name="home"),
path('lost/',views.LostView.as_view(),name="lost"),
path('found/',views.FoundView.as_view(),name="found"),
path('about/',views.AboutView.as_view(),name="about_us")
]

