from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='in'),
    url(r'^create$', views.create, name='ucreate'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='udestroy'),
    url(r'^end/(?P<id>\d+)$', views.end, name='uend'),
]