CREATE DATABASE  IF NOT EXISTS `frequency_main` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `frequency_main`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: frequency_main
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `search_frequency`
--

DROP TABLE IF EXISTS `search_frequency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `search_frequency` (
  `id` int NOT NULL AUTO_INCREMENT,
  `by_film` varchar(255) DEFAULT NULL,
  `by_actors` varchar(255) DEFAULT NULL,
  `by_directors` varchar(255) DEFAULT NULL,
  `frequency` int DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search_frequency`
--

LOCK TABLES `search_frequency` WRITE;
/*!40000 ALTER TABLE `search_frequency` DISABLE KEYS */;
INSERT INTO `search_frequency` VALUES (5,'Дом',NULL,NULL,3),(6,'дракон',NULL,NULL,13),(7,NULL,'Том',NULL,4),(8,'а',NULL,NULL,5),(9,'бодо',NULL,NULL,1),(10,'др',NULL,NULL,1),(11,'20',NULL,NULL,1),(12,NULL,'том круз',NULL,1),(13,NULL,NULL,'кэмирон',1),(14,NULL,NULL,'анатолий',2),(15,'д',NULL,NULL,2),(16,'бег',NULL,NULL,1),(17,NULL,'а',NULL,1),(18,NULL,NULL,'а',2),(19,'два',NULL,NULL,1),(20,NULL,NULL,'ева',1),(21,NULL,'боб',NULL,1),(22,NULL,'мих',NULL,1),(23,'и',NULL,NULL,1),(24,'к',NULL,NULL,1),(25,'п',NULL,NULL,1),(26,NULL,'тони',NULL,1),(27,NULL,'fil',NULL,1),(28,'Fallout',NULL,NULL,1),(29,'Игра',NULL,NULL,1);
/*!40000 ALTER TABLE `search_frequency` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-25 21:27:04
