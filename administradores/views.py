# administradores/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Usuario ingresado: {username}")
        print(f"Contraseña ingresada: {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "¡Ingreso exitoso! Redirigiendo...")
            print("Error: Credenciales correctas.")
            return redirect('inicio') # Cambiado a la URL completa
        else:
            messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo.")
            print("Error: Credenciales incorrectas.")
    
    return render(request, 'core/login.html')



def formulario_view(request):
    if request.method == 'POST':
        data = request.POST
        # Puedes manejar el almacenamiento de datos aquí (como en una base de datos)
        # Para este ejemplo, simplemente los pasamos a la siguiente vista.
        return render(request, 'administrativas/administrativas.html', {'data': data})

    return render(request, 'administrativas/administrativasform.html')


def notificacion_view(request):
    if request.method == 'POST':
        # Aquí puedes procesar los datos del formulario
        datos = {
            'tipo': request.POST['tipo'],
            'numeroIdentidad': request.POST['numeroIdentidad'],
            'fechaNotificacion': request.POST['fechaNotificacion'],
            'horaNotificacion': request.POST['horaNotificacion'],
            'nombreCompleto': request.POST['nombreCompleto'],
            'domicilio': request.POST['domicilio'],
            'distrito': request.POST['distrito'],
            'numeroDomicilio': request.POST['numeroDomicilio'],
            'giroUso': request.POST['giroUso'],
            'codigoInfraccion': request.POST['codigoInfraccion'],
            'fechaDeteccion': request.POST['fechaDeteccion'],
            'horaDeteccion': request.POST['horaDeteccion'],
            'denominacionInfraccion': request.POST['denominacionInfraccion'],
            'lugarInfraccion': request.POST['lugarInfraccion'],
            'numeroPlaca': request.POST['numeroPlaca'],
            'marca': request.POST['marca'],
            'modelo': request.POST['modelo'],
            'color': request.POST['color'],
            'numeroActa': request.POST['numeroActa'],
            'medidaProvisional': request.POST['medidaProvisional'],
            'baseLegalEspecifica': request.POST['baseLegalEspecifica'],
            'resenaInfraccion': request.POST['resenaInfraccion'],
            'nombreInspector': request.POST['nombreInspector'],
            'dniInspector': request.POST['dniInspector'],
            'firmaInspector': request.POST['firmaInspector'],
            'nombreInfractor': request.POST['nombreInfractor'],
            'dniInfractor': request.POST['dniInfractor'],
            'firmaInfractor': request.POST['firmaInfractor'],
        }
        # Puedes guardar los datos en la base de datos o hacer lo que necesites aquí
        return render(request, 'administrativas/administrativas.html', {'datos': datos})
    
    return render(request, 'administrativas/administrativas.html')

def inicio(request):
    return render(request, 'core/inicio.html' )

def formulario2_view(request):
    if request.method == 'POST':
        data = request.POST
        # Puedes manejar el almacenamiento de datos aquí (como en una base de datos)
        # Para este ejemplo, simplemente los pasamos a la siguiente vista.
        return render(request, 'administrativas/administrativas2.html', {'data': data})

    return render(request, 'administrativas/administrativasform2.html')

def notificacion2_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario POST
        datos = {
            'nombreInfractor': request.POST.get('nombreInfractor', ''),
            'documentoIdentidad': request.POST.get('documentoIdentidad', ''),
            'domicilioInfractor': request.POST.get('domicilioInfractor', ''),
            'inicioMedida': request.POST.get('inicioMedida', ''),
            'lugarMedida': request.POST.get('lugarMedida', ''),
            'fechaMedida': request.POST.get('fechaMedida', ''),
            'resumenHechos': request.POST.get('resumenHechos', ''),
        }
        
        # Pasar los datos a la plantilla 'administrativas2.html'
        return render(request, 'administrativas/administrativas2.html', {'datos': datos})
    
    return render(request, 'administrativas/administrativas2.html')

def formulario3_view(request):
    if request.method == 'POST':
        data = request.POST
        # Puedes manejar el almacenamiento de datos aquí (como en una base de datos)
        # Para este ejemplo, simplemente los pasamos a la siguiente vista.
        return render(request, 'administrativas/administrativas3.html', {'data': data})

    return render(request, 'administrativas/administrativasform3.html')

def notificacion3_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario POST
        datos = {
            'nombreAdmin': request.POST.get('nombreAdmin', ''),
            'domicilioAdmin': request.POST.get('domicilioAdmin', ''),
            'documentoAdmin': request.POST.get('documentoAdmin', ''),
            'constatacion': request.POST.get('constatacion', ''),
            'alegatosAdmin': request.POST.get('alegatosAdmin', ''),
            'nombreConductor': request.POST.get('nombreConductor', ''),
            'dniConductor': request.POST.get('dniConductor', ''),
            'vinculoConductor': request.POST.get('vinculoConductor', ''),
            'nombreInspector': request.POST.get('nombreInspector', ''),
            'dniInspector': request.POST.get('dniInspector', ''),
            'credencialInspector': request.POST.get('credencialInspector', ''),
        }
        
        # Pasar los datos a la plantilla 'acta_fiscalizacion.html'
        return render(request, 'administrativas/administrativas3.html', {'datos': datos})
    
    return render(request, 'administrativas/administrativas3.html')
