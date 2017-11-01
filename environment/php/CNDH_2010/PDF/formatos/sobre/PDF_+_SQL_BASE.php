<?php
$con = mysql_connect("localhost","root","");
if (!$con)
{
die('Could not connect: ' . mysql_error());
}

mysql_select_db("pruebas", $con);

$resultados = mysql_query("SELECT * FROM ejemplo ");
//$row = mysql_fetch_array($resultados);
mysql_close($con);


require('../lib/PDF/fpdf.php');



class PDF extends FPDF
{
//Cabecera de página
function Header()
{
    //Logo
     $this->Image('../imagenes/1.PNG',10,10,40);
    //Arial bold 15
    $this->SetFont('Arial','B',12);
    //Movernos a la derecha
    $this->Cell(80);
    //Título
	//$this->Ln(5);
	$this->Cell(0,0,'COMISION DE DERECHOS HUMANOS DEL ESTADO DE COLIMA',0,0,'C');
    //$this->Cell(30,10,'Title',1,0,'C');
    //Salto de línea
    $this->Ln(50);
}



}

  
$pdf=new PDF();


while($row=mysql_fetch_array($resultados)){


$pdf->AliasNbPages();
$pdf->AddPage();


}
$pdf->Output();

?>