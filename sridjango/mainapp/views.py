from multiprocessing import context
from django.shortcuts import HttpResponse
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib import messages
from .forms import *
from faulthandler import is_enabled
from operator import ne
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException
from datetime import time
from tkinter import * 
from hashlib import new
import time
import os
import pymysql
import xmltosql


# Create your views here.

def index(request):
    template_name = 'datos_admin.html'

    if request.method =="POST":
        print('Aqui')
        form = DatosForm(request.POST or None)
        errors = None

        if form.is_valid():
            Datos.objects.create(
                ruc = form.cleaned_data.get('ruc'),
                clave = form.cleaned_data.get('clave'),
                origen =form.cleaned_data.get('origen'),
                tipo = form.cleaned_data.get('tipo'),
                establecimiento = form.cleaned_data.get('establecimiento'),
                dia = form.cleaned_data.get('dia'),
                mes = form.cleaned_data.get('mes'),
                anio = form.cleaned_data.get('anio')
            )

            return HttpResponseRedirect("/s/")

        if form.errors:
            errors = form.errors

        return render(request, template_name, {'form':form})

    else:
        form = DatosForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, template_name, {'form':form})
    # nombre_list = Nombre.objects.all()
    # context = {
    #     'nombre_list': nombre_list
    # }
    return render(request, 'index.html',context)

def add_nombre(request):
    if request.method=="POST":
        name = request.POST['name']
        description = request.POST['description']
        nombre = Nombre(name = name, description = description)
        nombre.save()
        messages.info(request, "Nombre Agregado")
    else:
        pass

    nombre_list = Nombre.objects.all()
    context = {
        'nombre_list': nombre_list
    }

    return render(request, 'index.html', context)

def delete_nombre(request,myid):
    nombre = Nombre.objects.get(id = myid)
    nombre.delete()
    messages.info(request,"Nombre Borrado")
    return redirect(index)

def edit_nombre(request,myid):
    sel_nombre = Nombre.objects.get(id = myid)
    nombre_list = Nombre.objects.all()
    context = {
        'sel_nombre': sel_nombre,
        'nombre_list': nombre_list
    }
    return render(request, 'index.html', context)

# def datos_admin(request):
#     template_name = 'datos_admin.html'

#     if request.method =="POST":
#         print('Aqui')
#         form = DatosForm(request.POST or None)
#         errors = None

#         if form.is_valid():
#             Datos.objects.create(
#                 ruc = form.cleaned_data.get('ruc'),
#                 clave = form.cleaned_data.get('clave'),
#                 origen =form.cleaned_data.get('origen'),
#                 tipo = form.cleaned_data.get('tipo'),
#                 establecimiento = form.cleaned_data.get('establecimiento'),
#                 dia = form.cleaned_data.get('dia'),
#                 mes = form.cleaned_data.get('mes'),
#                 anio = form.cleaned_data.get('anio')
#             )

#             return HttpResponseRedirect("/s/")

#         if form.errors:
#             errors = form.errors

#         return render(request, template_name, {'form':form})

#     else:
#         form = DatosForm()
#         if 'submitted' in request.GET:
#             submitted = True
#         return render(request, template_name, {'form':form})

def update_nombre(request,myid):
    nombre = Nombre.objects.get(id = myid)
    nombre.name = request.POST['name']
    nombre.description = request.POST['description']
    nombre.save()
    messages.info(request,"Nombre Actualizado")
    return redirect('index')


###Conexion BD###

def conectar():

    conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='comprobante_sri'
    )
    print("Conexion Exitosa")
    info_server=conn.get_server_info()
    cursor = conn.cursor()
    cursor.execute("show databases")

    row = cursor.fetchone()
    print("Conectado a la base de datos: {}".format(row))


###Descarga SRI###

@csrf_exempt
def descargar(request):
    if request.method=="POST":
        ruc = request.POST['ruc']
        clave = request.POST['clave']
        origen = request.POST['origen']
        tipo = request.POST['tipo']
        establecimiento = request.POST['establecimiento']
        dia = request.POST['dia']
        mes = request.POST['mes']
        anio = request.POST['anio']
        datos = Datos(ruc = ruc, clave = clave, origen = origen, tipo = tipo, establecimiento = establecimiento, dia = dia, mes = mes, anio = anio)
        datos.save()
        messages.info(request, "Parametros Enviados")
        num_mes = mes
        num_anio = anio

        json_directorios = {
        '01': 'enero',
        '02': 'febrero',
        '03': 'marzo',
        '04': 'abril',
        '05': 'mayo',
        '06': 'junio',
        '07': 'julio',
        '08': 'agosto',
        '09': 'septiembre',
        '10': 'octubre',
        '11': 'noviembre',
        '12': 'diciembre'
    }

    conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='comprobante_sri'
    )
    print("Conexion Exitosa")
    info_server=conn.get_server_info()
    cursor = conn.cursor()
    cursor.execute("show databases")

    row = cursor.fetchone()
    print("Conectado a la base de datos: {}".format(row))

    #############LEVANTA EL NAVEGADOR###########
    options = Options()
    preferences = {"download.default_directory": 'D:\\Users\\defaultuser0\\Desktop\\sriDjango\\sridjango\\Comprobantes', # pass the variable
                   "download.prompt_for_download": False,
                   "directory_upgrade": True,
                   "safebrowsing.enabled": 'false' }
    options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=options)
    driver.get("https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=60&idGrupo=58")

    # ruc = ruc
    # clave = clave
    # Origen = Origen
    # Tipo = Tipo
    # Establecimiento = Establecimiento

    #####INICIA SESION#######

    driver.find_element(By.XPATH, "//input[contains(@id,'usuario')]").send_keys(ruc)
    #print('escribio el ruc')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys(clave)
    #print('escribio la clave')
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[contains(@id,'kc-login')]").click()

    ######INGRESAR A COMPROBANTES######

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="consultaDocumentoForm:panelPrincipal"]/ul/li[2]/a').click()

    #####INGRESO DE DATOS####

    json_mes_num_dias = {
        '01': '31',
        '02': '30',
        '03': '31',
        '04': '30',
        '05': '31',
        '06': '30',
        '07': '31',
        '08': '31',
        '09': '30',
        '10': '31',
        '11': '30',
        '12': '31'
    }

    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbTipoComprobante"]').send_keys(tipo)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbEstablecimiento"]').send_keys(establecimiento)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbProcesos"]').send_keys(origen)

    len_for = json_mes_num_dias['01']
    len_for = int(len_for) + 1
    i = dia
    for i in range(int(dia), int(len_for)):
        
        if len(str(i)) == 0:

            cont = '0'+ str(i)
        else:
            cont = str(i)  
        fecha = cont + '/' + num_mes + '/' + num_anio
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="frmPrincipal:calendarFechaDesde_input"]').clear()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="frmPrincipal:calendarFechaDesde_input"]').send_keys(fecha)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btnRecaptcha"]').click()
        time.sleep(1)
        try:
            time.sleep(20)
            for j in range(0, 49 + 1):
                try:
                    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(j) +':lnkXml"]').click()
                except:
                    break
            next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
            time.sleep(2)
            for i in range(50, 99 + 1):
                try:
                    button = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(i) +':lnkXml"]')
                    webdriver.ActionChains(driver).move_to_element(button).click(button).perform()  
                except:
                    break
            next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
            time.sleep(2)
            for t in range(100, 149 + 1):
                try:
                    button1 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(t) +':lnkXml"]')
                    webdriver.ActionChains(driver).move_to_element(button1).click(button1).perform()
                except:
                    break
            next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
            time.sleep(2)
            for q in range(150, 199 + 1):
                try:
                    button2 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(q) +':lnkXml"]')
                    webdriver.ActionChains(driver).move_to_element(button2).click(button2).perform()
                except:
                    break
            next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
            time.sleep(2)
            for s in range(200, 249 + 1):
                try:
                    button3 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(s) +':lnkXml"]')
                    webdriver.ActionChains(driver).move_to_element(button3).click(button3).perform()
                except:
                    break
            next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
            time.sleep(2)
            for a in range(250, 299 + 1):
                try:
                    button4 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(a) +':lnkXml"]')
                    webdriver.ActionChains(driver).move_to_element(button4).click(button4).perform()
                except:
                    break
            next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
            time.sleep(2)
            for u in range(300, 349 + 1):
                try:
                    button5 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(u) +':lnkXml"]')
                    webdriver.ActionChains(driver).move_to_element(button5).click(button5).perform()
                except:
                    break
            next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
            time.sleep(2)
            for p in range(350, 399 + 1):
                try:
                    button6 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(p) +':lnkXml"]')
                    webdriver.ActionChains(driver).move_to_element(button6).click(button6).perform()
                except:
                    break
            #driver.quit()    
        except:
            continue
        primera_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[1]').click()
        xmltosql.xmlTosql()
    return render(request, 'index.html')
    # else:
    #     pass

    #return render(request, 'index.html', context)

    # num_mes = mes
    # num_anio = anio

    # json_directorios = {
    #     '01': 'enero',
    #     '02': 'febrero',
    #     '03': 'marzo',
    #     '04': 'abril',
    #     '05': 'mayo',
    #     '06': 'junio',
    #     '07': 'julio',
    #     '08': 'agosto',
    #     '09': 'septiembre',
    #     '10': 'octubre',
    #     '11': 'noviembre',
    #     '12': 'diciembre'
    # }

    # #############LEVANTA EL NAVEGADOR###########
    # options = Options()
    # path = os.path.join('Comprobantes', json_directorios[num_mes])
    # try:
    #     os.mkdir(path)
    # except:
    #     pass
    # preferences = {"download.default_directory": 'D:\\Users\\defaultuser0\\Documents\\Validez_Comprobantes\\'+ 
    #                         json_directorios[num_mes], # pass the variable
    #                "download.prompt_for_download": False,
    #                "directory_upgrade": True,
    #                "safebrowsing.enabled": 'false' }
    # options.add_experimental_option("prefs", preferences)

    # driver = webdriver.Chrome(options=options)
    # driver.get("https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=60&idGrupo=58")

    # ruc = ruc
    # clave = clave
    # Origen = Origen
    # Tipo = Tipo
    # Establecimiento = Establecimiento

    # #####INICIA SESION#######

    # driver.find_element(By.XPATH, "//input[contains(@id,'usuario')]").send_keys(ruc)
    # #print('escribio el ruc')
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//input[contains(@id,'password')]").send_keys(clave)
    # #print('escribio la clave')
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//input[contains(@id,'kc-login')]").click()

    # ######INGRESAR A COMPROBANTES######

    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@id="consultaDocumentoForm:panelPrincipal"]/ul/li[2]/a').click()

    # #####INGRESO DE DATOS####

    # json_mes_num_dias = {
    #     '01': '31',
    #     '02': '30',
    #     '03': '31',
    #     '04': '30',
    #     '05': '31',
    #     '06': '30',
    #     '07': '31',
    #     '08': '31',
    #     '09': '30',
    #     '10': '31',
    #     '11': '30',
    #     '12': '31'
    # }

    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbTipoComprobante"]').send_keys(Tipo)
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbEstablecimiento"]').send_keys(Establecimiento)
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbProcesos"]').send_keys(Origen)

    # len_for = json_mes_num_dias['01']
    # len_for = int(len_for) + 1
    # i = dia
    # for i in range(int(dia), int(len_for)):
        
    #     if len(str(i)) == 0:

    #         cont = '0'+ str(i)
    #     else:
    #         cont = str(i)  
    #     fecha = cont + '/' + num_mes + '/' + num_anio
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, '//*[@id="frmPrincipal:calendarFechaDesde_input"]').clear()
    #     time.sleep(1)
    #     driver.find_element(By.XPATH, '//*[@id="frmPrincipal:calendarFechaDesde_input"]').send_keys(fecha)
    #     time.sleep(1)
    #     driver.find_element(By.XPATH, '//*[@id="btnRecaptcha"]').click()
    #     time.sleep(1)
    #     try:
    #         time.sleep(40)
    #         for j in range(0, 49 + 1):
    #             try:
    #                 driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(j) +':lnkXml"]').click()
    #                 time.sleep(50/1000)
    #                 clave_acceso = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(j)+':j_idt108"]').text
    #                 clave_acceso = [numero_auto.text for numero_auto in clave_acceso]
    #                 c.execute('''INSERT INTO claves VALUES(?)''',(clave_acceso))
    #                 conn.commit()
    #             except:
    #                 break
    #         next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
    #         time.sleep(2)
    #         for i in range(50, 99 + 1):
    #             try:
    #                 button = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(i) +':lnkXml"]')
    #                 webdriver.ActionChains(driver).move_to_element(button).click(button).perform()  
    #             except:
    #                 break
    #         next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
    #         time.sleep(2)
    #         for t in range(100, 149 + 1):
    #             try:
    #                 button1 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(t) +':lnkXml"]')
    #                 webdriver.ActionChains(driver).move_to_element(button1).click(button1).perform()
    #             except:
    #                 break
    #         next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
    #         time.sleep(2)
    #         for q in range(150, 199 + 1):
    #             try:
    #                 button2 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(q) +':lnkXml"]')
    #                 webdriver.ActionChains(driver).move_to_element(button2).click(button2).perform()
    #             except:
    #                 break
    #         next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
    #         time.sleep(2)
    #         for s in range(200, 249 + 1):
    #             try:
    #                 button3 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(s) +':lnkXml"]')
    #                 webdriver.ActionChains(driver).move_to_element(button3).click(button3).perform()
    #             except:
    #                 break
    #         next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
    #         time.sleep(2)
    #         for a in range(250, 299 + 1):
    #             try:
    #                 button4 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(a) +':lnkXml"]')
    #                 webdriver.ActionChains(driver).move_to_element(button4).click(button4).perform()
    #             except:
    #                 break
    #         next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
    #         time.sleep(2)
    #         for u in range(300, 349 + 1):
    #             try:
    #                 button5 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(u) +':lnkXml"]')
    #                 webdriver.ActionChains(driver).move_to_element(button5).click(button5).perform()
    #             except:
    #                 break
    #         next_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[4]').click()
    #         time.sleep(2)
    #         for p in range(350, 399 + 1):
    #             try:
    #                 button6 = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(p) +':lnkXml"]')
    #                 webdriver.ActionChains(driver).move_to_element(button6).click(button6).perform()
    #             except:
    #                 break
    #         #driver.quit()    
    #     except:
    #         continue
    #     primera_page = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos_paginator_bottom"]/span[1]').click()
    #     xmltosql.xmlTosql(Mes)
    # return render(request, 'index.html')