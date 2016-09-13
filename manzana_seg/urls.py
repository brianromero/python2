from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.inicial, name='vista inicial'),
    

    # menues
    #url(r'^segmentacion/$', views.segmentacion),
    #url(r'^croquisylistado/$', views.croquis),
    
    # segmentacion
    #url(r'^segmentacion/recargaTabla/(\d+)/(\d+)/(\d+)/$', views.recargaTabla),
    #url(r'^segmentacion/recargaDepa/(\d+)/$', views.recargaDepa),
    #url(r'^segmentacion/recargaProv/(\d+)/(\d+)/$', views.recargaProv),
    #url(r'^segmentacion/recargaDis/(\d+)/(\d+)/(\d+)/$', views.recargaDis),
    #url(r'^segmentacion/recargaZona/(\d+)/$', views.recargaZona),

    # croquis y listado
    #url(r'^croquisylistado/recargaTabla/(\d+)/(\d+)/(\d+)/$', views.recargaTabla),
    #url(r'^croquisylistado/recargaDepa/(\d+)/$', views.recargaDepa),
    #url(r'^croquisylistado/recargaProv/(\d+)/(\d+)/$', views.recargaProv),
    #url(r'^croquisylistado/recargaDis/(\d+)/(\d+)/(\d+)/$', views.recargaDis),
    #url(r'^croquisylistado/recargaZona/(\d+)/$', views.recargaZona),

    url(r'^recargaTabla/(\d+)/(\d+)/(\d+)/$', views.recargaTabla),

    url(r'^recargaDepa/(\d+)/$', views.recargaDepa),
    url(r'^recargaProv/(\d+)/(\d+)/$', views.recargaProv),
    url(r'^recargaDis/(\d+)/(\d+)/(\d+)/$', views.recargaDis),
    url(r'^recargaZona/(\d+)/$', views.recargaZona),


    # No los uso...
    #url(r'^inicio/$', views.recargaFiltroIni, name='hello'),
    #url(r'^obtenerdata/$', views.obtener_data),
    #url(r'^obtenerdata2/(\d+)/(\d+)/(\d+)/$', views.obtener_data2),
    #url(r'^recargaFiltro/(\d+)/(\d+)/(\d+)/$', views.recargaFiltro),

]
