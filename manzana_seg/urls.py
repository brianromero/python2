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
    url(r'^crorecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla01),
    url(r'^crorecargaTabla02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla02)
    # Croquis y listado...
#    url(r'^croquisrecargaTabla/(\d+)/(\d+)/$', views.CroquisrecargaTabla),
#    url(r'^croquisrecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.CroquisrecargaTabla01),
#    url(r'^croquisrecargaTabla02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.CroquisrecargaTabla02),
#    url(r'^croquisrecargaDepa/$', views.CroquisrecargaDepa),
#    url(r'^croquisrecargaProv/(\d+)/(\d+)/$', views.CroquisrecargaProv),
#    url(r'^croquisrecargaDis/(\d+)/(\d+)/(\d+)/$', views.CroquisrecargaDis),
#    url(r'^croquisrecargaZona/(\d+)/$', views.CroquisrecargaZona)

]
