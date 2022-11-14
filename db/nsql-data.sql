-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Počítač: localhost:3306
-- Vytvořeno: Pon 14. lis 2022, 14:20
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
-- Databáze: `nsql`
--

-- --------------------------------------------------------

--
-- Struktura tabulky `login`
--

CREATE TABLE `login` (
  `username` varchar(60) NOT NULL,
  `password` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Vypisuji data pro tabulku `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('ahoj', 'ahoj'),
('asdsd', 'asdasd'),
('boubik', '123'),
('bubla', 'koupilpudla'),
('dfgdfg', 'dfgd'),
('pisek', '123'),
('sdfsdf', 'sdfsd');

--
-- Klíče pro exportované tabulky
--

--
-- Klíče pro tabulku `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;