/*!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.4.2-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: hbnb_dev_db
-- ------------------------------------------------------
-- Server version	11.4.2-MariaDB-4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;


-- Drop database
DROP DATABASE IF EXISTS hbnb_dev_db;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- FLUSH PRIVILEGES;

USE hbnb_dev_db;

--
-- Table structure for table `amenities`
--

DROP TABLE IF EXISTS `amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `amenities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amenities`
--

LOCK TABLES `amenities` WRITE;
/*!40000 ALTER TABLE `amenities` DISABLE KEYS */;
INSERT INTO `amenities` VALUES
('0ae4343d-21a5-461c-a44b-5d4f8469eb82','2024-08-30 21:30:54','2024-08-30 21:30:54','parking'),
('139c0fd7-efa8-4509-ac3e-4d1cc9871643','2024-08-30 21:07:58','2024-08-30 21:07:58','my zi'),
('24f989b0-0e6e-4cee-8348-98866df0da20','2024-08-30 21:30:54','2024-08-30 21:30:54','gym'),
('3598b2ee-87c2-4a76-aea0-23e260c8837c','2024-08-30 21:07:48','2024-08-30 21:07:48','villa'),
('36e09485-1f43-4610-8459-5f88c4695f60','2024-08-30 21:07:06','2024-08-30 21:07:06','held d'),
('5288b7aa-cdbb-4539-af78-d5002e901e2b','2024-08-30 21:08:47','2024-08-30 21:08:47','bed'),
('ac7ab6b5-f365-4659-9471-506377700a7f','2024-08-30 21:30:54','2024-08-30 21:30:54','washer dryer'),
('b195d83e-8ac2-4bc9-8523-608fdf726dd0','2024-08-30 21:09:10','2024-08-30 21:09:10','1337'),
('b59ced0f-9e45-4f12-b3d8-5e1c27951429','2024-08-30 21:05:03','2024-08-30 21:05:03','Wifi'),
('c6a57fd3-d248-4079-b072-415075f13802','2024-08-30 21:07:43','2024-08-30 21:07:43','phone'),
('c81575ce-fb81-465d-bd6b-00b5d395f9dd','2024-08-30 21:30:54','2024-08-30 21:30:54','pool'),
('dd13c387-0f6f-4185-b2a9-b4180784ade3','2024-08-30 21:30:54','2024-08-30 21:30:54','air conditioning');
/*!40000 ALTER TABLE `amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `state_id` varchar(60) NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES
('025e588a-b226-4157-b6fd-20db9b09b8b3','2024-08-30 06:08:00','2024-08-30 06:08:00','cf2fb938-80be-42cb-8c2c-58f2b39368d2','ind2'),
('06d6a6cf-80dd-4416-bc18-9eb0e9d73d85','2024-08-30 05:55:52','2024-08-30 05:55:52','cf2fb938-80be-42cb-8c2c-58f2b39368d2','ind'),
('23d0473c-3ddb-4e4d-bcc4-4bd97be3c4cf','2024-08-30 06:08:56','2024-08-30 06:08:56','f85eb6ff-5a04-4764-a469-ca386274aec8','ala3'),
('263d582e-8b01-4465-9889-088db982392e','2024-08-30 06:08:50','2024-08-30 06:08:50','cf2fb938-80be-42cb-8c2c-58f2b39368d2','ind3'),
('37037b67-c4e3-4cd2-928d-869ae22ff952','2024-08-30 06:07:13','2024-08-30 06:07:13','44cea7ab-6245-495a-b0d7-4b8d837d02c5','ari2'),
('4a80b000-3159-4dc9-b6cc-8086b517a656','2024-08-30 05:54:27','2024-08-30 05:54:27','f85eb6ff-5a04-4764-a469-ca386274aec8','alb'),
('581184f6-09d1-4cb6-8479-2d90c53ac21e','2024-08-30 05:55:22','2024-08-30 05:55:22','88da8b66-1d3a-4156-af97-adfbf00f6e73','cal'),
('9e98c863-09f3-40ab-bcb7-80383d81e6ec','2024-08-30 06:08:36','2024-08-30 06:08:36','44cea7ab-6245-495a-b0d7-4b8d837d02c5','ari3'),
('a80dd9cf-6922-4847-a91e-1ba63cd14163','2024-08-30 06:08:28','2024-08-30 06:08:28','f85eb6ff-5a04-4764-a469-ca386274aec8','ala2'),
('c853e5cd-a314-4941-8f04-abed0380f774','2024-08-30 06:08:43','2024-08-30 06:08:43','88da8b66-1d3a-4156-af97-adfbf00f6e73','cal3'),
('ca98683b-86bd-41b2-9b35-467ce9841067','2024-08-30 06:07:39','2024-08-30 06:07:39','88da8b66-1d3a-4156-af97-adfbf00f6e73','cal2');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `places`
--

DROP TABLE IF EXISTS `places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `places` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `city_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `name` varchar(128) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `number_rooms` int(11) NOT NULL,
  `number_bathrooms` int(11) NOT NULL,
  `max_guest` int(11) NOT NULL,
  `price_by_night` int(11) NOT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `city_id` (`city_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `places_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`),
  CONSTRAINT `places_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `places`
--

LOCK TABLES `places` WRITE;
/*!40000 ALTER TABLE `places` DISABLE KEYS */;
INSERT INTO `places` VALUES
('24f4a84e-100e-45a5-881d-77b4a519b9af','2024-08-30 21:28:23','2024-08-30 21:28:23','4a80b000-3159-4dc9-b6cc-8086b517a656','98109d79-ede4-4ddc-875b-0468ccc97355','Elegant Villa',NULL,6,4,12,500,37.7749,-122.419),
('528102ef-7220-4bc1-a6c3-102ff08ec7f1','2024-08-30 21:28:23','2024-08-30 21:28:23','a80dd9cf-6922-4847-a91e-1ba63cd14163','deb5c588-12c7-42fc-8ecb-4f9226179634','Luxury Penthouse',NULL,4,3,8,400,36.1699,-115.14),
('59ec9adc-8714-4ae3-9726-9e833d7af541','2024-08-30 21:28:23','2024-08-30 21:28:23','37037b67-c4e3-4cd2-928d-869ae22ff952','8ed672a6-f8d3-414b-8607-ca0609fe4718','Charming Cabin',NULL,2,1,4,90,36.1699,-115.14),
('63bf0823-0fe1-4078-b783-1e10d78c5dc5','2024-08-30 21:28:24','2024-08-30 21:28:24','c853e5cd-a314-4941-8f04-abed0380f774','e392244e-eccc-46ee-9f3a-5c957c8a3dfe','Seaside Estate',NULL,5,3,10,350,37.774,-122.431),
('a8259436-1760-4198-9f7f-7df72f6e63ca','2024-08-30 21:28:23','2024-08-30 21:28:23','025e588a-b226-4157-b6fd-20db9b09b8b3','03bbbca9-6c9a-498e-bd88-402a53419634','Cozy Cottage',NULL,2,1,4,85,34.0522,-118.244),
('af6d768d-2d12-4fee-8be7-4135b60b48f8','2024-08-30 21:28:23','2024-08-30 21:28:23','9e98c863-09f3-40ab-bcb7-80383d81e6ec','db98ab2e-dd7d-412c-a390-6daacf1c91b9','City Center Apartment',NULL,2,1,3,110,34.0522,-118.244),
('b14b4a74-3cfe-4222-acd4-318b1378914d','2024-08-30 21:28:23','2024-08-30 21:28:23','263d582e-8b01-4465-9889-088db982392e','64bf816b-8d20-4cc6-9839-9b6f6ff60eab','Modern House',NULL,5,3,10,300,34.0522,-118.244),
('b87f3198-2fd1-4d03-a2bc-a7b1194b04c9','2024-08-30 21:28:23','2024-08-30 21:28:23','23d0473c-3ddb-4e4d-bcc4-4bd97be3c4cf','536f4017-b813-4e36-a384-98a81c4755d5','Urban Suite',NULL,4,2,8,200,37.7749,-122.419),
('ccb75dd5-4e37-4068-bb34-8bc9a1e621ba','2024-08-30 21:28:23','2024-08-30 21:28:23','581184f6-09d1-4cb6-8479-2d90c53ac21e','c15e30fd-6ffd-4729-9646-f844aeff3a19','Rustic Cottage',NULL,3,2,6,130,40.7128,-74.006),
('e63a5d0a-6519-410a-adaa-a069f6114706','2024-08-30 21:28:23','2024-08-30 21:28:23','06d6a6cf-80dd-4416-bc18-9eb0e9d73d85','2e298e65-7261-4d11-b4ba-f9aec1649c27','Sunny Apartment',NULL,3,2,6,150,40.7128,-74.006);
/*!40000 ALTER TABLE `places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `text` varchar(1024) NOT NULL,
  `place_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `place_id` (`place_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`place_id`) REFERENCES `places` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES
('1c52f24f-a1d3-4af7-b057-0ec6d0f5df3c','2024-08-30 21:37:52','2024-08-30 21:37:52','Nice place but a bit noisy at night.','a8259436-1760-4198-9f7f-7df72f6e63ca','8ed672a6-f8d3-414b-8607-ca0609fe4718'),
('1ecd1c5c-8640-42e9-b192-c3d097d83e78','2024-08-30 21:37:52','2024-08-30 21:37:52','Wonderful experience would definitely recommend!','63bf0823-0fe1-4078-b783-1e10d78c5dc5','64bf816b-8d20-4cc6-9839-9b6f6ff60eab'),
('40ac4217-5908-4399-825f-77836f14e05e','2024-08-30 21:37:52','2024-08-30 21:37:52','Good location but the place was a bit cramped.','ccb75dd5-4e37-4068-bb34-8bc9a1e621ba','deb5c588-12c7-42fc-8ecb-4f9226179634'),
('42fb7845-d5df-419c-bc10-7f29755cc074','2024-08-30 21:37:52','2024-08-30 21:37:52','Perfect for a weekend getaway Clean and modern.','b87f3198-2fd1-4d03-a2bc-a7b1194b04c9','db98ab2e-dd7d-412c-a390-6daacf1c91b9'),
('6cc499cf-2577-43ae-9d08-284104645c9e','2024-08-30 21:37:52','2024-08-30 21:37:52','Lovely spot very cozy and welcoming.','af6d768d-2d12-4fee-8be7-4135b60b48f8','98109d79-ede4-4ddc-875b-0468ccc97355'),
('922502c4-11a0-498b-bfcf-5e14fb9da6c8','2024-08-30 21:37:52','2024-08-30 21:37:52','Had an amazing stay highly recommended!','e63a5d0a-6519-410a-adaa-a069f6114706','e392244e-eccc-46ee-9f3a-5c957c8a3dfe'),
('99599298-85e4-4fc1-b24b-73a40305ec50','2024-08-30 21:37:52','2024-08-30 21:37:52','Had a fantastic stay very comfortable and clean.','528102ef-7220-4bc1-a6c3-102ff08ec7f1','2e298e65-7261-4d11-b4ba-f9aec1649c27'),
('c3309c87-6b92-401b-a10f-0e9efa8160ba','2024-08-30 21:37:52','2024-08-30 21:37:52','Great place with amazing views!','24f4a84e-100e-45a5-881d-77b4a519b9af','03bbbca9-6c9a-498e-bd88-402a53419634'),
('c3cf4f8d-26de-477e-9294-da6cbabd2c28','2024-08-30 21:37:52','2024-08-30 21:37:52','The location was perfect but the amenities could be improved.','59ec9adc-8714-4ae3-9726-9e833d7af541','536f4017-b813-4e36-a384-98a81c4755d5'),
('c9910cc0-6315-437b-ac08-261366defb39','2024-08-30 21:37:52','2024-08-30 21:37:52','The place was nice but could use some updates.','24f4a84e-100e-45a5-881d-77b4a519b9af','03bbbca9-6c9a-498e-bd88-402a53419634'),
('cabcb646-acd9-4f79-8034-3ab2cd4cd6a4','2024-08-30 21:37:52','2024-08-30 21:37:52','The amenities were great but the check in process was slow.','b14b4a74-3cfe-4222-acd4-318b1378914d','c15e30fd-6ffd-4729-9646-f844aeff3a19'),
('fe3bbbde-56f6-45ed-978c-b0c7f5c5e499','2024-08-30 21:37:53','2024-08-30 21:37:53','Great amenities and location Would stay again!','528102ef-7220-4bc1-a6c3-102ff08ec7f1','2e298e65-7261-4d11-b4ba-f9aec1649c27');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `states` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES
('1c158578-7dd5-4e88-b78c-d11a211f95ea','2024-08-30 21:21:15','2024-08-30 21:21:15','Texas'),
('44cea7ab-6245-495a-b0d7-4b8d837d02c5','2024-08-30 05:24:42','2024-08-30 05:24:42','Arizona'),
('88da8b66-1d3a-4156-af97-adfbf00f6e73','2024-08-30 05:24:50','2024-08-30 05:24:50','California'),
('9001117d-e84e-43ff-9ffd-c4664481f969','2024-08-30 21:21:17','2024-08-30 21:21:17','NewYork'),
('be8672e6-7ebd-404e-91c0-c558c27939de','2024-08-30 21:21:15','2024-08-30 21:21:15','Florida'),
('cf2fb938-80be-42cb-8c2c-58f2b39368d2','2024-08-30 05:25:01','2024-08-30 05:25:01','Indiana'),
('f85eb6ff-5a04-4764-a469-ca386274aec8','2024-08-30 05:24:34','2024-08-30 05:24:34','Alabama');
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
('03bbbca9-6c9a-498e-bd88-402a53419634','2024-08-30 21:14:49','2024-08-30 21:14:49','user4@x.m','pass101','Diana','Williams'),
('2e298e65-7261-4d11-b4ba-f9aec1649c27','2024-08-30 21:15:08','2024-08-30 21:15:08','user2@x.m','pass456','Bob','Miller'),
('536f4017-b813-4e36-a384-98a81c4755d5','2024-08-30 21:19:05','2024-08-30 21:19:05','user11@x.m','pass808','Kevin','Young'),
('64bf816b-8d20-4cc6-9839-9b6f6ff60eab','2024-08-30 21:18:52','2024-08-30 21:18:52','user7@x.m','pass404','George','Harris'),
('8ed672a6-f8d3-414b-8607-ca0609fe4718','2024-08-30 21:19:05','2024-08-30 21:19:05','user10@x.m','pass707','Julia','Hall'),
('98109d79-ede4-4ddc-875b-0468ccc97355','2024-08-30 21:14:58','2024-08-30 21:14:58','user3@x.m','pass789','Charlie','Brown'),
('c15e30fd-6ffd-4729-9646-f844aeff3a19','2024-08-30 21:15:18','2024-08-30 21:15:18','user1@x.m','pass123','Alice','Johnson'),
('db98ab2e-dd7d-412c-a390-6daacf1c91b9','2024-08-30 21:14:39','2024-08-30 21:14:39','user5@x.m','pass202','Edward','Taylor'),
('deb5c588-12c7-42fc-8ecb-4f9226179634','2024-08-30 21:19:05','2024-08-30 21:19:05','user9@x.m','pass606','Ian','Walker'),
('e392244e-eccc-46ee-9f3a-5c957c8a3dfe','2024-08-30 21:18:51','2024-08-30 21:18:51','user6@x.m','pass303','Fiona','Anderson');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2024-08-30 21:43:33
