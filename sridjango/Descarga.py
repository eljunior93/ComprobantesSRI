from faulthandler import is_enabled
from operator import ne
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException
from datetime import time
from tkinter import * 
import time
import os
import pymysql
import xmltosql
import sqlite3
#0190111881001

conn = sqlite3.connect('claves.db')
c = conn.cursor()
#c.execute('''CREATE TABLE claves(clave_acceso TEXT unique)''')

conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='comprobante_sri'
)
cursor = conn.cursor()

def descargar(ruc, clave, Origen, Tipo, Establecimiento, Mes, Anio, Dia):
    num_mes = Mes
    num_anio = Anio

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

    #############LEVANTA EL NAVEGADOR###########
    options = Options()
    path = os.path.join('Comprobantes', json_directorios[num_mes])
    try:
        os.mkdir(path)
    except:
        pass
    preferences = {"download.default_directory": 'D:\\Users\\defaultuser0\\Documents\\Validez_Comprobantes\\'+ 
                            json_directorios[num_mes], # pass the variable
                   "download.prompt_for_download": False,
                   "directory_upgrade": True,
                   "safebrowsing.enabled": 'false' }
    options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=options)
    driver.get("https://srienlinea.sri.gob.ec/tuportal-internet/accederAplicacion.jspa?redireccion=60&idGrupo=58")

    ruc = str(ruc)
    clave = clave
    Origen = Origen
    Tipo = Tipo
    Establecimiento = Establecimiento

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
    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbTipoComprobante"]').send_keys(Tipo)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbEstablecimiento"]').send_keys(Establecimiento)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:cmbProcesos"]').send_keys(Origen)

    len_for = json_mes_num_dias['01']
    len_for = int(len_for) + 1
    i = Dia
    for i in range(int(Dia), int(len_for)):
        
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
            time.sleep(40)
            for j in range(0, 49 + 1):
                try:
                    driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(j) +':lnkXml"]').click()
                    time.sleep(50/1000)
                    clave_acceso = driver.find_element(By.XPATH, '//*[@id="frmPrincipal:tablaCompRecibidos:'+str(j)+':j_idt108"]').text
                    clave_acceso = [numero_auto.text for numero_auto in clave_acceso]
                    c.execute('''INSERT INTO claves VALUES(?)''',(clave_acceso))
                    conn.commit()
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
        xmltosql.xmlTosql(Mes)
        

