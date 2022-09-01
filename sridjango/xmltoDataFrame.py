from hashlib import new
import xml.etree.cElementTree as ET
import xml.etree.ElementTree as ElementTree
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import listar
import time

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


    
    #num_mes = Mes
substring = ".xml"
array_final = listar.ls_method()
list_disctionary = []
for doc in array_final:
    if substring in doc:
        RUTA = "enero_2021\\"+doc
        print(RUTA)
        tree = ET.parse(RUTA)
        root = tree.getroot()

        dictionary_xml = {

        }
        ####infoTributaria####
        for child in root.findall("comprobante"):
            cdatatext = child.text
            root_xml_cdata = ET.fromstring(cdatatext)

        for list_head in root_xml_cdata.findall('infoTributaria'):
            try:
                Ambiente = list_head.find('ambiente').text
            except:
                Ambiente = ''
                pass
            try:    
                TipoEmision = list_head.find('tipoEmision').text
            except:
                TipoEmision = ''
                pass
            try:    
                razon_social = list_head.find('razonSocial').text
            except:
                razon_social = ''
                pass
            try:
                nombre_comercial = list_head.find('nombreComercial').text
            except:
                nombre_comercial = ''
                pass
            try:
                Ruc = list_head.find('ruc').text
            except:
                Ruc = ''
                pass
            try:
                clave_acceso = list_head.find('claveAcceso').text
            except:
                clave_acceso = ''
                pass
            try:    
                cod_doc = list_head.find('codDoc').text
            except:
                cod_doc = ''
                pass
            try:
                Estab = list_head.find('estab').text
            except:
                Estab = ''
                pass
            try:
                pto_emi = list_head.find('ptoEmi').text
            except:
                pto_emi = ''
                pass
            try:
                Secuencial = list_head.find('secuencial').text
            except:
                Secuencial = ''
                pass
            try:
                dir_matriz = list_head.find('dirMatriz').text    
            except:
                dir_matriz = ''
                pass
            dictionary_xml['ambiente'] = Ambiente
            dictionary_xml['tipo_emision'] = TipoEmision
            dictionary_xml['razon_social'] = razon_social
            dictionary_xml['nombre_comercial'] = nombre_comercial
            dictionary_xml['ruc'] = Ruc
            dictionary_xml['clave_acceso'] = clave_acceso
            dictionary_xml['cod_documento'] = cod_doc
            dictionary_xml['establecimiento'] = Estab
            dictionary_xml['pto_emision'] = pto_emi
            dictionary_xml['secuencial'] = Secuencial
            dictionary_xml['dir_matriz'] = dir_matriz
        for list_head in root_xml_cdata.findall('infoCompRetencion'):
            try:
                Fecha_Emision = list_head.find('fechaEmision').text
            except:
                Fecha_Emision = ''
                pass
            try:    
                dir_establecimiento =list_head.find('dirEstablecimiento').text
            except:
                dir_establecimiento = ''
                pass
            try:
                contribuyente_especial = list_head.find('contribuyenteEspecial').text
            except:
                contribuyente_especial = ''
                pass
            try:
                obligado_contabilidad = list_head.find('obligadoContabilidad').text
            except:
                obligado_contabilidad = ''
                pass
            try:
                tipo_Identificacion_Sujeto_Retenido = list_head.find('tipoIdentificacionSujetoRetenido').text
            except:
                tipo_Identificacion_Sujeto_Retenido = ''
                pass
            try:
                razon_Social_Sujeto_Retenido = list_head.find('razonSocialSujetoRetenido').text
            except:
                razon_Social_Sujeto_Retenido = ''
                pass
            try:
                identificacion_Sujeto_Retenido = list_head.find('identificacionSujetoRetenido').text
            except:
                identificacion_Sujeto_Retenido = ''
                pass
            try:
                periodo_Fiscal = list_head.find('periodoFiscal').text
            except:
                periodo_Fiscal = ''
                pass
            dictionary_xml['fecha_emision'] = Fecha_Emision
            dictionary_xml['dir_establecimiento'] = dir_establecimiento
            dictionary_xml['contribuyente_especial'] = contribuyente_especial
            dictionary_xml['obligado_contabilidad'] = obligado_contabilidad
            dictionary_xml['tipo_identificacion_sujeto_retenido'] = tipo_Identificacion_Sujeto_Retenido
            dictionary_xml['razon_social_sujeto_retenido'] = razon_Social_Sujeto_Retenido
            dictionary_xml['identificacion_sujeto_retenido'] = identificacion_Sujeto_Retenido
            dictionary_xml['periodo_fiscal'] = periodo_Fiscal
        for impuestos_xml in root_xml_cdata.findall('impuestos'):
            for obj_dt in impuestos_xml:
                try:
                    codig_imp=obj_dt.find('codigo').text
                except:
                    codig_imp=''
                    pass
                try:
                    codigo_retencio_imp = obj_dt.find('codigoRetencion').text
                except:
                    codigo_retencio_imp = ''
                    pass
                try:
                    base_Imp_imp = obj_dt.find('baseImponible').text
                except:
                    base_Imp_imp = ''
                    pass
                try:
                    porcentaje_retener_imp = obj_dt.find('porcentajeRetener').text
                except:
                    porcentaje_retener_imp = ''
                    pass
                try:
                    valor_retenido_imp = obj_dt.find('valorRetenido').text
                except:
                    valor_retenido_imp = ''
                    pass
                try:
                    cod_doc_sustento_imp = obj_dt.find('codDocSustento').text
                except:
                    cod_doc_sustento_imp = ''
                    pass
                try:
                    num_doc_sustento_imp = obj_dt.find('numDocSustento').text
                except:
                    num_doc_sustento_imp = ''
                    pass
                try:
                    fecha_emision_doc_sustento_imp = obj_dt.find('fechaEmisionDocSustento').text
                except:
                    fecha_emision_doc_sustento_imp = ''
                    pass
                #if codig_imp == "1":
                dictionary_xml['codigo'] = codig_imp
                dictionary_xml['codigo_retencion'] = codigo_retencio_imp
                dictionary_xml['base_imponible'] = base_Imp_imp
                dictionary_xml['porcentaje_retener'] = porcentaje_retener_imp
                dictionary_xml['valor_retenido'] = valor_retenido_imp
                dictionary_xml['cod_doc_sustento'] = cod_doc_sustento_imp
                dictionary_xml['num_doc_sustento'] = num_doc_sustento_imp
                dictionary_xml['fecha_emision_doc_sustento'] = fecha_emision_doc_sustento_imp
        
        list_disctionary.append(dictionary_xml)    
df2 = pd.DataFrame(list_disctionary)
df2.head()
df2.to_excel("ArchivoExcel.xlsx", index=False)
#df2.to_csv("ArchivoCSV.csv", index=False)
#df2.to_csv("ArchivoTXT.txt",sep="\t")


    
