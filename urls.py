from django.urls import path
from django.http import HttpResponse
from django.urls import reverse
from . import views


urlpatterns = [
    #    path("<int:pk>", views.project_detail),
    path("", views.index, name="index"),
    path("resourcepage", views.resourcepage, name="resourcespage"),
    path("clientpage", views.clientpage, name="clientpage"),



]
