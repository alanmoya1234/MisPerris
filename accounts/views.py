from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm

# Create your views here.


def register(request):
    #guardamos el formulario para ser enviado al
    #template
    variables = {
        'form':CustomCreationForm
    }

    if request.POST:
        #le pasamos todos los campos que vienen
        #desde el navegador al formulario
        form = CustomCreationForm(request.POST)

        if form.is_valid():
            #el formulario se encarga de guardar
            #los datos en la BBDD
            form.save()
            variables['mensaje'] = "Usuario creado"
        else:
            variables['mensaje'] = "No se ha registrado el usuario"
            variables['form'] = form

    return render(request, 'accounts/register.html', variables)