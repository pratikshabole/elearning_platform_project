from django.contrib import admin
from django.urls import path, include
from quiz import views


urlpatterns = [
    path('start_quiz',views.start_quiz , name='start_quiz'),
    path('quiz/',views.quiz , name='quiz'),
    path('result/',views.result, name='result'),
    path('saveans/',views.saveans, name='saveans'),
]