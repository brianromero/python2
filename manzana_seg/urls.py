from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.inicial, name='vista inicial'),


    # menues
    #url(r'^segmentacion/$', views.segmentacion),
    #url(r'^croquisylistado/$', views.croquis),

    # segmentacion
    #url(r'^segmentacion/recargaTabla/(\d+)/(\d+)/(\d+)/$', views.SegrecargaTabla),
    #url(r'^segmentacion/recargaDepa/(\d+)/$', views.SegrecargaDepa),
    #url(r'^segmentacion/recargaProv/(\d+)/(\d+)/$', views.SegrecargaProv),
    #url(r'^segmentacion/recargaDis/(\d+)/(\d+)/(\d+)/$', views.SegrecargaDis),
    #url(r'^segmentacion/recargaZona/(\d+)/$', views.SegrecargaZona),

    # croquis y listado
    #url(r'^croquisylistado/recargaTabla/(\d+)/(\d+)/(\d+)/$', views.recargaTabla),
    #url(r'^croquisylistado/recargaDepa/(\d+)/$', views.recargaDepa),
    #url(r'^croquisylistado/recargaProv/(\d+)/(\d+)/$', views.recargaProv),
    #url(r'^croquisylistado/recargaDis/(\d+)/(\d+)/(\d+)/$', views.recargaDis),
    #url(r'^croquisylistado/recargaZona/(\d+)/$', views.recargaZona),

    #url(r'^SegrecargaTabla/(\d+)/(\d+)/(\d+)/$', views.SegrecargaTabla),

    url(r'^segrecargaTabla/(\d+)/(\d+)/$', views.segrecargaTabla),

    url(r'^segrecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.segrecargaTabla01),

    url(r'^segrecargaDepa/$', views.SegrecargaDepa),
    url(r'^segrecargaProv/(\d+)/(\d+)/$', views.SegrecargaProv),
    url(r'^segrecargaDis/(\d+)/(\d+)/(\d+)/$', views.SegrecargaDis),
    url(r'^segrecargaZona/(\d+)/$', views.SegrecargaZona)

    # No los uso...
    #url(r'^inicio/$', views.recargaFiltroIni, name='hello'),
    #url(r'^obtenerdata/$', views.obtener_data),
    #url(r'^obtenerdata2/(\d+)/(\d+)/(\d+)/$', views.obtener_data2),
    #url(r'^recargaFiltro/(\d+)/(\d+)/(\d+)/$', views.recargaFiltro),

]
