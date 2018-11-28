from django.shortcuts import render,redirect
from .models import *


#importamos la mensajeria de django
from django.contrib import messages
#importamos decorador que nos permitirá
#solicitar login en determinado view
from django.contrib.auth.decorators import login_required
#nuevo comentario

# Create your views here.
def home(request):
    maLan=Mascota.objects.all()
    variables= {
        'maLan':maLan
    }
    return render(request, 'core/home.html',variables)

def registro(request):
    
    region=Region.objects.all()
    ciudad=Comuna.objects.all()
    vivienda=Tipo_Vivienda.objects.all()
    usuario=Tipo_usuario.objects.all()

    variables= {
        
          'region':region,
          'ciudad':ciudad,
          'vivienda':vivienda,
          'usuario':usuario
    }

    if request.POST:
        usuario= Usuario()
        usuario.rut_usuario=request.POST.get('txtRun')
        usuario.nombre=request.POST.get('txtNombre')
        usuario.ap_pat=request.POST.get('txtApPat')
        usuario.ap_mat=request.POST.get('txtApMat')
        usuario.id_genero=request.POST.get('cboGenero')



        usuario.fec_nac=request.POST.get('txtNacimiento')
        usuario.telefon=request.POST.get('txtfono')

        region=Region()
        region.id=int(request.POST.get('cboRegion'))
        usuario.region=region


        #error al registrar comuna 
        ciudad=Comuna()
        ciudad.id=int(request.POST.get('cboCuidad'))
        usuario.id_comuna=ciudad


        usuario.direccion=request.POST.get('txtDireccion')
        usuario.mail=request.POST.get('txtMail')


        tipoVivienda=Tipo_Vivienda()
        tipoVivienda.id=int(request.POST.get('cboTipoVivienda'))
        usuario.id_tip_vivienda=tipoVivienda



        tipoUsuario=Tipo_usuario()
        tipoUsuario.id=int(request.POST.get('cboUser'))
        usuario.id_usuario=tipoUsuario


        try:
            usuario.save()
            variables['mensaje']= "Se registro el usuario"
        except Exception as a:
            variables['mensaje']= "Error al registrar Usuario" + str(a)

    return render(request, 'core/registro.html',variables)

def registroComunas(request,id):  #nuevo metodo view que filtra las comunas segun el id rescatado
    ciudad=Comuna.objects.filter(idregion=id) #filtro por idregion (id de clase en models.py)
    return render(request, 'core/comboComuna.html',{ #usa el html combo comuna para escribir los opcion
          'ciudad':ciudad, #retorna tambien la ciudad
   })

@login_required
def registroMascotas(request):
    raza=Raza.objects.all()
    origen=Origen_mascota.objects.all()
    refugio=Refugio.objects.all()
    masc=Mascota.objects.all()

    variables={
        'raza':raza,
        'origen':origen,
        'refugio':refugio,
        'masc':masc

    }


    if request.POST:
        mascota=Mascota()
        mascota.nombre=request.POST.get('txtNombre')
        mascota.esterilizado=request.POST.get('cboEsterilizado')
        mascota.chip=request.POST.get('cboChip')
        mascota.fec_nac=request.POST.get('txtNacimiento')
        
        #agregamos la imagen
        mascota.imagen = request.FILES.get('txtImagen')

        raza=Raza()
        raza.id=int(request.POST.get('cboRaza'))
        mascota.id_raza=raza



        origen=Origen_mascota()
        origen.id=int(request.POST.get('cboOrigen'))
        mascota.id_orig_masc=origen


        refugio=Refugio()
        refugio.id=int(request.POST.get('cboRefugio'))
        mascota.cod_refugio=refugio

        usuario=Usuario()
        usuario.rut_usuario=request.POST.get('txtRut')
        mascota.rut_usuario=usuario


        try:
            mascota.save()
            messages.success(request, "Se registro la mascota")
        except Exception as a:
            messages.error(request, "Error al registrar Mascota" + str(a))


        #tipoUsuario=Tipo_usuario()
        #tipoUsuario.id=int(request.POST.get('cboUser'))
        #usuario.id_usuario=tipoUsuario
        




    return render(request,'core/registroMascotas.html',variables)

@login_required
def eliminarMascota(request, id):

    #para eliminar es necesario primero buscar el automovil
    mascota = Mascota.objects.get(id=id)

    #una vez encontrado el automovil se procede a eliminarlo
    try:
        mascota.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje ="No se ha podido eliminar"
        messages.error(request, mensaje)
        
    #el redirect lo redirige por alias de una ruta
    return redirect(to="registroMascotas")

@login_required
def modificarMascota(request, id):
    mascota= Mascota.objects.all()
    mascBus= Mascota.objects.get(id=id)
    raza=Raza.objects.all()
    origen= Origen_mascota.objects.all()
    refugio= Refugio.objects.all()
    usuario= Usuario.objects.all()

    variables={
        'masc':mascota,
        'mb':mascBus,
        'raza':raza,
        'origen':origen,
        'refugio':refugio,
        'user':usuario
    }

    if request.POST:
        pet=Mascota()
        pet.id=request.POST.get('txtId')
        pet.nombre=request.POST.get('txtNombre')
        pet.esterilizado=request.POST.get('cboEsterilizado')
        pet.chip=request.POST.get('cboChip')
        pet.fec_nac=request.POST.get('txtNacimiento')
        
        #agregamos la imagen
        pet.imagen = request.FILES.get('txtImagen')

        raza=Raza()
        raza.id=int(request.POST.get('cboRaza'))
        pet.id_raza=raza



        origen=Origen_mascota()
        origen.id=int(request.POST.get('cboOrigen'))
        pet.id_orig_masc=origen


        refugio=Refugio()
        refugio.id=int(request.POST.get('cboRefugio'))
        pet.cod_refugio=refugio
        
        pet.rut_usuario=request.POST.get('txtRut')


        try:
            pet.save()
            messages.success(request, "Se registro la mascota")
        except Exception as a:
            messages.error(request, "Error al registrar Mascota" + str(a))
        return redirect(to="registroMascotas")

    return render(request,'core/modificarMascota.html',variables)