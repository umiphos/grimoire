<?php
include ("funciones.php");
 
 
 
 
if( isset($_GET['gestion'])) {
	 conexionDB();
	
	$IDPERSONA=$_GET['IDPERSONA'];
	$IDCOMITE=$_GET['IDCOMITE'];
	$FINICIO=$_GET['FINICIO'];
	$FTERMINO=$_GET['FTERMINO'];
	$ATENDIDOPOR=$_GET['ATENDIDOPOR'];
   $ASUNTO=$_GET['ASUNT'];
   $TIPO=$_GET['TIPO'];
   $CANALIZADO=$_GET['CANALIZADO'];
   $DESCRIPCION=$_GET['DESCRIPCION'];
	 $IDGESTION =agregarGestion($IDPERSONA,$IDCOMITE,$FINICIO,$FTERMINO,$ATENDIDOPOR,$ASUNTO,$TIPO,$CANALIZADO,$DESCRIPCION);
    header('Location:http://localhost/../Mgestion.php?= IDGESTION="'.$IDGESTION.'"');	 
	 
	}else if ( isset($_GET['Cnombre']) and isset($_GET['insercion'])){
   
  
   conexionDB();
    agregar($_GET['Cnombre'], $_GET['Cfecha'],$_GET['Cdistrito'],$_GET['Ccp'],$_GET['Cmunicipio']); 
   
 
   
      if($_GET['Cderechos'] != null){
	   $DERECHOS=1;
	  }else{ $DERECHOS=0; }
	  if($_GET['Cquejas'] != null){
	    $QUEJAS=1;
	     
	  }else{$QUEJAS=0;}
	  
	  if($_GET['Cfunciones'] != null){
	  $FUNCIONES =1 ;
	  
	  }else{ $FUNCIONES =0 ;}
   
   $resultado=selectElecomite($_GET['Cnombre'],'');
   
   
   while($row=mysql_fetch_array($resultado)){
			      $IDCOMITE=$row[0];
				   
	}
   
     agregarCapasitaciones($IDCOMITE,$DERECHOS,$QUEJAS,$FUNCIONES);
     header('Location:http://localhost/../Mcomite.php?comite='.$IDCOMITE.'');
   
   exit;
}else if ( isset($_GET['Cnombre']) and isset($_GET['modificar'])){
 	    conexionDB();
  $IDCOMITE=$_GET['IDCOMITE'];
  $COMITE=$_GET['Cnombre'];
  $FECHA=$_GET['Cfecha'];
  $DISTRITO=$_GET['Cdistrito'];
  $CP=$_GET['Ccp'];
  $MUNICIPIO=$_GET['Cmunicipio'];


      if($_GET['Cderechos'] != null){
	   $DERECHOS=1;
	  }else{ $DERECHOS=0; }
	  if($_GET['Cquejas'] != null){
	    $QUEJAS=1;
	     
	  }else{$QUEJAS=0;}
	  
	  if($_GET['Cfunciones'] != null){
	  $FUNCIONES =1 ;
	  
	  }else{ $FUNCIONES =0 ;}

  modificarcomite($IDCOMITE,$COMITE,$FECHA,$DISTRITO,$CP,$MUNICIPIO);
  
  MCapacitaciones($IDCOMITE,$DERECHOS,$QUEJAS,$FUNCIONES); 
  
	header('Location:http://localhost/../Mcomite.php?comite='.$IDCOMITE.'');
	exit;
	
	}


/// insertar miembro o gestor
if(isset($_GET['modificar']) and isset($_GET['Mnombres']) ){
	
	
	conexionDB();
///obtener ids datos del miembro	
 /* if(isset($_POST['miembro'])){
  
  $PUESTO=$_POST['miembro'];
  
  }else if( isset($_GET['miembro'])){
   $PUESTO=$_GET['miembro'];   
  }
  */ 
  
 if(isset($_POST['comite'])){
    $IDCOMITE=$_POST['comite'];
    
  }else if(isset($_GET['comite'])){
    $IDCOMITE=$_GET['comite'];
  
  }  
  
   $PUESTO =$_GET['Mpuesto'];
  switch ($PUESTO){
   case 'p': $PUESTO ="Presidente"; break;
   case 's': $PUESTO ="Secretario"; break;
   case 'v': $PUESTO ="Vocal"; break;
   }

	 $resultado =selectMiembro2($IDCOMITE,$PUESTO);
	 
	 while( $row=mysql_fetch_array($resultado) ){
	 	$IDPERSONA = $row[2];
	 	$IDLOCALIZACION = $row[3];
      $IDENTREGABLES = $row[4];
      $IDMIEMBRO= $row[5];
      
	 	}
	
	
	
	
	
 
 //datos personas  
$FOTOGRAFIA=$comite.$miembros.'.jpg';
$NOMBRES=$_GET['Mnombres'];
$APATERNO=$_GET['Mapaterno'];
$AMATERNO =$_GET['Mamaterno'];
$SEXO=$_GET['Mgenero'];
$FNACIMIENTO=$_GET['Mfechan'];
$OCUPACION=$_GET['Mocupacion'];
$ESCOLARIDAD=$_GET['Mescolaridad'];
	
	
//datos de localizacion 
 
 $TCELULAR=$_GET['Mcelular'];
 $TCASA= $_GET['Mtcasa'];
 $EMAIL=$_GET['Mmail'];
 $COLONIA=$_GET['Mcolonia'];
 $CALLE=$_GET['Mcalle'];
 $NUMERO=$_GET['Mnumero'];
 $DISTRITOFEDERAL=$_GET['Dfederal'];
 $DISTRITOLOCAL=$_GET['Dlocal'];
 $CP=$_GET['CP'];
 
  
    
 
 ///datos entregables
 
   if(isset($_GET['Ncamiseta'])) {                  
     $CAMISETA =1;}else {$CAMISETA =1;}
   if(isset($_GET['Ncredencial'])) { 
     $CREDENCIAL=1;}else { $CREDENCIAL=0;}
   if(isset($_GET['Ncarta'])) {  
  $CBIENBENIDA =1;}else {$CBIENBENIDA =0;}
    
 
 
	
	
	 	
	//datos personas  
	Mpersona($FOTOGRAFIA,$NOMBRES,$APATERNO,$AMATERNO,$SEXO,$FNACIMIENTO,$OCUPACION,$ESCOLARIDAD,$IDPERSONA);
	  
   //datos de localizacion 
    Mlocalizacion ($TCELULAR,$TCASA,$EMAIL,$COLONIA,$CALLE,$NUMERO,$DISTRITOFEDERAL,$DISTRITOLOCAL,$CP,$IDLOCALIZACION);
   ///datos entregables
   Mentregables($CAMISETA,$CBIENBENIDA,$CREDENCIAL,$IDENTREGABLES);
   //datos de miembro 
	 //Mmiembro($IDPERSONA,$IDLOCALIZACION,$PUESTO,$IDENTREGABLES,$IDCOMITE,$IDMIEMBRO);
   header('Location:http://localhost/../Mcomite.php?comite='.$IDCOMITE.'');





	}else if(isset($_GET['Mnombres']) and isset($_GET['Mpuesto'])){
 conexionDB();
 
   if(isset($_POST['miembro'])){
  
  $PUESTO=$_POST['miembro'];
  
  }else if( isset($_GET['miembro'])){
   $PUESTO=$_GET['miembro'];   
  }
  
  if(isset($_POST['comite'])){
    $IDCOMITE=$_POST['comite'];
    
  }else if(isset($_GET['comite'])){
    $IDCOMITE=$_GET['comite'];
  
  }  
  
 //datos personas  
$FOTOGRAFIA=$comite.$miembros.'.jpg';
$NOMBRES=$_GET['Mnombres'];
$APATERNO=$_GET['Mapaterno'];
$AMATERNO =$_GET['Mamaterno'];
$SEXO=$_GET['Mgenero'];
$FNACIMIENTO=$_GET['Mfechan'];
$OCUPACION=$_GET['Mocupacion'];
$ESCOLARIDAD=$_GET['Mescolaridad'];


 
 
 //$PUESTO=$_GET['Mpuesto'];
 
//datos de localizacion 
 
 $TCELULAR=$_GET['Mcelular'];
 $TCASA= $_GET['Mtcasa'];
 $EMAIL=$_GET['Mmail'];
 $COLONIA=$_GET['Mcolonia'];
 $CALLE=$_GET['Mcalle'];
 $NUMERO=$_GET['Mnumero'];
 $DISTRITOFEDERAL=$_GET['Dfederal'];
 $DISTRITOLOCAL=$_GET['Dlocal'];
 $CP=$_GET['CP'];
 
  
    
 
 ///datos entregables
 
   if(isset($_GET['Ncamiseta'])) {                  
     $CAMISETA =1;}else {$CAMISETA =1;}
   if(isset($_GET['Ncredencial'])) { 
     $CREDENCIAL=1;}else { $CREDENCIAL=0;}
   if(isset($_GET['Ncarta'])) {  
  $CBIENBENIDA =1;}else {$CBIENBENIDA =0;}
    
 
 
 
//datos de miembro 
 
 
 $PUESTO =$_GET['Mpuesto'];
  switch ($PUESTO){
   case 'p': $PUESTO ="Presidente"; break;
   case 's': $PUESTO ="Secretario"; break;
   case 'v': $PUESTO ="Vocal"; break;
   }
   
   
 

 if(isset($IDCOMITE) and isset($PUESTO)){
     $IDLOCALIZACION =agregarLocalizacion($TCELULAR,$TCASA,$EMAIL,$COLONIA,$CALLE,$NUMERO,$DISTRITOFEDERAL,$DISTRITOLOCAL,$CP);
    $IDENTREGABLES =agregarEntregables($CAMISETA,$CBIENBENIDA,$CREDENCIAL);
    $IDPERSONA= agregarPersona($FOTOGRAFIA,$NOMBRES,$APATERNO,$AMATERNO,$SEXO,$FNACIMIENTO,$OCUPACION,$ESCOLARIDAD,$PUESTO);  
   agregarMiembro($IDPERSONA,$IDLOCALIZACION,$PUESTO,$IDENTREGABLES, $IDCOMITE);
 } 


 header('Location:http://localhost/../Nmiembro.php?comite='.$comite.'&miembro='.$miembros.'');
 
 

 
}


?>