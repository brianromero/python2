from django.http import HttpResponse
from django.template import loader
from .models import Segmentacion_prueba, Departamento, Provincia, Distrito, Zona
import json
from django.db.models import Count

def inicial(request):
    lista = Segmentacion_prueba.objects.all().values().annotate(dcount=Count('cod_dd'))
    template = loader.get_template('index.html')
    context = {
        'lista': lista,
    }
    return HttpResponse(template.render(context, request))

def recargaTabla(request, dep, pro, dis):
#    if dep == '0':
#        filtroDepa = Segmentacion_prueba.objects.all().values().distinct()
#    elif pro == '0':
#        filtroDepa = Segmentacion_prueba.objects.filter(cod_dd=dep).values().distinct()
#    elif dis == '0':
#        filtroDepa = Segmentacion_prueba.objects.filter(cod_dd=dep, cod_prov=pro).values().distinct()
#    else:
#        filtroDepa = Segmentacion_prueba.objects.filter(cod_dd=dep, cod_prov=pro, cod_dis=dis).values().distinct()
#    data = list(filtroDepa)
#    return HttpResponse(json.dumps(data), content_type='application/json')


#def recargaTabla(request, ubigeo, zona):
    depa = dep.split("??") #ubigeo.split("??")
    prov = pro.split("????") #ubigeo.split("????")
    dist = dis.split("??????") #ubigeo.split("??????")
    if depa[0] == '0':
        filtro = Segmentacion_prueba.objects.all().values().distinct()
    elif prov[0] == '0':
        filtro = Segmentacion_prueba.objects.filter(cod_dd=dep).values().distinct()
    elif dist[0] == '0':
        filtro = Segmentacion_prueba.objects.filter(cod_dd=dep, cod_prov=pro).values().distinct()
    else:
        filtro = Segmentacion_prueba.objects.filter(cod_dd=dep, cod_prov=pro, cod_dis=dis).values().distinct()
        print "entro fin..."
    data = list(filtro)
    return HttpResponse(json.dumps(data), content_type='application/json')



def recargaDepa(request,depa):
    filtroDepa = Departamento.objects.values('ccdd','departamento').annotate(data=Count('ccdd'))
    data = list(filtroDepa)
    return HttpResponse(json.dumps(data), content_type='application/json')

def recargaProv(request, depa, prov):
    filtroPro = Provincia.objects.filter(ccdd=depa).values('ccpp','provincia').annotate(data=Count('ccdd','ccpp'))
    data = list(filtroPro)
    return HttpResponse(json.dumps(data), content_type='application/json')
    
def recargaDis(request, depa, prov, dis):    
    filtroDist = Distrito.objects.filter(ccdd=depa, ccpp=prov).values('ccdi','distrito').annotate(data=Count('ccpp','ccdi'))
    data = list(filtroDist)
    return HttpResponse(json.dumps(data), content_type='application/json')

def recargaZona(request, ubigeo):
    print "ubigeo"
    print ubigeo
    filtroZona = Zona.objects.filter(ubigeo=ubigeo).values('ubigeo','zona').annotate(data=Count('ubigeo'))
    data = list(filtroZona)
    print "zona"
    print data
    print "fin zona"
    return HttpResponse(json.dumps(data), content_type='application/json')
