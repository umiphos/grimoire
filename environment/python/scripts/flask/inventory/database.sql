DROP DATABASE IF EXISTS FM4Demo;
CREATE DATABASE IF NOT EXISTS  FM4Demo;

USE FM4Demo;
CREATE TABLE admin_info(
	id_admin	INT NOT NULL AUTO_INCREMENT,
    user_name	VARCHAR(50),
	pass		VARCHAR(50),
    secret		VARCHAR(50),
    name		VARCHAR(50),
    last_name	VARCHAR(50),
    mail		VARCHAR(50),
	PRIMARY KEY (id_admin)
);
CREATE TABLE volunteer(
	id_volunter			int NOT NULL AUTO_INCREMENT,
	user_name_volunter	VARCHAR(50),
	pass			VARCHAR(50),
	name_volunter		VARCHAR(50),
	last_name_volunter	VARCHAR(50),
	email_volunter		VARCHAR(50),
	PRIMARY KEY (id_volunter)
);
CREATE TABLE migrant(
	id_migrant			int NOT NULL AUTO_INCREMENT,
	name				VARCHAR(50),
	last_name			VARCHAR(50),
	photo				VARCHAR(100),
	id_volunter			int,	
	PRIMARY KEY (id_migrant)
);

INSERT INTO  admin_info(user_name,pass,name,last_name,mail)	VALUES ("admin","pass","test","TEST","this@test.com");
INSERT INTO  volunteer(user_name_volunter,pass,name_volunter,last_name_volunter,email_volunter)	VALUES ("volunteer","pass","test","TEST","this@test.com");

CREATE PROCEDURE InsertAdmin
(
    IN  var1		VARCHAR(50),
    IN	var2		VARCHAR(50),
    IN  var3		VARCHAR(50),
    IN  var4    	VARCHAR(50),
    IN  var5		VARCHAR(50)
)

INSERT INTO  admin_info
(user_name,pass,name,last_name,mail)	
VALUES (var1,var2,var3,var4,var5);


CREATE PROCEDURE InsertVolunteer
(
    IN  var1    VARCHAR(50),
    IN	var2    VARCHAR(50),
    IN  var3    VARCHAR(50),
    IN  var4    VARCHAR(50),
    IN  var5    VARCHAR(50)
)

INSERT INTO  volunteer (user_name_volunter,pass,name_volunter,last_name_volunter,email_volunter)
VALUES (var1,var2,var3,var4,var5);


CREATE PROCEDURE InsertMigrant
(
    IN  var1			VARCHAR(50),
    IN	var2		VARCHAR(50),
    IN  var3			VARCHAR(50),
    IN 	var4		int
)
INSERT INTO  migrant(name,last_name,photo,id_volunter)	
VALUES (var1,var2,var3,var4);
 
CREATE PROCEDURE LoginAdmin
(
    IN var1     varchar(50),
    IN var2     varchar(50)
)
SELECT * FROM admin_info WHERE user_name=var1 AND pass=var2;


CREATE PROCEDURE LoginVolunteer
(
    IN var1		varchar(50),
    IN var2		varchar(50)
)
SELECT * FROM volunteer WHERE user_name_volunter=var1 AND pass=var2;

CREATE PROCEDURE SelectAllMigrants()
SELECT * FROM migrant ORDER BY id_record DESC;


