from django.db import models

# Create your models here.

list_origen = [
    ('Comprobantes emitidos por el contribuyente', 'Comprobantes emitidos por el contribuyente'),
    ('Comprobantes recibidos por el contribuyente', 'Comprobantes recibidos por el contribuyente')
]

list_tipo = [
    ('Factura', 'Factura'),
    ('Liquidación de compra de bienes y prestación de servicios', 'Liquidación de compra de bienes y prestación de servicios'),
    ('Notas de Crédito', 'Notas de Crédito'),
    ('Notas de Débito', 'Notas de Débito'),
    ('Guías de Remisión', 'Guías de Remisión'),
    ('Comprobante de Retención', 'Comprobante de Retención')
]

list_establecimiento = [
    ('Todos', 'Todos'),
    ('001', '001'),
    ('002', '002'),
    ('003', '003')
]

list_dia = [
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31')
]

list_mes = [
    ('01', 'Enero'),
    ('02', 'Febrero'),
    ('03', 'Marzo'),
    ('04', 'Abril'),
    ('05', 'Mayo'),
    ('06', 'Junio'),
    ('07', 'Julio'),
    ('08', 'Agosto'),
    ('09', 'Septiembre'),
    ('10', 'Octubre'),
    ('11', 'Noviembre'),
    ('12', 'Diciembre')
]

list_anio = [
    ('2022', '2022'),
    ('2021', '2021'),
    ('2020', '2020'),
    ('2019', '2019'),
    ('2018', '2018'),
    ('2017', '2017'),
    ('2016', '2016'),
    ('2015', '2015')
]

class Nombre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Datos(models.Model):
    ruc = models.TextField()
    clave = models.TextField()
    origen = models.TextField(
        null=False, blank=False,
        choices=list_origen,
        default='Comprobantes recibidos por el contribuyente'
    )
    tipo = models.TextField(
        null=False, blank=False,
        choices=list_tipo,
        default='Comprobante de Retención'
    )
    establecimiento = models.TextField(
        null=False, blank=False,
        choices=list_establecimiento,
        default='Todos'
    )
    dia = models.TextField(
        null=False, blank=False,
        choices=list_dia
    )
    mes = models.TextField(
        null=False, blank=False,
        choices=list_mes
    )
    anio = models.TextField(
        null=False, blank=False,
        choices=list_anio
    )