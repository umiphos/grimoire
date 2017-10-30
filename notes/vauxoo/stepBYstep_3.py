"""
Este documento trata sobre el capitulo 3. Estaremos anotando comando por comando de lo que escribe Moy para poder replicarlo en cualquier momento.

Se divide de igual manera que el anterior, primera seccion es acerca de el paso a paso de como agrega y modifica cosas en el proyecto de Odoo. 

La siguiente seccion de comandos que pueden ser utiles
La siguiente seccion es de bugs que encontramos, pueden de momento repetirse con los bugs que 

"""









##################COMMENTS BY TIME



"""
Agregamos esta zona de comentarios de Moy... posiblemente sean utiles y no quier volver a ver un video de 3 horas para obtener esta informacion....
CTP-T-3-1
    <0:50>--<0:00> Menciona cosas de herencia... sin embargo no se ve aun esto en practica y pues aun no endiendo que pedo.....
    <1:54>--<0:00> Hace mencion de como usar la notacion polaca supongo, pero lo que esta chingon es la explicacion
    <2:13>--<0:00> Modifica uno de los contactos y le agrega un "tag" para ver un ejemplo sobre lo que se ha modificado.
    <2:32>--<0:00> Empieza lo de las funciones y algo de los decoradores
    <2:38>--<0:00> ¿Que hace el decorador @api.one?
    <2:42>--<0:00> Explicacion de "On the fly"
Esto es una variable, no importa....creo....        domain=[
Este es el operador OR                              '|',
Parametro 1                                         ('instructor','=', True),
Parametro 2                                         ('category_id.name', 'ilike', "Teacher")])
Basicamente se lee como sigue:
Si cualquiera de los siguientes se cumple, entonces:

    
    

"""


"""xpath
hasta el momento sabemos que sirve para buscar en xml como si fuese un...buscador...de xml....vaya me he superado....
#This is the opportunity to introduce the developer mode to inspect the view, find its external ID and the place to put the new field.
"""


##################STEP BY STEP SECTION



"""
inherit
inherits
Es el tema de herencias, sin embargo aun no entiendo como las manejan en Odoo
Menciona algo de "notacion polaca" otra cosa que aun no entiendo...
Cierto estamos comentando cosas de nuevo porque el sprint del fin de semana no fue tan productivo....
"""




"""Empezando la creacion del partner.py para el ejercicio


"""

#<1:00>
#touch /home/odoo/my-modules/openacademy/model/partner.py
#nano /home/odoo/my-modules/openacademy/model/partner.py

"""

# -*- coding: utf-8 -*-

from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

# Add a new column to the res.partner model, by default partners are not
# instructors
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
    string="Attended Sessions", readonly=True)

"""


#touch /home/odoo/my-modules/openacademy/view/partner_view.xml
#nano /home/odoo/my-modules/openacademy/view/partner_view.xml

"""
<?xml version="1.0" encoding="UTF-8"?>
 <openerp>
    <data>
        <!-- Add instructor field to existing view -->
        <record model="ir.ui.view" id="partner_instructor_form_view">
            <field name="name">partner.instructor</field>
            <field name="model">res.partner</field>
            <field name="inherit_id" ref="base.view_partner_form"/>
            <field name="arch" type="xml">
                <notebook position="inside">
                    <page string="Sessions">
                        <group>
                            <field name="instructor"/>
                            <field name="session_ids"/>
                        </group>
                    </page>
                </notebook>
            </field>
        </record>

        <record model="ir.actions.act_window" id="contact_list_action">
            <field name="name">Contacts</field>
            <field name="res_model">res.partner</field>
            <field name="view_mode">tree,form,kanban</field>
        </record>
        <menuitem id="configuration_menu" name="Configuration"
                  parent="main_openacademy_menu"/>

        <menuitem id="contact_menu" name="Contacts"
                  parent="configuration_menu"
                  action="contact_list_action"/>
    </data>
</openerp>
"""


#nano /home/odoo/my-modules/openacademy/__openerp__.py
"""
++[
view/partner_view.xml',
]
"""
#nano /home/odoo/my-modules/openacademy/model/__init__.py
"""
++[
from . import partner
]
"""
###RUN

#nano /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
<1:44>
    Basicamente aqui hace unos cambios en openacademy_session.py, son rapidos por eso ponemos este comentario.
    Si no se requiere modificar todo, solo se puede agregar el "domain", pero aqui pongo toda la cadena, por si acaso.

--- [
    instructor = fields.Boolean("Instructor", default=False)
    ]

+++ [
    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=[('instructor', '=', True)])
    ]
"""

"""
<1:47>
Tambien aqui hacen una pregunta sobre identacion y vi y cosas asi, mas adelante vim trollea a Moy no soltandole un error cuando metio un <TAB>
<1:50>
Esto no es codigo...pero hizo que Vauxoo fuese instructor.
Contacts--->vauxoo--->Sessions--->Instructor=True

<1:52>
Aqui ya pone un nuevo OR, donde un partner pueda ser teacher...o algo asi....
"""

#nano /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""<1:50>
--- [
    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=[('instructor', '=', True)])
    ]

+++ [

    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=['|', ('instructor', '=', True),
        ('category_id.name', 'ilike', "Teacher")]),
    ]

el valor del "=" o "ilike" puede ser cambiado a discrecion para poder utilizar un regex en la busqueda
"""
#GIT PUSH

#Creamos en docker curso_vauxoo_dia3:parte1

#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
from openerp import models, fields, api#agregamos el api de openerp
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    @api.one###este no esta en la documentacion oficial, pero si en el video
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        if self.seats == 0:
            self.taken_seats = 0
        else:
            self.taken_seats = 100.0 * len(self.attendee_ids)/self.seats
"""
#:w
#:q

#vi /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
"""
<2:47:50>
#dentro de form view
<field name="taken_seats" widget="progressbar"/>


#dentro de tree view
#<field name="taken_seats" widget="progressbar"/>#esto aun no

"""

#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
<2:50:00>
---[
    start_date = fields.Date()
    start_date = fields.Date(default=fields.Date.today())
    ]

+++[
    start_date = fields.Date(default=fields.Date.today())


    ]
"""


###Basicamente es la hora de la ultima compilacion, no pareciera muy util...mejor no usarlo...
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
Aqui moy dice que hara un ejemplo de algo con los campos de tiempo, posiblemente este campo sera eliminado
    datetime_eg = fields.Datetime(default=fields.Datetime.now())
    datetime_eg = fields.Datetime(default=fields.Datetime.now)

Ya esta la explicacion, el primero queda mas estatico, ya que es un valor que se obtiene al momento de compilacion.
El segundo sirve para ser llamado y actualizado cada vez que nosotros lo ocupamos.

"""


#vi /home/odoo/my-modules/openacademy/model/openacademy_session_view.py
"""
<group string="Schedule">
    +++[
        <field name="datetime_eg"/>
    ]
"""

#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
<3:00:00>
---[
    start_date = fields.Date(default=fields.Date.today())
    ]

+++[
    start_date = fields.Date(default=fields.Date.today)
    active = fields.Boolean(default=True)
    ]
"""

#vi /home/odoo/my-modules/openacademy/model/openacademy_session_view.xml
"""

<field name="instructor_id"/>
    +++[
        <field name="active"/>
    ]
</group>
"""
#########################################
#########################################
#########################################Hasta aqui es el video 3.1
#########################################Creamos en docker curso_vauxoo_dia3:parte1_2 
#########################################



#####3.2.1
@Onchange
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
+++[
 @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

]
"""
#RUN

@constrains
#<0:12>Explicacion entre python_constraints y sql_constraints
#constrain=python constraint=sql
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""


+++[El que usa moy
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        if self.instructor_id and self.instructor_id in self.attendee_ids:
            raise exceptions.ValidationError("A session's instructor can't be an attendee")
   ]


+++[El que usa en este momento el curso de vauxoo backend
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")
   ]
Al minuto 20 de este video podemos ver que le da un error, asi lo deja moy, ya que no impide que funcione el constrain.
"""


#########3.2.2
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
+++[EOF
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


Aqui esto fallara... peeeero
lo eliminamos mas adelante... lo pongo igual para ver el error que avienta y documentarlo.

En caso de que hayas seguido ciegamente este paso, para solucionalo es con una linea:
ALTER TABLE openacademy_session DROP CONSTRAINT openacademy_session_name_unique;
"""

#vi /home/odoo/my-modules/openacademy/model/openacademy_course.py
"""
+++[EOF
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


Si da un error es...normal... tambien en el video en el minuto <0:44:11> se ve el error.
"""

@constrains.copy
#vi /home/odoo/my-modules/openacademy/model/openacademy_course.py
"""
<1:00:00> 
+++[
    @api.one#en odoo viene como 'multi', en el video lo ponen como 'one'
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)
    ]

Esto es importante revisarlo mas tarde, ya que aun no entiendo porque usan de esta forma una tupla...
"""

@advancedViews
@advancedViews.treeView
#vi /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
"""
---[
<tree string="Session Tree">
---]

+++[
<tree string="Session Tree" colors="#0000ff:duration&lt;5;red:duration&gt;15">
+++]
"""


@advancedViews.calendar
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py

"""
Antes de copiar y pegar esto: En el video hay un codigo distinto a lo que hay en la documentacion. Por lo tanto usaremos el del video, y al final se pega el actual de la documentacion.
+++[
from datetime import timedelta   
    #dentro de Class Session
    end_date = fields.Date(string="End Date", store=True,
        compute='_get_end_date', inverse='_set_end_date')
        
    #EOF
    @api.one
    @api.depends('duration', 'start_date')
    def _get_end_date(self):
        if not(self.start_date and self.duration):
            self.end_date = self.start_date
            return
        print "estoy dentro de _get_end_date"
        start = fields.Datetime.from_string(self.start_date)
        duration = timedelta(days=self.duration, seconds=-1)
        self.end_date = start + duration
        
    @api.one
    def _set_end_date(self):
        if not (self.start_date and self.end_date):
            return
        print "estoy dentro de _set_end_date"    
        start_date = fields.Datetime.from_string(self.start_date)
        end_date = fields.Datetime.from_string(self.end_date)
        self.duration = (end_date - start_date).days+1
+++]
######Esto viene en la documentacion oficial
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1
"""
#vi /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
"""
<group string="Schedule>
+++[
    <field name="end_date"/>
+++]
"""

#vi /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
"""
        <!-- calendar view -->
        <record model="ir.ui.view" id="session_calendar_view">
            <field name="name">session.calendar</field>
            <field name="model">openacademy.session</field>
            <field name="arch" type="xml">
                <calendar string="Session Calendar" date_start="start_date"
                          date_stop="end_date"
                          color="instructor_id">
                    <field name="name"/>
                </calendar>
            </field>
        </record>
"""

#########################################Creamos en docker curso_vauxoo_dia3:parte1_2_2 


@advancedViews.searchViews
#vi /home/odoo/my-modules/openacademy/view/openacademy_course_view.xml
"""Dentro de la vista search de cursos...
<field name="description"/>
+++[
        <filter name="my_courses" string="My Courses"
            domain="[('responsible_id', '=', uid)]"/>
            <group string="Group By">
                <filter name="by_responsible" string="Responsible" context="{'group_by': 'responsible_id'}"/>
            </group>
+++]
#dentro de ir.actions.act_windo: sirve para poner en default "My courses"
+++[
        <field name="context" eval="{'search_default_my_courses': 1}"/>
+++]

"""


@advancedViews.gantt
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
Recordemos que para insertar un nuevo campo es en la raiz de la clase en python, pero lo agregamos al final de las demas.
+++[
hours = fields.Float(string="Duration in hours",
    compute='_get_hours', inverse='_set_hours')
+++] Tomar en cuenta que utiliza dos funciones que debemos declarar mas adelante: _get_hours y _set_hours, que estan asignadas a esas dos propiedades, posiblemente son convenciones de Odoo.

+++[
    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24
+++]

"""

#vi /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
"""
Como se acaba de agregar un nuevo campo 'hours' necesitamos agregarlo a la vista para que aparezca.
Se agrega en el grupo 'Schedule'.
+++[
<field name="hours"/>
+++]

Se agrega esta nueva vista:
+++[
    <!--Gant View-->
    <record model="ir.ui.view" id="session_gantt_view">
        <field name="name">session.gantt</field>
        <field name="model">openacademy.session</field>
        <field name="arch" type="xml">
            <gantt string="Session Gantt" color="course_id"
                date_start="start_date" date_delay="hours"
                default_group_by='instructor_id'>
                <field name="name"/>
            </gantt>
        </field>
    </record>
+++]


Lo agregamos a los modelos de vista que tenemos, ahora tenemos tree,form,calendar, gantt:


+++[
    <field name="view_mode">tree,form,calendar,gantt</field>

+++]

"""


@advancedViews.graphViews
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
Se agrega un nuevo campo: Recordemos que si agregamos un nuevo campo debemos agregar una funcion si le agregamos alguno de los parametros que ya hemos visto, por ejemplo compute, inverse, 
+++[
    attendees_count = fields.Integer(
        string="Attendees count", compute='_get_attendees_count', store=True)
+++]

Se agrega un nuevo decorador(aun no sabemos que pex con esto, se parece un buen a Flask....)
+++[
    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

+++]

"""

#vi /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
"""Como es una nueva vista, se agrega completa.
+++[
    <!---Graph view->
        <record model="ir.ui.view" id="openacademy_session_graph_view">
            <field name="name">openacademy.session.graph</field>
            <field name="model">openacademy.session</field>
            <field name="arch" type="xml">
                <graph string="Participations by Courses">
                    <field name="course_id"/>
                    <field name="attendees_count" type="measure"/>
                </graph>
            </field>
        </record>
+++]
Este ultimo paso no lo pondremos como codigo, para que el futuro yo o usuario de este manual esta poniendo atención a la mitad del curso.
Acabamos de agregar una vista, ahora, que hacemos?
'graph'


"""
@advancedViews.kanban
#vi /home/odoo/my-modules/openacademy/model/openacademy_session.py
"""
Se agregara esta propiedad como si fuese un campo, solo que esta vez es solo eso, una propiedad, no necesitamos agregar nada para que funcione, ya que lo invocaremos en la vista kanban 
+++[
    color = fields.Integer()
+++]
"""

#vi /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
"""Se agrega esta nueva vista kanban.
+++[
        <record model="ir.ui.view" id="view_openacad_session_kanban">
            <field name="name">openacad.session.kanban</field>
            <field name="model">openacademy.session</field>
            <field name="arch" type="xml">
                <kanban default_group_by="course_id">
                    <field name="color"/>
                    <templates>
                        <t t-name="kanban-box">
                            <div
                                    t-attf-class="oe_kanban_color_{{kanban_getcolor(record.color.raw_value)}}
                                                  oe_kanban_global_click_edit oe_semantic_html_override
                                                  oe_kanban_card {{record.group_fancy==1 ? 'oe_kanban_card_fancy' : ''}}">
                                <div class="oe_dropdown_kanban">
                                    <!-- dropdown menu -->
                                    <div class="oe_dropdown_toggle">
                                        <span class="oe_e">#</span>
                                        <ul class="oe_dropdown_menu">
                                            <li>
                                                <a type="delete">Delete</a>
                                            </li>
                                            <li>
                                                <ul class="oe_kanban_colorpicker"
                                                    data-field="color"/>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="oe_clear"></div>
                                </div>
                                <div t-attf-class="oe_kanban_content">
                                    <!-- title -->
                                    Session name:
                                    <field name="name"/>
                                    <br/>
                                    Start date:
                                    <field name="start_date"/>
                                    <br/>
                                    duration:
                                    <field name="duration"/>
                                </div>
                            </div>
                        </t>
                    </templates>
                </kanban>
            </field>
        </record>
+++]


Esto dara error, revisa que pudo haber fallado :)
"""
##################USEFUL COMMANDS SECTION
"""
Busca donde diga "widget":      rgrep widget -l 
En esta direccion:              . 
En los archivos .py:            --include=*.py 
Ademas:                         |
Resalta la palabra "web":       grep web
"""
rgrep widget -l . --include=*.py |grep web


"""
Sirve para localizar paquetes o archivos.
Requiere permisos root
"""
apt-get install locate
updatedb
locate filename.extensions

"""
Borra solo una columna de una tabla... muy util!
"""
ALTER TABLE openacademy_session DROP COLUMN datetime_eg;
##################BUGS SECTION
#2017-01-31 19:30:28,910 621 ERROR odoo_curso openerp.http: Exception during JSON request handling.
#AttributeError: type object 'openacademy.session' has no attribute '_get_attendees_count'
"""
Este but menciona que no agregue el atributo "_get_attendees_count", basicamente olvide agregar la funcion de ese nombre, asi que es llamada pero jamas funciona, ya que no la declare
"""
#Field(s) `arch` failed against a constraint: Invalid view definition
"""
Basicamente olvide agregar el campo en el archivo py, pero si lo estoy invocando.
"""
