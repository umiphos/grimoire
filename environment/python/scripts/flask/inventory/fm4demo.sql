-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-12-2016 a las 06:45:13
-- Versión del servidor: 10.1.19-MariaDB
-- Versión de PHP: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fm4demo`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertAdmin` (IN `user_name` VARCHAR(50), IN `pass` VARCHAR(50), IN `name` VARCHAR(50), IN `last_name` VARCHAR(50), IN `mail` VARCHAR(50))  BEGIN
	INSERT INTO  admin_info
    (user_name,pass,name,last_name,mail)	
    VALUES (user_name,pass,name,last_name,mail);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertMigrant` (IN `name` VARCHAR(50), IN `last_name` VARCHAR(50), IN `photo` VARCHAR(50), IN `id_volunter` INT)  BEGIN
	INSERT INTO  migrant
    (name,last_name,photo,id_volunter)	
    VALUES (name,last_name,photo,id_volunter);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertVolunteer` (IN `user_name_volunter` VARCHAR(50), IN `password` VARCHAR(50), IN `name_volunter` VARCHAR(50), IN `last_name_volunter` VARCHAR(50), IN `id_admin` INT(50))  BEGIN
	INSERT INTO  admin_info
    (user_name,pass,name,last_name,mail)	
    VALUES (user_name,pass,name,last_name,mail);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `LoginAdmin` (IN `user_name` VARCHAR(50), IN `pass` VARCHAR(50))  BEGIN
	SELECT * FROM admin_info WHERE user_name=user_name AND pass=pass;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `LoginVolunteer` (IN `user_name_volunter` VARCHAR(50), IN `password` VARCHAR(50))  BEGIN
	SELECT * FROM volunteer WHERE user_name_volunter=user_name_volunter AND password=password;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `SelectAllMigrants` ()  BEGIN
	SELECT * FROM migrant ORDER BY id_record DESC;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin_info`
--

CREATE TABLE `admin_info` (
  `id_admin` int(11) NOT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `pass` varchar(50) DEFAULT NULL,
  `secret` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `admin_info`
--

INSERT INTO `admin_info` (`id_admin`, `user_name`, `pass`, `secret`, `name`, `last_name`, `mail`) VALUES
(1, 'test_admin', 'pass', NULL, 'test_name', 'test_lastname', 'test@test.com'),
(2, 'insert_test', 'pass', NULL, 'test_name', 'test_lastname', 'test_email'),
(3, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `migrant`
--

CREATE TABLE `migrant` (
  `id_migrant` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `id_volunter` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `migrant`
--

INSERT INTO `migrant` (`id_migrant`, `name`, `last_name`, `photo`, `id_volunter`) VALUES
(1, 'm_name', 'm_lastname', 'void', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `volunteer`
--

CREATE TABLE `volunteer` (
  `id_volunter` int(11) NOT NULL,
  `user_name_volunter` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `name_volunter` varchar(50) DEFAULT NULL,
  `last_name_volunter` varchar(50) DEFAULT NULL,
  `email_volunter` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `volunteer`
--

INSERT INTO `volunteer` (`id_volunter`, `user_name_volunter`, `password`, `name_volunter`, `last_name_volunter`, `email_volunter`) VALUES
(1, 'test_volunteer', 'pass', 'test_name_volunteer', 'test_lastname_volunteer', 'test_volunteer@test.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admin_info`
--
ALTER TABLE `admin_info`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indices de la tabla `migrant`
--
ALTER TABLE `migrant`
  ADD PRIMARY KEY (`id_migrant`);

--
-- Indices de la tabla `volunteer`
--
ALTER TABLE `volunteer`
  ADD PRIMARY KEY (`id_volunter`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `admin_info`
--
ALTER TABLE `admin_info`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT de la tabla `migrant`
--
ALTER TABLE `migrant`
  MODIFY `id_migrant` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `volunteer`
--
ALTER TABLE `volunteer`
  MODIFY `id_volunter` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
