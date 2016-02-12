from django.conf.urls import url

from . import views
from views import BasicView

urlpatterns = [
    url(r'^$', views.BasicView.as_view(), name='index'),
#    url(r'AjaxOutput', RestView.as_view(),name='rest'),
]