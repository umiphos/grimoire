<?php


function conexionDB(){
  global $link;
  $link = mysql_connect('localhost','root','');
     if (!$link) {
          die('Could not connect: ' . mysql_error());
     }
     
  $db_selected =   mysql_select_db('cndh', $link);
   if(!$db_selected) {
      die('  lo siento pero la conexion ha fallado : ' . mysql_error());
      }
	  return "conectado";
}

	  
	  ////////insertar datos de comite

function agregar($COMITE,$FECHA,$DISTRITO,$CP,$MUNICIPIO) {
      $sql="INSERT INTO `cndh`.`comites` (`IDCOMITE`,`COMITE`,`FECHA`,`DISTRITO`,`CP`,`MUNICIPIO`) VALUE ('NULL','".$COMITE."','".$FECHA."','".$DISTRITO."','".$CP."','".$MUNICIPIO."')";
              //echo $sql;
          global $link;  
          $query= mysql_query($sql,$link); 
          return $sql; 
    }
	
	
   ////insertar datos Capasitaciones	
	function agregarCapasitaciones($IDCOMITE,$DERECHOS,$QUEJAS,$FUNCIONES) {
      $sql="INSERT INTO `cndh`.`capacitaciones` (`IDCAPACITACIONES`,`IDCOMITE`,`DERECHOS`,`QUEJAS`,`FUNCIONES`) VALUE ('NULL','".$IDCOMITE."','".$DERECHOS."','".$QUEJAS."','".$FUNCIONES."')";
            // echo $sql;                                                                                                                
          global $link;  
          $query= mysql_query($sql,$link); 
          return $sql; 
    }

	
	
 
//////modificar comite	

	
	function modificarcomite($IDCOMITE,$COMITE,$FECHA,$DISTRITO,$CP,$MUNICIPIO) {
      $sql="UPDATE `cndh`.`comites` SET `COMITE` ='".$COMITE ."',`FECHA`='".$FECHA ."',`DISTRITO`='".$DISTRITO."',`CP`='".$CP."',`MUNICIPIO`='".$MUNICIPIO."' WHERE IDCOMITE='".$IDCOMITE."'";	
         
                                                                                                                             
          global $link;  
          $query= mysql_query($sql,$link); 
           //echo $sql;
    }
	
   ///modificar capacitaciones
   
   function MCapacitaciones($IDCOMITE,$DERECHOS,$QUEJAS,$FUNCIONES) {
      $sql="UPDATE  `cndh`.`capacitaciones` SET `DERECHOS`= '$DERECHOS' , `QUEJAS`= '$QUEJAS' , `FUNCIONES`='$FUNCIONES' WHERE IDCOMITE='$IDCOMITE'";
          //   echo $sql;                                                                                                                
          global $link;  
          $query= mysql_query($sql,$link); 
          return $sql; 
    }
     	
   	
   		
	
	////////insertar datos de persona
function agregarPersona($FOTOGRAFIA,$NOMBRES,$APATERNO,$AMATERNO,$SEXO,$FNACIMIENTO,$OCUPACION,$ESCOLARIDAD) {
      $sql="INSERT INTO `cndh`.`personas`(`IDPERSONA`,`FOTOGRAFIA`,`NOMBRES`,`APATERNO`,`AMATERNO`,`SEXO`,`FNACIMIENTO`,`OCUPACION`,`ESCOLARIDAD`  ) VALUE ('NULL','".$FOTOGRAFIA."','".$NOMBRES."','".$APATERNO."','".$AMATERNO."','".$SEXO."','".$FNACIMIENTO."','".$OCUPACION."','".$ESCOLARIDAD."')";
          //   echo $sql;                                                                                                                
          global $link;  
          $query= mysql_query($sql,$link); 
        
           $resultado= mysql_insert_id();
           return $resultado;       
       
	} 
///modificar personas
function Mpersona($FOTOGRAFIA,$NOMBRES,$APATERNO,$AMATERNO,$SEXO,$FNACIMIENTO,$OCUPACION,$ESCOLARIDAD,$IDPERSONA){
	$sql="UPDATE `cndh`.`personas` SET `NOMBRES`='".$NOMBRES."',`APATERNO`='".$APATERNO ."',`AMATERNO`='".$AMATERNO."',`SEXO`='".$SEXO."',`FNACIMIENTO`='".$FNACIMIENTO."',`OCUPACION`='".$OCUPACION."', `ESCOLARIDAD`='".$ESCOLARIDAD."' WHERE IDPERSONA='".$IDPERSONA."'";	
         echo $sql;
                                                                                                                             
          global $link;  
          $query= mysql_query($sql,$link); 
   	
	
	}	
	
	/////agregar datos de localizacion
	
function agregarLocalizacion($TCELULAR,$TCASA,$EMAIL,$COLONIA,$CALLE,$NUMERO,$DISTRITOFEDERAL,$DISTRITOLOCAL,$CP) {
      $sql="INSERT INTO `cndh`.`localizacion`(`IDLOCALIZACION`,`TCELULAR`,`TCASA`,`EMAIL`,`COLONIA`,`CALLE`,`NUMERO`,`DISTRITOFEDERAL`,`DISTRITOLOCAL`,`CP`) VALUE ('NULL','".$TCELULAR."','".$TCASA."','".$EMAIL."','".$COLONIA."','".$CALLE."','".$NUMERO."','".$DISTRITOFEDERAL."','".$DISTRITOLOCAL ."','".$CP."')";
            // echo $sql;                                                                                                                                                                    

	 
          global $link;  
          $query= mysql_query($sql,$link); 
        
          $resultado= mysql_insert_id();
           return $resultado;   
	
	}	
	//MODIFICAR LOCALIZACION 
	function Mlocalizacion ($TCELULAR,$TCASA,$EMAIL,$COLONIA,$CALLE,$NUMERO,$DISTRITOFEDERAL,$DISTRITOLOCAL,$CP,$IDLOCALIZACION) { 
		$sql="UPDATE `cndh`.`localizacion` SET `TCELULAR`='".$TCELULAR."',`TCASA`='".$TCASA ."',`EMAIL`='".$EMAIL."',`COLONIA`='".$COLONIA."',`CALLE`='".$CALLE."', `NUMERO`='".$NUMERO."', `DISTRITOFEDERAL`='".$DISTRITOFEDERAL."', `DISTRITOLOCAL`='".$DISTRITOLOCAL."', `CP`='".$CP."' WHERE IDLOCALIZACION='".$IDLOCALIZACION."'";	
         echo $sql;
                                                                                                                             
          global $link;  
          $query= mysql_query($sql,$link); 
	
	}
////	agregardatos de entregables
	
	function agregarEntregables($CAMISETA,$CBIENBENIDA,$CREDENCIAL) {
      $sql = "INSERT INTO `cndh`.`entregables`(`IDENTREGABLES`,`CAMISETA`,`CBIENBENIDA`,`CREDENCIAL`) VALUE ('NULL','".$CAMISETA."','".$CBIENBENIDA."','".$CREDENCIAL."')";
                                        	 
          global $link;  
          $query= mysql_query($sql,$link); 
           $resultado= mysql_insert_id();
           return $resultado;   
     
   }	
	
///MODIFICAR	ENTREGABLES
 function Mentregables($CAMISETA,$CBIENBENIDA,$CREDENCIAL,$IDENTREGABLES) {
      $sql="UPDATE  `cndh`.`entregables` SET `CAMISETA`= '$CAMISETA' , `CBIENBENIDA`= '$CBIENBENIDA' , `CREDENCIAL`='$CREDENCIAL' WHERE IDENTREGABLES='$IDENTREGABLES'";
          //   echo $sql;                                                                                                                
          global $link;  
          $query= mysql_query($sql,$link); 
          return $sql; 
    }
	
	
 ///insertar miembro
  function agregarMiembro($IDPERSONA,$IDLOCALIZACION,$PUESTO,$IDENTREGABLES,$IDCOMITE) {
      $sql="INSERT INTO `cndh`.`miembros` (`IDMIEMBRO`,`IDCOMITE`,`IDPERSONA`,`IDENTREGABLES`,`IDLOCALIZACION`,`PUESTO`) VALUE ('NULL','".$IDCOMITE."','".$IDPERSONA."','".$IDENTREGABLES."','".$IDLOCALIZACION."','".$PUESTO."')";
                        
          global $link;  
          $query= mysql_query($sql,$link); 
          $resultado= mysql_insert_id();
          return $resultado;   
    }	
///modificar miembro

  function Mmiembro($IDPERSONA,$IDLOCALIZACION,$PUESTO,$IDENTREGABLES,$IDCOMITE,$IDMIEMBRO) {
  	 $sql="UPDATE  `cndh`.`miembros` SET `IDPERSONA`= '$IDPERSONA' , `IDLOCALIZACION`= '$IDLOCALIZACION' , `PUESTO`='$PUESTO', `IDENTREGABLES`='$IDENTREGABLES', `IDCOMITE`='$IDCOMITE' WHERE IDMIEMBRO='$IDMIEMBRO'";
           echo $sql;                                                                                                                
          global $link;  
          $query= mysql_query($sql,$link); 
          return $sql; 
  	
  	}	
	
//agregar gestion	
function agregarGestion($IDPERSONA,$IDCOMITE,$FINICIO,$FTERMINO,$ATENDIDOPOR,$ASUNTO,$TIPO,$CANALIZADO,$DESCRIPCION) {
      $sql="INSERT INTO `cndh`.`gestiones` (`IDGESTIONES`,`IDPERSONA`,`IDCOMITE`,`FINICIO`,`FTERMINO`,`ATENDIDOPOR`,`ASUNTO`,`TIPO`,`CANALIZADO`,`DESCRIPCION`) VALUE ('NULL','".$IDPERSONA."','".$IDCOMITE."','".$FINICIO."','".$FTERMINO."','".$ATENDIDOPOR."','".$ASUNTO."','".$TIPO."','".$CANALIZADO."','".$DESCRIPCION."')";
              echo $sql;                              
          global $link;  
          $query= mysql_query($sql,$link); 
           $resultado= mysql_insert_id();
           return $resultado;   
    }
	
	
///seleccionar todo de comites


function selectAllcomites(){
      global $link;     
      
      $sql="SELECT * FROM comites ";
      $query= mysql_query($sql,$link);
     // echo $sql;
      return $query;
    }
///seleccionar comite especifico	
	function selectElecomite($comite,$id){
      global $link;     
       //echo 1;
	  if ($id != ''){
	  $sql="SELECT * FROM comites WHERE  IDCOMITE ='".$id."'";
	  }else{
      $sql="SELECT * FROM comites WHERE  COMITE ='".$comite."'";
       }    
	 $query= mysql_query($sql,$link);
      
      return $query;
    }

/// seleccionar capacitacion de un cite en especifico
function selectLacapacitacion($capacitacion,$comite){
      global $link;     
      
	  if ($comite != ''){
	  $sql="SELECT * FROM capacitaciones WHERE  IDCOMITE ='".$comite."'";
	  }else{
      $sql="SELECT * FROM capacitaciones WHERE  IDCAPACITACIONES  ='".$capacitacion."'";
       }    
        //echo $sql;	   
	 $query= mysql_query($sql,$link);
      
      return $query;
    }

function selectMiembro($nombres,$apaterno,$amaterno,$IDMIEMBRO){
      global $link;     
      
	  if ($nombres != '' and $apaterno != '' and $amaterno != ''){
	  $sql="SELECT * FROM miembros WHERE  NOMBRES ='".$nombres."'  AND APATERNO='".$apaterno."' AND AMATERNO='".$amaterno."'";
	  }else{
      $sql="SELECT * FROM miembros WHERE  IDCAPACITACIONES  ='".$IDMIEMBRO."'";
       }    
      //  echo $sql;	   
	 $query= mysql_query($sql,$link);
      
      return $query;
    }	

function selectMiembro2($COMITE,$PUESTO){
      global $link;     
      $sql="SELECT * FROM miembros WHERE  IDCOMITE  ='".$COMITE."' AND 	PUESTO='".$PUESTO."' ";
	   $query= mysql_query($sql,$link);
	 //  echo $sql;
	         return $query; 
    }	


function selecPersona($IDPERSONA) {
	 global $link;
	 $sql="SELECT * FROM personas WHERE  IDPERSONA ='".$IDPERSONA."'";
	// echo $sql;
	 $query= mysql_query($sql,$link);
      
      return $query;
	}	

function selectLocaliza($IDLOCALIZACION){
      global $link;     
		
      $sql="SELECT * FROM localizacion WHERE  IDLOCALIZACION  ='".$IDLOCALIZACION."' ";
       
     // echo $sql;	   
	 $query= mysql_query($sql,$link);
      
      return $query;
    }	
    
 
function selectEntregable($IDENTREGABLE){
      global $link;     
		
      $sql="SELECT * FROM entregables WHERE  IDENTREGABLES ='".$IDENTREGABLE."'";  
      //echo $sql;	   
	   $query= mysql_query($sql,$link);
      return $query;
    }	   


	
function selectGestion($IDGESTION,$IDCOMITE,$IDSOLICITANTE){
      global $link;     
       
	   if($IDGESTION != ''){
          $sql="SELECT * FROM gestiones WHERE  IDGESTION ='".$IDGESTION."'";
        } 
	
		if($IDCOMITE != ''){
          $sql="SELECT * FROM gestiones WHERE  IDCOMITE  ='".$IDCOMITE."'";
        }
		
		if($IDSOLICITANTE != ''){
          $sql="SELECT * FROM gestiones WHERE  IDSOLICITANTE  ='".$IDSOLICITANTE."'";
        }
		if ($IDSOLICITANTE == '' and  $IDCOMITE == '' and $IDGESTION == ''){
		   $sql="SELECT * FROM gestiones";
		}
     echo $sql;
	 $query= mysql_query($sql,$link);
      
      return $query;
    }	
	
	
	
	
	
	////subir imagenes
function subirImagenes($serverIpaddres,$userName,$serverPassword,$file,$nameIntoserver){

  
  $conectFtp_id=ftp_connect($serverIpaddres);    
  $loginFtp=ftp_login($conectFtp_id,$userName,$serverPassword);
  
  //$nameIntoserver ='somefile34.jpg';
 
  //direccion del archivo
//    echo $nameIntoserver;
  if(isset($_POST['subirImagen'])){ 
    if(ftp_put($conectFtp_id,$nameIntoserver,$file,FTP_BINARY)){
    return ("Fotografia cargada con exito");
    
  }else{
    return("Error no ha sio posible subir su foto");
   
  }

  ftp_close($conectFtp_id);
  
  header('Location:http://localhost/codigos/Nmiembro.php?comite='.$_GET['comite'].'&miembro='.$miembros.'');
}
}	

	 
	 
	  function busquedas($presona_comite,$Cmunicipio,$sexo,$escolaridad,$ocupacion,$Cfecha,$Ccp,$distrito,$buscar){

global $link;

	if ($presona_comite=="Personas"){
		$sql="
		SELECT FNACIMIENTO,NOMBRES,APATERNO,AMATERNO,SEXO,COLONIA,TCASA,personas.IDPERSONA
		FROM miembros 
		INNER JOIN comites ON miembros.IDCOMITE=comites.IDCOMITE 
		INNER JOIN personas ON miembros.IDPERSONA=personas.IDPERSONA
		INNER JOIN localizacion ON miembros.IDLOCALIZACION=localizacion.IDLOCALIZACION
		WHERE comites.MUNICIPIO LIKE '%$Cmunicipio%'
		AND personas.SEXO LIKE '%$sexo%'
		AND personas.NOMBRES LIKE '%$buscar%'
		AND personas.ESCOLARIDAD LIKE '%$escolaridad%'
		AND personas.OCUPACION LIKE '%$ocupacion%'
		AND personas.FNACIMIENTO LIKE '%$Cfecha%'
		AND localizacion.CP LIKE '%$Ccp%'";
		//AND personas.DISTRITO LIKE '%$distrito%'//que distrito busco? hay 2 distritos, local y federal
		
		
		
		
		//		AND miembros.GENERO LIKE '%$genero%' 

	
	}
	else{//$var1=Comites
		$sql=" SELECT  COMITE,FECHA,DISTRITO,CP,MUNICIPIO,IDCOMITE
		FROM comites 
		WHERE comites.MUNICIPIO LIKE '%$Cmunicipio%' 
		AND COMITE LIKE '%$buscar%'
		AND CP LIKE '%$Ccp%'
		AND FECHA LIKE '%$Cfecha%'
		";
	}



	




$query = mysql_query($sql,$link);
return $query;

	}

	  
?>
