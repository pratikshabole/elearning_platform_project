from django.urls import path
from . import views

app_name = 'curiculum'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('<slug:slug>/', views.TopicListView.as_view(), name='topic_list'),
    path('<str:course>/<slug:slug>/', views.LectureListView.as_view(), name='lecture_list'),
    path('<str:course>/<str:slug>/create/', views.LectureCreateView.as_view(), name='lecture_create'),
    path('<str:course>/<str:topic>/<slug:slug>/', views.LectureDetailView.as_view(), name='lecture_detail'),
    path('<str:course>/<str:topic>/<slug:slug>/update/', views.LectureUpdateView.as_view(), name='lecture_update'),
    path('<str:course>/<str:topic>/<slug:slug>/delete/', views.LectureDeleteView.as_view(), name='lecture_delete'),
]
