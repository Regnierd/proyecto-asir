-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: prueba
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `prueba`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `prueba` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `prueba`;

--
-- Table structure for table `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `peliculas` (
  `id_pelicula` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `descripcion` varchar(400) DEFAULT NULL,
  `clasificacion` int(2) NOT NULL,
  `img` varchar(255) DEFAULT NULL,
  `estreno` date DEFAULT NULL,
  `video` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id_pelicula`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
INSERT INTO `peliculas` VALUES (1,'Spiderman: Home Coming','Jon Watts','Peter Parker asume su nueva identidad como Spider-Man y regresa a vivir con su tía después de su aventura con los Vengadores. Al volver, mientras sigue bajo la tutela de Tony Stark, descubre que ha surgido un nuevo y despiadado enemigo que pretende destruir todo lo que ama: el Buitre.',13,'https://vignette.wikia.nocookie.net/spiderman/images/2/21/Spider_Man_Homecoming_One_Sheet_1.png/revision/latest?cb=20170524163000&path-prefix=es','2017-07-28','https://cdn.jwplayer.com/players/66gVU1X7-TF4pi9hT.html'),(2,'Deadpool','Tim Miller','Un exmercenario quien, tras haber sido sometido a un cruel experimento, adquiere el superpoder de sanar rápidamente y pretende vengarse del hombre que destrozó su vida.',16,'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTb11AYigsgi1T_1rgQQhp5VhnHpA6u6eVKu1dz6A--WPNcYok7','2016-01-21','https://cdn.jwplayer.com/players/BWWsFyVy-TF4pi9hT.html'),(3,'Doctor Strange','Scott Derrickson','Después de sufrir un accidente, un brillante y arrogante cirujano busca rehabilitarse mediante técnicas alternativas. Sus intentos le llevan a descubrir que ha sido designado para encabezar la lucha contra una fuerza oscura y sobrenatural.',13,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1-MK7tHomhOcaLsoMzbNaTsfDIYG4nvx9iOXJEV93wtDdFTbC','2016-10-28','https://cdn.jwplayer.com/players/JuI6XY3a-TF4pi9hT.html'),(4,'Los Vengadores: La era de Ultron','Joss Whedon','Los Vengadores se reúnen de nuevo y juntan sus fuerzas con las de los recién llegados Quicksilver y Bruja Escarlata para luchar contra un robot maquiavélico llamado Ultrón, el cual Tony Stark creó con el fin de defender la paz, pero resultó defectuoso y ahora pretende exterminar a toda la humanidad.',13,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQqLHA9NtdPJjQW-emn5o1pAX8Ja3Ud_UkC9SvAxYK0p8UVuY1','2015-04-29','https://cdn.jwplayer.com/players/b0Lde6ss-TF4pi9hT.html'),(5,'Guardianes de la galaxia Vol.2','James Gunn','Una poderosa raza alienígena contrata a los Guardianes para que protejan sus valiosas baterías de energía, pero, cuando Rocket las roba, los alienígenas envían a sus tropas de combate a vengarse de los Guardianes. Mientras tratan de escapar con vida, intentan resolver el misterio de los verdaderos orígenes de Peter Quill',13,'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTOsgcygSuIfxi4pU0PB7Id1HeubElL6IllSe-X5vmOYzEz9EO0','2017-04-19','https://cdn.jwplayer.com/players/VAWJo3Tq-TF4pi9hT.html');
/*!40000 ALTER TABLE `peliculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id_user` int(255) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Javier','javier@gmail.com','924fe882875572f202b764092c2ca12e5708f8a22a363cff89b2ff2bc2958b9c',1),('maria','maria@gmail.com','eabf85100f233cc904a0c30a39d6f25cd4811da7715737a6d9c3af6021d087e2',8),('pedro','pedro@gmail.com','30bf3298f91837dd60864a0a1ba4e960cf5e785b7811c4f54258fffaa789f025',10),('nyar','nyar@gmail.com','a8c0d483b0ba0a91d10bf59718fa21dd420e8d92a754002b46e868c29c1802ba',11),('pepe','pepe@gmail.com','9c8ced31a34f0d3e2e48220fac6b60a17ac8c3b7ee335f664487674e7ca91059',12),('tino','tino@gmail.com','9a19e7a8822d8934e3cfcab8a20ce265dda363fb4e20b252c26c04e2054c5439',14),('carmen','carmen@gmail.com','c7146e39dd8f3325d75c5f629ad42a1a570a3ff6c7e7def67443d62ef031d8b4',15),('asir','asir@gmail.com','df1617e63e1a5c5ef15af93b394d1c5d1627c3a5103ae0b338bca691b25ad474',16);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-29 13:44:32
