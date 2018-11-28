from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
#el serializer permite transformar un arreglo en un json
from django.core import serializers
import json
from core.models import Mascota,Origen_mascota,Raza,Refugio

from django.views.decorators.http import require_http_methods 
from django.views.decorators.csrf import csrf_exempt 

#listado en formato json

def listar_mascotas(request):
    masc=Mascota.objects.all()
    #transformamos los datos a json
    mascJson=serializers.serialize('json',masc)
    #mostramos el json
    return HttpResponse(mascJson,content_type="application/json")



@csrf_exempt #evitamos que haga la verificacion
@require_http_methods(['POST'])#solo acepte post
def agregar_mascota(request):
    #obtenemos lo del body
    body = request.body.decode('utf-8')
    #el body viene en string por lo que lo transformamos
    bodyDict = json.loads(body) #lo parse a json

    #ahora guardaremos la mascota en la base de datos
    m=Mascota()
    m.nombre=bodyDict['nombre']  # de donde sacamos este campo ?????????????????????????????
    m.esterilizado=bodyDict['esterilizado']
    m.chip=bodyDict['chip']
    m.fec_nac=bodyDict['fec_nac']
    m.id_raza=Raza(id=bodyDict['id_raza'])
    m.id_orig_masc=Origen_mascota(id=bodyDict['id_orig_masc'])
    m.cod_refugio=Refugio(id=bodyDict['cod_refugio'])
    m.rut_usuario=bodyDict['rut_usuario']

    try:
        m.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}),content_type="application/json")
    except:
        #retornaremos un nmensaje con el codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'No se ha podido guardar'}),content_type="application/json")


@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        #primero buscamos la mascota que eliminaremos
        masc = Mascota.objects.get(id=id)
        masc.delete()
        return HttpResponse(json.dumps({'mensaje':'eliminada correctamente'}),
         content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':"no se ha podido eliminar"}),
        content_type="application/json")
    


#POST
@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #modificamos la mascota en la BBDD
    masc = Mascota()
    masc.id = bodyDict['id']
    masc.nombre=bodyDict['nombre']  # de donde sacamos este campo ?????????????????????????????
    masc.esterilizado=bodyDict['esterilizado']
    masc.chip=bodyDict['chip']
    masc.fec_nac=bodyDict['fec_nac']
    masc.id_raza=Raza(id=bodyDict['id_raza'])
    masc.id_orig_masc=Origen_mascota(id=bodyDict['id_orig_masc'])
    masc.cod_refugio=Refugio(id=bodyDict['cod_refugio'])
    masc.rut_usuario=bodyDict['rut_usuario']

    try:
        masc.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido modificar'}), content_type="application/json")
