from django.shortcuts import render
from django.urls import path
from . import views
from .models import Project, Resource


# def project_detail(request, pk):
#     project = Project.objects.get(pk=pk)
#     return render(
#         request=request,
#         template_name="projects/detail.html",
#         context={"projects": project},
#     )


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html")


def resourcepage(request):
    if request.method == "GET":
        print(Resource.objects.all())
        # print(data.resource_id)
        return render(
            request=request,
            template_name="resourcepage.html",
            context={"source": source},
        )


def blogpage(request):
    return render(request=request, template_name="blogpage.html")


def clientpage(request):
    return render(request=request, template_name="clientpage.html")
