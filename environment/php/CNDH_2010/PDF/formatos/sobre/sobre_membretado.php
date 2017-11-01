<?php
function PDFsobre(){
$con = mysql_connect("localhost","root","");
if (!$con)
{
die('Could not connect: ' . mysql_error());
}
mysql_select_db("cndh", $con);
$resultados = mysql_query("
SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA,PUESTO,MUNICIPIO,FECHA,COMITE,CALLE,NUMERO,localizacion.CP
		FROM miembros 
		INNER JOIN comites ON miembros.IDCOMITE=comites.IDCOMITE 
		INNER JOIN personas ON miembros.IDPERSONA=personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION=localizacion.IDLOCALIZACION

");
mysql_close($con);




require('../../lib/PDF/fpdf.php');



class PDF extends FPDF
{
//Cabecera de página



}



$pdf=new PDF();
while($row=mysql_fetch_array($resultados)){
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
$comite =$row ['COMITE'];
$calle=$row ['CALLE'];
$numero=$row ['NUMERO'];
$cp=$row ['CP'];
$comite=$row['COMITE']; 

//$pdf->AddFont('Arial','','poorich.php');
$pdf->SetFont('Arial','',11);

$pdf->Image('../../imagenes/1.PNG',20,15,40);
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










/*
$pdf->Cell(0,0,'COMISIÓN DE DERECHOS HUMANOS DEL ESTADO DE COLIMA',0,0,'R');
$pdf->Ln(45);
$pdf->Cell(0,0,'NOMBRE',0,0,'R');
$pdf->Ln(5);
$pdf->Cell(0,0,'CARGO',0,0,'R');
$pdf->Ln(5);
$pdf->Cell(0,0,'NOMBRE DEL COMITÉ',0,0,'R');
$pdf->Ln(5);
$pdf->Cell(0,0,'DOMICILIO (aquí van todos los datos del domicilio: calle, núm, colonia)',0,0,'R');
$pdf->Ln(5);
$pdf->Cell(0,0,'Municipio, EDO. ',0,0,'R');
$pdf->Ln(5);
$pdf->Cell(0,0,'C.P.',0,0,'R');
$pdf->Ln(5);

*/





}
$pdf->Output();
}
?>