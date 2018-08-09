from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.index, name="index_page"),
    url(r'^signup/$', views.SignUp, name="signup"),
    url(r'^api/lessons/$', views.LessonList.as_view(), name="lesson_api"),
    url(r'^api/validation/$', views.ValidationView.as_view()),
]