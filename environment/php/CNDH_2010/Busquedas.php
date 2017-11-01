<?php 
  include ("PHP/funciones.php"); 
   conexionDB();
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<link rel="stylesheet" type="text/css" href="CSS/Eprincipal.css" media="screen" />
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	<title>comites</title>
	<script type="text/javascript" src="jscalendar-1.0/calendar.js"></script>
	<script type="text/javascript" src="jscalendar-1.0/calendar-setup.js"></script>
	<script type="text/javascript" src="jscalendar-1.0/lang/calendar-es.js"></script>
	<style type="text/css"> @import url("jscalendar-1.0/calendar-win2k-cold-1.css"); </style>
	<script type="text/javascript" src="JAVA/funciones.js"/> </script>
</head>

<body> 
	<div id="Encabezado">
		SISTEMA PARA ADMINISTRACION DE COMITES
	</div>
	<div id="Subtitulo">
		<h2>COMITES</h2>
	</div>
	<div id="Menu">
		<ul>
		  <lI> <a href="comites.php">COMITES </a></LI> 
		  <lI><a href="gestiones.php" > GESTIONES</a></LI>
		  <lI> <a href="Busquedas.php">BUSQUEDAS</a></LI>
		  <LI><a href="#"> EVENTOS</a></LI>
		  <LI><a href="#">PUBLICACIONES</a></LI>
		</ul> 
	</div> 
	<div id="Contenedor">
		<div id="BuscadorAvansado">
			<legend>Búsqueda avanzada</legend>
			<div class="clear">
	  		</div>
			<div class="form1">
				<form  action="Busquedas.php" method="GET">
					<ul class="menu "> 				
						Palabras clave:<li><input type="text" id="buscar" name="clave" onclick="javascript:BlancoOnselect('buscar','Buscar');" /></li>
						Persona/Comite<li>
						<select name="persona_comite" >
						<option>Comites</option>
						<option>Personas </option>
						</select></li><br/>
						<li><input type="submit" value="Buscar" name="search"> </li>
						
				    </ul>
			</div>
			<div class="form1">
				<ul class="menu" >
					<li>Distrito
						<select name="distrito" name="distrito">
							<option value="">Todos</option>		
							<option>1</option>
							<option>2</option>
							<option>3</option>
							<option>4</option>
							<option>5</option>
							<option>6</option>
							<option>7</option>
							<option>8</option>
							<option>9</option>
							<option>10</option>
							<option>11</option>
							<option>12</option>
							<option>13</option>
							<option>14</option>
							<option>15</option>
							<option>16</option>									
										
								  
						</select> 								  
					</li>
				   
					Codigo Postal  <li><input type="text" name="Ccp" /></li>	 	 	 	 
					Municipio  
					<li> 
						<select name="Cmunicipio"  > 
							<option value="" >Todos</option>
							<option value="Armeria" > Armería </option>
							<option value="Colima"   >Colima</option>
							<option value="Comala">Cómala </option>
							<option value="Coquimatlan" >Coquimatlán </option>
							<option value="Cuauhtemoc">Cuauhtémoc </option>
							<option value="Ixtlahuacan"  >Ixtlahuacán </option >
							<option value="Manzanillo" >Manzanillo </option>
							<option value="Minatitlan" >Minatitlán </option>
							<option value="Tecoman" >Tecomán </option>
							<option value="Villa de Alvarez" >Villa de Álvarez</option>                                            
						</select>
					</li>
				</ul>				  
			</div>
		         <div class="form1">  		   
      				   <ul class="menu" >
				           Genero<li><select name="genero">
										<option value="">Ambos</option>
										<option>Hombre</option>
										<option>Mujer</option>
									 </select>
								 </li>
							 Fecha nacimiento <li> <input type="text" id="cal-field-1" name="Cfecha"/>
                                              <img  src="icons/calendar-add-icon.png"  id="cal-button-1" >
                                                <script type="text/javascript">
                                                Calendar.setup({
                                                inputField    : "cal-field-1",
                                                 button        : "cal-button-1",
			                                    ifFormat: "%d / %m / %Y",
                                                align         : "Tr",
		                                    	 weekNumbers: ""
                                                   });
                                                </script>
										 </li>		  	 	 	 	 	 	 	 
	                         Ocupacion<li><input type="text" name="ocupacion" /></li>		 	 	 	 	 	 	 
	                         Escolaridad<li><input type="text"name="escolaridad"/></li>	 	
				  
				 
				       </ul>
				 </div>
				    </form>
				 		
		             
	   </div>
	 
	   
 	   <div class="clear">
	  
	  </div>
		<div id="ResultadosAvansado" >
	       	<form  action="pdfs.php" method="GET">
		
		  <?php  
		  
			if(isset($_GET['search'])){
				
			
		
				$resultados=busquedas($_GET['persona_comite'],$_GET['Cmunicipio'],
				$_GET['genero'],$_GET['escolaridad'],$_GET['ocupacion'],$_GET['Cfecha'],
				$_GET['Ccp'],$_GET['distrito'],$_GET['clave']);
				$var3=$_GET['persona_comite'];
				if($var3=="Comites"){
						
				
					echo"<table border='2' class='' summary='Resultados'> ";
					echo"<tr><td class='columna'></td>";
					echo"<td class='columna' >Comite </td>";
					echo"<td class='columna' >Fecha</td>";
					echo"<td class='columna' >Distrito</td>";
					echo"<td class='columna' >Codigo Postal</td>";
					echo"<td class='columna' >Municipio</td>";
					echo"</tr>";
				
					while($row=mysql_fetch_array($resultados)){
						echo"<tr>";
						echo"<th><input type='radio' name='commies[]' value='".$row['IDCOMITE'] ."'/><img src='icons/group-gear-icon.png '> </th>";
						echo"";
						echo"<th><a href='comites.php?comite=".$row['IDCOMITE']."'>". $row['COMITE']."</a></th>";
						echo"<th>".$row['FECHA']."</th>";
						echo"<th>".$row['DISTRITO']."</th>";
						echo"<th>".$row['CP']."</th>";
						echo"<th>".$row['MUNICIPIO']."</th>";
						echo"</tr>";
						
					}
					
				}

					
					
					else{
					
						echo"<table border='2' class='' summary='Resultado'> ";
						echo"<tr><td class='columna'></td>";
						echo"<td class='columna' >Nombre </td>";
						echo"<td class='columna' >Sexo</td>";
						echo"<td class='columna' >Fecha de nacimiento</td>";
						echo"<td class='columna' >Colonia</td>";
						echo"<td class='columna' >Telefono</td>";
						
						while($row=mysql_fetch_array($resultados)){
						echo"<tr>";
					
						echo"";
						echo"<th><input type='checkbox' name='chekie[]' value=".$row['IDPERSONA']."> </th>";
						echo"<th>".$row['NOMBRES']." ".$row['APATERNO']." ".$row['AMATERNO']."</th>";
						echo"<th>".$row['SEXO']."</th>";
						echo"<th>".$row['FNACIMIENTO']."</th>";
						echo"<th>".$row['COLONIA']."</th>";
						echo"<th>".$row['TCASA']."</th>";
						}
					
					}
			
			
			/*
			<select name="Cmunicipio"  > 
			<option value="" >Todos</option>
			<option value="Armeria" > Armería </option>
			<option value="Colima"   >Colima</option>
			<option value="Comala">Cómala </option>
			<option value="Coquimatlan" >Coquimatlán </option>
			<option value="Cuauhtemoc">Cuauhtémoc </option>
			<option value="Ixtlahuacan"  >Ixtlahuacán </option >
			<option value="Manzanillo" >Manzanillo </option>
			<option value="Minatitlan" >Minatitlán </option>
			<option value="Tecoman" >Tecomán </option>
			<option value="Villa de Alvarez" >Villa de Álvarez</option>                                            
			</select>*/
			echo "<select name='docu'  > ";
			echo "<option  value='1'> Bienvenida";
			echo "<option  value='2'> Nombramiento";
			echo "<option  value='3'> Membretado";
			echo "<option  value='4'> Sobres";
			echo "<option  value='5'> Credencial";
			echo "</select>";
			//echo "<th></th>";
			echo "<input name='show' type='submit' value='Mostrar'>";
			$rew=$_GET['persona_comite'];
			echo "<input type='hidden' name='id_commie' value='".$rew."'></>";
			
			}


		
		
		



///en comentario devidoa que usaremos cookies and cream, asi que se usaran otras validaciones


echo"</tr>";
	
					
echo "</table>";
/*
print('<pre>');
print_r($_GET);
print('</pre>');	
*/
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		echo "</table>";
	
	
		
		  ?>
		
		
        </form>    
		</div>
	  
        <!-- <form  action="pdfs.php" method="GET">  -->
		 
		
      	 


	
     
	</div>	
			  	
		
  
 
  
   <div id="pie">
  cccccccccccpie
   </div>   
   
 </body>
</html>