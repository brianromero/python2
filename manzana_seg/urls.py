from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.inicial, name='vista inicial'),

    # Segmentacion...
    url(r'^segrecargaDepa/$', views.SegrecargaDepa),
    url(r'^segrecargaProv/(\d+)/(\d+)/$', views.SegrecargaProv),
    url(r'^segrecargaDis/(\d+)/(\d+)/(\d+)/$', views.SegrecargaDis),
    url(r'^segrecargaZona/(\d+)/$', views.SegrecargaZona),
    url(r'^segrecargaTabla/(\d+)/(\d+)/$', views.segrecargaTabla),
    url(r'^segrecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.segrecargaTabla01),
    
    # Croquis...
    url(r'^crorecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla01),
    url(r'^crorecargaTabla02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla02)    
]
