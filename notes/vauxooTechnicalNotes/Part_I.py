#Intro:
"""
    Este curso es sobre Odoo 10 funcional, es una breve guia de los puntos a tratar para quien quiere aprender Odoo 10. Se hara en esta primera parte una lista de los puntos importantes que se obserban en el video, despues se haran, sobre esa lista comentarios. En las versiones primeras de esto estara todo en desorden...sin embargo deberiamos poder ver algo bien hecho en versiones posteriores.

Creacion de base de datos--> nada que no sepamos ya...
Company Data
    General setting-->configure 
        Now you can have a party or whatever.
    Agregar Idioma
    Creacion de usuarios
        Agregar idioma al usuario
        Y puedes hacer tu desmadre en el nuevo usuario.
        
Como cargar una traudccion
Como asignar un idioma a un usuario        
Clickear dos veces  sobre una listra grande para ver todos los elementos
Como archivar productos:que pareciera mas bien esto en inventario que en introduccion

"""
@Discuss
"""
Primer modulo que vemos, es basicamente Slack dentro de Odoo, totalmente web.

Creacion de listas de correo

Canales
    Publicos(Todos lo ven)
    Privados(Todos deben ser invitados)
    
    accesar mediante el @
    en los globitos de chat para buscar chats o notificaciones
    Puedes enviar logs o mensajes directamente a los customer mediante
"""
@Calendario
    Meetings
        Filtro por correo, alertas, repetitivos, etc
    Sync con google calendar
        settings, google calendar check
        w
@Contactos
    """
    Los requeridos son lo que tienen una linea negra bajo de ellos
    Explicar el campo buscador
    Podemos crear un grupo de archivos.
    Los filtros pueden tener AND y OR
    Group By en listas los convierte en una lista desplegable
        puede tener niveles 
        puede tener filtros
        
    Many2many<-->one2Mane
    Creacion de contactos
    Importacion de contactos por archivo
    Filtros para busquedas
    
    Para mostrar como editar N cantidad de contactos y mostrar como hacerlo mediante CVS
    """



@CRM
"""
Pipeline de grupos de ventas
configuracion de estos grupos de ventas


Objetivos de 10 actividades?
KPI?
Agregar miembros a cada grupo de venta.
Agregar estados a un pipeline de un Kanban del equipo de ventas

Dashboard oportunities
crear oportunities
eliminar
modificar
@#Que es assume probability????

Creacion de actividades
Dias que tomara la actividad
asignar una tarea siguiente


Asignacion de tareas y mostrar el Log de mensajes

Creacion de Leads 
    convertirlo en oportunities
    
    
    
Los colorsitos del kanban
    gris: sin asignacion
    Verde con asignacion en tiempo
    Rojo con asignacion atrasada
    
Los incoiced del KPI son actualizados cuando validas los invoices
    Los invoices deben venir de sales(ventas)

Para alertar a un grupo especifico de ventas puedes crear un alias del correo
Puedes tener dos direcciones distintas para tus clientes:
    La direccion fisica y la direccion invoice
sThe best way to add a separate billing address is to create a new address from the "Contacts & Addresses" tab of the customer form. Be sure to select the type "invoice address". When invoice is generated, this address will be used automatically.    
"""


@Sales
"""
Instalar Sales, cambia el nombre pero queda el icono
Sales-->Creacion de productos

En sales esta product
Se crean como creando un usuario
Existen 2 principales:
    Consumable      No lleva un registro de los items
    Service         No tiene registros
    
Internal reference para identificacion de tipo de producto
Barcode
Internal category

Quotations=cotizaciones
Las puedes crear con los productos o servicios
Puedes agregarles valores negativos


Creacion de secciones para cotizaciones

Creacion de cotizaciones en linea
Stepts:
Sales
Setting
Enable sales quotation





Pricelists
Esto es una de las cosas mas utiles que he visto, y esta bastante sencillo
Existen 3 formas asignar los precios:
item por item
grupos de clientes 
Categorias avanzadas
Los primeros se explican solos, los ultimos requieren mas detalle
"""



@invoicing

@accounting
@accounting.accounting
"""
Accounts type:
Receivable:                 Dinero que me deben
Payable:                    Dinero que debemos
Bank and Cash:              Dineron en el banco y dinero entre tansacciones de bancos
Current Assets:             Deben ser pagadas o recibidas en el año actual del cierre
Non-current Assets:         No Deben ser pagadas o recibidas en el año actual del cierre
Prepayments:                
Fixed Assets:               
Current Liabilities:        Deben ser pagadas o recibidas en el año actual del cierre
Non-current Liabilities:    No Deben ser pagadas o recibidas en el año actual del cierre
Equity                      Ganancias y perdidas de dinero
Current year earnings
Other Income
Income                      Crean una declaracion de ganancia
Expenses                    Crean una declaracion de ganancia
Cost of revenue
"""
@accounting.journals
"""
Journal: se registran todas las operaciones, sirve para organizar estos eventos
Basicamente no es un tema aun tan grande, sirve para organizar las formas en que eldinero fluye en la empresa.



"""
