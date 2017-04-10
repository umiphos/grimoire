MDF deployv
==================================

Todo empieza con un simple pip install, that needs some dependencies:
> sudo apt-get install build-essential python-setuptools python-dev libpq-dev libffi-dev
> pip install deployv
> vi /etc/postgresql/9.5/main/postgresql.conf
    > listen_addresses = '*' #puedes seguir los tutoriales y poner algunas IP ahi, pero a mi me funciona con esto....
> vi /etc/postgresql/9.5/main/pg_hba.conf
    # "local" is for Unix domain socket connections only
    # Agregaremos esta linea justo debajo de este comentario
    > host    all             all             all                     md5
> deployvcmd create -f config.json -z database.tar.bz2

## Nota: en el json que me dieron tiene un user "dbuser" cableado, una de dos, o lo creas o vives con el error que te tirara al final de la creación de la imagen


Corriendo imagen generada por deployv
===========================================

# Hasta este punto debemos de tener una imagen creada, si aparecen errores de base de datos al final revisa y categoriza:
    > No se pudo conectar, esta realmente abierto? este error significa que se cago lo que estabas haciendo
    > No se encontro X usuario y no pude eliminar mis vainas: significa que si funciono, que tienes una imagen, pero mucha mierda en tu postgres local
    > Los lentes aca significa que el barrio te respalda.

> docker start hash-Image
> vi .openerp_serverrc
> ps uxa | grep odoo
> supervisor stop odoo
> su odoo
> vi .openerp_serverrc
    #hablar con José Morales para ver que hacer aquí
> supervisor start odoo


Grillos tutorial
=================================

deployvcmd restore -n <container-name> -z <backup_database> -s pass -x abastotal90 -t <develop/updates>

