from django.conf.urls import url

from xiaoshuo import views

urlpatterns = [
    url(r'^showit/', views.get_caption),

]
