<?php
function PDFnombramiento(){
$con = mysql_connect("localhost","root","");
if (!$con)
{
die('Could not connect: ' . mysql_error());
}

mysql_select_db("cndh", $con);

$resultados = mysql_query("SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA,PUESTO,MUNICIPIO,FECHA
		FROM miembros 
		INNER JOIN comites ON miembros.IDCOMITE=comites.IDCOMITE 
		INNER JOIN personas ON miembros.IDPERSONA=personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION=localizacion.IDLOCALIZACION

");

mysql_close($con);


require('../../lib/PDF/fpdf.php');

class PDF extends FPDF
{


}
  
$pdf=new PDF();


while($row=mysql_fetch_array($resultados)){


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
$pdf->Image('../../imagenes/1.PNG',94,15,30);
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
$pdf->Cell(0,0,'LOS DERECHOS HUMANOS DE LA COLONIA'.$colonia,0,0,'C');


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


/*

A T E N T A M E N T E
Colima, Col., a  20 de enero de 2011.



LIC. ROBERTO CHAPULA DE LA MORA
Presidente 

*/




}
$pdf->Output();
}
?>