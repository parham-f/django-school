from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# CBV Import
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

# Create your views here.

# normal function way to do this
# def index(request):
#     return render(request, 'index.html')

# SIMPLE CBV(Class Base Views) way to do this
# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CLASS BASED VIEWS ARE COOL!')

# CBVs and TemplateView
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context


class SchoolListView(ListView):
    model = models.School
    # ListView returns school_list
    # do this if you want your own name for that school_list
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    # DetailView returns school
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')


class StudentCreateView(CreateView):
    fields = ('name', 'age', 'school')
    model = models.Student

class StudentUpdateView(UpdateView):
    fields = ('name', 'age', 'school')
    model = models.Student

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy('basic_app:list')
    # kwargs={'pk':model.school}
