-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Počítač: localhost:3306
-- Vytvořeno: Pon 14. lis 2022, 14:19
-- Verze serveru: 10.5.15-MariaDB-0+deb11u1
-- Verze PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáze: `nsql-ujep`
--

-- --------------------------------------------------------

--
-- Struktura tabulky `clovek`
--

CREATE TABLE `clovek` (
  `id` int(11) NOT NULL,
  `jmeno` varchar(45) DEFAULT NULL,
  `prijmeni` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `clovek`
--

INSERT INTO `clovek` (`id`, `jmeno`, `prijmeni`) VALUES
(1, 'Martin', 'Balej'),
(2, 'Martin', 'Novák'),
(3, 'Alena', 'Chvátalová'),
(4, 'Pavel', 'Doulík'),
(5, 'Jaroslav', 'Zukerstein'),
(6, 'Leoš', 'Nergl'),
(7, 'Jana', 'Kasaničová'),
(8, 'Pavel', 'Kuráň'),
(9, 'Diana', 'Holcová'),
(10, 'Jan', 'Popelka'),
(11, 'Josef', 'Trögl'),
(12, 'Miloslav', 'Kolenatý'),
(13, 'Jan', 'Vojtíšek'),
(14, 'Ondřej', 'Moc'),
(15, 'Dagmar', 'Kubišová'),
(16, 'Miroslav', 'Kopáček'),
(17, 'Lucie', 'Povolná'),
(18, 'Jan', 'Slavík'),
(19, 'Jitka', 'Laštovková'),
(20, 'Štefan', 'Balkó'),
(21, 'Jiří', 'Škoda'),
(22, 'Martin', 'Černý'),
(23, 'Ladislav', 'Zilcher'),
(24, 'Lenka', 'Hřebejková'),
(25, 'Zdeněk', 'Havel'),
(26, 'Stanislav', 'Novák'),
(27, 'Karel', 'Hrach'),
(28, 'Miloš', 'Němček'),
(29, 'Kateřina', 'Tichá'),
(30, 'Veronika', 'Davídková'),
(31, 'Pavel', 'Mrkus'),
(32, 'Zdena', 'Kolečková'),
(33, 'Michaela', 'Thelenová'),
(34, 'Marcel', 'Mochal'),
(35, 'Miroslav', 'Matoušek'),
(36, 'Zita', 'Šauerová'),
(37, 'Michaela', 'Hrubá'),
(38, 'Jiří', 'Koumar'),
(39, 'Stanislava', 'Musilová'),
(40, 'Pavel', 'Maškarinec'),
(41, 'Terezie', 'Tahalová'),
(42, 'Štefan', 'Michna'),
(43, 'Šárka', 'Fockeová'),
(44, 'Pavel', 'Houška'),
(45, 'Lucie', 'Skrčená'),
(46, 'Soňa', 'Olivová'),
(47, 'Stanislava', 'Zindulková Prošková'),
(48, 'Michal', 'Varady'),
(49, 'Regina', 'Herma'),
(50, 'Michaela', 'Liegertová'),
(51, 'Martin', 'Švec'),
(52, 'Petr', 'Lauterbach'),
(53, 'Hana Auer', 'Malinská'),
(54, 'Eva', 'Hejnová'),
(55, 'Pavel', 'Raška'),
(56, 'Jan', 'Čermák'),
(57, 'Jiří', 'Škvor'),
(58, 'Jan', 'Malý'),
(59, 'Kateřina', 'Jančaříková'),
(60, 'Jaromír', 'Havlica'),
(61, 'Jiří', 'Fišer'),
(62, 'Zbyšek', 'Posel'),
(63, 'Jaroslav', 'Tichý'),
(64, 'Petr', 'Kubera'),
(65, 'Eva', 'Heřmanová'),
(66, 'Jiří', 'Barilla'),
(67, 'Viktor', 'Maškov'),
(68, 'Sergii', 'Babichev'),
(69, 'Pavel', 'Beránek'),
(70, 'Jiří', 'Fišer'),
(71, 'Petr', 'Haberzettl'),
(72, 'Jan', 'Krejčí'),
(73, 'Pavel', 'Kuba'),
(74, 'Petr', 'Kubera'),
(75, 'Hossein', 'Moosaei'),
(76, 'Zbyšek', 'Posel'),
(77, 'Ricardo', 'Rodríguez Jorge'),
(78, 'Květuše', 'Sýkorová'),
(79, 'Jiří', 'Škvára'),
(80, 'Jiří', 'Škvor'),
(81, 'Kamil', 'Balín'),
(82, 'Jaroslav', 'Tichý'),
(83, 'Marek', 'Macek'),
(84, 'Martin', 'Láňa'),
(85, 'Roman', 'Saňa'),
(86, 'Štěpánka', 'Zimová');

-- --------------------------------------------------------

--
-- Struktura tabulky `clovek_has_pozice`
--

CREATE TABLE `clovek_has_pozice` (
  `clovek_id` int(11) NOT NULL,
  `pozice_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `clovek_has_pozice`
--

INSERT INTO `clovek_has_pozice` (`clovek_id`, `pozice_id`) VALUES
(1, 19),
(2, 16),
(3, 16),
(4, 16),
(5, 16),
(6, 17),
(7, 18),
(8, 1),
(9, 2),
(10, 2),
(11, 2),
(12, 2),
(13, 3),
(14, 1),
(15, 3),
(16, 2),
(17, 2),
(18, 2),
(19, 2),
(20, 2),
(21, 1),
(22, 2),
(23, 2),
(24, 3),
(25, 1),
(26, 2),
(27, 2),
(28, 2),
(29, 2),
(30, 3),
(31, 1),
(32, 2),
(33, 2),
(34, 2),
(35, 3),
(36, 10),
(37, 1),
(38, 2),
(39, 2),
(40, 2),
(41, 3),
(42, 1),
(43, 4),
(44, 3),
(45, 5),
(46, 5),
(47, 5),
(48, 1),
(49, 2),
(50, 2),
(51, 2),
(52, 3),
(53, 6),
(54, 6),
(55, 6),
(56, 6),
(57, 6),
(58, 7),
(59, 7),
(60, 11),
(61, 8),
(62, 8),
(63, 7),
(64, 9),
(65, 10),
(66, 11),
(67, 11),
(68, 12),
(69, 12),
(70, 12),
(71, 12),
(72, 12),
(73, 12),
(74, 12),
(75, 12),
(76, 12),
(77, 12),
(78, 12),
(79, 12),
(80, 12),
(81, 13),
(82, 14),
(83, 14),
(84, 15),
(85, 15),
(86, 15);

-- --------------------------------------------------------

--
-- Struktura tabulky `clovek_has_titul`
--

CREATE TABLE `clovek_has_titul` (
  `clovek_id` int(11) NOT NULL,
  `titul_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `clovek_has_titul`
--

INSERT INTO `clovek_has_titul` (`clovek_id`, `titul_id`) VALUES
(1, 3),
(1, 4),
(1, 12),
(2, 2),
(2, 3),
(2, 4),
(3, 3),
(3, 12),
(4, 3),
(4, 6),
(4, 16),
(5, 3),
(5, 9),
(6, 2),
(7, 1),
(8, 2),
(8, 4),
(8, 5),
(9, 1),
(9, 3),
(10, 2),
(10, 3),
(11, 2),
(11, 3),
(11, 4),
(12, 1),
(13, 1),
(14, 1),
(14, 3),
(15, 2),
(16, 2),
(16, 3),
(17, 2),
(17, 3),
(18, 2),
(18, 3),
(18, 4),
(19, 1),
(19, 3),
(20, 3),
(20, 9),
(21, 3),
(21, 6),
(21, 9),
(21, 14),
(22, 2),
(22, 9),
(22, 15),
(23, 3),
(23, 4),
(23, 9),
(24, 2),
(25, 4),
(25, 9),
(25, 11),
(26, 6),
(26, 11),
(26, 12),
(27, 3),
(27, 12),
(28, 2),
(29, 3),
(29, 9),
(30, 2),
(31, 1),
(31, 4),
(31, 7),
(32, 1),
(32, 3),
(32, 6),
(33, 1),
(33, 4),
(34, 8),
(35, 1),
(37, 3),
(37, 6),
(37, 9),
(38, 3),
(38, 9),
(39, 1),
(39, 3),
(40, 1),
(40, 3),
(40, 4),
(41, 2),
(42, 2),
(42, 3),
(42, 6),
(43, 10),
(44, 2),
(45, 10),
(48, 3),
(48, 4),
(48, 12),
(49, 3),
(49, 12),
(50, 1),
(50, 3),
(51, 3),
(51, 12),
(52, 2),
(53, 1),
(53, 3),
(54, 3),
(54, 12),
(55, 1),
(55, 3),
(55, 4),
(56, 2),
(56, 4),
(56, 11),
(57, 3),
(57, 12),
(58, 1),
(58, 3),
(59, 3),
(59, 4),
(59, 9),
(60, 2),
(60, 3),
(60, 4),
(61, 1),
(61, 3),
(62, 3),
(62, 12),
(63, 10),
(64, 3),
(64, 12),
(65, 10),
(66, 2),
(66, 4),
(66, 17),
(67, 4),
(67, 12),
(67, 17),
(68, 6),
(68, 18),
(69, 1),
(69, 2),
(70, 1),
(70, 3),
(71, 2),
(72, 3),
(72, 12),
(73, 2),
(73, 3),
(74, 3),
(74, 12),
(75, 5),
(76, 3),
(76, 12),
(77, 3),
(78, 1),
(79, 3),
(79, 12),
(80, 3),
(80, 12),
(81, 1),
(81, 19),
(82, 10),
(84, 1),
(85, 1),
(86, 2);

-- --------------------------------------------------------

--
-- Struktura tabulky `fakulta`
--

CREATE TABLE `fakulta` (
  `id` int(11) NOT NULL,
  `nazev` varchar(60) DEFAULT NULL,
  `univerzita_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `fakulta`
--

INSERT INTO `fakulta` (`id`, `nazev`, `univerzita_id`) VALUES
(1, 'Rektorát', 1),
(2, 'Fakulta životního prostředí', 1),
(3, 'Fakulta sociálně ekonomická', 1),
(4, 'Pedagogická fakulta', 1),
(5, 'Fakulta zdravotních studií', 1),
(6, 'Filozofická fakulta', 1),
(7, 'Fakulta umění a designu', 1),
(8, 'Fakulta strojního inženýrství', 1),
(9, 'Přírodovědecká fakulta', 1);

-- --------------------------------------------------------

--
-- Struktura tabulky `fakulta_has_clovek`
--

CREATE TABLE `fakulta_has_clovek` (
  `fakulta_id` int(11) NOT NULL,
  `clovek_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `fakulta_has_clovek`
--

INSERT INTO `fakulta_has_clovek` (`fakulta_id`, `clovek_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(2, 8),
(2, 9),
(2, 10),
(2, 11),
(2, 12),
(2, 13),
(3, 14),
(3, 15),
(3, 16),
(3, 17),
(3, 18),
(3, 19),
(4, 20),
(4, 21),
(4, 22),
(4, 23),
(4, 24),
(5, 25),
(5, 26),
(5, 27),
(5, 28),
(5, 29),
(5, 30),
(6, 37),
(6, 38),
(6, 39),
(6, 40),
(6, 41),
(7, 31),
(7, 32),
(7, 33),
(7, 34),
(7, 35),
(7, 36),
(8, 42),
(8, 43),
(8, 44),
(8, 45),
(8, 46),
(8, 47),
(9, 48),
(9, 49),
(9, 50),
(9, 51),
(9, 52),
(9, 53),
(9, 54),
(9, 55),
(9, 56),
(9, 57),
(9, 58),
(9, 59),
(9, 60),
(9, 61),
(9, 62),
(9, 63),
(9, 64),
(9, 65),
(9, 66),
(9, 67),
(9, 68),
(9, 69),
(9, 70),
(9, 71),
(9, 72),
(9, 73),
(9, 74),
(9, 75),
(9, 76),
(9, 77),
(9, 78),
(9, 79),
(9, 80),
(9, 81),
(9, 82),
(9, 83),
(9, 84),
(9, 85),
(9, 86);

-- --------------------------------------------------------

--
-- Struktura tabulky `pozice`
--

CREATE TABLE `pozice` (
  `id` int(11) NOT NULL,
  `pozice` varchar(45) DEFAULT 'učitel'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `pozice`
--

INSERT INTO `pozice` (`id`, `pozice`) VALUES
(1, 'děkan'),
(2, 'proděkan'),
(3, 'tajemník'),
(4, 'sekretářka děkana'),
(5, 'referent'),
(6, 'vedoucí katedry'),
(7, 'vedoucí centra'),
(8, 'zástupce vedoucího katedry'),
(9, 'katederní koordinátor programu Erasmus'),
(10, 'sekretářka'),
(11, 'docent'),
(12, 'odborný asistent'),
(13, 'lektor'),
(14, 'technická podpora'),
(15, 'externí pracovník'),
(16, 'prorektor'),
(17, 'kvestor'),
(18, 'kancléřka'),
(19, 'rektor');

-- --------------------------------------------------------

--
-- Struktura tabulky `titul`
--

CREATE TABLE `titul` (
  `id` int(11) NOT NULL,
  `titul` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `titul`
--

INSERT INTO `titul` (`id`, `titul`) VALUES
(1, 'Mgr.'),
(2, 'Ing.'),
(3, 'Ph.D.'),
(4, 'doc.'),
(5, 'Dr.'),
(6, 'prof.'),
(7, 'A.'),
(8, 'MgA.'),
(9, 'PhDr.'),
(10, 'Bc.'),
(11, 'CSc.'),
(12, 'RNDr.'),
(13, 'MUDr.'),
(14, 'MBA'),
(15, 'Msc.'),
(16, 'PaeDr.'),
(17, 'DrSc.'),
(18, 'DSc.'),
(19, 'et Bc.');

-- --------------------------------------------------------

--
-- Struktura tabulky `univerzita`
--

CREATE TABLE `univerzita` (
  `id` int(11) NOT NULL,
  `nazev` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `univerzita`
--

INSERT INTO `univerzita` (`id`, `nazev`) VALUES
(1, 'Univerzita Jana Evangelisty Purkyně');

--
-- Klíče pro exportované tabulky
--

--
-- Klíče pro tabulku `clovek`
--
ALTER TABLE `clovek`
  ADD PRIMARY KEY (`id`);

--
-- Klíče pro tabulku `clovek_has_pozice`
--
ALTER TABLE `clovek_has_pozice`
  ADD PRIMARY KEY (`clovek_id`,`pozice_id`),
  ADD KEY `fk_clovek_has_pozice_pozice1_idx` (`pozice_id`),
  ADD KEY `fk_clovek_has_pozice_clovek_idx` (`clovek_id`);

--
-- Klíče pro tabulku `clovek_has_titul`
--
ALTER TABLE `clovek_has_titul`
  ADD PRIMARY KEY (`clovek_id`,`titul_id`),
  ADD KEY `fk_clovek_has_titul_titul1_idx` (`titul_id`),
  ADD KEY `fk_clovek_has_titul_clovek1_idx` (`clovek_id`);

--
-- Klíče pro tabulku `fakulta`
--
ALTER TABLE `fakulta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_fakulta_univerzita1_idx` (`univerzita_id`);

--
-- Klíče pro tabulku `fakulta_has_clovek`
--
ALTER TABLE `fakulta_has_clovek`
  ADD PRIMARY KEY (`fakulta_id`,`clovek_id`),
  ADD KEY `fk_fakulta_has_clovek_clovek1_idx` (`clovek_id`),
  ADD KEY `fk_fakulta_has_clovek_fakulta1_idx` (`fakulta_id`);

--
-- Klíče pro tabulku `pozice`
--
ALTER TABLE `pozice`
  ADD PRIMARY KEY (`id`);

--
-- Klíče pro tabulku `titul`
--
ALTER TABLE `titul`
  ADD PRIMARY KEY (`id`);

--
-- Klíče pro tabulku `univerzita`
--
ALTER TABLE `univerzita`
  ADD PRIMARY KEY (`id`);

--
-- Omezení pro exportované tabulky
--

--
-- Omezení pro tabulku `clovek_has_pozice`
--
ALTER TABLE `clovek_has_pozice`
  ADD CONSTRAINT `fk_clovek_has_pozice_clovek` FOREIGN KEY (`clovek_id`) REFERENCES `clovek` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_clovek_has_pozice_pozice1` FOREIGN KEY (`pozice_id`) REFERENCES `pozice` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `clovek_has_titul`
--
ALTER TABLE `clovek_has_titul`
  ADD CONSTRAINT `fk_clovek_has_titul_clovek1` FOREIGN KEY (`clovek_id`) REFERENCES `clovek` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_clovek_has_titul_titul1` FOREIGN KEY (`titul_id`) REFERENCES `titul` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `fakulta`
--
ALTER TABLE `fakulta`
  ADD CONSTRAINT `fk_fakulta_univerzita1` FOREIGN KEY (`univerzita_id`) REFERENCES `univerzita` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `fakulta_has_clovek`
--
ALTER TABLE `fakulta_has_clovek`
  ADD CONSTRAINT `fk_fakulta_has_clovek_clovek1` FOREIGN KEY (`clovek_id`) REFERENCES `clovek` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_fakulta_has_clovek_fakulta1` FOREIGN KEY (`fakulta_id`) REFERENCES `fakulta` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;