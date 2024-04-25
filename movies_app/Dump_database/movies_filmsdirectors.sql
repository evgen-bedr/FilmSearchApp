CREATE DATABASE  IF NOT EXISTS `movies` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `movies`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: movies
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
-- Table structure for table `filmsdirectors`
--

DROP TABLE IF EXISTS `filmsdirectors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `filmsdirectors` (
  `film_id` int NOT NULL,
  `director_id` int NOT NULL,
  PRIMARY KEY (`film_id`,`director_id`),
  KEY `director_id` (`director_id`),
  CONSTRAINT `filmsdirectors_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `films` (`id`) ON DELETE CASCADE,
  CONSTRAINT `filmsdirectors_ibfk_2` FOREIGN KEY (`director_id`) REFERENCES `directors` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filmsdirectors`
--

LOCK TABLES `filmsdirectors` WRITE;
/*!40000 ALTER TABLE `filmsdirectors` DISABLE KEYS */;
INSERT INTO `filmsdirectors` VALUES (1,1),(1,2),(1,3),(2,4),(2,5),(1544,5),(2,6),(3,7),(4,8),(5,9),(6,10),(49,10),(80,10),(96,10),(183,10),(201,10),(214,10),(268,10),(489,10),(931,10),(7,11),(546,11),(8,12),(1352,12),(8,13),(8,14),(9,15),(10,16),(10,17),(10,18),(11,19),(565,19),(12,20),(1157,20),(13,21),(13,22),(13,23),(14,24),(14,25),(14,26),(192,26),(15,27),(15,28),(16,29),(16,30),(17,31),(299,31),(18,32),(19,33),(20,34),(21,35),(22,36),(23,37),(24,38),(1333,38),(25,39),(26,40),(350,40),(364,40),(26,41),(27,42),(28,43),(29,44),(29,45),(29,46),(39,46),(30,47),(31,48),(32,49),(33,50),(34,51),(35,52),(35,53),(36,54),(36,55),(37,56),(38,57),(39,59),(40,60),(1038,60),(40,61),(41,62),(41,63),(42,64),(43,65),(44,66),(901,66),(44,67),(44,68),(45,69),(45,70),(45,71),(46,72),(47,73),(48,74),(48,75),(50,77),(51,78),(1095,78),(52,79),(53,80),(189,80),(1043,80),(54,81),(55,82),(56,83),(57,84),(58,85),(59,86),(60,87),(61,88),(61,89),(62,90),(1179,90),(63,91),(64,92),(1069,92),(65,93),(65,94),(65,95),(337,95),(66,96),(67,97),(68,98),(72,98),(1316,98),(69,99),(1563,99),(70,100),(70,101),(71,102),(71,103),(71,104),(73,106),(74,107),(75,108),(75,109),(76,110),(76,111),(1034,111),(77,112),(78,113),(911,113),(79,114),(985,114),(81,116),(1024,116),(82,117),(82,118),(83,119),(83,120),(84,121),(1607,121),(85,122),(85,123),(86,124),(90,124),(87,125),(503,125),(87,126),(88,127),(1088,127),(89,128),(91,130),(92,131),(93,132),(590,132),(691,132),(727,132),(94,133),(94,134),(95,135),(97,137),(98,138),(98,139),(99,140),(1123,140),(100,141),(101,142),(102,143),(102,144),(102,145),(103,146),(104,147),(105,148),(106,149),(107,150),(325,150),(108,151),(108,152),(108,153),(109,154),(110,155),(111,156),(112,157),(1352,157),(112,158),(112,159),(113,160),(412,160),(114,161),(115,162),(116,163),(117,164),(118,165),(119,166),(119,167),(119,168),(120,169),(121,170),(121,171),(121,172),(122,173),(123,174),(124,175),(125,176),(125,177),(125,178),(126,179),(127,180),(128,181),(129,182),(129,183),(130,184),(131,185),(132,186),(133,187),(133,188),(134,189),(654,189),(135,190),(136,191),(137,192),(137,193),(137,194),(138,195),(139,196),(139,197),(139,198),(140,199),(141,200),(142,201),(143,202),(144,203),(144,204),(145,205),(146,206),(147,207),(148,208),(149,209),(150,210),(150,211),(151,212),(151,213),(152,214),(152,215),(152,216),(153,217),(1149,217),(154,218),(156,219),(157,220),(158,221),(1056,221),(159,222),(714,222),(725,222),(160,223),(160,224),(160,225),(161,226),(162,227),(163,228),(163,229),(164,230),(165,231),(166,232),(167,233),(167,234),(959,234),(167,235),(959,235),(168,236),(168,237),(169,238),(169,239),(170,240),(515,240),(171,241),(171,242),(171,243),(172,244),(173,245),(174,246),(175,247),(176,248),(177,249),(178,250),(179,251),(180,252),(181,253),(181,254),(181,255),(182,256),(1382,256),(184,258),(185,259),(186,260),(186,261),(186,262),(187,263),(188,264),(188,265),(188,266),(189,268),(189,269),(190,270),(190,271),(191,272),(191,273),(191,274),(1600,274),(192,275),(192,276),(193,278),(193,279),(193,280),(194,281),(195,282),(196,283),(197,284),(198,285),(199,286),(200,287),(200,288),(200,289),(202,291),(203,292),(204,293),(204,294),(204,295),(205,296),(206,297),(207,298),(207,299),(208,300),(208,301),(208,302),(209,303),(210,304),(211,305),(212,306),(213,307),(215,309),(215,310),(216,311),(217,312),(218,313),(219,314),(220,315),(221,316),(221,317),(221,318),(222,319),(223,320),(224,321),(225,322),(226,323),(226,324),(227,325),(227,326),(228,327),(229,328),(230,329),(231,330),(231,331),(232,332),(233,333),(234,334),(235,335),(236,336),(236,337),(237,338),(238,339),(239,340),(240,341),(241,342),(242,343),(243,344),(244,345),(245,346),(246,347),(247,348),(248,349),(249,350),(250,351),(451,351),(251,352),(252,353),(252,354),(253,355),(254,356),(254,357),(254,358),(1170,358),(255,359),(255,360),(256,361),(257,362),(257,363),(258,364),(494,364),(259,365),(260,366),(261,367),(262,368),(262,369),(263,370),(1455,370),(264,371),(265,372),(265,373),(265,374),(266,375),(267,376),(269,378),(269,379),(269,380),(270,381),(270,382),(270,383),(271,384),(272,385),(273,386),(1363,386),(1426,386),(274,387),(275,388),(276,389),(277,390),(278,391),(279,392),(280,393),(281,394),(1481,394),(281,395),(282,396),(283,397),(283,398),(283,399),(284,400),(284,401),(285,402),(286,403),(287,404),(288,405),(288,406),(288,407),(289,408),(290,409),(290,410),(291,411),(292,412),(293,413),(294,414),(295,415),(296,416),(297,417),(298,418),(300,420),(301,421),(302,422),(1255,422),(302,423),(302,424),(303,425),(304,426),(305,427),(305,428),(306,429),(464,429),(525,429),(629,429),(678,429),(685,429),(694,429),(699,429),(786,429),(789,429),(873,429),(1452,429),(1472,429),(307,430),(307,431),(308,432),(309,433),(310,434),(311,435),(1058,435),(312,436),(313,437),(314,438),(315,439),(748,439),(315,440),(315,441),(316,442),(316,443),(317,444),(565,444),(318,445),(319,446),(320,447),(321,448),(322,449),(323,450),(324,451),(1254,451),(326,453),(327,454),(328,455),(329,456),(329,457),(329,458),(330,459),(331,460),(332,461),(332,462),(333,463),(334,464),(335,465),(336,466),(337,468),(337,469),(953,469),(338,470),(339,471),(340,472),(340,473),(340,474),(1013,474),(1454,474),(341,475),(342,476),(343,477),(344,478),(345,479),(345,480),(346,481),(346,482),(346,483),(347,484),(348,485),(349,486),(351,488),(352,489),(353,490),(354,491),(354,492),(355,493),(356,494),(357,495),(358,496),(359,497),(360,498),(361,499),(362,500),(363,501),(365,503),(366,504),(367,505),(367,506),(367,507),(368,508),(368,509),(368,510),(369,511),(1443,511),(370,512),(370,513),(1238,513),(371,514),(372,515),(373,516),(1410,516),(374,517),(375,518),(376,519),(377,520),(378,521),(379,522),(380,523),(381,524),(382,525),(526,525),(382,526),(383,527),(384,528),(385,529),(386,530),(837,530),(387,531),(388,532),(389,533),(390,534),(391,535),(392,536),(393,537),(394,538),(395,539),(396,540),(396,541),(397,542),(398,543),(399,544),(400,545),(401,546),(1329,546),(402,547),(402,548),(402,549),(548,549),(403,550),(442,550),(404,551),(405,552),(536,552),(406,553),(407,554),(408,555),(409,556),(410,556),(411,558),(413,560),(414,561),(415,562),(416,563),(417,564),(418,565),(419,566),(420,567),(421,568),(422,569),(423,570),(424,571),(425,572),(426,573),(427,574),(427,575),(427,576),(428,577),(429,578),(429,579),(429,580),(430,581),(430,582),(431,583),(432,584),(433,585),(434,586),(1272,586),(435,587),(435,588),(435,589),(436,590),(437,591),(438,592),(438,593),(438,594),(439,595),(440,596),(440,597),(440,598),(441,599),(441,600),(441,601),(443,603),(444,604),(444,605),(445,606),(446,607),(447,608),(448,609),(448,610),(448,611),(449,612),(449,613),(450,614),(452,616),(452,617),(452,618),(625,618),(453,619),(454,620),(505,620),(455,621),(455,622),(455,623),(456,624),(456,625),(456,626),(457,627),(458,628),(459,629),(459,630),(459,631),(460,632),(1030,632),(461,633),(462,634),(463,635),(465,637),(466,638),(466,639),(467,640),(468,641),(468,642),(469,643),(470,644),(471,645),(472,646),(473,647),(474,648),(475,649),(476,650),(477,651),(478,652),(479,653),(480,654),(481,655),(482,656),(483,657),(484,658),(485,659),(486,660),(487,661),(487,662),(487,663),(488,664),(490,666),(491,667),(492,668),(493,669),(495,671),(496,672),(496,673),(497,674),(498,675),(498,676),(499,677),(500,678),(501,679),(502,680),(504,682),(505,684),(506,685),(507,686),(507,687),(508,688),(508,689),(509,690),(510,691),(511,692),(512,693),(513,694),(514,695),(516,697),(517,698),(518,699),(519,700),(520,701),(1322,701),(521,702),(522,703),(522,704),(523,705),(523,706),(523,707),(524,708),(753,708),(528,711),(529,712),(530,713),(530,714),(735,714),(530,715),(531,716),(531,717),(531,718),(556,718),(665,718),(767,718),(532,719),(532,720),(532,721),(533,722),(544,722),(558,722),(592,722),(593,722),(533,723),(544,723),(558,723),(592,723),(593,723),(534,724),(534,725),(534,726),(535,727),(536,729),(536,730),(537,731),(538,732),(539,733),(610,733),(540,734),(541,735),(542,736),(542,737),(543,738),(603,738),(729,738),(543,739),(543,740),(603,740),(544,743),(545,744),(547,746),(547,747),(547,748),(548,750),(548,751),(549,752),(549,753),(549,754),(550,755),(551,756),(551,757),(552,758),(552,759),(553,760),(553,761),(553,762),(554,763),(655,763),(554,764),(554,765),(749,765),(555,766),(555,767),(555,768),(557,770),(559,773),(560,774),(561,775),(562,776),(563,777),(563,778),(563,779),(564,780),(564,781),(564,782),(566,785),(567,786),(568,787),(569,788),(570,789),(571,790),(571,791),(572,792),(573,793),(764,793),(574,794),(771,794),(574,795),(574,796),(575,797),(575,798),(575,799),(576,800),(576,801),(577,802),(578,803),(579,804),(580,805),(581,806),(664,806),(740,806),(582,807),(583,808),(705,808),(584,809),(585,810),(732,810),(586,811),(587,812),(587,813),(587,814),(588,815),(588,816),(589,817),(589,818),(589,819),(590,820),(591,822),(592,823),(594,828),(595,829),(595,830),(595,831),(596,832),(597,833),(634,833),(695,833),(597,834),(634,834),(597,835),(598,836),(598,837),(598,838),(599,839),(599,840),(599,841),(600,842),(600,843),(600,844),(601,845),(601,846),(602,847),(602,848),(604,851),(604,852),(605,853),(605,854),(605,855),(606,856),(651,856),(607,857),(608,858),(608,859),(608,860),(609,861),(611,863),(770,863),(611,864),(612,865),(725,865),(612,866),(612,867),(613,868),(614,869),(614,870),(614,871),(615,872),(615,873),(616,874),(616,875),(616,876),(617,877),(618,878),(619,879),(619,880),(620,881),(687,881),(621,882),(621,883),(622,884),(623,885),(623,886),(624,887),(657,887),(625,888),(625,890),(626,891),(626,892),(626,893),(670,893),(627,894),(627,895),(628,896),(630,898),(631,899),(632,900),(750,900),(632,901),(633,902),(635,905),(636,906),(739,906),(637,907),(638,908),(639,909),(640,910),(641,911),(641,912),(641,913),(642,914),(643,915),(644,916),(644,917),(644,918),(645,919),(646,920),(647,921),(647,922),(647,923),(648,924),(649,925),(649,926),(649,927),(650,928),(710,928),(759,928),(652,930),(652,931),(652,932),(653,933),(656,936),(657,938),(658,939),(1408,939),(659,940),(745,940),(659,941),(659,942),(660,943),(660,944),(660,945),(661,946),(661,947),(662,948),(662,949),(663,950),(666,953),(666,954),(667,955),(668,956),(669,957),(671,959),(671,960),(671,961),(672,962),(673,963),(674,964),(674,965),(674,966),(675,967),(676,968),(677,969),(677,970),(677,971),(679,973),(679,974),(739,974),(680,975),(681,976),(681,977),(681,978),(682,979),(763,979),(682,980),(682,981),(683,982),(683,983),(684,984),(1519,984),(686,986),(1387,986),(688,988),(689,989),(690,990),(690,991),(691,993),(691,994),(692,995),(693,996),(748,996),(696,999),(696,1000),(697,1001),(698,1002),(700,1004),(701,1005),(711,1005),(701,1006),(770,1006),(701,1007),(711,1007),(702,1008),(703,1009),(704,1010),(706,1012),(707,1013),(708,1014),(709,1015),(711,1019),(712,1020),(713,1021),(713,1022),(713,1023),(715,1025),(716,1026),(717,1027),(718,1028),(718,1029),(718,1030),(719,1031),(719,1032),(719,1033),(720,1034),(721,1035),(733,1035),(721,1036),(733,1036),(722,1037),(722,1038),(723,1039),(724,1040),(726,1043),(728,1045),(728,1046),(728,1047),(730,1049),(731,1050),(732,1052),(734,1055),(736,1057),(737,1058),(737,1059),(738,1060),(739,1062),(741,1065),(741,1066),(741,1067),(742,1068),(742,1069),(742,1070),(743,1071),(744,1072),(746,1074),(746,1075),(747,1076),(751,1081),(752,1082),(752,1083),(753,1085),(754,1086),(755,1087),(756,1088),(757,1089),(758,1090),(758,1091),(760,1093),(761,1094),(761,1095),(761,1096),(762,1097),(762,1098),(762,1099),(763,1101),(764,1103),(764,1104),(765,1105),(766,1106),(766,1107),(767,1109),(768,1110),(768,1111),(769,1112),(770,1114),(772,1117),(772,1118),(772,1119),(773,1120),(774,1121),(774,1122),(774,1123),(775,1124),(775,1125),(775,1126),(776,1127),(777,1128),(778,1129),(778,1130),(779,1131),(779,1132),(780,1133),(781,1134),(782,1135),(783,1136),(784,1137),(784,1138),(784,1139),(785,1140),(787,1142),(788,1143),(925,1143),(1086,1143),(790,1145),(791,1146),(792,1147),(793,1148),(794,1149),(795,1150),(796,1151),(797,1152),(1389,1152),(798,1153),(799,1154),(800,1155),(801,1156),(802,1157),(803,1158),(804,1159),(805,1160),(806,1161),(807,1162),(808,1163),(809,1164),(810,1165),(810,1166),(810,1167),(811,1168),(812,1169),(813,1170),(814,1171),(815,1172),(816,1173),(817,1174),(818,1175),(819,1176),(820,1177),(821,1178),(822,1179),(822,1180),(823,1181),(824,1182),(825,1183),(826,1184),(827,1185),(827,1186),(828,1187),(829,1188),(830,1189),(831,1190),(831,1191),(832,1192),(833,1193),(834,1194),(835,1195),(836,1196),(837,1197),(838,1199),(839,1200),(840,1201),(841,1202),(842,1203),(843,1204),(844,1205),(845,1206),(846,1207),(846,1208),(847,1209),(847,1210),(1509,1210),(848,1211),(849,1212),(850,1213),(851,1214),(852,1215),(853,1216),(854,1217),(855,1218),(855,1219),(855,1220),(1153,1220),(856,1221),(857,1222),(858,1223),(859,1224),(860,1225),(861,1226),(862,1227),(863,1228),(864,1229),(865,1230),(866,1231),(866,1232),(867,1233),(868,1234),(869,1235),(870,1236),(934,1236),(870,1237),(870,1238),(871,1239),(871,1240),(872,1241),(872,1242),(872,1243),(874,1245),(874,1246),(875,1247),(875,1248),(875,1249),(876,1250),(877,1251),(878,1252),(879,1253),(880,1254),(880,1255),(880,1256),(881,1257),(881,1258),(882,1259),(883,1260),(884,1261),(885,1262),(886,1263),(887,1264),(888,1265),(889,1266),(890,1267),(891,1268),(891,1269),(891,1270),(892,1271),(892,1272),(893,1273),(978,1273),(894,1274),(895,1275),(896,1276),(897,1277),(898,1278),(899,1279),(900,1280),(902,1282),(903,1283),(904,1284),(905,1285),(906,1286),(907,1287),(908,1288),(909,1289),(910,1290),(912,1292),(913,1293),(914,1294),(1471,1294),(915,1295),(916,1296),(917,1297),(918,1298),(919,1299),(919,1300),(919,1301),(920,1302),(920,1303),(921,1304),(922,1305),(923,1306),(924,1307),(925,1308),(926,1310),(926,1311),(1302,1311),(926,1312),(927,1313),(928,1314),(929,1315),(930,1316),(932,1318),(933,1319),(933,1320),(935,1322),(935,1323),(936,1324),(936,1325),(936,1326),(937,1327),(938,1328),(938,1329),(938,1330),(939,1331),(1167,1331),(940,1332),(941,1333),(942,1334),(943,1335),(943,1336),(969,1336),(944,1337),(945,1338),(946,1339),(947,1340),(948,1341),(949,1342),(950,1343),(951,1344),(952,1345),(953,1346),(953,1347),(954,1349),(955,1350),(956,1351),(957,1352),(958,1353),(960,1356),(961,1357),(962,1358),(963,1359),(964,1360),(965,1361),(965,1362),(965,1363),(966,1364),(967,1365),(968,1366),(969,1368),(970,1369),(971,1370),(972,1371),(973,1372),(974,1373),(975,1374),(975,1375),(976,1376),(977,1377),(979,1379),(980,1380),(981,1381),(982,1382),(983,1383),(984,1384),(985,1385),(986,1387),(986,1388),(987,1389),(988,1390),(989,1391),(989,1392),(990,1393),(991,1394),(992,1395),(993,1396),(994,1397),(995,1398),(996,1399),(997,1400),(998,1401),(999,1402),(1000,1403),(1001,1404),(1002,1405),(1003,1406),(1201,1406),(1597,1406),(1004,1407),(1005,1408),(1006,1409),(1007,1410),(1008,1411),(1009,1412),(1010,1413),(1011,1414),(1012,1415),(1014,1417),(1015,1418),(1016,1419),(1017,1420),(1017,1421),(1017,1422),(1018,1423),(1019,1424),(1194,1424),(1020,1425),(1021,1426),(1021,1427),(1021,1428),(1022,1429),(1023,1430),(1023,1431),(1024,1433),(1025,1434),(1025,1435),(1025,1436),(1026,1437),(1026,1438),(1027,1439),(1028,1440),(1166,1440),(1028,1441),(1029,1442),(1030,1443),(1031,1445),(1031,1446),(1031,1447),(1032,1448),(1033,1449),(1034,1450),(1035,1452),(1036,1453),(1037,1454),(1038,1456),(1038,1457),(1039,1458),(1039,1459),(1039,1460),(1040,1461),(1041,1462),(1041,1463),(1042,1464),(1044,1466),(1045,1467),(1046,1468),(1047,1469),(1048,1470),(1048,1471),(1049,1472),(1050,1473),(1379,1473),(1051,1474),(1052,1475),(1201,1475),(1053,1476),(1054,1477),(1055,1478),(1057,1480),(1059,1482),(1060,1483),(1061,1484),(1062,1485),(1063,1486),(1064,1487),(1065,1488),(1066,1489),(1067,1490),(1067,1491),(1067,1492),(1068,1493),(1070,1495),(1071,1496),(1072,1497),(1129,1497),(1073,1498),(1074,1499),(1075,1500),(1076,1501),(1077,1502),(1078,1503),(1523,1503),(1078,1504),(1079,1505),(1079,1506),(1080,1507),(1081,1508),(1081,1509),(1082,1510),(1083,1511),(1084,1512),(1085,1513),(1087,1515),(1088,1516),(1088,1517),(1089,1519),(1520,1519),(1090,1520),(1091,1521),(1365,1521),(1092,1522),(1093,1523),(1094,1524),(1094,1525),(1096,1527),(1097,1528),(1097,1529),(1097,1530),(1098,1531),(1099,1532),(1099,1533),(1099,1534),(1100,1535),(1100,1536),(1101,1537),(1102,1538),(1140,1538),(1183,1538),(1369,1538),(1103,1539),(1104,1540),(1105,1541),(1106,1542),(1107,1543),(1108,1544),(1109,1545),(1110,1546),(1111,1547),(1112,1548),(1113,1549),(1114,1550),(1115,1551),(1203,1551),(1116,1552),(1117,1553),(1117,1554),(1118,1555),(1119,1556),(1120,1557),(1395,1557),(1121,1558),(1121,1559),(1122,1560),(1124,1562),(1125,1563),(1126,1564),(1127,1565),(1128,1566),(1490,1566),(1130,1568),(1131,1569),(1132,1570),(1133,1571),(1134,1572),(1135,1573),(1136,1574),(1137,1575),(1138,1576),(1139,1577),(1250,1577),(1141,1579),(1142,1580),(1143,1581),(1144,1582),(1145,1583),(1146,1584),(1147,1585),(1148,1586),(1148,1587),(1148,1588),(1332,1588),(1149,1590),(1149,1591),(1150,1592),(1150,1593),(1150,1594),(1151,1595),(1151,1596),(1151,1597),(1152,1598),(1153,1599),(1153,1600),(1154,1602),(1155,1603),(1155,1604),(1155,1605),(1156,1606),(1156,1607),(1156,1608),(1157,1609),(1157,1611),(1158,1612),(1158,1613),(1159,1614),(1159,1615),(1159,1616),(1160,1617),(1160,1618),(1161,1619),(1162,1620),(1163,1621),(1164,1622),(1164,1623),(1164,1624),(1165,1625),(1166,1627),(1166,1628),(1168,1630),(1168,1631),(1168,1632),(1169,1633),(1169,1634),(1169,1635),(1170,1636),(1170,1638),(1171,1639),(1171,1640),(1171,1641),(1172,1642),(1173,1643),(1174,1644),(1175,1645),(1176,1646),(1176,1647),(1177,1648),(1178,1649),(1180,1651),(1181,1652),(1181,1653),(1181,1654),(1182,1655),(1184,1657),(1185,1658),(1186,1659),(1187,1660),(1188,1661),(1189,1662),(1190,1663),(1191,1664),(1192,1665),(1192,1666),(1193,1667),(1195,1669),(1195,1670),(1195,1671),(1196,1672),(1196,1673),(1196,1674),(1197,1675),(1197,1676),(1197,1677),(1198,1678),(1198,1679),(1198,1680),(1199,1681),(1199,1682),(1200,1683),(1202,1686),(1203,1687),(1203,1689),(1204,1690),(1204,1691),(1204,1692),(1205,1693),(1205,1694),(1206,1695),(1207,1696),(1208,1697),(1208,1698),(1209,1699),(1210,1700),(1211,1701),(1211,1702),(1211,1703),(1212,1704),(1213,1705),(1214,1706),(1215,1707),(1216,1708),(1217,1709),(1218,1710),(1219,1711),(1220,1712),(1221,1713),(1222,1714),(1223,1715),(1560,1715),(1224,1716),(1579,1716),(1225,1717),(1226,1718),(1227,1719),(1228,1720),(1229,1721),(1230,1722),(1231,1723),(1232,1724),(1233,1725),(1234,1726),(1235,1727),(1236,1728),(1236,1729),(1237,1730),(1237,1731),(1307,1731),(1237,1732),(1239,1734),(1240,1735),(1241,1736),(1241,1737),(1241,1738),(1242,1739),(1243,1740),(1244,1741),(1244,1742),(1245,1743),(1245,1744),(1246,1745),(1247,1746),(1384,1746),(1403,1746),(1248,1747),(1248,1748),(1249,1749),(1249,1750),(1251,1752),(1252,1753),(1252,1754),(1253,1755),(1256,1758),(1257,1759),(1258,1760),(1259,1761),(1260,1762),(1261,1763),(1262,1764),(1263,1765),(1264,1766),(1265,1767),(1266,1768),(1267,1769),(1268,1770),(1269,1771),(1270,1772),(1271,1773),(1273,1775),(1274,1776),(1275,1777),(1276,1778),(1277,1779),(1278,1780),(1279,1781),(1280,1782),(1281,1783),(1282,1784),(1283,1785),(1283,1786),(1283,1787),(1284,1788),(1285,1789),(1286,1790),(1287,1791),(1288,1792),(1289,1793),(1290,1794),(1291,1795),(1582,1795),(1292,1796),(1293,1797),(1294,1798),(1295,1799),(1296,1800),(1297,1801),(1298,1802),(1299,1803),(1300,1804),(1301,1805),(1303,1807),(1304,1808),(1305,1809),(1305,1810),(1306,1811),(1308,1813),(1309,1814),(1310,1815),(1311,1816),(1311,1817),(1311,1818),(1312,1819),(1312,1820),(1312,1821),(1313,1822),(1314,1823),(1314,1824),(1315,1825),(1315,1826),(1315,1827),(1317,1829),(1318,1830),(1319,1831),(1320,1832),(1320,1833),(1320,1834),(1321,1835),(1321,1836),(1322,1838),(1322,1839),(1323,1840),(1324,1841),(1324,1842),(1324,1843),(1325,1844),(1326,1845),(1327,1846),(1327,1847),(1327,1848),(1328,1849),(1328,1850),(1328,1851),(1329,1853),(1330,1854),(1330,1855),(1330,1856),(1331,1857),(1331,1858),(1331,1859),(1332,1861),(1332,1862),(1333,1864),(1334,1865),(1335,1866),(1336,1867),(1337,1868),(1495,1868),(1338,1869),(1339,1870),(1340,1871),(1341,1872),(1342,1873),(1343,1874),(1344,1875),(1345,1876),(1346,1877),(1347,1878),(1348,1879),(1349,1880),(1350,1881),(1350,1882),(1351,1883),(1352,1886),(1353,1887),(1354,1888),(1355,1889),(1356,1890),(1356,1891),(1357,1892),(1358,1893),(1359,1894),(1360,1895),(1361,1896),(1362,1897),(1364,1899),(1366,1901),(1367,1902),(1368,1903),(1370,1905),(1371,1906),(1372,1907),(1373,1908),(1373,1909),(1373,1910),(1374,1911),(1375,1912),(1376,1913),(1377,1914),(1378,1915),(1380,1917),(1381,1918),(1383,1920),(1384,1921),(1384,1922),(1385,1924),(1386,1925),(1388,1927),(1389,1928),(1390,1930),(1391,1931),(1392,1932),(1393,1933),(1394,1934),(1396,1936),(1397,1937),(1398,1938),(1399,1939),(1400,1940),(1401,1941),(1402,1942),(1402,1943),(1402,1944),(1404,1946),(1404,1947),(1405,1948),(1406,1949),(1407,1950),(1409,1952),(1411,1954),(1412,1955),(1413,1956),(1414,1957),(1415,1958),(1604,1958),(1416,1959),(1417,1960),(1418,1961),(1419,1962),(1420,1963),(1421,1964),(1422,1965),(1423,1966),(1424,1967),(1425,1968),(1427,1970),(1428,1971),(1428,1972),(1429,1973),(1430,1974),(1431,1975),(1432,1976),(1433,1977),(1434,1978),(1435,1979),(1436,1980),(1437,1981),(1437,1982),(1437,1983),(1438,1984),(1439,1985),(1440,1986),(1441,1987),(1441,1988),(1442,1989),(1444,1991),(1444,1992),(1445,1993),(1446,1994),(1447,1995),(1448,1996),(1449,1997),(1450,1998),(1451,1999),(1453,2001),(1518,2001),(1455,2004),(1456,2005),(1456,2006),(1456,2007),(1457,2008),(1458,2009),(1459,2010),(1460,2011),(1461,2012),(1462,2013),(1463,2014),(1463,2015),(1463,2016),(1464,2017),(1465,2018),(1466,2019),(1467,2020),(1468,2021),(1469,2022),(1470,2023),(1473,2026),(1473,2027),(1474,2028),(1475,2029),(1476,2030),(1477,2031),(1478,2032),(1478,2033),(1478,2034),(1479,2035),(1479,2036),(1479,2037),(1480,2038),(1482,2040),(1483,2041),(1483,2042),(1483,2043),(1484,2044),(1485,2045),(1485,2046),(1486,2047),(1487,2048),(1488,2049),(1489,2050),(1491,2052),(1492,2053),(1493,2054),(1493,2055),(1494,2056),(1494,2057),(1494,2058),(1496,2060),(1497,2061),(1498,2062),(1499,2063),(1500,2064),(1500,2065),(1501,2066),(1502,2067),(1503,2068),(1504,2069),(1505,2070),(1506,2071),(1507,2072),(1508,2073),(1510,2075),(1511,2076),(1512,2077),(1513,2078),(1514,2079),(1515,2080),(1516,2081),(1517,2082),(1519,2084),(1519,2085),(1521,2088),(1522,2089),(1523,2090),(1524,2092),(1525,2093),(1526,2094),(1527,2095),(1528,2096),(1529,2097),(1530,2098),(1531,2099),(1531,2100),(1532,2101),(1533,2102),(1534,2103),(1535,2104),(1536,2105),(1537,2106),(1538,2107),(1539,2108),(1540,2109),(1541,2110),(1542,2111),(1543,2112),(1545,2114),(1546,2115),(1547,2116),(1548,2117),(1549,2118),(1550,2119),(1551,2120),(1552,2121),(1553,2122),(1554,2123),(1555,2124),(1556,2125),(1557,2126),(1558,2127),(1559,2128),(1561,2130),(1562,2131),(1564,2133),(1565,2134),(1566,2135),(1567,2136),(1568,2137),(1569,2138),(1570,2139),(1571,2140),(1572,2141),(1573,2142),(1574,2143),(1575,2144),(1576,2145),(1577,2146),(1578,2147),(1580,2149),(1581,2150),(1583,2152),(1583,2153),(1584,2154),(1585,2155),(1586,2156),(1587,2157),(1588,2158),(1589,2159),(1590,2160),(1591,2161),(1592,2162),(1592,2163),(1593,2164),(1594,2165),(1595,2166),(1596,2167),(1598,2169),(1598,2170),(1599,2171),(1601,2173),(1602,2174),(1603,2175),(1605,2177),(1606,2178),(1608,2180),(1609,2181),(1610,2182),(1611,2183),(1612,2184),(1613,2185),(1614,2186),(1614,2187),(1615,2188);
/*!40000 ALTER TABLE `filmsdirectors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-25 21:27:05