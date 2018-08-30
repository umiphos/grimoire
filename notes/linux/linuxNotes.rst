### Like the name says, this is for linux notes, commands and useful stuff

Finding and removing stuff on linux
==================================

Link 2
https://www.cyberciti.biz/faq/linux-unix-how-to-find-and-remove-files/

Reloading .profile
===============

source ~/.profile

Comparar 2 archivos y generando un tercero con esos cambios
==========================================================

http://stackoverflow.com/questions/18069611/fastest-way-of-finding-differences-between-two-files-in-unix



Eliminar lineas vacias
===========================
http://stackoverflow.com/questions/706076/vim-delete-blank-lines

ELiminar una linea si contiene algun valor
===========================
http://vim.wikia.com/wiki/Delete_all_lines_containing_a_pattern


Enlace que paso grillo
====================
http://changes.deployv.net/api/wohlert80/updates

Copiar archivos dentro de contenedor
==================================

docker cp foo.txt mycontainer:/foo.txt
docker cp mycontainer:/foo.txt foo.txt


Escribir con vi en archivos protegidos
======================================

:w !sudo tee %

Cambiar puerto de escucha de postgresql
=======================================

vi /etc/postgresql/9.5/main/postgresql.conf


psql: FATAL: role "user" does not exist
========================================
sudo su - postgres
createuser username
createdb -O username username8
http://stackoverflow.com/questions/28213929/psql-fatal-role-does-not-exist

Uninstall postgresql
======================
http://stackoverflow.com/questions/2748607/how-to-thoroughly-purge-and-reinstall-postgresql-on-ubuntu

Permission denied to create database
==============================================

sudo -u postgres createdb -O user dbname_you_want
https://superuser.com/questions/507721/user-permissions-for-creating-postgresql-db

whoami kdb
https://superuser.com/questions/507721/user-permissions-for-creating-postgresql-db

Comandos utiles para postgres
=========================================
dropdb wohlert
createdb -O umiho -E utf8 wohlert
psql -f database.sql -d wohlert
createuser -d -S -R -P usuario


Revisar conexion a postgres
===============================
export PGHOST=IPSERVERLOCAL
export PGUSER=umiho
export PGPASSWORD=claveumiho

Respaldando una base de datos desde un archivo
=====================================

https://dba.stackexchange.com/questions/137636/how-to-duplicate-the-database-in-postgresql

Levantar una instansia local de cualquier repo
================================================

crear directorio de trabajo
cd a odoo
pip install -r requirements.txt
    rm lxml python-ldap
    apt-get install python-lxml python-ldap
editar lo que sea necesario de los errores que de este comando anterior
instalar por apt los paquetes eliminados de requirements.txt
python odoo-bin --addons-path=<lista_de_addons_> -s
cp ~/.odoorc odoo.conf
vi odoo.conf 
	aqui editaremos el dbfilter o la base de datos

python odoo-bin --conf=../odoo.conf
	con esto ejecutamos odoo como siempre lo hemos hecho


Restaurando una base de datos en postgres
==========================================

createdb dbname
cd al area donde este la base.sql
psql dbname < database_bump.sql
enjoy.


=============================================
Public key, private key, and a funny journey
=============================================

To see if your private key is secure
=====================================
ssh-keygen -y -f your_file.pem

Certificate Decoder (open a certificate and shows us all it's content)
======================================================================

openssl x509 -in certificate.crt -text -noout
https://www.sslhopper.com/certificate-decoder.html
https://www.sslshopper.com/ssl-converter.html

Certificate .crt to PEM
=============================

openssl x509 -in certificado.crt -inform PEM -out certificado.pem
openssl x509 -pubkey -noout < cert.pem > pubkey.pem
http://stackoverflow.com/questions/17560006/how-can-i-extract-a-key-from-an-ssl-certificate

Full class of certificates, really, here is tons of info
========================================================
https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs

How search with grep leaving out some files
=========================================================
Tested and working well in every environment so far
grep -r --color --exclude-dir={custom,lib,scripts} --exclude={*.xml,error_log} "beta" .

https://gist.github.com/a1phanumeric/5346170


Search and replace
=========================

grep -rl --exclude-dir=.git <keyword> |xargs sed -i 's/find/replace/g'

grep -rl will show us the results in a list
--exclude will do that, exclude a dir
<keyword> is what we are searching

| pipe is to apply another layer of analisis to the current list
xargs is to grab the previous results and apply another layer of application
sed -i is to replace
's/find/replace/g' string to find and replace in the results

