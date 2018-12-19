# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.template import RequestContext
from marcadores.forms import *
from marcadores.models import *

def pagina_guardar_marcador(request):
    if request.method == 'Post':
        form = GuardarMarcadorFormulario(request.POST)
        if form.is_valid():
            #Crear o coger Link
            link, dummy = Link.objects.get_or_create(
                url = form.clean_data['url']
            )
            #Crear o coger marcador
            marcador, creado = Marcadores.objects.get_or_create(
                usuario = request.user,
                link = link
            )

            #Actualizar
            marcador.titulo = form.clean_data['titulo']
            
            #Si un marcador ha sido actualizado, limpiar el antiguo y listarlo
            if not creado:
                marcador.tag_set.add(tag)
            
            #Crear un nuevo tag
            tag_nombres = form.clean_data['tags'].split()
            for tag_nombre in tag_nombres:
                tag, dummy = Tag.objects.get_or_create(nombre=tag_nombre)
                marcador.tag_set.add(tag)

            #Guardar marcador en la bd
            marcador.save()
            return HttpResponseRedirect(
                '/usuario/%s' % request.user.username
            )
        else:
            form = GuardarMarcadorFormulario()
            variables = RequestContext(request,{
                'form' : form
            })
        return render_to_response('registration/guardar_marcador.html',variables)




def pagina_principal(request):
    return render_to_response('marcadores/pagina_principal.html', RequestContext(request)
)

def pagina_usuario(request, nombreusuario):
    try:
        usuario = User.objects.get(username=nombreusuario)
    except:
        raise Http404('Respuesta de usuario no encontrada')
    marcadores = usuario.marcadores_set.all()
    variables = RequestContext(request, {
        'nombreusuario': nombreusuario,
        'marcadores':marcadores
    })
    return render_to_response('marcadores/pagina_usuario.html', variables)

def pagina_logout(request):
  logout(request)
  return HttpResponseRedirect('/registro/exitoso')

def pagina_registro(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.clean_data['username'],
                password=form.clean_data['password1'],
                email=form.clean_data['email']
        )
        return HttpResponseRedirect('/registro/exitoso')
    else:
        form = RegistroFormulario()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
        'registration/pagina_registro.html', 
        variables
    )