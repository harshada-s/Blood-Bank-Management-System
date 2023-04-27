CREATE DATABASE  IF NOT EXISTS `bloodbankdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bloodbankdb`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: bloodbankdb
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `admin_fname` varchar(500) DEFAULT NULL,
  `admin_lname` varchar(500) DEFAULT NULL,
  `admin_username` varchar(500) NOT NULL,
  `admin_password` varchar(20) NOT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `admin_phone` varchar(20) DEFAULT NULL,
  `admin_email` varchar(200) DEFAULT NULL,
  `bloodbank_name` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`admin_id`),
  UNIQUE KEY `admin_password` (`admin_password`),
  UNIQUE KEY `admin_phone` (`admin_phone`),
  UNIQUE KEY `admin_email` (`admin_email`),
  KEY `bloodbank_name` (`bloodbank_name`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`bloodbank_name`) REFERENCES `bloodbank` (`bloodbank_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Cody','Conner','codyconner','Password1','123 Main St','Boston','MA','02115','555-1434','codyconner@email.com','Boston Blood Bank'),(2,'Paul','Hernandez','paulhernandez','Password2','456 Elm St','Cambridge','MA','02139','555-5778','paulhernandez@email.com','Harvard Blood Bank'),(3,'Robert','Johnson','robertjohnson','Password3','789 Oak St','Somerville','MA','02143','555-9002','robertjohnson@email.com','Beth Israel Blood Bank'),(4,'Joyce','Brooks','joycebrooks','Password4','321 Pine St','Newton','MA','02458','555-3556','joycebrooks@email.com','Tufts Blood Bank'),(5,'William','Wilson','williamwilson','Password5','654 Cedar St','Brookline','MA','02445','555-7890','williamwilson@email.com','Massachusetts Blood Bank'),(6,'Jennifer','Brown','jenniferbrown','Password6','987 Maple St','Medford','MA','02155','555-2245','jenniferbrown@email.com','Brigham Blood Bank'),(7,'Michael','Taylor','michaeltaylor','Password7','210 Walnut St','Belmont','MA','02478','555-6709','michaeltaylor@email.com','Boston Children Blood Bank'),(8,'Sarah','Anderson','sarahanderson','Password8','543 Birch St','Waltham','MA','02452','555-9123','sarahanderson@email.com','Dana-Farber Blood Bank'),(9,'Gregory','Sweeney','gregorysweeney','Password9','876 Pine St','Lexington','MA','02420','555-4507','gregorysweeney@email.com','St. Elizabeth Blood Bank'),(10,'Jessica','Wilson','jessicawilson','Password10','321 Oak St','Arlington','MA','02474','555-8981','jessicawilson@email.com','Boston VA Blood Bank');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `appointment_date` date NOT NULL,
  `appointment_time` time NOT NULL,
  `donor_id` int DEFAULT NULL,
  `camp_id` int DEFAULT NULL,
  PRIMARY KEY (`appointment_id`),
  KEY `donor_id` (`donor_id`),
  KEY `camp_id` (`camp_id`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`donor_id`) REFERENCES `donor` (`donor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`camp_id`) REFERENCES `donationcamp` (`camp_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (1,'2023-04-01','10:00:00',1,1),(2,'2023-04-02','14:00:00',2,2),(3,'2023-04-03','12:00:00',3,3),(4,'2023-04-04','15:00:00',4,4),(5,'2023-04-05','16:00:00',5,5),(6,'2023-04-06','13:00:00',6,6),(7,'2023-04-07','20:00:00',7,7),(8,'2023-04-08','16:00:00',8,8),(9,'2023-04-09','18:30:00',1,9),(10,'2023-04-10','12:30:00',2,10);
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `timecheck_before_appointment_insert` AFTER INSERT ON `appointment` FOR EACH ROW begin
declare MESSAGE_TEXT varchar(50);
if new.appointment_time<(select camp_time from donationcamp where camp_id=new.camp_id) then
    signal sqlstate '45000'
	SET MESSAGE_TEXT = 'Cannot insert. Appointment time should be greater than the camp time';
end if;
if new.appointment_date!=(select camp_date from donationcamp where camp_id=new.camp_id) then
    signal sqlstate '45000'
	SET MESSAGE_TEXT = 'Cannot insert. Appointment date should be equal to the camp date';
end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `bloodbank`
--

DROP TABLE IF EXISTS `bloodbank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bloodbank` (
  `bloodbank_name` varchar(500) NOT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `hospital_name` varchar(500) DEFAULT NULL,
  `bloodbank_phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bloodbank_name`),
  UNIQUE KEY `bloodbank_phone` (`bloodbank_phone`),
  KEY `hospital_name` (`hospital_name`),
  CONSTRAINT `bloodbank_ibfk_1` FOREIGN KEY (`hospital_name`) REFERENCES `hospital` (`hospital_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bloodbank`
--

LOCK TABLES `bloodbank` WRITE;
/*!40000 ALTER TABLE `bloodbank` DISABLE KEYS */;
INSERT INTO `bloodbank` VALUES ('Beth Israel Blood Bank','330 Brookline Ave','Boston','MA','02215','Beth Israel Deaconess Medical Center','2376467850'),('Boston Blood Bank','1 Main St','Boston','MA','02110','Boston General Hospital','8764578345'),('Boston Children Blood Bank','300 Longwood Ave','Boston','MA','02115','Boston Children\'s Hospital','5674575678'),('Boston VA Blood Bank','1400 VFW Pkwy','West Roxbury','MA','02132','Boston VA Healthcare System','4345785333'),('Brigham Blood Bank','75 Francis St','Boston','MA','02115','Brigham and Women\'s Hospital','8341227676'),('Dana-Farber Blood Bank','450 Brookline Ave','Boston','MA','02215','Dana-Farber Cancer Institute','6786789995'),('Harvard Blood Bank','10 Medical Center Dr','Boston','MA','02115','Harvard Medical Center','2934872747'),('Massachusetts Blood Bank','55 Fruit St','Boston','MA','02114','Massachusetts General Hospital','2341234123'),('St. Elizabeth Blood Bank','736 Cambridge St','Brighton','MA','02135','Saint Elizabeth\'s Medical Center','3457854333'),('Tufts Blood Bank','800 Washington St','Boston','MA','02111','Tufts Medical Center','2342343244');
/*!40000 ALTER TABLE `bloodbank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bloodgroup`
--

DROP TABLE IF EXISTS `bloodgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bloodgroup` (
  `bloodgroup_name` varchar(10) NOT NULL,
  PRIMARY KEY (`bloodgroup_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bloodgroup`
--

LOCK TABLES `bloodgroup` WRITE;
/*!40000 ALTER TABLE `bloodgroup` DISABLE KEYS */;
INSERT INTO `bloodgroup` VALUES ('A-'),('A+'),('AB-'),('AB+'),('B-'),('B+'),('O-'),('O+');
/*!40000 ALTER TABLE `bloodgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donationcamp`
--

DROP TABLE IF EXISTS `donationcamp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donationcamp` (
  `camp_id` int NOT NULL AUTO_INCREMENT,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `camp_date` date NOT NULL,
  `camp_time` time NOT NULL,
  `bloodbank_name` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`camp_id`),
  KEY `bloodbank_name` (`bloodbank_name`),
  CONSTRAINT `donationcamp_ibfk_1` FOREIGN KEY (`bloodbank_name`) REFERENCES `bloodbank` (`bloodbank_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donationcamp`
--

LOCK TABLES `donationcamp` WRITE;
/*!40000 ALTER TABLE `donationcamp` DISABLE KEYS */;
INSERT INTO `donationcamp` VALUES (1,'1 Main St','Boston','MA','02110','2023-04-01','10:00:00','Boston Blood Bank'),(2,'10 Medical Center Dr','Boston','MA','02115','2023-04-02','09:00:00','Harvard Blood Bank'),(3,'330 Brookline Ave','Boston','MA','02215','2023-04-03','12:00:00','Beth Israel Blood Bank'),(4,'800 Washington St','Boston','MA','02111','2023-04-04','11:00:00','Tufts Blood Bank'),(5,'55 Fruit St','Boston','MA','02114','2023-04-05','14:00:00','Massachusetts Blood Bank'),(6,'75 Francis St','Boston','MA','02115','2023-04-06','13:00:00','Brigham Blood Bank'),(7,'300 Longwood Ave','Boston','MA','02115','2023-04-07','15:00:00','Boston Children Blood Bank'),(8,'450 Brookline Ave','Boston','MA','02215','2023-04-08','16:00:00','Dana-Farber Blood Bank'),(9,'736 Cambridge St','Brighton','MA','02135','2023-04-09','17:00:00','St. Elizabeth Blood Bank'),(10,'1400 VFW Pkwy','West Roxbury','MA','02132','2023-04-10','10:00:00','Boston VA Blood Bank');
/*!40000 ALTER TABLE `donationcamp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donor`
--

DROP TABLE IF EXISTS `donor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donor` (
  `donor_id` int NOT NULL AUTO_INCREMENT,
  `donor_fname` varchar(500) DEFAULT NULL,
  `donor_lname` varchar(500) DEFAULT NULL,
  `donor_username` varchar(500) NOT NULL,
  `donor_password` varchar(20) NOT NULL,
  `donor_age` int DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `donor_weight` int DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `donor_phone` varchar(20) DEFAULT NULL,
  `donor_email` varchar(200) DEFAULT NULL,
  `donor_hemoglobin` varchar(20) DEFAULT NULL,
  `donor_blood_group` varchar(20) DEFAULT NULL,
  `lab_technician_id` int DEFAULT NULL,
  PRIMARY KEY (`donor_id`),
  UNIQUE KEY `donor_password` (`donor_password`),
  UNIQUE KEY `donor_phone` (`donor_phone`),
  UNIQUE KEY `donor_email` (`donor_email`),
  KEY `lab_technician_id` (`lab_technician_id`),
  KEY `donor_blood_group` (`donor_blood_group`),
  CONSTRAINT `donor_ibfk_1` FOREIGN KEY (`lab_technician_id`) REFERENCES `lab_technician` (`lab_technician_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `donor_ibfk_2` FOREIGN KEY (`donor_blood_group`) REFERENCES `bloodgroup` (`bloodgroup_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donor`
--

LOCK TABLES `donor` WRITE;
/*!40000 ALTER TABLE `donor` DISABLE KEYS */;
INSERT INTO `donor` VALUES (1,'John','Doe','johndoe','Pass1',25,'Male',150,'123 Main St','Boston','MA','02111','555-1234','john.doe@email.com','14.5 g/dL','A+',1),(2,'Jane','Smith','janesmith','Pass2',32,'Female',125,'456 Elm St','Cambridge','MA','02138','555-5678','jane.smith@email.com','13.8 g/dL','B+',1),(3,'Michael','Johnson','michaeljohnson','Pass3',28,'Male',170,'789 Oak St','Somerville','MA','02143','555-9012','michael.johnson@email.com','15.2 g/dL','O+',2),(4,'Emily','Davis','EDavis','Pass4',22,'Female',110,'10 Pine St','Boston','MA','02109','555-3456','emily.davis@email.com','12.6 g/dL','AB+',2),(5,'David','Wilson','DavidW','Pass5',30,'Male',155,'11 Maple St','Cambridge','MA','02139','555-7890','david.wilson@email.com','14.0 g/dL','A-',3),(6,'Samantha','Brown','SamanthaB','Pass6',27,'Female',120,'12 Oak St','Boston','MA','02108','555-2345','samantha.brown@email.com','12.8 g/dL','B-',3),(7,'Matthew','Garcia','MatthewGarcia','Pass7',29,'Male',165,'13 Elm St','Somerville','MA','02144','555-6789','matthew.garcia@email.com','15.5 g/dL','O-',4),(8,'Ashley','Rodriguez','AshleyR','Pass8',26,'Female',130,'14 Maple St','Boston','MA','02110','555-1235','ashley.rodriguez@email.com','13.5 g/dL','AB-',4);
/*!40000 ALTER TABLE `donor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital`
--

DROP TABLE IF EXISTS `hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital` (
  `hospital_name` varchar(500) NOT NULL,
  `hpt_username` varchar(500) NOT NULL,
  `hpt_password` varchar(20) NOT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `hpt_phone` varchar(20) DEFAULT NULL,
  `hpt_email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`hospital_name`),
  UNIQUE KEY `hpt_password` (`hpt_password`),
  UNIQUE KEY `hpt_phone` (`hpt_phone`),
  UNIQUE KEY `hpt_email` (`hpt_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital`
--

LOCK TABLES `hospital` WRITE;
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` VALUES ('Beth Israel Deaconess Medical Center','bidmc','hospass3','330 Brookline Ave','Boston','MA','02215','6573526749','bidmc@gmail.com'),('Boston Children\'s Hospital','bch','hospass7','300 Longwood Ave','Boston','MA','02115','7599734954','bch@gmail.com'),('Boston General Hospital','bgh','hospass1','1 Main St','Boston','MA','02110','3743746346','bgh@gmail.com'),('Boston VA Healthcare System','bvahs','hospass10','1400 VFW Pkwy','West Roxbury','MA','02132','2834672783','bvahs@gmail.com'),('Brigham and Women\'s Hospital','bawh','hospass6','75 Francis St','Boston','MA','02115','8745873457','bawh@gmail.com'),('Dana-Farber Cancer Institute','dfci','hospass8','450 Brookline Ave','Boston','MA','02215','4636573464','dfci@gmail.com'),('Harvard Medical Center','hmc','hospass2','10 Medical Center Dr','Boston','MA','02115','6745389465','hmc@gmail.com'),('Massachusetts General Hospital','mgh','hospass5','55 Fruit St','Boston','MA','02114','6573564992','mchh@gmail.com'),('Saint Elizabeth\'s Medical Center','semc','hospass9','736 Cambridge St','Brighton','MA','02135','9784778244','scmc@gmail.com'),('Tufts Medical Center','tmc','hospass4','800 Washington St','Boston','MA','02111','4537284673','tmc@gmail.com');
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `bloodbank_name` varchar(500) NOT NULL,
  `bloodgroup_name` varchar(10) NOT NULL,
  `amount_litres` int DEFAULT NULL,
  PRIMARY KEY (`bloodgroup_name`,`bloodbank_name`),
  KEY `bloodbank_name` (`bloodbank_name`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`bloodgroup_name`) REFERENCES `bloodgroup` (`bloodgroup_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`bloodbank_name`) REFERENCES `bloodbank` (`bloodbank_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('Massachusetts Blood Bank','A-',32),('Boston Blood Bank','A+',100),('Harvard Blood Bank','A+',150),('Massachusetts Blood Bank','A+',200),('Boston Blood Bank','AB-',20),('Massachusetts Blood Bank','AB+',75),('Dana-Farber Blood Bank','B-',40),('Boston Blood Bank','B+',50),('Massachusetts Blood Bank','B+',100),('Harvard Blood Bank','O+',100);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab_technician`
--

DROP TABLE IF EXISTS `lab_technician`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lab_technician` (
  `lab_technician_id` int NOT NULL AUTO_INCREMENT,
  `lab_technician_fname` varchar(500) DEFAULT NULL,
  `lab_technician_lname` varchar(500) DEFAULT NULL,
  `lab_technician_username` varchar(500) NOT NULL,
  `lab_technician_password` varchar(20) NOT NULL,
  `street` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `lab_technician_phone` varchar(20) DEFAULT NULL,
  `lab_technician_email` varchar(200) DEFAULT NULL,
  `bloodbank_name` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`lab_technician_id`),
  UNIQUE KEY `lab_technician_password` (`lab_technician_password`),
  UNIQUE KEY `lab_technician_phone` (`lab_technician_phone`),
  UNIQUE KEY `lab_technician_email` (`lab_technician_email`),
  KEY `bloodbank_name` (`bloodbank_name`),
  CONSTRAINT `lab_technician_ibfk_1` FOREIGN KEY (`bloodbank_name`) REFERENCES `bloodbank` (`bloodbank_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab_technician`
--

LOCK TABLES `lab_technician` WRITE;
/*!40000 ALTER TABLE `lab_technician` DISABLE KEYS */;
INSERT INTO `lab_technician` VALUES (1,'Joseph','Rodriguez','josephrodriguez','Password1','123 Main St','Boston','MA','02115','555-3234','josephrodriguez@email.com','Boston Blood Bank'),(2,'Marcia','Atkins','marciaatkins','Password2','456 Elm St','Cambridge','MA','02139','555-7678','marciaatkins@email.com','Harvard Blood Bank'),(3,'Adam','Edwards','adamedwards','Password3','789 Oak St','Somerville','MA','02143','555-8012','adamedwards@email.com','Beth Israel Blood Bank'),(4,'Kenneth','Ruiz','kennethruiz','Password4','321 Pine St','Newton','MA','02458','555-4456','kennethruiz@email.com','Tufts Blood Bank'),(5,'Calvin','Medina','calvinmedina','Password5','654 Cedar St','Brookline','MA','02445','555-9890','calvinmedina@email.com','Massachusetts Blood Bank'),(6,'Selena','Miller','selenamiller','Password6','987 Maple St','Medford','MA','02155','555-1345','selenamiller@email.com','Brigham Blood Bank'),(7,'Alyssa','Moran','alyssamoran','Password7','210 Walnut St','Belmont','MA','02478','555-4789','alyssamoran@email.com','Boston Children Blood Bank'),(8,'Stephen','Hardy','stephenhardy','Password8','543 Birch St','Waltham','MA','02452','555-3123','stephenhardy@email.com','Dana-Farber Blood Bank'),(9,'Karen','Gonzalez','karengonzalez','Password9','876 Pine St','Lexington','MA','02420','555-0567','karengonzalez@email.com','St. Elizabeth Blood Bank'),(10,'Scott','Lee','scottlee','Password10','321 Oak St','Arlington','MA','02474','555-0901','scottlee@email.com','Boston VA Blood Bank');
/*!40000 ALTER TABLE `lab_technician` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `requested_blood_group` varchar(10) NOT NULL,
  `requested_amount` int NOT NULL,
  `is_open` tinyint(1) NOT NULL DEFAULT '1',
  `hospital_name` varchar(500) DEFAULT NULL,
  `completed_by_bloodbank` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`request_id`),
  KEY `completed_by_bloodbank` (`completed_by_bloodbank`),
  KEY `hospital_name` (`hospital_name`),
  KEY `requested_blood_group` (`requested_blood_group`),
  CONSTRAINT `request_ibfk_1` FOREIGN KEY (`completed_by_bloodbank`) REFERENCES `bloodbank` (`bloodbank_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `request_ibfk_2` FOREIGN KEY (`hospital_name`) REFERENCES `hospital` (`hospital_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `request_ibfk_3` FOREIGN KEY (`requested_blood_group`) REFERENCES `bloodgroup` (`bloodgroup_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
INSERT INTO `request` VALUES (1,'A+',5,0,'Boston General Hospital','Boston Blood Bank'),(2,'B-',10,0,'Harvard Medical Center','Harvard Blood Bank'),(3,'O+',7,1,'Beth Israel Deaconess Medical Center',NULL),(4,'AB-',15,0,'Tufts Medical Center','Tufts Blood Bank'),(5,'A-',8,0,'Massachusetts General Hospital','Massachusetts Blood Bank'),(6,'B+',12,0,'Brigham and Women\'s Hospital','Brigham Blood Bank'),(7,'O-',3,1,'Boston Children\'s Hospital',NULL),(8,'AB+',20,1,'Dana-Farber Cancer Institute',NULL),(9,'A+',6,0,'Saint Elizabeth\'s Medical Center','St. Elizabeth Blood Bank'),(10,'B-',9,0,'Boston VA Healthcare System','Boston VA Blood Bank');
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'bloodbankdb'
--

--
-- Dumping routines for database 'bloodbankdb'
--
/*!50003 DROP FUNCTION IF EXISTS `check_registration` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `check_registration`(username varchar(500)) RETURNS tinyint(1)
    READS SQL DATA
begin
declare check_flag bool;
if (exists (SELECT * FROM donor WHERE donor_username = username) or 
	exists (SELECT * FROM admin WHERE admin_username = username) or
    exists (SELECT * FROM lab_technician WHERE lab_technician_username = username) or
    exists (SELECT * FROM hospital WHERE hpt_username = username))
then
	set check_flag = true;
else
    set check_flag = false;
end if;
return (check_flag);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `login` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `login`(username varchar(500), pswd varchar(50)) RETURNS varchar(20) CHARSET utf8mb4
    READS SQL DATA
begin
declare usertype varchar(20);
if exists (SELECT * FROM donor WHERE donor_username = username AND donor_password = pswd) then
	set usertype='donor'; 
elseif exists (SELECT * FROM admin WHERE admin_username = username AND admin_password = pswd) then
	set usertype='admin';
elseif exists (SELECT * FROM lab_technician WHERE lab_technician_username = username AND lab_technician_password = pswd) then
	set usertype='lab_technician';
elseif exists (SELECT * FROM hospital WHERE hpt_username = username AND hpt_password = pswd) then
	set usertype='hospital';
else
    set usertype = null;
end if;
return (usertype);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_appointments` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_appointments`(donor_username_p varchar(500),appointment_date_p date, bloodbank_name_p varchar(500))
begin
if (appointment_date_p is not NULL AND bloodbank_name_p!="Select an Option") then
	SELECT a.*,d.street,d.bloodbank_name FROM appointment a join donationcamp d on a.camp_id=d.camp_id WHERE a.donor_id = (select donor_id from donor where donor_username=donor_username_p) and a.appointment_date = appointment_date_p and a.camp_id = any (select camp_id from donationcamp  where bloodbank_name=bloodbank_name_p);
            
elseif appointment_date_p is not NULL then
	SELECT a.*,d.street,d.bloodbank_name FROM appointment a join donationcamp d on a.camp_id=d.camp_id WHERE a.donor_id = (select donor_id from donor where donor_username=donor_username_p) and a.appointment_date = appointment_date_p;
            
elseif bloodbank_name_p!="Select an Option" then
	SELECT a.*,d.street,d.bloodbank_name FROM appointment a join donationcamp d on a.camp_id=d.camp_id WHERE a.donor_id = (select donor_id from donor where donor_username=donor_username_p) and a.camp_id = any (select d.camp_id from donationcamp d where bloodbank_name=bloodbank_name_p);
            
else
	SELECT a.*,d.street,d.bloodbank_name FROM appointment a join donationcamp d on a.camp_id=d.camp_id WHERE a.donor_id = (select donor_id from donor where donor_username=donor_username_p);
end if;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_camps` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_camps`(donor_username_p varchar(500),appointment_date_p date, bloodbank_name_p varchar(500))
begin
if (appointment_date_p is not NULL AND bloodbank_name_p!="Select an Option") then
	SELECT * FROM donationcamp WHERE camp_date = appointment_date_p and bloodbank_name= bloodbank_name_p;
            
elseif appointment_date_p is not NULL then
	SELECT * FROM donationcamp WHERE camp_date = appointment_date_p;
            
elseif bloodbank_name_p!="Select an Option" then
	SELECT * FROM donationcamp WHERE bloodbank_name= bloodbank_name_p;
            
else
	SELECT * FROM donationcamp;
end if;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_request` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_request`(hpt_username_p varchar(500), requested_blood_group_p varchar(10),status bool)
begin
if (requested_blood_group_p!='' and status is not null) then
	SELECT  requested_amount, completed_by_bloodbank from request where hospital_name=hpt_username_p and requested_blood_group=requested_blood_group_p and is_open=status;
                
                
elseif requested_blood_group_p!='' then
	SELECT  requested_amount, is_open, completed_by_bloodbank from request where hospital_name=hpt_username_p and requested_blood_group=requested_blood_group_p;
                
                
elseif status is not null then
	SELECT  requested_blood_group, requested_amount, completed_by_bloodbank from request where hospital_name=hpt_username_p and is_open=status;
                
else
	SELECT requested_blood_group,  requested_amount, is_open, completed_by_bloodbank from request where hospital_name=hpt_username_p;

end if;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_donor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_donor`(donor_email_p varchar(200),donor_weight_p int, donor_hemoglobin_p varchar(20), donor_blood_group_p varchar(20))
begin
if (donor_weight_p != 0) then
	update donor set donor_weight=donor_weight_p where donor_email=donor_email_p;
end if;
if (donor_hemoglobin_p!='') then
	update donor set donor_hemoglobin=donor_hemoglobin_p where donor_email=donor_email_p;
end if;
if (donor_blood_group_p!='') then
	update donor set donor_blood_group=donor_blood_group_p where donor_email=donor_email_p;
end if;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-20 12:55:58
