from django.conf.urls import url,include
from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.index),
    url(r'^orden/detalle/(?P<pk>[0-9]+)/$', views.orden_detalle,''),
    url(r'^administrador/$', views.admin),
    url(r'^user/tecnico/$', views.tecnicoview),
    url(r'^listar/', views.cliente_list),
    url(r'^tecnico/$',views.tecnico_nuevo,''),
    url(r'^cliente/$',views.cliente_nuevo,''),
    url(r'^orden/$',views.orden_nuevo,''),
    url(r'^ver/orden/$',views.ver_orden),
]