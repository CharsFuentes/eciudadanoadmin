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
            return redirect('formulario') # Cambiado a la URL completa
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