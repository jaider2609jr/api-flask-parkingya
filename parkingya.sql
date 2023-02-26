-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-12-2022 a las 21:28:15
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `parkingya`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_parametros`
--

CREATE TABLE `detalles_parametros` (
  `idDet` int(11) NOT NULL,
  `idDetPar` int(11) DEFAULT NULL,
  `nombre` varchar(25) NOT NULL,
  `estado` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `detalles_parametros`
--

INSERT INTO `detalles_parametros` (`idDet`, `idDetPar`, `nombre`, `estado`, `created_at`) VALUES
(1, 1, 'CC', 1, '2022-10-11 01:49:15'),
(2, 1, 'DNI', 1, '2022-10-06 17:40:09'),
(3, 1, 'TI', 1, '2022-10-06 17:40:40'),
(4, 2, 'carro', 1, '2022-10-06 17:40:40'),
(5, 2, 'moto', 1, '2022-10-06 17:41:06'),
(6, 2, 'bicicleta', 1, '2022-10-06 17:41:06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parametros`
--

CREATE TABLE `parametros` (
  `idPar` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `estado` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `parametros`
--

INSERT INTO `parametros` (`idPar`, `nombre`, `estado`, `created_at`) VALUES
(1, 'tipo documento', 1, '2022-10-11 01:30:48'),
(2, 'tipo vehiculo', 1, '2022-10-06 17:29:09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parqueaderos`
--

CREATE TABLE `parqueaderos` (
  `idParquedero` int(11) NOT NULL,
  `idUsuarioPar` int(11) DEFAULT NULL,
  `direccion` varchar(50) NOT NULL,
  `longitud` varchar(100) NOT NULL,
  `latitud` varchar(100) NOT NULL,
  `precio` int(11) NOT NULL,
  `horaApertura` time NOT NULL,
  `horaCierre` time NOT NULL,
  `puestos` int(20) NOT NULL,
  `estado` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `parqueaderos`
--

INSERT INTO `parqueaderos` (`idParquedero`, `idUsuarioPar`, `direccion`, `longitud`, `latitud`, `precio`, `horaApertura`, `horaCierre`, `puestos`, `estado`, `created_at`) VALUES
(1, 1, 'calle 53#45-10', '-74.789738', '10.987628', 2000, '13:30:00', '19:50:00', 3, 1, '2022-12-05 01:27:59'),
(2, 1, 'Cl. 52 #37-119', '-74.7927761077881', '10.980838409619334', 1000, '12:30:00', '19:50:00', 1, 1, '2022-12-04 04:18:34'),
(3, 1, 'calle 55#45-12', '-74.79129552841188', '10.988748136934904', 1000, '14:30:00', '20:50:00', 2, 0, '2022-11-28 00:12:31'),
(4, 5, 'calle 56#46-12', '-74.79234695434572', '10.990243694034813', 3500, '13:20:00', '21:30:00', 3, 0, '2022-11-16 19:43:20'),
(5, 6, 'calle 54#44-12', '-74.79198217391969', '10.985662209948911', 3500, '12:00:00', '20:00:00', 2, 1, '2022-11-12 02:17:07'),
(8, 7, 'Cra. 45 #7650', '-74.7773653', '10.983939699999999', 4000, '10:00:00', '18:30:00', 3, 1, '2022-12-05 01:35:39'),
(10, 9, 'calle31#7d104', '-74.7860642', '10.946149199999999', 3500, '12:00:00', '22:00:00', 2, 1, '2022-12-07 17:02:04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parqueadero_vehiculo`
--

CREATE TABLE `parqueadero_vehiculo` (
  `idParVeh` int(11) NOT NULL,
  `idPar` int(11) NOT NULL,
  `idVeh` int(11) NOT NULL,
  `estado` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre`) VALUES
(1, 'admin'),
(2, 'usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `pNombre` varchar(15) NOT NULL,
  `sNombre` varchar(15) DEFAULT NULL,
  `pApellido` varchar(15) NOT NULL,
  `sApellido` varchar(15) NOT NULL,
  `tipoId` int(11) DEFAULT NULL,
  `rol_id` int(11) NOT NULL DEFAULT 2,
  `numeroId` varchar(15) NOT NULL,
  `estado` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `username`, `password`, `correo`, `pNombre`, `sNombre`, `pApellido`, `sApellido`, `tipoId`, `rol_id`, `numeroId`, `estado`, `created_at`) VALUES
(1, 'jaiderby10', '1998jaider', 'jaiderby10@gmail.com', 'jaider', '', 'rodriguez', 'jimenez', 1, 1, '1143143228', 1, '2022-12-05 00:53:14'),
(5, 'leomessi10', 'lm10messi', 'leo10messi@gmail.com', 'lionel', 'andres', 'messi', 'cuccitini', 1, 2, '42123574', 1, '2022-11-01 17:51:09'),
(6, 'andresv19', '123456A', 'andresvilla19@gmail.com', 'andres', 'jose', 'villalobos', 'fonseca', 1, 2, '1143111234', 1, '2022-11-06 21:58:58'),
(7, 'jesus1812', '1812jesus', 'jesus123@gmail.com', 'jesus', 'david', 'Rodriguez', 'jimenez', 1, 2, '1001844762', 1, '2022-11-23 22:01:54'),
(8, 'jeiner10', '1234567', 'jeiner10@gmail.com', 'jeiner', 'javier', 'miranda', 'sierra', 1, 2, '19283748', 1, '2022-12-07 05:26:16'),
(9, 'jaiderby11', '1234567', 'jaiderby11@itsa.edu.co', 'jaider', 'junior', 'rodriguez', 'jimenez', 1, 2, '12345681', 1, '2022-12-07 16:56:37');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `idVehiculo` int(11) NOT NULL,
  `idUsuarioVeh` int(11) DEFAULT NULL,
  `placa` varchar(10) NOT NULL,
  `tipoV` int(11) DEFAULT NULL,
  `estado` tinyint(4) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`idVehiculo`, `idUsuarioVeh`, `placa`, `tipoV`, `estado`, `created_at`) VALUES
(1, 1, 'wzt-328', 1, 1, '2022-10-18 21:24:42');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `detalles_parametros`
--
ALTER TABLE `detalles_parametros`
  ADD PRIMARY KEY (`idDet`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `idDetPar` (`idDetPar`);

--
-- Indices de la tabla `parametros`
--
ALTER TABLE `parametros`
  ADD PRIMARY KEY (`idPar`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `parqueaderos`
--
ALTER TABLE `parqueaderos`
  ADD PRIMARY KEY (`idParquedero`),
  ADD UNIQUE KEY `direccion` (`direccion`),
  ADD KEY `idUsuarioPar` (`idUsuarioPar`);

--
-- Indices de la tabla `parqueadero_vehiculo`
--
ALTER TABLE `parqueadero_vehiculo`
  ADD PRIMARY KEY (`idParVeh`),
  ADD KEY `idVeh` (`idVeh`),
  ADD KEY `parqueadero_vehiculo_ibfk_2` (`idPar`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD UNIQUE KEY `numeroId` (`numeroId`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `tipoId` (`tipoId`),
  ADD KEY `rol_usuario_fk` (`rol_id`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`idVehiculo`),
  ADD UNIQUE KEY `placa` (`placa`),
  ADD KEY `idUsuarioVeh` (`idUsuarioVeh`),
  ADD KEY `tipoV` (`tipoV`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `detalles_parametros`
--
ALTER TABLE `detalles_parametros`
  MODIFY `idDet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `parametros`
--
ALTER TABLE `parametros`
  MODIFY `idPar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `parqueaderos`
--
ALTER TABLE `parqueaderos`
  MODIFY `idParquedero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `parqueadero_vehiculo`
--
ALTER TABLE `parqueadero_vehiculo`
  MODIFY `idParVeh` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  MODIFY `idVehiculo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalles_parametros`
--
ALTER TABLE `detalles_parametros`
  ADD CONSTRAINT `detalles_parametros_ibfk_1` FOREIGN KEY (`idDetPar`) REFERENCES `parametros` (`idPar`);

--
-- Filtros para la tabla `parqueaderos`
--
ALTER TABLE `parqueaderos`
  ADD CONSTRAINT `parqueaderos_ibfk_1` FOREIGN KEY (`idUsuarioPar`) REFERENCES `usuarios` (`idUsuario`);

--
-- Filtros para la tabla `parqueadero_vehiculo`
--
ALTER TABLE `parqueadero_vehiculo`
  ADD CONSTRAINT `parqueadero_vehiculo_ibfk_1` FOREIGN KEY (`idVeh`) REFERENCES `vehiculos` (`idVehiculo`),
  ADD CONSTRAINT `parqueadero_vehiculo_ibfk_2` FOREIGN KEY (`idPar`) REFERENCES `parqueaderos` (`idParquedero`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `rol_usuario_fk` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`tipoId`) REFERENCES `detalles_parametros` (`idDet`);

--
-- Filtros para la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `vehiculos_ibfk_1` FOREIGN KEY (`idUsuarioVeh`) REFERENCES `usuarios` (`idUsuario`),
  ADD CONSTRAINT `vehiculos_ibfk_2` FOREIGN KEY (`tipoV`) REFERENCES `detalles_parametros` (`idDet`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
