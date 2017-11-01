<?php
$server = "sql8.ezhostingserver.com";
$user = "plaimos_db_user";
$password = "oL7wY5Blou5hEd";
$database = 'plaimos_db';

$conn = odbc_connect("Driver={SQL Server};Server=$server;Database=$database;", $user, $password);




if ($conn){
    echo "Connection established.";
	$query = "insert into dbo.records (id_record,id_sensor,sensor_value,sensor_date,sensor_time) values (1,1,1,1,1)";

	
	$result = odbc_exec($conn,$query);
print $result;

	
	
	
	
	
	
	
	
}
	
else{
    die("Connection could not be established.");
}
?>