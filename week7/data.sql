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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'雯雯','ruru','$2b$12$YsChKiXiMUxYZrjT4kF54.ZbxL5UHsxUFSjs4.SZKHs/VknBv58x.',0,'2024-05-06 16:05:56'),(2,'雯雯','aaa','$2b$12$f5EWVQjoEVIar4I9YW9cWOiNnipJ01J/vJOVZbYhiu7HIWWBjRdt2',0,'2024-05-06 18:06:41'),(3,'凱文','ccc','$2b$12$yQ493YoRGtw6aWmS6BgE0.vKoHB0azNHPFSSLvKP0KI93kt.MuEYe',0,'2024-05-06 18:13:32'),(4,'雯雯','bbb','$2b$12$j3fRkFxGCgv6SuexLHynBuJ7WQGEQl/iYv7LMIQ6W51I5AQTfEYLC',0,'2024-05-07 10:50:25'),(5,'雯雯','dddd','$2b$12$HEK9.Difsnuv3ingaYdl/.nbHvpt4cMYZIn.N8V0FbHqiThlfdV0W',0,'2024-05-07 12:28:10'),(6,'雯雯','qqq','$2b$12$rkUowAYyc/DZgsXpm.Hea.avvXwZ1mCD9d9or1BVTnieHJJJu2oMG',0,'2024-05-07 12:28:44'),(7,'小胖','fat','$2b$12$9VAOhM.zjG1VBJMjjXHQA.VkcUc8b2fsaZFHyO.ZgAImurE8zlADu',0,'2024-05-07 17:35:40'),(8,'test','test','$2b$12$zMYLqC0yDK3p5JUFo5oRk.SHycsBeARHQg9asA7R2Tptfivjl5aUy',0,'2024-05-08 09:59:18'),(9,'雪莉','www','$2b$12$cVxAqAbHXX2N9NUTK/8or.d8qeWS69pXg6QxJFTboOzwPuUDbvu5S',0,'2024-05-08 17:18:50'),(10,'jinx','jinx','$2b$12$6g1Fr6zXDLMxfvhMpi/Tmu6TFu64DpcDvaJncp6.XHh3ivs5Xng0C',0,'2024-05-08 17:23:01');
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
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (5,7,'我最胖',0,'2024-05-07 17:35:51'),(7,3,'我是凱文',0,'2024-05-08 08:15:11'),(8,3,'笨笨',0,'2024-05-08 08:17:56'),(9,3,'好好玩',0,'2024-05-08 08:17:58'),(15,8,'測試測試',0,'2024-05-08 09:59:29'),(18,9,'我是雪莉',0,'2024-05-08 17:19:00'),(19,10,'dddd',0,'2024-05-08 17:23:11'),(20,10,'??????',0,'2024-05-09 09:28:47'),(22,3,'sd',0,'2024-05-09 11:15:46'),(29,6,'666',0,'2024-05-12 09:14:44'),(30,6,'ewrse',0,'2024-05-12 09:14:50'),(31,8,'11111',0,'2024-05-12 09:29:42'),(32,8,'2222',0,'2024-05-12 09:29:44'),(33,8,'3333',0,'2024-05-12 09:29:46'),(34,8,'23213',0,'2024-05-12 09:29:48'),(35,8,'123132',0,'2024-05-12 09:29:49'),(36,8,'k',0,'2024-05-12 09:30:33'),(37,8,'唷唷唷',0,'2024-05-12 09:38:25'),(38,8,'ㄎ ',0,'2024-05-12 09:48:38'),(39,8,'唷',0,'2024-05-12 09:48:50'),(43,6,'你還好嗎',0,'2024-05-12 09:50:50'),(44,6,'你好嗎',0,'2024-05-12 09:52:27'),(45,6,'k',0,'2024-05-12 09:53:53'),(46,6,'???',0,'2024-05-12 09:53:57'),(47,6,'AOU',0,'2024-05-12 09:54:24'),(48,6,'哈摟',0,'2024-05-12 09:56:08'),(49,7,'我最胖',0,'2024-05-12 09:56:33'),(51,7,'凹',0,'2024-05-12 13:23:22'),(52,6,'YAYAYAYA',0,'2024-05-14 10:46:26'),(53,6,'d',0,'2024-05-14 10:46:40');
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

-- Dump completed on 2024-05-14 10:50:54
