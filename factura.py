from cgitb import text
import tkinter as tk
from tokenize import String
import datetime
from datetime import date


class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry('1100x680')
        self.ventana1.title('Proyecto de Aula ')
        self.ventana1.resizable(False,False)
        self.ventana1.config(background= '#DEDCDE')
        main_title = tk.Label(text= 'Factura de Venta', font=('Cambria', 18),bg='#00D870', fg='white', width='550', height='2' )
        main_title.pack()

# Etiquetas
        self.nombrecliente_label=tk.Label(self.ventana1, text='Nombre del Cliente: ')
        self.nombrecliente_label.place(x=22, y=70)
        self.documento_label=tk.Label(self.ventana1, text='Cedula o Nit: ')
        self.documento_label.place(x=22, y=100)
        self.phone_label=tk.Label(self.ventana1, text='Telefono: ')
        self.phone_label.place(x=22, y=130)
        self.date_label=tk.Label(self.ventana1, text='Fecha: ')
        self.date_label.place(x=450, y=70)
        self.day_label = tk.Label(text=('hola'), font=('Tahoma',10), fg='black', bg='white', pady=2, padx=10)
        self.day_label.place(x=500, y=70)
        self.codProd_label=tk.Label(self.ventana1, text='Codigo: ')
        self.codProd_label.place(x=22, y=190)
        self.producto_label=tk.Label(self.ventana1, text='Descripcion Producto: ')
        self.producto_label.place(x=200, y=190)
        self.valor_label=tk.Label(self.ventana1, text='Valor Unitario: ')
        self.valor_label.place(x=570, y=190)
        self.cantidad_label=tk.Label(self.ventana1, text='Cantidad: ')
        self.cantidad_label.place(x=775, y=190)
        self.descuento_label=tk.Label(self.ventana1, text='Descuento %: ')
        self.descuento_label.place(x=930, y=190)

        self.get_date()

# Entrada de Datos
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width='40', background='WHITE', textvariable=self.dato,)
        self.entry1.place(x=170, y=70)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width='40', background='WHITE',textvariable=self.dato2)
        self.entry2.place(x=170, y=100)
        self.dato7=tk.StringVar()
        self.entry7=tk.Entry(self.ventana1, width='40', background='WHITE',textvariable=self.dato7)
        self.entry7.place(x=170, y=130)
        self.dato1=tk.StringVar()
        self.entry=tk.Entry(self.ventana1, width='15', background='WHITE',textvariable=self.dato1,)
        self.entry.place(x=90, y=190)
        self.dato3=tk.StringVar()
        self.entry3=tk.Entry(self.ventana1, width='35', background='WHITE',textvariable=self.dato3)
        self.entry3.place(x=340, y=190)
        self.dato4=tk.IntVar()
        self.entry4=tk.Entry(self.ventana1, width='15', background='WHITE',textvariable=self.dato4)
        self.entry4.place(x=670, y=190)
        self.dato5=tk.IntVar()
        self.entry5=tk.Entry(self.ventana1, width='10', background='WHITE',textvariable=self.dato5)
        self.entry5.place(x=850, y=190)
        self.dato6=tk.IntVar()
        self.entry6=tk.Entry(self.ventana1, width='7', background='WHITE',textvariable=self.dato6)
        self.entry6.place(x=1015, y=190)

# Imagen 
        imagenP=tk.PhotoImage(file='Logopython.png')
        self.lblImagen=tk.Label(self.ventana1, image=imagenP)
        self.lblImagen.place(x=150, y=340)


# Botones 
        self.boton1=tk.Button(self.ventana1, text='FACTURAR',font=('Cambria', 16),bg='#142D3B', fg='white',width=15, command=self.facturar)
        self.boton1.place(x=780, y=340)

# Etiquetas      
        self.label7=tk.Label(self.ventana1, text='SubTotal: ')
        self.label7.place(x=780, y=400)
        self.label12=tk.Label(self.ventana1, text='Descuento %: ')
        self.label12.place(x=780, y=460)
        self.label6=tk.Label(self.ventana1, text='Iva del 19%: ')
        self.label6.place(x=780, y=520)
        self.label8=tk.Label(self.ventana1, text='Total Neto: ')
        self.label8.place(x=780, y=580)
        self.label9=tk.Label(self.ventana1, background='WHITE',width='20')
        self.label9.place(x=870, y=400)
        self.label12=tk.Label(self.ventana1, background='WHITE',width='20')
        self.label12.place(x=870, y=460)
        self.label10=tk.Label(self.ventana1, background='WHITE',width='20')
        self.label10.place(x=870, y=520)
        self.label11=tk.Label(self.ventana1, background='WHITE',width='20')
        self.label11.place(x=870, y=580)

        self.ventana1.mainloop()

# Metodos

    def get_date(self):
        datetime_object = datetime.datetime.now()
        day = datetime_object.strftime("%A")

        today = date.today()
        d1= today.strftime("%d/%m /%y")
        self.day_label.configure(text=  d1 + ' | ' + day )

    def facturar(self):
        subtotal=int(self.dato4.get()*self.dato5.get())
        self.label9.configure(text=subtotal)
        descuento=int((self.dato6.get()*subtotal)/100)
        self.label12.configure(text= descuento)
        iva=(subtotal-descuento)*0.19
        self.label10.configure(text=iva)
        total=(subtotal+iva)-descuento
        self.label11.configure(text=total)



# Bloque Principal 
aplicacion1=aplicacion()