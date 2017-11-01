<html>
<head>
</head>
<body> 
	<form enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF'];?>" method="GET">
		User  <th><input type='text' name="user"></th> <br>
		Pass  <th><input type='password' name="pass"></th> <br>
		<input type="submit" name="solicitud"/>
	</form>
 </body>
</html>
<?php
if(isset($_GET['solicitud'])){
$user=$_GET['user'];
$pass=$_GET['pass'];

echo "Hola $user";
echo "<br>";
echo "Contrasenia: $pass";
echo "<br>";
$dbhost='127.0.0.1';
$dbusername='root';
$dbuserpass='';
$dbname='compras';
$sql = "SELECT * FROM compras";
$conexion=mysql_connect ($dbhost, $dbusername, $dbuserpass);
$query = mysql_query($sql,$conexion);
$db_selected = mysql_select_db("compras",$conexion);
$sql="SELECT * FROM `directores` WHERE  `user`='".$user."' AND `contrasena`='".$pass."'";

	if($result = mysql_query($sql,$conexion)){
		print_r(mysql_fetch_array($result));
		echo "Redireccionando...Espere";
		sleep(1);
		 ///echo "<input type='hidden' name='id_commie' value='".$rew."'></>";
		
		setcookie("user",$user, time()+3600);
		setcookie("pass",$pass, time()+3600);

		header ("Location: http://127.0.0.1/new_users.php");

	}
	else{
		echo "nop, este usuario no ta'";
	}

mysql_close($conexion);	
}
?>