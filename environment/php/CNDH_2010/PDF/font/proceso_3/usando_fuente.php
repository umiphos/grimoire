<?php
require('../../lib/PDF/fpdf.php');


$pdf=new FPDF();
$pdf->AddFont('colibri','','colibri.php');
$pdf->AddFont('colibri');
$pdf->SetFont('colibri','',12);
$pdf->AddPage();
$pdf->SetFont('colibri','',8);

$pdf->Cell(0,10,'This font is colibri and looks cool');
$pdf->SetFont('colibri','',16);

$pdf->Ln(10);
$pdf->Cell(0,0,'This font is ccr(comic) and looks cool');
$pdf->Output();

?>