<?php

function bienvenidap(){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);
//echo "hola estoy dando salida a pdff";
require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
	function Footer()
		{
		$fecha2=date("d/m/Y");
			$this->SetY(-30);
			
				
			$this->SetFont('Arial','I',7);
			$this->Cell(0,0,'_____________________________________________________________________________________________________',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Degollado No. 79, Zona Centro. C.P. 28000. Colima, Col. Teléfonos: (312) 31.477.95;  31.471.86;  31.229.94. ',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Lada sin Costo: 01.800.696.7672. Página Web: www.cdhcolima.org.mx  Celular:   044-312-155 13 33.',0,0,'C');
			$this->Ln(5);	
		}
	}

	if ($a==0){
	//echo "hola, a es igualita a cero";
	$pdf=new PDF();
	$ultimo=$_GET['chekie'];
	$salida=count($ultimo); 
	}
	foreach ($_GET["chekie"] as $id){
				
				
				$resultados = mysql_query("
				SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA
				FROM miembros
				INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
				INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
				INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
				WHERE miembros.IDMIEMBRO=$id");

		while($row=mysql_fetch_array($resultados)){
		//aqui inicia
		
		//echo $salida;
			if ($salida!=0){
				$a=1;
				
				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];

				$pdf->AliasNbPages();
				$pdf->AddPage();
				$pdf->SetXY(0,0);

				$pdf->SetLeftMargin(17);
				$pdf->SetRightMargin(30);
				$pdf->SetTopMargin(30); 
				$pdf->SetFont('Arial','B',12);
				$pdf->Image('PDF/imagenes/1.PNG',20,20,40);
				$pdf->Ln(30);
				$pdf->Cell(0,5,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO',0,1,'R');
				$pdf->Ln(2);
				$pdf->Cell(0,5,'DE COLIMA',0,1,'R');
				$pdf->Ln(25);
				$pdf->SetFont('Arial','B',12);

				$pdf->Image('PDF/imagenes/firma.png',85,190,40,40);

				$pdf->Cell(40,10,'C.'.$nombreS." ".$nombreP." ".$nombreM,0,1);
				$pdf->SetFont('Times','',12);
				$pdf->Cell(0,10,'P r e s e n t e ');
				$pdf->Ln(10);
				$pdf->Write(5,'        En mi calidad de Presidente de la Comisión de Derechos Humanos del Estado de Colima, y amigo tuyo, me complace saludarte, felicitarte y darte la bienvenida como');
				$pdf->SetFont('Arial','B',12);
				$pdf->write(5,' '.$cargo);
				$pdf->SetFont('Times','',12);
				$pdf->Write(5,' del Comité Voluntario de Promoción y Defensa de los Derechos Humanos de la colonia ');
				$pdf->SetFont('Arial','B',12);
				$pdf->write(5,' '.$colonia);
				$pdf->SetFont('Times','',12);
				$pdf->Write(5,' del municipio de ');
				$pdf->SetFont('Arial','B',12);
				$pdf->write(5,' '.$municipio);
				$pdf->SetFont('Times','',12);
				$pdf->Write(5,', Colima. ');
				$pdf->Ln(10);

				$pdf->Write(5,'Estoy seguro que sumando esfuerzos lograremos consolidar en nuestra entidad el respeto de las autoridades a la dignidad de las personas y a sus derechos humanos; fomentar la cultura de la legalidad y el cumplimiento de nuestros deberes fortaleciendo así las instituciones y la vida democrática. ');
				$pdf->Ln(15);
				$pdf->Write(5,'Sin más por el momento te reitero mi disposición y la de todo el equipo que conformamos este Organismo Público de trabajar por tus derechos, los de todos los colimenses y de las personas que viven en el Estado o transitan por él.');
				$pdf->Ln(20);
				$pdf->SetFont('Arial','B',12);  
				$pdf->Ln(10);
				$pdf->Write(5,'¡No estás solo, la Comisión de Derechos Humanos del Estado de Colima está de tu lado!');
				$pdf->SetFont('Times','',12);
				$pdf->Ln(10);
				$pdf->Cell(0,0,'A t e n t a m e n t e.',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'Colima, Col.'.$fecha,0,0,'C');

				$pdf->Ln(30);
				$pdf->SetFont('Arial','B',12);  
				$pdf->Cell(0,0,'LIC. ROBERTO CHAPULA DE LA MORA',0,0,'C');
				$pdf->SetFont('Times','',12);
				$pdf->Ln(5);
				$pdf->Cell(0,0,'P R E S I D E N T E ',0,0,'C');
			}
			$salida=$salida-1;

		//hasta aqui el ciclo
		//si el es ultimo 
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function nombramientop(){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);

require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
	}

	if ($a==0){
	$pdf=new PDF();
	$ultimo=$_GET['chekie'];
	$salida=count($ultimo); 
	}
	foreach ($_GET["chekie"] as $id){
				
				
				$resultados = mysql_query("
				SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA,PUESTO
				FROM miembros
				INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
				INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
				INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
				WHERE miembros.IDMIEMBRO=$id");

		while($row=mysql_fetch_array($resultados)){
			if ($salida!=0){
				$a=1;
				
								
				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];

				$cargo =$row['PUESTO']; 

				$colonia=$row['COLONIA']; 

				$municipio=$row['MUNICIPIO']; 

				$fecha =$row ['FECHA'];



				$pdf->AliasNbPages();
				$pdf->AddPage();

				//$pdf->SetMargins(30) ;
				$pdf->SetLeftMargin(17);
				$pdf->SetRightMargin(30);
				$pdf->SetTopMargin(30); 

				$pdf->SetXY(0,0);
				$pdf->Image('PDF/imagenes/1.PNG',94,15,30);
				$pdf->AddFont('poorich');

				$pdf->AddFont('poorich','','poorich.php');
				$pdf->SetFont('poorich','',12);
				$pdf->Ln(25);
				$pdf->Cell(0,0,'Con fundamento en lo dispuesto por',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'los artículos 4, 7, 8, 10, 11, 13, 15 y',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'demás relativos del Reglamento',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'aplicable a los  Comités Voluntarios',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'de Promoción y Defensa de los Derechos Humanos aprobado en sesión ordinaria del Honorable Consejo',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'de  la Comisión  de  Derechos  Humanos del Estado  de Colima el  17 de Mayo de 2010 y cumpliendo con',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'los  requisitos  previstos  en  el  ordenamiento  anteriormente  citado,  la  Comisión   Estatal  por  conducto',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'del  Presidente,  LIC.  ROBERTO  CHAPULA  DE  LA  MORA otorga a:',0,0,'L');

				$pdf->Ln(15);
				$pdf->AddFont('poorich','B','poorich.php');
				$pdf->SetFont('poorich','B',16);
				$pdf->Cell(0,0,''.$nombreS." ".$nombreP." ".$nombreM,0,0,'C');

				$pdf->Ln(15);
				$pdf->SetFont('poorich','',12);
				$pdf->Cell(0,0,'el presente ',0,0,'C');

				$pdf->Ln(15);
				$pdf->SetFont('poorich','',17);
				$pdf->Cell(0,0,'N  O  M  B  R  A  M  I  E  N  T  O ',0,0,'C');


				$pdf->Ln(15);
				$pdf->SetFont('poorich','',12);
				$pdf->Cell(0,0,'de',0,0,'C');


				$pdf->Ln(15);
				$pdf->SetFont('poorich','B',18);
				$pdf->Cell(0,0,''.$cargo,0,0,'C');

				$pdf->Ln(15);
				$pdf->AddFont('poorich','I','poorich.php');
				$pdf->SetFont('poorich','I',16);
				$pdf->Cell(0,0,'DEL COMITÉ VOLUNTARIO DE PROMOCIÓN Y DEFENSA DE',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'LOS DERECHOS HUMANOS DE LA COLONIA  '.$colonia,0,0,'C');


				$pdf->Ln(15);
				$pdf->SetFont('poorich','I',12);
				$pdf->Cell(0,0,'En la ciudad  de Colima, Colima, quedando obligado a ejercer las facultades y deberes que se le',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'confieren  con el objeto esencial de promover  acciones tendientes a impulsar  la observancia  de',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'los Derechos Humanos y el respeto a la dignidad de las personas, vigilando la debida  actuación',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'de las autoridades, canalizando a la  población de  su  comunidad a este Organismo Estatal para',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'brindarles la  orientación,  apoyo  y  protección  previstas  en  nuestro ordenamiento jurídico.         ',0,0,'C');

				$pdf->Ln(15);
				$pdf->Cell(0,0,'A T E N T A M E N T E',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$fecha,0,0,'C');


				$pdf->Ln(15);
				$pdf->Cell(0,0,'LIC. ROBERTO CHAPULA DE LA MORA',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'Presidente ',0,0,'C');


			}
			$salida=$salida-1;

		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function membretadap($texto){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);

require('PDF/lib/PDF/fpdf.php');
	
	class PDF extends FPDF
	{
		function Footer()
		{
		$fecha2=date("d/m/Y");
			$this->SetY(-70);
			$this->Cell(0,0,'A t e n t a m e n t e.',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Colima, Col., a ',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,''.$fecha2,0,0,'C');
			$this->Ln(15);
			$this->Cell(0,0,'LIC. ROBERTO CHAPULA DE LA MORA',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'P R E S I D E N T E',0,0,'C');
			$this->Ln(10);
				
			$this->SetFont('Arial','I',7);
			$this->Cell(0,0,'_____________________________________________________________________________________________________',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Degollado No. 79, Zona Centro. C.P. 28000. Colima, Col. Teléfonos: (312) 31.477.95;  31.471.86;  31.229.94. ',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Lada sin Costo: 01.800.696.7672. Página Web: www.cdhcolima.org.mx  Celular:   044-312-155 13 33.',0,0,'C');
			$this->Ln(5);	
		}

	}

	if ($a==0){
	//echo "hola, a es igualita a cero";
	$pdf=new PDF();
	$ultimo=$_GET['test'];
	$salida=count($ultimo); 
	}
	foreach ($_GET["test"] as $id){
				
				
				$resultados = mysql_query("
				SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA
				FROM miembros
				INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
				INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
				INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
				WHERE miembros.IDMIEMBRO=$id");

		while($row=mysql_fetch_array($resultados)){
			if ($salida!=0){
				$a=1;
				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];
				$pdf->AliasNbPages();
				$pdf->AddPage();
				//$pdf->SetMargins(30) ;
				$pdf->SetLeftMargin(17);
				$pdf->SetRightMargin(30);
				$pdf->SetTopMargin(30); 

				$pdf->Image('PDF/imagenes/1.PNG',15,15,30);
				$pdf->Image('PDF/imagenes/firma.PNG',80,230,40);
				
				$pdf->SetXY(0,0);
				$pdf->SetFont('Arial','B',12);
				$pdf->Ln(25);
				$pdf->Cell(0,0,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'DE COLIMA',0,0,'R');

				$pdf->Ln(20);
				$pdf->Cell(0,0,''.$nombreS." ".$nombreP." ".$nombreM,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cargo,0,0,'L');
				$pdf->Ln(5);
				$pdf->SetFont('Arial','',12);
				$pdf->Cell(0,0,'Comité Voluntario de Promoción y Defensa de La Colonia '.$colonia,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'Del municipio de '.$municipio,0,0,'L');
				$pdf->Ln(5);
				$pdf->write(5,''.$texto);	
				
			}
			$salida=$salida-1;

		//hasta aqui el ciclo
		//si el es ultimo 
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function sobrep(){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);
//echo "hola estoy dando salida a pdff";
require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
	//Cabecera de página
	}
		
	if ($a==0){
	//echo "hola, a es igualita a cero";
	$pdf=new PDF();
	$ultimo=$_GET['chekie'];
	$salida=count($ultimo); 
	}
	foreach ($_GET["chekie"] as $id){
		$resultados = mysql_query("
		SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA,PUESTO,MUNICIPIO,
		FECHA,COMITE,CALLE,NUMERO,localizacion.CP
		FROM miembros
		INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
		INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
		WHERE miembros.IDMIEMBRO=$id");

		while($row=mysql_fetch_array($resultados)){
		//aqui inicia
		
		//echo $salida;
			if ($salida!=0){
				$a=1;
	
				$pdf->AliasNbPages();
				$pdf->AddPage();
				$pdf->SetXY(0,0);
				//$pdf->SetXY(0,0);
				$pdf->SetLeftMargin(20);
				$pdf->SetRightMargin(15);
				$pdf->SetTopMargin(30);

				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];
				$calle=$row ['CALLE'];
				$numero=$row ['NUMERO'];
				$cp=$row ['CP'];
				$comite=$row['COMITE']; 

				//$pdf->AddFont('Arial','','poorich.php');
				$pdf->SetFont('Arial','',11);

				$pdf->Image('PDF/imagenes/1.PNG',20,15,40);
				$pdf->Ln(30);
				$pdf->Cell(0,0,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO DE COLIMA',0,0,'R');
				$pdf->Ln(25);

				$pdf->Cell(0,0,''.$nombreS.' '.$nombreP.' '.$nombreM,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cargo,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$comite,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$calle." ".$numero." ".$colonia,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$municipio.", Colima",0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cp,0,0,'L');
				$pdf->Ln(5);

			}
			$salida=$salida-1;
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function bienvenidac($salida){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);

require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
	function Footer()
		{
		$fecha2=date("d/m/Y");
			$this->SetY(-30);
			
				
			$this->SetFont('Arial','I',7);
			$this->Cell(0,0,'_____________________________________________________________________________________________________',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Degollado No. 79, Zona Centro. C.P. 28000. Colima, Col. Teléfonos: (312) 31.477.95;  31.471.86;  31.229.94. ',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Lada sin Costo: 01.800.696.7672. Página Web: www.cdhcolima.org.mx  Celular:   044-312-155 13 33.',0,0,'C');
			$this->Ln(5);	
		}
	}

	if ($a==0){
	//echo "hola, a es igualita a cero";
	$pdf=new PDF();
	//$ultimo=$_GET['chekie'];
	//$salida=count($ultimo); 
	$control=$salida;
	}
	while($control!=0){
	//foreach ($_GET["chekie"] as $id){
				
				
				$resultados = mysql_query("
				SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA
				FROM miembros
				INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
				INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
				INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
				WHERE miembros.IDMIEMBRO=$control");
				$control=$control-1;

		while($row=mysql_fetch_array($resultados)){
		//aqui inicia
		
		//echo $salida;
			if ($salida!=0){
				$a=1;
				
				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];

				$pdf->AliasNbPages();
				$pdf->AddPage();
				$pdf->SetXY(0,0);

				$pdf->SetLeftMargin(17);
				$pdf->SetRightMargin(30);
				$pdf->SetTopMargin(30); 
				$pdf->SetFont('Arial','B',12);
				$pdf->Image('PDF/imagenes/1.PNG',20,20,40);
				$pdf->Ln(30);
				$pdf->Cell(0,5,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO',0,1,'R');
				$pdf->Ln(2);
				$pdf->Cell(0,5,'DE COLIMA',0,1,'R');
				$pdf->Ln(25);
				$pdf->SetFont('Arial','B',12);

				$pdf->Image('PDF/imagenes/firma.png',85,190,40,40);

				$pdf->Cell(40,10,'C.'.$nombreS." ".$nombreP." ".$nombreM,0,1);
				$pdf->SetFont('Times','',12);
				$pdf->Cell(0,10,'P r e s e n t e ');
				$pdf->Ln(10);
				$pdf->Write(5,'        En mi calidad de Presidente de la Comisión de Derechos Humanos del Estado de Colima, y amigo tuyo, me complace saludarte, felicitarte y darte la bienvenida como');
				$pdf->SetFont('Arial','B',12);
				$pdf->write(5,' '.$cargo);
				$pdf->SetFont('Times','',12);
				$pdf->Write(5,' del Comité Voluntario de Promoción y Defensa de los Derechos Humanos de la colonia ');
				$pdf->SetFont('Arial','B',12);
				$pdf->write(5,' '.$colonia);
				$pdf->SetFont('Times','',12);
				$pdf->Write(5,' del municipio de ');
				$pdf->SetFont('Arial','B',12);
				$pdf->write(5,' '.$municipio);
				$pdf->SetFont('Times','',12);
				$pdf->Write(5,', Colima. ');
				$pdf->Ln(10);

				$pdf->Write(5,'Estoy seguro que sumando esfuerzos lograremos consolidar en nuestra entidad el respeto de las autoridades a la dignidad de las personas y a sus derechos humanos; fomentar la cultura de la legalidad y el cumplimiento de nuestros deberes fortaleciendo así las instituciones y la vida democrática. ');
				$pdf->Ln(15);
				$pdf->Write(5,'Sin más por el momento te reitero mi disposición y la de todo el equipo que conformamos este Organismo Público de trabajar por tus derechos, los de todos los colimenses y de las personas que viven en el Estado o transitan por él.');
				$pdf->Ln(20);
				$pdf->SetFont('Arial','B',12);  
				$pdf->Ln(10);
				$pdf->Write(5,'¡No estás solo, la Comisión de Derechos Humanos del Estado de Colima está de tu lado!');
				$pdf->SetFont('Times','',12);
				$pdf->Ln(10);
				$pdf->Cell(0,0,'A t e n t a m e n t e.',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'Colima, Col.'.$fecha,0,0,'C');

				$pdf->Ln(30);
				$pdf->SetFont('Arial','B',12);  
				$pdf->Cell(0,0,'LIC. ROBERTO CHAPULA DE LA MORA',0,0,'C');
				$pdf->SetFont('Times','',12);
				$pdf->Ln(5);
				$pdf->Cell(0,0,'P R E S I D E N T E ',0,0,'C');
			}
			$salida=$salida-1;

		//hasta aqui el ciclo
		//si el es ultimo 
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function nombramientoc($salida){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);

require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
	
	}

	if ($a==0){
	$pdf=new PDF();
	$control=$salida;
	}
	while($control!=0){
	
				
				
		$resultados = mysql_query("
		SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA
		FROM miembros
		INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
		INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
		WHERE miembros.IDMIEMBRO=$control");
		$control=$control-1;

		while($row=mysql_fetch_array($resultados)){
			if ($salida!=0){
				$a=1;
							
				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];

				$cargo =$row['PUESTO']; 

				$colonia=$row['COLONIA']; 

				$municipio=$row['MUNICIPIO']; 

				$fecha =$row ['FECHA'];



				$pdf->AliasNbPages();
				$pdf->AddPage();

				//$pdf->SetMargins(30) ;
				$pdf->SetLeftMargin(30);
				$pdf->SetRightMargin(30);
				$pdf->SetTopMargin(30); 

				$pdf->SetXY(0,0);
				$pdf->Image('PDF/imagenes/1.PNG',94,15,30);
				$pdf->AddFont('poorich');

				$pdf->AddFont('poorich','','poorich.php');
				$pdf->SetFont('poorich','',12);
				$pdf->Ln(25);
				$pdf->Cell(0,0,'Con fundamento en lo dispuesto por',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'los artículos 4, 7, 8, 10, 11, 13, 15 y',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'demás relativos del Reglamento',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'aplicable a los  Comités Voluntarios',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'de Promoción y Defensa de los Derechos Humanos aprobado en sesión ordinaria del Honorable Consejo',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'de  la Comisión  de  Derechos  Humanos del Estado  de Colima el  17 de Mayo de 2010 y cumpliendo con',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'los  requisitos  previstos  en  el  ordenamiento  anteriormente  citado,  la  Comisión   Estatal  por  conducto',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'del  Presidente,  LIC.  ROBERTO  CHAPULA  DE  LA  MORA otorga a:',0,0,'L');

				$pdf->Ln(15);
				$pdf->AddFont('poorich','B','poorich.php');
				$pdf->SetFont('poorich','B',16);
				$pdf->Cell(0,0,''.$nombreS." ".$nombreP." ".$nombreM,0,0,'C');

				$pdf->Ln(15);
				$pdf->SetFont('poorich','',12);
				$pdf->Cell(0,0,'el presente ',0,0,'C');

				$pdf->Ln(15);
				$pdf->SetFont('poorich','',17);
				$pdf->Cell(0,0,'N  O  M  B  R  A  M  I  E  N  T  O ',0,0,'C');


				$pdf->Ln(15);
				$pdf->SetFont('poorich','',12);
				$pdf->Cell(0,0,'de',0,0,'C');


				$pdf->Ln(15);
				$pdf->SetFont('poorich','B',18);
				$pdf->Cell(0,0,''.$cargo,0,0,'C');

				$pdf->Ln(15);
				$pdf->AddFont('poorich','I','poorich.php');
				$pdf->SetFont('poorich','I',16);
				//$pdf->Cell(0,0,'DEL COMITÉ VOLUNTARIO DE PROMOCIÓN Y DEFENSA DE',0,0,'C');
				//$pdf->Ln(5);
				//$pdf->Cell(0,0,'LOS DERECHOS HUMANOS DE LA COLONIA  '.$colonia."",0,0,'C');
				$pdf->write(5,"DEL COMITÉ VOLUNTARIO DE PROMOCIÓN Y DEFENSA DE LOS DERECHOS HUMANOS DE LA COLONIA".$colonia);

				$pdf->Ln(15);
				$pdf->SetFont('poorich','I',12);
				$pdf->Cell(0,0,'En la ciudad  de Colima, Colima, quedando obligado a ejercer las facultades y deberes que se le',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'confieren  con el objeto esencial de promover  acciones tendientes a impulsar  la observancia  de',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'los Derechos Humanos y el respeto a la dignidad de las personas, vigilando la debida  actuación',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'de las autoridades, canalizando a la  población de  su  comunidad a este Organismo Estatal para',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'brindarles la  orientación,  apoyo  y  protección  previstas  en  nuestro ordenamiento jurídico.         ',0,0,'C');

				$pdf->Ln(15);
				$pdf->Cell(0,0,'A T E N T A M E N T E',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$fecha,0,0,'C');


				$pdf->Ln(15);
				$pdf->Cell(0,0,'LIC. ROBERTO CHAPULA DE LA MORA',0,0,'C');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'Presidente ',0,0,'C');

			}
			$salida=$salida-1;

		//hasta aqui el ciclo
		//si el es ultimo 
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function membretadoc($salida,$texto){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);

require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
		function Footer()
		{
		$fecha2=date("d/m/Y");
			$this->SetY(-70);
			$this->Cell(0,0,'A t e n t a m e n t e.',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Colima, Col., a ',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,''.$fecha2,0,0,'C');
			$this->Ln(15);
			$this->Cell(0,0,'LIC. ROBERTO CHAPULA DE LA MORA',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'P R E S I D E N T E',0,0,'C');
			$this->Ln(10);
				
			$this->SetFont('Arial','I',7);
			$this->Cell(0,0,'_____________________________________________________________________________________________________',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Degollado No. 79, Zona Centro. C.P. 28000. Colima, Col. Teléfonos: (312) 31.477.95;  31.471.86;  31.229.94. ',0,0,'C');
			$this->Ln(5);
			$this->Cell(0,0,'Lada sin Costo: 01.800.696.7672. Página Web: www.cdhcolima.org.mx  Celular:   044-312-155 13 33.',0,0,'C');
			$this->Ln(5);	
		}
	}

	if ($a==0){
	$pdf=new PDF();
	$control=$salida;
	}
	while($control!=0){
	
				
				
		$resultados = mysql_query("
		SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA
		FROM miembros
		INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
		INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
		WHERE miembros.IDMIEMBRO=$control");
		$control=$control-1;

		while($row=mysql_fetch_array($resultados)){
			if ($salida!=0){
				$a=1;
							
				$a=1;
				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];
				$pdf->AliasNbPages();
				$pdf->AddPage();
				//$pdf->SetMargins(30) ;
				$pdf->SetLeftMargin(30);
				$pdf->SetRightMargin(30);
				$pdf->SetTopMargin(30); 

				$pdf->Image('PDF/imagenes/1.PNG',15,15,30);
				$pdf->Image('PDF/imagenes/firma.PNG',80,230,40);
				
				$pdf->SetXY(0,0);
				$pdf->SetFont('Arial','B',12);
				$pdf->Ln(25);
				$pdf->Cell(0,0,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO',0,0,'R');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'DE COLIMA',0,0,'R');

				$pdf->Ln(20);
				$pdf->Cell(0,0,''.$nombreS." ".$nombreP." ".$nombreM,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cargo,0,0,'L');
				$pdf->Ln(5);
				$pdf->SetFont('Arial','',12);
				$pdf->Cell(0,0,'Comité Voluntario de Promoción y Defensa de La Colonia '.$colonia,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,'Del municipio de '.$municipio,0,0,'L');
				$pdf->Ln(5);
				$pdf->write(5,''.$texto);	
				

			}
			$salida=$salida-1;

		//hasta aqui el ciclo
		//si el es ultimo 
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}
	
function sobrec($salida){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);

require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
		
	}

	if ($a==0){
	$pdf=new PDF();
	$control=$salida;
	}
	while($control!=0){
	
				
				
		$resultados = mysql_query("
		SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA,PUESTO,MUNICIPIO,
		FECHA,COMITE,CALLE,NUMERO,localizacion.CP
		FROM miembros
		INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
		INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
		WHERE miembros.IDMIEMBRO=$control");
		$control=$control-1;

		while($row=mysql_fetch_array($resultados)){
			if ($salida!=0){
				$a=1;
	
				$pdf->AliasNbPages();
				$pdf->AddPage();
				$pdf->SetXY(0,0);
				//$pdf->SetXY(0,0);
				$pdf->SetLeftMargin(20);
				$pdf->SetRightMargin(15);
				$pdf->SetTopMargin(30);

				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];
				$calle=$row ['CALLE'];
				$numero=$row ['NUMERO'];
				$cp=$row ['CP'];
				$comite=$row['COMITE']; 

				//$pdf->AddFont('Arial','','poorich.php');
				$pdf->SetFont('Arial','',11);

				$pdf->Image('PDF/imagenes/1.PNG',20,15,40);
				$pdf->Ln(30);
				$pdf->Cell(0,0,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO DE COLIMA',0,0,'R');
				$pdf->Ln(25);

				$pdf->Cell(0,0,''.$nombreS.' '.$nombreP.' '.$nombreM,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cargo,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$comite,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$calle." ".$numero." ".$colonia,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$municipio.", Colima",0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cp,0,0,'L');
				$pdf->Ln(5);

			}
			$salida=$salida-1;

		//hasta aqui el ciclo
		//si el es ultimo 
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function credc($salida){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);
//$wasd=2;
require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
		
	}

	if ($a==0){
	$pdf=new PDF();
	$control=$salida;
	}
	$wasd=7;
	$qwerty=1;
	while($control!=0){
	
		
				
		$resultados = mysql_query("
		SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA,PUESTO,MUNICIPIO,
		FECHA,COMITE,CALLE,NUMERO,localizacion.CP
		FROM miembros
		INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
		INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
		WHERE miembros.IDMIEMBRO=$control");
		$control=$control-1;
		
		while($row=mysql_fetch_array($resultados)){
			if ($salida!=0){
						
				if ($wasd==7){
					$pdf->AliasNbPages();
					$pdf->AddPage();
					$pdf->SetXY(0,0);
					$wasd=1;
				
				}
				
				
				$pdf->SetLeftMargin(20);
				$pdf->SetRightMargin(15);
				$pdf->SetTopMargin(30);
				
				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];
				$calle=$row ['CALLE'];
				$numero=$row ['NUMERO'];
				$cp=$row ['CP'];
				$comite=$row['COMITE']; 

				$pdf->AddFont('Arial','','poorich.php');
				$pdf->SetFont('Arial','',11);
				//aqui habra un case para una variable de control qwerty, con esta iremos agregando cada uno de los tem
				//templates de imagen, espero funcione como estoy pensando
				switch ($qwerty) {
					case 1:
						$pdf->Image('PDF/imagenes/creden.jpg',40,10,60);
						$pdf->AddFont('colibri_negro','','colibri.php');
						$pdf->AddFont('colibri_negro');
						$pdf->SetFont('colibri_negro','',4);
						$pdf->Ln(10);
						$pdf->text(50,15,'COMITÉ VOLUNTARIO DE PROMOCIÓN');	
						//$pdf->Ln(3);
						$pdf->text(50,17,'Y DEFENSA DE LOS DERECHOS HUMANOS');	
						//$pdf->Ln(3);
						$pdf->text(50,19,'DE LA COLONIA'.$colonia);	
						$pdf->SetFont('colibri_negro','',10);
						$pdf->text(60,35,''.$nombreS.' '.$nombreP.' '.$nombreM);	
						$pdf->text(70,40,''.$cargo);	
						
						
						//$pdf->Cell(0,0,''.$nombreS.' '.$nombreP.' '.$nombreM,0,0,'L');
						//$pdf->Ln(5);
						//$pdf->Cell(0,0,''.$cargo,0,0,'L');
					break;
					case 2:
						$pdf->Image('PDF/imagenes/creden.jpg',120,10,60);
						
					break;
					case 3:
						$pdf->Image('PDF/imagenes/creden.jpg',40,100,60);
						
					break;
					case 4:
						$pdf->Image('PDF/imagenes/creden.jpg',120,100,60);
						
					break;
					case 5:
						$pdf->Image('PDF/imagenes/creden.jpg',40,190,60);
						
					break;
					case 6:
						$pdf->Image('PDF/imagenes/creden.jpg',120,190,60);
						$qwerty=0;
					break;
					case 7:
						
						
					break;
					
				}
				$a=1;
				$qwerty=$qwerty+1;
				$wasd=$wasd+1;
				/*$pdf->Image('PDF/imagenes/creden.jpg',60,20,60);
				$pdf->Image('PDF/imagenes/creden.jpg',120,20,60);
				
				$pdf->Image('PDF/imagenes/creden.jpg',60,100,60);
				$pdf->Image('PDF/imagenes/creden.jpg',120,100,60);
				
				$pdf->Image('PDF/imagenes/creden.jpg',60,180,60);
				$pdf->Image('PDF/imagenes/creden.jpg',120,180,60);
				
				$pdf->Ln(30);
				$pdf->Cell(0,0,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO DE COLIMA',0,0,'R');
				$pdf->Ln(25);
				$pdf->Cell(0,0,''.$nombreS.' '.$nombreP.' '.$nombreM,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cargo,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$comite,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$calle." ".$numero." ".$colonia,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$municipio.", Colima",0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cp,0,0,'L');
				$pdf->Ln(5);
				*/

			}
			$salida=$salida-1;

		//hasta aqui el ciclo
		//si el es ultimo 
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}

function credp(){
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);
//echo "hola estoy dando salida a pdff";
require('PDF/lib/PDF/fpdf.php');
	class PDF extends FPDF
	{
	//Cabecera de página
	}
	
	$wasd=2;
		
	if ($a==0){
	//echo "hola, a es igualita a cero";
	$pdf=new PDF();
	$ultimo=$_GET['chekie'];
	$salida=count($ultimo); 
	}
	foreach ($_GET["chekie"] as $id){
		$resultados = mysql_query("
		SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA,PUESTO,MUNICIPIO,
		FECHA,COMITE,CALLE,NUMERO,localizacion.CP
		FROM miembros
		INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
		INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
		WHERE miembros.IDMIEMBRO=$id");

		while($row=mysql_fetch_array($resultados)){
		//aqui inicia
		
		//echo $salida;
			if ($salida!=0){
				$a=1;
					if ($wasd==2){
					$pdf->AliasNbPages();
					$pdf->AddPage();
					$pdf->SetXY(0,0);
					$wasd=0;
				
				}
				$wasd=$wasd+1;
				
				//$pdf->SetXY(0,0);
				$pdf->SetLeftMargin(20);
				$pdf->SetRightMargin(15);
				$pdf->SetTopMargin(30);

				$nombreS=$row['NOMBRES'];
				$nombreP=$row['APATERNO'];
				$nombreM=$row['AMATERNO'];
				$cargo =$row['PUESTO']; 
				$colonia=$row['COLONIA']; 
				$municipio=$row['MUNICIPIO']; 
				$fecha =$row ['FECHA'];
				$calle=$row ['CALLE'];
				$numero=$row ['NUMERO'];
				$cp=$row ['CP'];
				$comite=$row['COMITE']; 

				//$pdf->AddFont('Arial','','poorich.php');
				$pdf->SetFont('Arial','',11);

				$pdf->Image('PDF/imagenes/creden.jpg',50,20,100,120);
				$pdf->Ln(40);
				$pdf->Image('PDF/imagenes/creden.jpg',50,150,100,120);
				
				$pdf->Cell(0,0,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO DE COLIMA',0,0,'R');
				$pdf->Ln(25);

				$pdf->Cell(0,0,''.$nombreS.' '.$nombreP.' '.$nombreM,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cargo,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$comite,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$calle." ".$numero." ".$colonia,0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$municipio.", Colima",0,0,'L');
				$pdf->Ln(5);
				$pdf->Cell(0,0,''.$cp,0,0,'L');
				$pdf->Ln(5);

			}
			$salida=$salida-1;
		if ($salida==0){
		$pdf->Output();
		}

		}
	}
}



?>