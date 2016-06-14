from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^$', views.myMages, name='myMages'),
        url(r'^mage/(?P<pk>\d+)/$', views.mage_detail, name='mage_detail'),
        url(r'^add/new/$', views.add_new, name='add_new'),
]
