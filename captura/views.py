#encoding:utf-8

# Create your views here.

from captura.models import *
from captura.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import time
import simplejson as json

def GuardaTratamientos(tx, folio):
	tx = json.loads(tx)
	for item in tx:
		farma = TxCompleto()
		farma.folio = folio
		farma.tratamiento = item['tx']
		farma.meses = item['temp']
		farma.dosis = item['dosis']
		farma.ciclo = item['ciclo']
		farma.intervalos = item['inter']
		farma.ciclos = item['ciclos']
		farma.cateterismo = item['cateter']
		farma.save()
	pass

		

# Vista principal
@csrf_protect
def Main(request):
	template = 'inicio.html'
	reultado = {}

	if request.method=='POST':
		username = request.POST['usuario']
		password = request.POST['password']
		ip = request.META.get('REMOTE_ADDR')
		user = auth.authenticate(username=username, password=password)

		if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
			auth.login(request, user)
			# Redirect to a success page.
			#resultado = {'estado':'correcto','mensaje':'Su registro fue correcto'}
			#Guarda entrada
			fecha = time.strftime("%d/%m/%Y")
			hora = time.strftime("%H:%M:%S")

			resultado = {'estado':'correcto','mensaje':'Entrada registrada'} 
			a = RegEnt()
			a.usuario = username
			a.fecha_registro = fecha
			a.hora_registro = hora
			a.ip = ip
			a.tipo_registro = 'entrada'
			a.save()

			return HttpResponseRedirect('/menu')
		else:
		# Show an error page
			resultado = {'estado':'incorrecto','mensaje':'Sus datos no coinciden favor de verificarlos'}
			return render_to_response(template, resultado, context_instance=RequestContext(request))

	return render_to_response(template, context_instance=RequestContext(request))

@login_required(login_url='/')
def Menu(request):
	template = 'menu.html'
	return render_to_response(template, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapEntrev(request):
	template = 'formsEntre.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmEntrevistado(request.POST)
		if formulario.is_valid():
			formulario.save()
			request.session["folio"] = request.POST['folio']
			msg = 'true'
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmEntrevistado()
	resultado = {'form':formulario, 'msg':msg}
	print msg
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapSelec(request):
	template = 'formsSeleccion.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmSeleccion(request.POST)
		if formulario.is_valid():
			formulario.save()
			request.session["folio"] = request.POST['folio']
			msg = 'true'
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmSeleccion()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapControl(request):
	template = 'forms1.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmControl(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmControl()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapGenerales(request):
	template = 'formsGenerales.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmGenerales(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmGenerales()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapSintomas(request):
	template = 'forms3.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmSintomas(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmSintomas()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapComorb(request):
	template = 'forms4.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmComorbilidades(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmComorbilidades()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapEspe(request):
	template = 'forms5.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmEspecialista(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmEspecialista()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapHosp(request):
	template = 'forms6.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmHospitalizacion(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmHospitalizacion()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapLab(request):
	template = 'forms7.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmLaboratorio(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmLaboratorio()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapInter(request):
	template = 'forms8.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmIntervenciones(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmIntervenciones()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))

@login_required(login_url='/')
def CapTx(request):
	template = 'forms9.html'
	msg = 'false'
	if request.method=='POST':
		# print request.POST['valores']
		formulario = FrmTratamiento(request.POST)
		GuardaTratamientos(request.POST['valores'], request.POST['folio'])
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmTratamiento()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))


@login_required(login_url='/')
def CapComorbTx(request):
	template = 'forms10.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmComorbilidadesTx(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmComorbilidadesTx()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))


@login_required(login_url='/')
def CapComp(request):
	template = 'forms11.html'
	msg = 'false'
	if request.method=='POST':
		formulario = FrmComplicaciones(request.POST)
		if formulario.is_valid():
			formulario.save()
			msg = 'true'
			request.session["folio"] = request.POST['folio']
			return render_to_response(template, resultado, context_instance=RequestContext(request))
	else:
		formulario = FrmComplicaciones()
	resultado = {'form':formulario, 'msg':msg}
	return render_to_response(template, resultado, context_instance=RequestContext(request))