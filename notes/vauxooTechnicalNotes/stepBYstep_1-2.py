###############################################################################################################
##############################################Instalacion_base#################################################
###############################################################################################################
#es importante que  si son multiples comandos tengan un return, si no marcara errores por los caracteres especiales

docker -it ubuntu:16.04

Dentro de Ubuntu:
    DEBIAN_FRONTEND=noninteractive
    PYTHONIOENCODING=utf-8

    echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf \
    && echo 'APT::Get::force-yes "true";' >> /etc/apt/apt.conf

    apt-get update -q && apt-get upgrade -q

    apt-get install python-dateutil python-feedparser python-gdata python-ldap \
    python-libxslt1 python-lxml python-mako python-openid python-psycopg2 \
    python-pybabel python-pychart python-pydot python-pyparsing python-reportlab \
    python-simplejson python-tz python-vatnumber python-vobject python-webdav \
    python-werkzeug python-xlwt python-yaml python-zsi



    apt-get install --allow-unauthenticated -q bzr \
    python \
    python-dev \
    python-setuptools \
    git \
    vim \
    nano \
    wget \
    tmux \
    htop

git config --global user.name umiphos \
&& git config --global user.email umiphos@gmail.com

apt-get install locate

apt-get install --allow-unauthenticated -q libssl-dev \
libyaml-dev \
libjpeg-dev \
libgeoip-dev \
libffi-dev \
libqrencode-dev \
libfreetype6-dev \
zlib1g-dev \
libpq-dev

ln -s /usr/include/freetype2 /usr/local/include/freetype \
&& ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/ \
&& ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/ \
&& ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/

apt-get install python-pip

Pre requisitos para instalacion de Odoo
###############################################################################################################
##############################################instalacion_previa_##############################################
###############################################################################################################
locale-gen fr_FR \
    && locale-gen en_US.UTF-8 \
    && dpkg-reconfigure locales \
    && update-locale LANG=en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 \
    && echo 'LANG="en_US.UTF-8"' > /etc/default/locale

apt-get install --allow-unauthenticated -q postgresql-9.3 \
    postgresql-contrib-9.3 \
    postgresql-client-9.3

mkdir -p /etc/ssl/private-copy \
        && mkdir -p /etc/ssl/private \
        && mv /etc/ssl/private/* /etc/ssl/private-copy/ \
        && rm -rf /etc/ssl/private \
        && mv /etc/ssl/private-copy /etc/ssl/private \
        && chmod -R 0700 /etc/ssl/private \
        && chown -R postgres /etc/ssl/private

su - postgres /etc/init.d/postgresql start \
    && su - postgres -c 'psql -c "CREATE ROLE root LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE;"'

wget​ https://raw.githubusercontent.com/odoo/odoo/8.0/requirements.txt
sudo pip install -r requirements.txt

mkdir /extras

git clone https://github.com/OCA/maintainer-quality-tools.git -b master /extras/mqt
###Aqui hay pasos perdidos. Si seguimos tal cual los pasos de este Dockerfile entonces esto fallara... revisa bien que pedo, porque no podemos detenernos mas en este paso.....
#esto tambien le trueba a Moises en su Dockerfile....revisa esto: https://hub.docker.com/r/ocaimages/oca-odoo/builds/bsgcyiyfbkeprwvnk9rcarn/
#tiene un error relacionado con /root y /pylint
WITHOUT_ODOO=1 SHIPPABLE="true" WITHOUT_DEPENDENCIES="" /extras/mqt/travis/travis_install_nightly
WITHOUT_DEPENDENCIES=1


###############################################################################################################
##############################################instalacion_de_Odoo##############################################
###############################################################################################################
https://www.odoo.com/documentation/8.0/howtos/backend.html
#Basico_pre-Odoo
/etc/init.d/postgresql start
sudo useradd -d /home/odoo -m -s /bin/bash -p odoopwd odoo
sudo su - postgres
psql -c "CREATE ROLE odoo LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE;"
exit
sudo su - odoo
psql
    #mostrara un error de que no existe la base de datos, si esto persiste revisar el video CTP-T-1-1.mp4 <0:25>

#descargando Odoo
git clone https://github.com/odoo/odoo.git
#esto porque siempre se clona la version mas nueva, si requerimos la version 8.0 hay que hacer lo siguiente
git checkout 8.0
mkdir my-modules
cd my-modules
mkdir openacademy
touch __init__.py
########revisar esta carpeta o el enlace de backend.html para llenar los archivos que acabamos de crear
####__openerp__.py
    #Comentar:
        #demo
        #data



createdb odoo_curso
psql -l
python odoo.py -d odoo_curso
#revisar seccion de BUGS si tenemos algun tipo de problema...


###############################################################################################################
##############################################Adding_new_moodule###############################################
###############################################################################################################

psql odoo_curso -c "SELECT name FROM ir_module_module Where name ilike '%acade%'"

#aqui va a dar un problema
    #ERROR ? openerp.service.server: Failed to load server-wide module `web_kanban`.
python odoo/odoo.py -d odoo_curso --addons-path=/home/odoo/my-modules/
python odoo/odoo.py -d odoo_curso --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons/
    #con esto no aparece el error anterior

python odoo/odoo.py -d odoo_curso --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons/ -u all
python odoo/odoo.py -d odoo_curso --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons/ --init openacademy
#con esto ya deberia estar funcionando todo esto.


docker commit -m "Reinstalacion de Odoo, dia 1, hasta donde corres el --init openacademy  pero que aun no tiene nada." 355ccc696f17 curso_vauxoo_dia1:full

#####Hasta qui finaliza DIA_1
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################


###############################################################################################################
###############################################################################################################
Aqui comienza dia 2
###############################################################################################################
###############################################################################################################
docker run -v /home/umiphos/area/docker_shared:/home/odoo/docker_shared -it curso_vauxoo_dia1:full


/etc/init.d/postgresql start
sudo su - odoo
python odoo/odoo.py -d odoo_curso --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons/ -u all
python odoo/odoo.py -d odoo_curso --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons/ --init openacademy
python odoo/odoo.py -d odoo_curso --addons-path=/home/odoo/my-modules/,/home/odoo/odoo/addons/




http://172.17.0.2:8069
    admin
    *admin
ir a users-->seleccionar "Admin"
    Edit
        Add an item-->Usability/Technical Features





mkdir /home/odoo/my-modules/openacademy/model
touch /home/odoo/my-modules/openacademy/model/__init__.py
    from . import openacademy_course
    #revisar carpeta
touch /home/odoo/my-modules/openacademy/model/openacedemy_course.py
#####__openerp__.py es unico en openacademy
#####Parece que dia dos solo trata sobre GIT
<2.17>CTP-T2.1
nano /home/odoo/my-modules/openacademy/__init__.py
    from . import model
nano /home/odoo/my-modules/openacademy/openacedemy_course.py
    from openerp import models, fields, api

    class Course(models.Model):
    _name = 'openacademy.course'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()




###############################################################################################################
###############################################################################################################
Aqui comienza dia 2 parte 2
###############################################################################################################
###############################################################################################################
mkdir /home/odoo/my-modules/openacademy/demo
touch /home/odoo/my-modules/openacademy/demo/openacademy_course_demo.xml
nano /home/odoo/my-modules/openacademy/demo/openacademy_course_demo.xml
    <?xml version="1.0" encoding="UTF-8"?>
    <openerp>
        <data>
            <record model="openacademy.course" id="course0">
                <field name="name">Course 0</field>
                <field name="description">
                    Descripcion del curso 0.
                    Principiantes Odoo FTW!
                </field>


            </record>
            <record model="openacademy.course" id="course1">
                <field name="name">Course 1</field>
                <field name="description">
                    Descripcion del curso 1.
                    Pasantes Vauxoo FTW!
                </field>
            </record>
        </data>
    </openerp>

nano /home/odoo/my-modules/openacademy/__openerp__.py
    modificar 'demo':[/demo/openacademy_course_demo.xml,]

Hasta aqui va el video 2.2 al minuto <0:20>

mkdir /home/odoo/my-modules/openacademy/view
touch /home/odoo/my-modules/openacademy/view/openacademy_course_view.xml
nano /home/odoo/my-modules/openacademy/view/openacademy_course_view.xml
    <?xml version="1.0" encoding="UTF-8"?>
    <openerp>
        <data>
            <record model="ir.ui.view" id="course_form_view">
                <field name="name">course.form.view</field>
                <field name="model">openacademy.course</field>
                <field name="arch" type="xml">
                    <form string="Course Form">
                        <sheet>
                            <group>
                                <field name="name"/>
                                <field name="description"/>
                            </group>

                        </sheet>
                    </form>

                </field>
            </record>


            <record model="ir.actions.act_window" id="course_list_action">
                <field name="name">Courses</field>
                <field name="res_model">openacademy.course</field>
                <field name="view_type">form</field>
                <field name="view_mode">tree,form</field>
                <field name="help" type="html">
                    <p class="oe_view_nocontent_create">Create the first course</p>
                </field>
            </record>



        <!-- top level menu: no parent -->
        <menuitem id="main_openacademy_menu" name="Open Academy"/>
        <!-- A first level in the left side menu is needed
             before using action= attribute -->
        <menuitem id="openacademy_menu" name="Open Academy"
                  parent="main_openacademy_menu"/>
        <!-- the following menuitem should appear *after*
             its parent openacademy_menu and *after* its
             action course_list_action -->
        <menuitem id="courses_menu" name="Courses" parent="openacademy_menu"
                  action="course_list_action"/>
        <!-- Full id location:
             action="openacademy.course_list_action"
             It is not required when it is the same module -->
        </data>
    </openerp>


nano /home/odoo/my-modules/openacademy/__openerp__.py
    modificar:
        'data':[
        'view/openacademy_course_view.xml',

        ],
#####parte 2 de video 2.2
nano /home/odoo/my-modules/openacademy/view/openacademy_course_view.xml
        --[
        <field name="description"/>
        ]
        ++[
        <notebook>
            <page string="Description">
                <field name="description"/>
            </page>
            <page string="About">
                This is an example of notebooks
            </page>
        </notebook>

        ]

nano /home/odoo/my-modules/openacademy/view/openacademy_course_view.xml
#como un campo mas
#esto es los tooltips del campo de busqueda
        <record model="ir.ui.view" id="course_search_view">
            <field name="name">course.search</field>
            <field name="model">openacademy.course</field>
            <field name="arch" type="xml">
                <search>
                    <field name="name"/>
                    <field name="description"/>
                </search>
            </field>
        </record>

#prueba lo anterior antes de probar este :)
        <record model="ir.ui.view" id="course_tree_view">
                <field name="name">course.tree.view</field>
                <field name="model">openacademy.course</field>
                <field name="arch" type="xml">
                        <tree string="Course">
                            <field name="name"/>
                            <field name="description"/>
                        </tree>
                </field>
        </record>


time<1:15>CTP-T-2.2
touch /home/odoo/my-modules/openacademy/model/openacademy_session.py
nano /home/odoo/my-modules/openacad emy/model/openacademy_session.py
    # -*- coding: utf-8 -*-
    from openerp import fields, models
    class Session(models.Model):
        _name="openacademy.session'
        name = fields.Char(required=True)
        start_date = fields.Date()
        duration = fields.Float(digits=(6, 2),  help="Duration in days")
        seats = fields.Integer(string="Number of seats")

#basicamente el string="" es el texto que aparecera en el formulario.


nano /home/odoo/my-modules/openacad emy/model/__init__.py
    +[
    from . import openacademy_session

    ]
touch /home/odoo/my-modules/openacademy/view/openacademy_session_view.py
nano  /home/odoo/my-modules/openacademy/view/openacademy_session_view.py
    <?xml version="1.0"?>
    <openerp>
        <data>
            <!-- session form view -->
            <record model="ir.ui.view" id="session_form_view">
                <field name="name">session.form</field>
                <field name="model">openacademy.session</field>
                <field name="arch" type="xml">
                    <form string="Session Form">
                        <sheet>
                            <group>
                                <field name="name"/>
                                <field name="start_date"/>
                                <field name="duration"/>
                                <field name="seats"/>
                            </group>
                        </sheet>
                    </form>
                </field>
            </record>

            <record model="ir.actions.act_window" id="session_list_action">
                <field name="name">Sessions</field>
                <field name="res_model">openacademy.session</field>
                <field name="view_type">form</field>
                <field name="view_mode">tree,form</field>
            </record>

            <menuitem id="session_menu" name="Sessions"
                      parent="openacademy_menu"
                      action="session_list_action"/>
        </data>
    </openerp>

nano  /home/odoo/my-modules/openacademy/__openerp__.py
     +[
     'view/openacademy_session_view.xml',
     ]
_____________________-
Aqui vamos en v2.2 1:55


nano  /home/odoo/my-modules/openacademy/model/openacademy_course.py
    +[
        responsible_id = fields.Many2one('res.users',
            ondelete='set null',
            string = "Responsible", index=True)
    ]
#sin embargo aun ocupamos una sesion como lo indica el manual de backend de odoo 8
#asi que una vez que modificamos la parte funcional NECESITAMOS modificar tambien la vista (view) para que los cambios puedan ser visibles

nano  /home/odoo/my-modules/openacademy/view/openacademy_course_view.xml
    <record model="ir.ui.view" id="course_form_view">
        <field name="name">course.form.view</field>
        <field name="model">openacademy.course</field>
        <field name="arch" type="xml">
        <form string="Course Form">
            <sheet>
                <group>
                    <field name="name"/>
                    +[
                    <field name="responsible_id"/>
                    ]



nano  /home/odoo/my-modules/openacademy/model/openacademy_session_course.py
    ++[
        instructor_id = fields.Many2one('res.partner', string="Instructor")
        course_id = fields.Many2one('openacademy.course',
        ondelete='cascacde', string="Course", required=True)
    ]
nano  /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
--[
<form string="Session Form">
    <sheet>
        <group>
            <field name="name"/>
            <field name="start_date"/>
            <field name="duration"/>
            <field name="seats"/>
        </group>
    </sheet>
</form>
]

++[
    <form string="Session Form">
        <sheet>

            <group string="General">
                <field name="course_id"/>
                <field name="name"/>
                <field name="instructor_id"/>
            </group>
            <group string="Schedule">
                <field name="start_date"/>
                <field name="duration"/>
                <field name="seats"/>
            </group>
        </sheet>
    </form>



    <!-- session tree/list view -->
    <record model="ir.ui.view" id="session_tree_view">
        <field name="name">session.tree</field>
        <field name="model">openacademy.session</field>
        <field name="arch" type="xml">
            <tree string="Session Tree">
                <field name="name"/>
                <field name="course_id"/>
            </tree>
        </field>
    </record>
]


#agregando un one2many
nano  /home/odoo/my-modules/openacademy/model/openacademy_course.py
    ++[
        session_ids = fields.One2mane('openacademy.session', 'course_id', string="Sessions")
    ]



#no se nos olvide modificar la vista o si no tronara
nano  /home/odoo/my-modules/openacademy/view/openacademy_course_view.xml
<page string="Sessions">
    <field name="session_ids">
        <tree string="Registered sessions" editable="bottom"><!--el bottom se agrego despues-->
            <field name="name"/>
            <field name="instructor_id"/>
        </tree>
    </field>
</page>





#agregando un many2many
nano  /home/odoo/my-modules/openacademy/model/openacademy_session.py
    ++[
        attendee_ids = fields.Many2many('res.partner', string="Attendees")
    ]

nano  /home/odoo/my-modules/openacademy/view/openacademy_session_view.xml
    #al final de todos los <group></group>

                <field name="seats"/>
            </group>
        </group>
    ++[
        <label for="attendee_ids"/>
        <field name="attendee_ids"/>
    ]
</sheet>
___________________-
###############################################################################################################
###############################################################################################################

###############################################################################################################
##############################################Stuffy_stuff#####################################################
###############################################################################################################

###############################################################################################################
###############################################################################################################


###############################################################################################################
##############################################SQL_stuff########################################################
###############################################################################################################
VID 1.2
<1:50> sentencias SQL y explicacion de INNER JOIN
psql odoo_curso -c "SELECT * FROM ir_module_category"
psql odoo_curso -c "SELECT imm.name AS module_name, imc.name AS category_name FROM ir_module_category imc INNER JOIN ir_module_module imm ON imm.category_id = imc.id"

psql odoo_curso -c "SELECT * FROM openacademy"

psql odoo_curso -c "
SELECT openacademy_course.id, openacademy_course.name, openacademy_course.responsible_id, res_users.login
FROM openacademy_course
INNER JOIN res_users ON res_users.id = openacademy_course.responsible_id"
###############################################################################################################
##############################################ssh_Github#######################################################
###############################################################################################################

#https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/

ssh-keygen -t rsa -C "umiphos@gmail.com"
cd /home/odoo/.ssh/
    id_rsa es la llave privada
    id_rsa.pub es la llave publica

###############################################################################################################
##############################################levantar_contenedor_exiteado(xD)#################################
###############################################################################################################
docker ps -a
    (Identificas el container id)
docker start {CONTAINER_ID}
docker exec -it {CONTAINER_ID} bash

###############################################################################################################
##############################################Docker_stuff#####################################################
###############################################################################################################


docker rm $(docker ps -a -q) #el
    #-a muestra los contenedores....
    #-p muestra solo los ID de los contenedores(CONTAINER ID) es un filtro de esa columna

#creando imagen de container a docker image
docker commit -m "mensaje descriptivo" {id_container} {name}:tag


#corriendo imagen con carpeta compartida
docker run -v /home/umiphos/area/docker_shared:/home/odoo/docker_shared -it imageName:Tag


###############################################################################################################
##############################################BUGS#############################################################
###############################################################################################################
psql: FATAL:  database "root" does not exist
        sudo su - postgres
        psql -c "CREATE ROLE odoo LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE;"

/root/maintainer-quality-tools/travis/pylint_odoo_requirements.txt: No such file or directory
    #es normal, hasta a Moylop le pasa, revisa su hub.docker

Can't roll back python-ldap; was not uninstalled
    Esto ocurre posiblemente porque no instalamos "python-dev" se corrige con esta liga
    apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev

ImportError: No module named unittest2
    Basicamente no instalaste algunas librerias, por lo tanto necesitas bajar lo siguiente:
    wget​ https://raw.githubusercontent.com/odoo/odoo/8.0/requirements.txt
    sudo pip install -r requirements.txt

Can't roll back lxml; was not uninstalled
ERROR: /bin/sh: 1: xslt-config: not found
    Basicamente tenemos problemas con estas dos librerias
    apt-get install libxslt1-dev libxml2

INFO odoo_curso openerp.modules.loading: loading openacademy/templates.xml
CRITICAL odoo_curso openerp.service.server: Failed to initialize database `odoo_curso`.
    Este error es bien basico, como ya habia avanzado antes, se me hizo facil avanzar mas rapido... tenemos que comentar en /my-modules/openacademy/__openerp__.py el "templates.xml" ya que de momento no lo ocupamos para ese tiempo de la prueba y de este documento
    Posiblemente tienes informacion que no requieres en __init__.py, posiblemente en esa etapa del requieres que este en blanco.

AssertionError: Invalid attribute type for element field, line 32
    en los atributos de tu record, el id="" no coincide con el que estas llamando en el field... revisar que si es form coincida con form
    si es tree coincida con tree

XMLSyntaxError: Opening and ending tag mismatch:
XMLSyntaxError: Premature end of data in tag openerp
XMLSyntaxError: XML declaration allowed only at the start of the document
    posiblemente en un xml falto cerrar un tag
    es posiblemente que sea un xml de un nuevo modelo, revisar siempre este tipo de errores


ERROR odoo_curso openerp.addons.base.ir.ir_ui_view: Field `responsible_idasdfasfdasdx` does not exist
    basicamente es un error de agregar en el /model.py un campo con X nombre y no respetar ese nombre en /view.xml
