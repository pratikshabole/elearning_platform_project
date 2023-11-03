from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView)
from .models import Course, Topic, Lecture
from django.urls import reverse_lazy
from .forms import LectureForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class CourseListView(ListView):
    context_object_name = "courses"
    model = Course
    template_name = 'curiculum/course_list_views.html'

class TopicListView(DetailView):
    context_object_name = "courses"
    model = Course
    template_name = 'curiculum/topic_list_views.html'

class LectureListView(DetailView):
    context_object_name = 'topics'
    model = Topic
    template_name = 'curiculum/lecture_list_views.html'

class LectureDetailView(DetailView):
    context_object_name = 'lectures'
    model = Lecture
    template_name = 'curiculum/lecture_detail_views.html'

class LectureCreateView(CreateView):
    form_class = LectureForm
    context_object_name = 'topics'
    model = Topic
    template_name = 'curiculum/lecture_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('curiculum:lecture_list', kwargs={'course':course.slug,
                                                              'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fs = form.save(commit=False)
        fs.created_by = self.request.user
        fs.Course = self.object.course
        fs.topic = self.object
        fs.save()
        return HttpResponseRedirect(self.get_success_url())
    

class LectureUpdateView(UpdateView):
    fields = ('name', 'position', 'video', 'notes')
    context_object_name = 'lectures'
    model = Lecture
    template_name = 'curiculum/lecture_update.html'

class LectureDeleteView(DeleteView):
    model = Lecture
    context_object_name = 'lectures'
    template_name = 'curiculum/lecture_delete.html'

    def get_success_url(self) -> str:
        course = self.object.Course
        topic = self.object.topic
        return reverse_lazy('curiculum:lecture_list', kwargs={'course':course.slug, 'slug':topic.slug})