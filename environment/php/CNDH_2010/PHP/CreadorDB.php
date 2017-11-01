<?php
$link=mysql_connect('localhost','root','');
 if(!$link){
   die('Couldnot connect: ' . mysaql_error());
 }




if (mysql_query("CREATE DATABASE cndh",$link))
  {
  echo "Database created";
  }
else
  {
  echo "Error creating database: " . mysql_error();
  }



 


 $db_select=mysql_select_db("cndh",$link);


 ///crear tabla de comites
 
 $sql="CREATE TABLE comites (
  IDCOMITE double NOT NULL AUTO_INCREMENT,
  PRIMARY KEY(IDCOMITE),
  COMITE varchar(50),
  FECHA  varchar(15),
  DISTRITO int,  
  CP varchar(15),
  MUNICIPIO varchar(16),
   FOTOGRAFIA varchar(50)  
 )type=innodb";
 
 
 mysql_query($sql,$link);
 
 ///crea tabla de capacitaciones
 $sql="CREATE TABLE capacitaciones (
 IDCAPACITACIONES double NOT NULL AUTO_INCREMENT,
 PRIMARY KEY (IDCAPACITACIONES),
 IDCOMITE double,
 DERECHOS boolean,
 QUEJAS boolean,
 FUNCIONES boolean,
 foreign key comites_capacitaciones (IDCOMITE) references comites(IDCOMITE) ON DELETE CASCADE
 )type=innodb";
 mysql_query($sql,$link); 
 

 
/// /crear tabla de miembros de comite

 $sql="CREATE TABLE personas (
 IDPERSONA double NOT NULL AUTO_INCREMENT,
 PRIMARY KEY(IDPERSONA),
 FOTOGRAFIA   varchar(50),
 NOMBRES varchar(20),
 APATERNO varchar(10),
 AMATERNO varchar(10),
 SEXO varchar(6),
 FNACIMIENTO  varchar(20),
 OCUPACION    varchar(30),
 ESCOLARIDAD  varchar(15)
 )type=innodb";
 
 mysql_query($sql,$link); 
 
  /////crear tabla de datos de localizacion de miembros y solicitantes
 $sql="CREATE TABLE localizacion (
 IDLOCALIZACION double NOT NULL AUTO_INCREMENT,
 PRIMARY KEY(IDLOCALIZACION),
 TCELULAR varchar(20),
 TCASA    varchar(20),
 EMAIL    varchar(10),
 COLONIA   varchar(14),
 CALLE     varchar(14),
 NUMERO    varchar(14),
 DISTRITOFEDERAL varchar(5),
 DISTRITOLOCAL varchar(5),
 CP  varchar(5)
 )type=innodb";

mysql_query($sql,$link);
 

 
$sql="CREATE TABLE entregables (
 IDENTREGABLES double NOT NULL AUTO_INCREMENT,
 PRIMARY KEY(IDENTREGABLES),
 CAMISETA boolean,
 CBIENBENIDA boolean,
 CREDENCIAL boolean
 )";
 
 mysql_query($sql,$link); 
 
 
 $sql="CREATE TABLE miembros (
 IDMIEMBRO double NOT NULL AUTO_INCREMENT,
 PRIMARY KEY(IDMIEMBRO),
 IDCOMITE boolean,
 IDPERSONA boolean,
 IDENTREGABLES boolean,
 IDLOCALIZACION boolean,
 PUESTO       varchar(10) ,
 foreign key comites_miembros (IDCOMITE) references comites(IDCOMITE) ON DELETE CASCADE,
 foreign key personas_miembros (IDPERSONA) references personas(IDPERSONA) ON DELETE CASCADE,
 foreign key entregables_miembros (IDENTREGABLES) references entregables(IDENTREGABLES) ON DELETE CASCADE,
 foreign key localizacion_miembros (IDLOCALIZACION) references localizacion(IDLOCALIZACION) ON DELETE CASCADE
 )";
 
 mysql_query($sql,$link); 

 
 $sql="CREATE TABLE gestiones (
 IDGESTIONES double NOT NULL AUTO_INCREMENT,
 PRIMARY KEY(IDGESTIONES),
 IDPERSONA double,
 IDCOMITE double, 
 FINICIO varchar(15),
 FTERMINO varchar(15),
 ATENDIDOPOR  varchar(40), 
 ASUNTO varchar(30),
 TIPO VARCHAR(8),
 CANALIZADO varchar(20), 
 DESCRIPCION varchar(100),
 foreign key comites_gestiones (IDCOMITE) references comites(IDCOMITE),
 foreign key persona_gestiones (IDPERSONA) references personas(IDPERSONA)
 )";
 
 mysql_query($sql,$link);
 
 

$sql = "CREATE TABLE usuario( ID int(11) primary key auto_increment not null,
 USUARIO varchar(15),
  PASAPORTE varchar(15),
  PRIBILEGIOS int(11)) ";

  mysql_query($sql,$link);

 
 
 
 

 
 
 
?>