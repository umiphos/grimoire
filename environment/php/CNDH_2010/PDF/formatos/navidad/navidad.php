<?php
$con = mysql_connect("localhost","root","");
if (!$con)
{
die('Could not connect: ' . mysql_error());
}
mysql_select_db("pruebas", $con);
$resultados = mysql_query("SELECT * FROM ejemplo ");
mysql_close($con);

$nombre=$row['nombre'];
$cargo =$row['cargo']; 
$fecha =$row ['fecha'];


require('../../lib/PDF/fpdf.php');

class PDF extends FPDF
{
//Cabecera de p�gina
function Header()
{
    //Logo
     $this->Image('../../imagenes/1.PNG',10,10,40);
    //Arial bold 15
    $this->SetFont('Arial','B',15);
    //Movernos a la derecha
    $this->Cell(80);
    //T�tulo
    //$this->Cell(30,10,'Title',1,0,'C');
    //Salto de l�nea
    $this->Ln(30);
}



}



  
$pdf=new PDF();


while($row=mysql_fetch_array($resultados)){
$pdf->AliasNbPages();
$pdf->AddPage();

$pdf->SetFont('Times','',16);
$pdf->Ln(30);
$pdf->Write(5,'C.'.$nombre);
$pdf->Write(5,'
DEL COMIT� VOLUNTARIO
DE PROMOCI�N Y DEFENSA DE LOS
DERECHOS HUMANOS DE LA COLONIA '.$colonia);
$pdf->Ln(10);
$pdf->Write(5,'
P r e s e n t e');
$pdf->Ln(20);
$pdf->SetFont('Times','',16);
$pdf->Write(5,'En esta �poca navide�a en que reina la paz espiritual y sentimos dicha y entusiasmo en nuestros corazones, es un buen momento para festejar los logros obtenidos y con la mayor alegr�a empezar un a�o nuevo.

Para el Organismo que presido, uno de los principales logros fue el acercamiento con la sociedad, dando como resultado la creaci�n de los Comit�s Voluntarios de Promoci�n y Defensa de los Derechos Humanos, de los cuales t� eres parte importante.

Por tu colaboraci�n y trabajo incondicional a favor de la sociedad, te reitero mi agradecimiento y aprovecho esta oportunidad para desearte, a nombre del Honorable Consejo y del equipo que aqu� colabora, una feliz navidad y un a�o 2011 lleno de salud, dicha y prosperidad.
');
$pdf->Ln(20);
$pdf->Cell(0,5,'Atentamente',0,1,'C');
$pdf->Cell(0,5,'Colima, Col., a 20 de diciembre de 2010.',0,1,'C');

$pdf->Ln(20);
$pdf->Cell(0,5,'LIC. ROBERTO CHAPULA DE LA MORA',0,1,'C');
$pdf->Cell(0,5,'PRESIDENTE',0,1,'C');
}



$pdf->Output();
?>