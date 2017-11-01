<?php



if(isset($_POST['archivos'])){
	$Host="127.0.0.1";
	$user="compras";
	$pass="";
	$FTP_con= ftp_connect($Host); 
	$login_result = ftp_login($FTP_con, $user, $pass);   

	$nombre_archivo= $_FILES["fail"]["name"];
	$extentation=$_FILES["fail"]["type"];
	$file_name=$_FILES["fail"]["name"];
	$myFile = $_FILES['fail']; // This will make an array out of the file information that was stored.
    $file = $myFile['tmp_name'];  //Converts the array into a new string containing the path name on the server where your file is.
	
	date_default_timezone_set("Mexico/General");
	$dathing=date("h_i_s");
	$nombre_archivo= $dathing.$nombre_archivo;
	
	echo "Temp: $file"; 
	echo "<br>" ;	
	echo "Type: $extentation" ;
	echo "<br>" ;
	echo "Name: $nombre_archivo";
	echo "<br>" ;	
		
	if (ftp_put($FTP_con,"/archivos/".$nombre_archivo."", $file, FTP_BINARY)) {
		echo "<span style='color:#F0A0BB'><h2>se ha cargado satisfactoriamente</h2></span>\n";
	} 
	else {
		echo "<span style='color:#FFA0BB'><h2>Hubo un problema durante la transferencia.</h2></span>\n";
	}
	ftp_close($FTP_con); 

}
?>
<html>
  <head></head>
  <body>
        <form enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF'];?>" method="POST">
           Dale clic! <input name="fail" type="file"/><br><br>
           <input type="submit" name="archivos" value="Upload File"/>
      </form>
  </body>
</html>