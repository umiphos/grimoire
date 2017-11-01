<?php 






function PDFbienvenida(){
$con = mysql_connect("localhost","root","");
if (!$con)
{
die('Could not connect: ' . mysql_error());
}
mysql_select_db("cndh", $con);
$resultados = mysql_query("
SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA,PUESTO,MUNICIPIO,FECHA
		FROM miembros 
		INNER JOIN comites ON miembros.IDCOMITE=comites.IDCOMITE 
		INNER JOIN personas ON miembros.IDPERSONA=personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION=localizacion.IDLOCALIZACION

");
mysql_close($con);
require('../../lib/PDF/fpdf.php');
//	require('PDF/PDF/fpdf.php');






class PDF extends FPDF
{
//Cabecera de página



}



$pdf=new PDF();
while($row=mysql_fetch_array($resultados)){

$nombreS=$row['NOMBRES'];
$nombreP=$row['APATERNO'];
$nombreM=$row['AMATERNO'];

$cargo =$row['PUESTO']; 

//NOMBRES 	APATERNO 	AMATERNO


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

$pdf->Image('../../imagenes/1.PNG',20,20,40);

$pdf->Ln(30);
$pdf->Cell(0,5,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO',0,1,'R');
$pdf->Ln(2);
$pdf->Cell(0,5,'DE COLIMA',0,1,'R');
$pdf->Ln(25);


$pdf->SetFont('Arial','B',12);


$pdf->Image('../../imagenes/firma.png',85,190,40,40);

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
$pdf->Output();

}
//PDFbienvenida();
//$fecha,0,0,'C');$municipio);$colonia);$cargo);$nombre

?>