<?php
include ("pdff.php"); 
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);



if (isset ($_GET["chekie"])){
	$prueba=$_GET['docu'];
	switch ($prueba[0]) {
		case 1:
		
			bienvenidap();
			
			echo "<br>";
			break;
		case 2:
			nombramientop();
			break;
		case 3:
			foreach ($_GET['chekie'] as $id){
				echo "<form action='pdfs.php' method='GET'>";
				echo "hola, estoy  comprobando que exista chekie y que docu sea igual a $id";
				echo "<br>";
				echo "<input type='hidden' name='test[]' value='".$id."'></>";
			}
	
			echo "<fieldset>";
			echo "<textarea name='metiendo_texto' rows='30' cols='69'>...Tus comentarios aquí...</textarea>";
			echo "<input name='membretado' type='submit' value='Mostrar'>";

			break;
		case 4:
			sobrep();
			
		break;
		case 5:
			credp();
			
		break;
	}
}
if(isset ($_GET['membretado'])){

membretadap($_GET['metiendo_texto']);

}

//hasta aqui para personas

//desde aqui para comites

	//echo "<META HTTP-EQUIV='refresh' CONTENT='2; URL=pdfs.php'>"; 
	/*
print('<pre>');
print_r($_GET);
print('</pre>');
echo "</form>";
*/
if (isset ($_GET["commies"])){
	$prueba=$_GET['docu'];
	
	
	$com=$_GET['commies'];
		$resultados = mysql_query("
				SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA,miembros.IDCOMITE
				FROM miembros
				INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
				INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
				INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
				WHERE miembros.IDCOMITE=$com[0]");
	while($row=mysql_fetch_array($resultados)){
	//echo "hola  ";
	//echo "<br>";
	$a=$a+1;
	
	}
	//echo $a;		

	switch ($prueba[0]) {
		case 1:
			//echo "hola, entraste al documento 1";
			bienvenidac($a);
			//echo "hola, estoy validando que la variable a=$a tenga un valor";
			break;
		case 2:
			//echo "hola, entraste al documento 2";
			nombramientoc($a);
			break;
		case 3:
			echo "<form action='pdfs.php' method='GET'>";
			echo "hola, estoy  comprobando que exista chekie y que docu sea igual a $id";
			echo "<br>";
			//echo "<input type='hidden' name='test' value='".$id."'></>";
			echo "<input type='hidden' name='test' value='".$a."'></>";
			echo "<fieldset>";
			echo "<textarea name='metiendo_texto' rows='30' cols='56'>...Tus comentarios aquí...</textarea>";
			echo "<input name='membretadoc' type='submit' value='Mostrar'>";
			break;
		case 4:
			sobrec($a);
			
		break;
		case 5:
			credc($a);
			
		break;
	}
}
if(isset ($_GET['membretadoc'])){

membretadoc($_GET['test'],$_GET['metiendo_texto']);
echo $a;
}


//}

?>



