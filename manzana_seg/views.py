from django.http import HttpResponse
from django.template import loader
from .models import Segmentacion_prueba, Departamento, Provincia, Distrito, Zona
import json
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

def inicial(request):
    lista = Segmentacion_prueba.objects.all().values().annotate(dcount=Count('cod_dd'))
    template = loader.get_template('index.html')
    context = {
        'lista': lista,
    }
    return HttpResponse(template.render(context, request))

#def SegrecargaTabla(request, dep, pro, dis):
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


def segrecargaTabla(request, ubigeo, zona):
    depa = ubigeo.split("??") #dep.split("??")
    prov = ubigeo.split("????") #pro.split("????")
    dist = ubigeo.split("??????") #dis.split("??????")
    if depa[0] == '0':
        filtro = Segmentacion_prueba.objects.all().values().distinct()
    elif prov[0] == '0':
        filtro = Segmentacion_prueba.objects.filter(cod_dd=dep).values().distinct()
    elif dist[0] == '0':
        filtro = Segmentacion_prueba.objects.filter(cod_dd=dep, cod_prov=pro).values().distinct()
    else:
        filtro = Zona.objects.filter(ubigeo=ubigeo, zona=zona).values().distinct()
        print "entro fin..."
    data = list(filtro)
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def SegrecargaDepa(request):
    filtroDepa = Departamento.objects.values('ccdd','departamento').annotate(data=Count('ccdd'))
    data = list(filtroDepa)
    return HttpResponse(json.dumps(data), content_type='application/json')

def SegrecargaProv(request, depa, prov):
    filtroPro = Provincia.objects.filter(ccdd=depa).values('ccpp','provincia').annotate(data=Count('ccdd','ccpp'))
    data = list(filtroPro)
    return HttpResponse(json.dumps(data), content_type='application/json')

def SegrecargaDis(request, depa, prov, dis):
    filtroDist = Distrito.objects.filter(ccdd=depa, ccpp=prov).values('ccdi','distrito').annotate(data=Count('ccpp','ccdi'))
    data = list(filtroDist)
    return HttpResponse(json.dumps(data), content_type='application/json')

def SegrecargaZona(request, ubigeo):
    print "ubigeo"
    print ubigeo
    filtroZona = Zona.objects.filter(ubigeo=ubigeo).values('ubigeo','zona').annotate(data=Count('ubigeo'))
    data = list(filtroZona)
    print "zona"
    print data
    print "fin zona"
    return HttpResponse(json.dumps(data), content_type='application/json')

#def segrecargaTabla01(request, tipo, ccdd):
#    dataAux = data(tipo, ccdd)
#    return HttpResponse(json.dumps(dataAux), content_type='application/json')

#def data(tipo, ccdd):
#    from django.db import connection
#   cursor = connection.cursor()
#    print(tipo)
#    print(ccdd)
#    cursor.execute('exec ActualizaTabla %s', [tipo, ccdd])
#    columns = [column[0] for column in cursor.description]
#    menu = []
#    for row in cursor.fetchall():
#        menu.append(dict(zip(columns, row)))
#    return menu


def segrecargaTabla01(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = data(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def data(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaTabla %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    print menu
    return menu
    