from django.conf.urls import url
from . import views
from .views import ( 
    index,
    OnlinePaymentAPIView

)





urlpatterns = [
    url(r'^$', views.index, name="index_page"),
    url(r'^signup/$', views.SignUp, name="signup"),
    url(r'^api/lessons/$', views.LessonList.as_view(), name="lesson_api"),
    url(r'^online/$', OnlinePaymentAPIView.as_view(),name='online'),
]