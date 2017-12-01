DROP DATABASE IF EXISTS Qamaleontis;
CREATE DATABASE IF NOT EXISTS  Qamaleontis;

USE Qamaleontis;
CREATE TABLE PERSONAL(
	id_tower	int,
    lat			varchar(50),
	lon			varchar(50),
    ip			varchar(50)
);
CREATE TABLE SENSORS(
	id_sensor		int NOT NULL,
    sensor_name		varchar(100),
	description		varchar(150),
	sensor_number	int,
	PRIMARY KEY (id_sensor)
);
CREATE TABLE RECORDS(
    id_record INT NOT NULL AUTO_INCREMENT,
    id_sensor INT,
    id_tower INT,
    data VARCHAR(100),
    date VARCHAR(100),
    time VARCHAR(100),
    PRIMARY KEY (id_record)
);
CREATE TABLE KNOWN_TOWERS(
	id_tower		int NOT NULL AUTO_INCREMENT,
    lat			varchar(50),
	lon			varchar(50),
	
    jumps			int,
    ip				varchar(50),
    ip_port			varchar(50),
    PRIMARY KEY (id_tower)
);
CREATE TABLE JUMPS(
	jumps			int,
    id_mac			varchar(50),
	t_lat			varchar(50),
	t_lon			varchar(50)
	
);

#nueva logica de desarrollo
create table ROLEPLAYING(
    role		varchar(50),
    descr		varchar(150)
    
    );
CREATE TABLE EVENTS(
	id_event		int NOT NULL AUTO_INCREMENT,
	e_lat			varchar(50),
	e_lon			varchar(50),
	category		varchar(50),
    date 			VARCHAR(100),
    time 			VARCHAR(100),	
	PRIMARY KEY (id_event)
);

#La diferencia es que este solo contendra el ac
CREATE TABLE CURRENT_EVENT(
	id_event		int NOT NULL,
	e_lat			varchar(50),
	e_lon			varchar(50),
	category		varchar(50),
	date 			VARCHAR(100),
    time 			VARCHAR(100),
	active			smallint,
	PRIMARY KEY (id_event)
);
#aqui a lo que pertenecen a las tablas generales
/*Comment*/

INSERT INTO PERSONAL(id_tower,ip,lat,lon) VALUES(1,"192.168.5.174","---","---");
INSERT INTO CURRENT_EVENT(id_event,e_lat,e_lon,category,active,	date,time) VALUES ('1', '1', '1', '1', 1,"date","time");

#aqui agregamos los valores que son necesarios en todas las tablas de desarrollo
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(0,"Dn","Direccion minima,viento, 0-180",0);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(1,"Dm","Direccion promedio,viento, 0-180",1);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(2,"Dx","Direccion maxima,viento, 0-180",2);

INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(3,"Sn","Velocidad minima,viento,m/s",3);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(4,"Sm","Velocidad media,viento,m/s",4);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(5,"Sx","Velocidad maxima,viento,m/s",5);

INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(6,"Rc","Cantidad,lluvia,caudal/m2",6);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(7,"Rd","Duracion,lluvia,s",7);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(8,"Ri","Intensidad,lluvia",8);

INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(9,"Hc","Cantidad,granizo",9);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(10,"Hd","Duracion,granizo",10);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(11,"Hi","Intensidad,granizo",11);

INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(12,"Rp","Pico,lluvia",12);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(13,"Hp","Pico,Granizo",13);

INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(14,"Th","Temperatura,calentador",14);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(15,"Vh","Voltaje,calentador",15);

INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(16,"Vs","Voltaje,alimentacion",16);

INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(100,"Pr","Presion atmosferica",100);
INSERT INTO SENSORS(id_sensor,sensor_name,description,sensor_number) VALUES(101,"Tp","Temperatura promedio",101);




#This SP makes easy to search for data in 2 tables.
USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Select_Last_Sensors
()
BEGIN
	SELECT *
	FROM
	(
		SELECT 
     	id_record,
		id_tower,
        data,
        date,
        time,
        sensor_name,
        description,
    	sensor_number
		FROM RECORDS,SENSORS 
		WHERE RECORDS.id_sensor=SENSORS.id_sensor 
		ORDER BY id_record DESC
	)
SUB GROUP BY sensor_number;
END //
DELIMITER ;

#This is simple a lazzy way to get the personal info from this device
USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Select_Personal_Info
()
BEGIN
	SELECT * FROM PERSONAL WHERE 1;
END //
DELIMITER ;

#The name says it all...
USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Update_Personal
(
IN latitude    	varchar(50),
IN longitude		varchar(50)
)
BEGIN
	UPDATE PERSONAL
    SET
    	lat=latitude,
        lon=longitude
    WHERE 
    	id_tower=1;
    	
END //
DELIMITER ;

#The name says it all...
USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Create_Event
(
IN latitude    	varchar(50),
IN longitude	varchar(50),
IN category		varchar(50),
IN time			varchar(50),
IN date			varchar(50)
)
BEGIN

INSERT INTO EVENTS
		(e_lat,e_lon,category,time,date)
	VALUES
		(latitude,longitude,category,time, date);

	
    	
END //
DELIMITER;


USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Select_Last_Event
()
BEGIN
	SELECT * FROM EVENTS Order by id_event DESC LIMIT 1;
END //
DELIMITER ;

USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Update_Current_Event
(
IN latitude    	varchar(50),
IN longitude	varchar(50),
IN category		varchar(50),
IN tim		varchar(50),
IN dat			varchar(50)
)
BEGIN
	UPDATE CURRENT_EVENT 
	SET 
		e_lat = latitude,
		e_lon = longitude,
		category = category,
		time =tim,
		date = dat
	WHERE CURRENT_EVENT.id_event = 1;
END //
DELIMITER ;
#TestS under this bar
######################################################
######################################################
######################################################
USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Select_Last_Current_Event
()
BEGIN
	SELECT * FROM CURRENT_EVENT Order by id_event DESC LIMIT 1;
END //
DELIMITER ;


USE Qamaleontis;
DELIMITER //
CREATE PROCEDURE Select_Last_Sensors_Simple
()
BEGIN
	SELECT * FROM (SELECT * FROM RECORDS ORDER BY id_record DESC) RECORDS Group BY id_sensor;
END //
DELIMITER ;



