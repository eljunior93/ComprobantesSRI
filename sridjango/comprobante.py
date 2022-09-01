from tkinter import *
from tkinter import ttk
import Bajar_Comprobantes_Page1
import conexion

vent = Tk()
vent.title("Descarga Comprobantes")
vent.geometry('490x470+300+200')
vent.configure(bg='#fff')
vent.resizable(False,False)

frame=Frame(vent, width=450,height=460,bg='#fff')
frame.place(x=20,y=20)

lbl1=Label(frame, text='Descarga de Comprobantes', fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',14,'bold'))
lbl1.place(x=100,y=5)

def on_enter(e):
        txtRuc.delete(0, 'end')

def on_leave(e):
    name=txtRuc.get() 
    if name=='':
        txtRuc.insert(0,'Ingrese Ruc')

txtRuc = Entry(frame, width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
txtRuc.place(x=30,y=55)
txtRuc.insert(0, 'Ingrese Ruc')
txtRuc.bind('<FocusIn>', on_enter)
txtRuc.bind('<FocusOut>', on_leave)

Frame(frame, width=275,height=2,bg='black').place(x=25,y=78)

def on_enter(e):
        txtClave.delete(0, 'end')

def on_leave(e):
    name=txtClave.get() 
    if name=='':
        txtClave.insert(0,'Ingrese Clave')

txtClave = Entry(frame, width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
txtClave.place(x=30,y=100)
txtClave.insert(0, 'Ingrese Clave')
txtClave.bind('<FocusIn>', on_enter)
txtClave.bind('<FocusOut>', on_leave)

Frame(frame, width=275,height=2,bg='black').place(x=25,y=123)

comboOrigen = ttk.Combobox(frame)
comboOrigen["values"] = ("Comprobantes emitidos por el contribuyente", "Comprobantes recibidos por el contribuyente")
comboOrigen.place(x=155,y=145, width=235)
lbl2 = Entry(frame, width=12,fg='black',border=0,bg='white',font=('Microsoft YaHei UI',10))
lbl2.place(x=30,y=145)
lbl2.insert(0, 'Origen Emisión')

comboTipo = ttk.Combobox(frame)
comboTipo["values"] = ("Factura", "Liquidación de compra de bienes y prestación de servicios", "Notas de Crédito", "Notas de Débito", "Guías de Remisión", "Comprobante de Retención")
comboTipo.place(x=155,y=185, width=235)
lbl3 = Entry(frame, width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI',10))
lbl3.place(x=30,y=185)
lbl3.insert(0, 'Tipo Comprobante')

comboEstablecimiento = ttk.Combobox(frame)
comboEstablecimiento["values"] = ("Todos", "001", "002", "003", "004", "005")
comboEstablecimiento.place(x=155,y=225, width=235)
lbl4 = Entry(frame, width=15,fg='black',border=0,bg='white',font=('Microsoft YaHei UI',10))
lbl4.place(x=30,y=225)
lbl4.insert(0, 'Establecimiento')

comboMes = ttk.Combobox(frame)
comboMes["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
comboMes.place(x=200,y=265, width=60)
lbl5 = Entry(frame, width=5,fg='black',border=0,bg='white',font=('Microsoft YaHei UI',10))
lbl5.place(x=158,y=265)
lbl5.insert(0, 'Mes')

comboDia = ttk.Combobox(frame)
comboDia["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12","13","14","15","16","17","18","19","20", "21", "22","23","24","25","26","27","28","29","30","31")
#comboDia.place(x=190,y=265, width=60)
comboDia.place(x=75,y=265, width=60)
lbl7 = Entry(frame, width=5,fg='black',border=0,bg='white',font=('Microsoft YaHei UI',10))
#lbl7.place(x=145,y=265)
lbl7.place(x=30,y=265)
lbl7.insert(0, 'Dia')

comboAño = ttk.Combobox(frame)
comboAño["values"] = ("2022", "2021", "2020", "2019", "2018", "2017")
comboAño.place(x=330,y=265, width=60)
lbl6 = Entry(frame, width=5,fg='black',border=0,bg='white',font=('Microsoft YaHei UI',10))
lbl6.place(x=288,y=265)
lbl6.insert(0, 'Año')

def start_progbar():
    ruc = txtRuc.get()
    clave = txtClave.get()
    Origen = comboOrigen.get()
    Tipo = comboTipo.get()
    Establecimiento = comboEstablecimiento.get()
    Dia = comboDia.get()
    Mes = comboMes.get()
    Anio = comboAño.get()
    conexion.conectar()
    Bajar_Comprobantes_Page1.descargar(ruc, clave, Origen, Tipo, Establecimiento, Mes, Anio, Dia)

Button(frame,width=20,pady=7,text='Descargar Comprobantes',bg='#57a1f8',fg='white',border=0,command=start_progbar).place(x=150,y=355)

vent.mainloop()

