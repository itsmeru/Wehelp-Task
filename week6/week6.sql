-- MySQL dump 10.13  Distrib 8.3.0, for macos14 (arm64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'ruru','ruru','$2b$12$YsChKiXiMUxYZrjT4kF54.ZbxL5UHsxUFSjs4.SZKHs/VknBv58x.',0,'2024-05-06 16:05:56'),(2,'ruru','aaa','$2b$12$f5EWVQjoEVIar4I9YW9cWOiNnipJ01J/vJOVZbYhiu7HIWWBjRdt2',0,'2024-05-06 18:06:41'),(3,'凱文','ccc','$2b$12$yQ493YoRGtw6aWmS6BgE0.vKoHB0azNHPFSSLvKP0KI93kt.MuEYe',0,'2024-05-06 18:13:32'),(4,'嚕嚕','bbb','$2b$12$j3fRkFxGCgv6SuexLHynBuJ7WQGEQl/iYv7LMIQ6W51I5AQTfEYLC',0,'2024-05-07 10:50:25'),(5,'ruru','dddd','$2b$12$HEK9.Difsnuv3ingaYdl/.nbHvpt4cMYZIn.N8V0FbHqiThlfdV0W',0,'2024-05-07 12:28:10'),(6,'betty','qqq','$2b$12$rkUowAYyc/DZgsXpm.Hea.avvXwZ1mCD9d9or1BVTnieHJJJu2oMG',0,'2024-05-07 12:28:44'),(7,'小胖','fat','$2b$12$9VAOhM.zjG1VBJMjjXHQA.VkcUc8b2fsaZFHyO.ZgAImurE8zlADu',0,'2024-05-07 17:35:40'),(8,'test','test','$2b$12$zMYLqC0yDK3p5JUFo5oRk.SHycsBeARHQg9asA7R2Tptfivjl5aUy',0,'2024-05-08 09:59:18');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,6,'哈哈哈哈',0,'2024-05-07 13:46:50'),(5,7,'我最胖',0,'2024-05-07 17:35:51'),(7,3,'我是凱文',0,'2024-05-08 08:15:11'),(8,3,'笨笨',0,'2024-05-08 08:17:56'),(9,3,'好好玩',0,'2024-05-08 08:17:58'),(12,6,'我是小乖',0,'2024-05-08 08:26:29'),(14,6,'YAYAYA',0,'2024-05-08 09:58:07'),(15,8,'測試測試',0,'2024-05-08 09:59:29');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-08 10:30:56
