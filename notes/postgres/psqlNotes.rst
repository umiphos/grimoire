# Vista vertical en una busqueda simple
Con **\x** podemos ver tener una vista vertical de los datos que estamos consultando, muy util para analizar mejor la informacion, es como un **read()** de un objeto.

# The PostgreSQL server failed to start. Please check the log output
(Source)[https://www.postgresql.org/docs/10/static/app-pg-ctl.html]
- Intentar usar **service postgres start**
- Revisar si tenemos espacio tanto en contenedor como en local con **df -h**
- Probablemente es el cluster que esta desactualizado, por lo tanto debemos reiniciar el cluster
  - **pg_lsclusters** nos mostrara el estado de las versiones de y donde podemos ver los logs
  - **pg_ctlcluster 9.6 main start** hara el proceso que no podemos con el primer comando
  - En el caso que manejo para este ejemplo con eso es mas que suficiente, intentar levantar nuevamente el servicio

Restaurando una base de datos en postgres
==========================================

createdb dbname
cd al area donde este la base.sql
psql dbname < database_bump.sql
enjoy.


Creando un backup para no actualizar cada vez si cometes un error
=================================================================

createdb -O odoo -T base_que_copiaremos base nueva


Copiando una base de datos sin hacer backup
===========================================
https://dba.stackexchange.com/questions/137636/how-to-duplicate-the-database-in-postgresql

createdb -T old_db new_db;

