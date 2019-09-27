from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^atlas$', views.atlas, name='atlas'),
    url(r'^tsi$', views.tsi, name='tsi'),
    url(r'^distribution$', views.distribution, name='distribution'),
]
