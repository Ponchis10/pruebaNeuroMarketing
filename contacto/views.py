from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre  = request.POST.get('nombre')
            asunto  = request.POST.get('asunto')
            email  = request.POST.get('email')
            contenido  = request.POST.get('contenido')

            email = EmailMessage('Mensaje desde app Django {}'.format(asunto), 
            'El usuario con nombre {} con la direccion {} escribe: \n\n {}'.format(nombre, email, contenido),
            '',
            ['apimentel1013@gmail.com'],
            reply_to=[email])
            try:
                email.send()
                return redirect("contacto?valido")
            except:
                return redirect("contacto?novalido")

    
    formulario_contacto = FormularioContacto()
    return render(request, 'contacto/contacto.html', {'miFormulario':formulario_contacto})