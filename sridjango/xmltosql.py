from hashlib import new
import xml.etree.cElementTree as ET
from sqlalchemy.types import VARCHAR
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

def xmlTosql():
    
    substring = ".xml"
    array_final = listar.ls_method()
    list_disctionary = []
    list_diccionario = []
    list_dicci = []
    for doc in array_final:
        if substring in doc:
            RUTA = "D:\\Users\\defaultuser0\\Desktop\\sriDjango\\sridjango\\Comprobantes\\"+doc
            print(RUTA)
            tree = ET.parse(RUTA)
            root = tree.getroot()

            dictionary_xml = {

            }

            diccionario_xml = {

            }
            dicci_xml = {

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
                dictionary_xml['Ambiente'] = Ambiente
                dictionary_xml['Tipo_Emision'] = TipoEmision
                dictionary_xml['Razon_Social'] = razon_social
                dictionary_xml['Nombre_Comercial'] = nombre_comercial
                dictionary_xml['RUC'] = Ruc
                dictionary_xml['Clave_Acceso'] = clave_acceso
                dictionary_xml['Cod_Documento'] = cod_doc
                dictionary_xml['Establecimiento'] = Estab
                dictionary_xml['Pto_Emision'] = pto_emi
                dictionary_xml['Secuencial'] = Secuencial
                dictionary_xml['Dir_Matriz'] = dir_matriz
        ####infoCompRetencion####
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
                dictionary_xml['Fecha_Emision'] = Fecha_Emision
                dictionary_xml['Dir_Establecimiento'] = dir_establecimiento
                dictionary_xml['Contribuyente_Especial'] = contribuyente_especial
                dictionary_xml['Obligado_Contabilidad'] = obligado_contabilidad
                dictionary_xml['Tipo_Identificacion_Sujeto_Retenido'] = tipo_Identificacion_Sujeto_Retenido
                dictionary_xml['Razon_Social_Sujeto_Retenido'] = razon_Social_Sujeto_Retenido
                dictionary_xml['Identificacion_Sujeto_Retenido'] = identificacion_Sujeto_Retenido
                dictionary_xml['Periodo_Fiscal'] = periodo_Fiscal

            for sustento_xml in root_xml_cdata.findall('docsSustento'):
                for obj_dt2 in sustento_xml:
                    try:
                        cod_sustento=obj_dt2.find('codSustento').text
                    except:
                        cod_sustento=''
                        pass
                    try:
                        cod_doc_sustento=obj_dt2.find('codDocSustento').text
                    except:
                        cod_doc_sustento=''
                        pass
                    try:
                        num_doc_sustento=obj_dt2.find('numDocSustento').text
                    except:
                        num_doc_sustento=''
                        pass
                    try:
                        fecha_emision_doc_sustento=obj_dt2.find('fechaEmisionDocSustento').text
                    except:
                        fecha_emision_doc_sustento=''
                        pass
                    try:
                        fecha_registro_contable=obj_dt2.find('fechaRegistroContable').text
                    except:
                        fecha_registro_contable=''
                        pass
                    try:
                        num_aut_doc_sustento=obj_dt2.find('numAutDocSustento').text
                    except:
                        num_aut_doc_sustento=''
                        pass
                    try:
                        pago_loc_ext=obj_dt2.find('pagoLocExt').text
                    except:
                        pago_loc_ext=''
                        pass
                    try:
                        total_sin_impuestos=obj_dt2.find('totalSinImpuestos').text
                    except:
                        total_sin_impuestos=''
                        pass
                    try:
                        importe_total=obj_dt2.find('importeTotal').text
                    except:
                        importe_total=''
                        pass
                    # dictionary_xml['codSustento'] = cod_sustento
                    # dictionary_xml['codDocSustento'] = cod_doc_sustento
                    # dictionary_xml['numDocSustento'] = num_doc_sustento
                    # dictionary_xml['fechaEmisionDocSustento'] = fecha_emision_doc_sustento
                    # dictionary_xml['numAutDocSustento'] = num_aut_doc_sustento
                    # dictionary_xml['pagoLocExt'] = pago_loc_ext
                    # dictionary_xml['totalSinImpuestos'] = total_sin_impuestos
                    # dictionary_xml['importeTotal'] = importe_total
                
                    try:
                        cod_impuesto_doc_sustento=obj_dt2.find('impuestosDocSustento').find('impuestoDocSustento').find('codImpuestoDocSustento').text
                    except:
                        cod_impuesto_doc_sustento=''
                        pass
                    try:
                        codigo_porcentaje=obj_dt2.find('impuestosDocSustento').find('impuestoDocSustento').find('codigoPorcentaje').text
                    except:
                        codigo_porcentaje=''
                        pass
                    try:
                        base_imponible=obj_dt2.find('impuestosDocSustento').find('impuestoDocSustento').find('baseImponible').text
                    except:
                        base_imponible=''
                        pass
                    try:
                        tarifa=obj_dt2.find('impuestosDocSustento').find('impuestoDocSustento').find('tarifa').text
                    except:
                        tarifa=''
                        pass
                    try:
                        valor_impuesto=obj_dt2.find('impuestosDocSustento').find('impuestoDocSustento').find('valorImpuesto').text
                    except:
                        valor_impuesto=''
                        pass
                    # dictionary_xml['codImpuestoDocSustento'] = cod_impuesto_doc_sustento
                    # dictionary_xml['codigoPorcentaje'] = codigo_porcentaje
                    # dictionary_xml['baseImponible'] = base_imponible
                    # dictionary_xml['tarifa'] = tarifa
                    # dictionary_xml['valorImpuesto'] = valor_impuesto
                
                    try:
                        forma_pago=obj_dt2.find('pagos').find('pago').find('formaPago').text
                    except:
                        forma_pago=''
                        pass
                    try:
                        Total=obj_dt2.find('pagos').find('pago').find('total').text
                    except:
                        Total=''
                        pass
                    dictionary_xml['formaPago'] = forma_pago
                    dictionary_xml['total'] = Total

                    for obj_ret in sustento_xml.iter('retencion'):
                        try:
                            Codigo=obj_ret.find('codigo').text
                        except:
                            Codigo=''
                            pass
                        try:
                            Codigo_Retencion=obj_ret.find('codigoRetencion').text
                        except:
                            Codigo_Retencion=''
                            pass
                        try:
                            Base_Imponible=obj_ret.find('baseImponible').text
                        except:
                            Base_Imponible=''
                            pass
                        try:
                            Porcentaje_Retener=obj_ret.find('porcentajeRetener').text
                        except:
                            Porcentaje_Retener=''
                            pass
                        try:
                            Valor_Retenido=obj_ret.find('valorRetenido').text
                        except:
                            Valor_Retenido=''
                            pass
                        if Codigo == "1":
                            dictionary_xml['Codigo'] = Codigo
                            dictionary_xml['Codigo_Retencion'] = Codigo_Retencion
                            dictionary_xml['Base_Imponible'] = Base_Imponible
                            dictionary_xml['Porcentaje_Retener'] = Porcentaje_Retener
                            dictionary_xml['Valor_Retenido'] = Valor_Retenido
                        elif Codigo == "2":
                            diccionario_xml['Codigo_2'] = Codigo
                            diccionario_xml['Codigo_Retencion_2'] = Codigo_Retencion
                            diccionario_xml['Base_Imponible_2'] = Base_Imponible
                            diccionario_xml['Porcentaje_Retener_2'] = Porcentaje_Retener
                            diccionario_xml['Valor_Retenido_2'] = Valor_Retenido

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
                    if codig_imp == "1":
                        dictionary_xml['Codigo'] = codig_imp
                        dictionary_xml['Codigo_Retencion'] = codigo_retencio_imp
                        dictionary_xml['Base_Imponible'] = base_Imp_imp
                        dictionary_xml['Porcentaje_Retener'] = porcentaje_retener_imp
                        dictionary_xml['Valor_Retenido'] = valor_retenido_imp
                        dictionary_xml['Cod_Doc_Sustento'] = cod_doc_sustento_imp
                        dictionary_xml['Num_Doc_Sustento'] = num_doc_sustento_imp
                        dictionary_xml['Fecha_Emision_Doc_Sustento'] = fecha_emision_doc_sustento_imp
                    
            for impuestos_xml2 in root_xml_cdata.findall('impuestos'):
                for obj_dt2 in impuestos_xml2:
                    try:
                        codig_imp2=obj_dt2.find('codigo').text
                    except:
                        codig_imp2=''
                        pass
                    try:
                        codigo_retencio_imp2 = obj_dt2.find('codigoRetencion').text
                    except:
                        codigo_retencio_imp2 = ''
                        pass
                    try:
                        base_Imp_imp2 = obj_dt2.find('baseImponible').text
                    except:
                        base_Imp_imp2 = ''
                        pass
                    try:
                        porcentaje_retener_imp2 = obj_dt2.find('porcentajeRetener').text
                    except:
                        porcentaje_retener_imp2 = ''
                        pass
                    try:
                        valor_retenido_imp2 = obj_dt2.find('valorRetenido').text
                    except:
                        valor_retenido_imp2 = ''
                        pass
                    try:
                        cod_doc_sustento_imp2 = obj_dt2.find('codDocSustento').text
                    except:
                        cod_doc_sustento_imp2 = ''
                        pass
                    try:
                        num_doc_sustento_imp2 = obj_dt2.find('numDocSustento').text
                    except:
                        num_doc_sustento_imp2 = ''
                        pass
                    try:
                        fecha_emision_doc_sustento_imp2 = obj_dt2.find('fechaEmisionDocSustento').text
                    except:
                        fecha_emision_doc_sustento_imp2 = ''
                        pass
                    if codig_imp2 == "2":
                        diccionario_xml['Codigo_2'] = codig_imp2
                        diccionario_xml['Codigo_Retencion_2'] = codigo_retencio_imp2
                        diccionario_xml['Base_Imponible_2'] = base_Imp_imp2
                        diccionario_xml['Porcentaje_Retener_2'] = porcentaje_retener_imp2
                        diccionario_xml['Valor_Retenido_2'] = valor_retenido_imp2
                        diccionario_xml['Cod_Doc_Sustento_2'] = cod_doc_sustento_imp2
                        diccionario_xml['Num_Doc_Sustento_2'] = num_doc_sustento_imp2
                        diccionario_xml['Fecha_Emision_Doc_Sustento_2'] = fecha_emision_doc_sustento_imp2
                    else:
                        pass
        
            for impuestos_xml6 in root_xml_cdata.findall('impuestos'):
                for obj_dt6 in impuestos_xml6:
                    try:
                        codig_imp6=obj_dt6.find('codigo').text
                    except:
                        codig_imp6=''
                        pass
                    try:
                        codigo_retencio_imp6 = obj_dt6.find('codigoRetencion').text
                    except:
                        codigo_retencio_imp6 = ''
                        pass
                    try:
                        base_Imp_imp6 = obj_dt6.find('baseImponible').text
                    except:
                        base_Imp_imp6 = ''
                        pass
                    try:
                        porcentaje_retener_imp6 = obj_dt6.find('porcentajeRetener').text
                    except:
                        porcentaje_retener_imp6 = ''
                        pass
                    try:
                        valor_retenido_imp6 = obj_dt6.find('valorRetenido').text
                    except:
                        valor_retenido_imp6 = ''
                        pass
                    try:
                        cod_doc_sustento_imp6 = obj_dt6.find('codDocSustento').text
                    except:
                        cod_doc_sustento_imp6 = ''
                        pass
                    try:
                        num_doc_sustento_imp6 = obj_dt6.find('numDocSustento').text
                    except:
                        num_doc_sustento_imp6 = ''
                        pass
                    try:
                        fecha_emision_doc_sustento_imp6 = obj_dt6.find('fechaEmisionDocSustento').text
                    except:
                        fecha_emision_doc_sustento_imp6 = ''
                        pass
                    if codig_imp6 == "6":
                        dicci_xml['Codigo_6'] = codig_imp6
                        dicci_xml['Codigo_Retencion_6'] = codigo_retencio_imp6
                        dicci_xml['Base_Imponible_6'] = base_Imp_imp6
                        dicci_xml['Porcentaje_Retener_6'] = porcentaje_retener_imp6
                        dicci_xml['Valor_Retenido_6'] = valor_retenido_imp6
                        dicci_xml['Cod_Doc_Sustento_6'] = cod_doc_sustento_imp6
                        dicci_xml['Num_Doc_Sustento_6'] = num_doc_sustento_imp6
                        dicci_xml['Fecha_Emision_Doc_Sustento_6'] = fecha_emision_doc_sustento_imp6
                    else:
                        pass

            list_disctionary.append(dictionary_xml)
            list_diccionario.append(diccionario_xml)
            list_dicci.append(dicci_xml)

    df = pd.DataFrame(list_diccionario)
    df2 = pd.DataFrame(list_disctionary)
    df3 = pd.DataFrame(list_dicci)
    df_final = pd.concat([df2, df, df3], axis=1)
    print(df_final)

    cadena_conexion = 'mysql+pymysql://root@localhost:3306/comprobante_sri'
    conexion = create_engine(cadena_conexion)
    df_final.reset_index()
    df_final.to_sql(name='comprobantes', if_exists='replace', con=conexion, dtype={'clave_acceso': sqlalchemy.types.NVARCHAR(length=255)})

    # with conexion.connect() as con:
    #     con.execute('ALTER TABLE comprobantes'+json_directorios[num_mes]+' ADD PRIMARY KEY (clave_acceso);')

