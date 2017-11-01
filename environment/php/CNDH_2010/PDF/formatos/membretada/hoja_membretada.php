<?php
function hoja_membretada(){
$texto="asdfffffffffffffffffffffffffffffff
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
asdfffffffffffffffffffffffffffffff

";
$con = mysql_connect("localhost","root","");
mysql_select_db("cndh", $con);

$resultados = mysql_query("
				SELECT IDMIEMBRO, FNACIMIENTO, NOMBRES, APATERNO, AMATERNO, SEXO, COLONIA, TCASA,MUNICIPIO,FECHA,PUESTO
				FROM miembros
				INNER JOIN comites ON miembros.IDCOMITE = comites.IDCOMITE
				INNER JOIN personas ON miembros.IDPERSONA = personas.IDPERSONA
				INNER JOIN localizacion ON miembros.IDLOCALIZACION = localizacion.IDLOCALIZACION
				");



require('../../lib/PDF/fpdf.php');

class PDF extends FPDF
{
function Footer()
{




    //Posición: a 1,5 cm del final
    $this->SetY(-70);
	
//$this->Ln(160);
$this->Cell(0,0,'A t e n t a m e n t e.',0,0,'C');
$this->Ln(5);
$this->Cell(0,0,'Colima, Col., a ',0,0,'C');
$this->Ln(5);
$this->Cell(0,0,''.$fecha,0,0,'C');LIC. 
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

$pdf->Image('../../imagenes/1.PNG',15,15,30);
$pdf->Image('../../imagenes/firma.PNG',80,230,40);
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
$pdf->write(5,' '.$texto);	
}
$pdf->Output();
}

hoja_membretada();

?>