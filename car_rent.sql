-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 13 Apr 2023 pada 16.10
-- Versi server: 10.4.25-MariaDB
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_rent`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `car`
--

CREATE TABLE `car` (
  `car_id` int(10) NOT NULL,
  `car_name` varchar(100) NOT NULL,
  `plat` varchar(9) DEFAULT NULL,
  `passanger` int(5) DEFAULT NULL,
  `year` int(4) NOT NULL,
  `fuel` varchar(10) NOT NULL,
  `transmision` varchar(10) DEFAULT NULL,
  `price` int(21) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `car`
--

INSERT INTO `car` (`car_id`, `car_name`, `plat`, `passanger`, `year`, `fuel`, `transmision`, `price`) VALUES
(1, 'Mazda 3 Hatchback', 'AD2889WYW', 5, 2021, 'gasoline', 'automatic', 500000),
(2, 'Honda Civic Type R', 'DK2889AZJ', 5, 2019, 'gasoline', 'manual', 1199000),
(3, 'Toyota Fortuner VRZ', 'BM2331SAC', 8, 2019, 'diesel', 'automatic', 500000),
(4, 'Hyundai Ioniq 5', 'KH2331AAE', 5, 2022, 'electric', 'automatic', 900000),
(5, 'Volvo XC90', 'DD1213ASD', 8, 2022, 'hybrid', 'automatic', 1000000),
(6, 'Honda Brio', 'D3122AZZ', 5, 2018, 'gasoline', 'manual', 250000),
(7, 'Mitsubishi Pajero Sport', 'B2331UAD', 8, 2019, 'diesel', 'manual', 500000),
(8, 'Toyota CHR', 'B3322TVZ', 5, 2021, 'hybrid', 'automatic', 400000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `customer`
--

CREATE TABLE `customer` (
  `cust_id` int(10) NOT NULL,
  `cust_name` varchar(50) NOT NULL,
  `phone` varchar(18) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `customer`
--

INSERT INTO `customer` (`cust_id`, `cust_name`, `phone`, `address`) VALUES
(1, 'Wakhid Yusuf', '081324576809', 'Karangdowo'),
(2, 'Pandu Dewantara', '087762335331', 'Klaten'),
(3, 'Freya Jayawardhana', '085277385647', 'Bantul'),
(4, 'Johnson Perkasa', '082273859366', 'Palangkaraya'),
(5, 'Sri Widodo', '089944381222', 'Pekanbaru'),
(6, 'Aditria Almukmin', '082155483999', 'Jatinegara');

-- --------------------------------------------------------

--
-- Struktur dari tabel `rent`
--

CREATE TABLE `rent` (
  `rent_id` int(15) NOT NULL,
  `cust_id` int(10) NOT NULL,
  `car_id` int(10) NOT NULL,
  `day` int(3) NOT NULL,
  `start_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `rent`
--

INSERT INTO `rent` (`rent_id`, `cust_id`, `car_id`, `day`, `start_date`) VALUES
(1, 1, 3, 3, '2022-03-21'),
(2, 4, 2, 1, '2022-04-24'),
(3, 3, 7, 4, '2023-04-10'),
(4, 2, 1, 1, '2022-05-11'),
(5, 5, 6, 2, '2022-06-07'),
(6, 2, 4, 2, '2022-07-01'),
(7, 5, 8, 23, '2022-08-23'),
(8, 3, 5, 3, '2022-09-30'),
(9, 1, 2, 3, '2022-10-31'),
(10, 3, 1, 3, '2022-11-02'),
(11, 5, 6, 3, '2022-12-09'),
(12, 4, 4, 43, '2023-01-10'),
(13, 3, 7, 3, '2022-02-28'),
(14, 2, 4, 3, '2022-03-24');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`car_id`);

--
-- Indeks untuk tabel `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cust_id`);

--
-- Indeks untuk tabel `rent`
--
ALTER TABLE `rent`
  ADD PRIMARY KEY (`rent_id`),
  ADD KEY `fk_custrent` (`cust_id`),
  ADD KEY `fk_carrent` (`car_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `car`
--
ALTER TABLE `car`
  MODIFY `car_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `customer`
--
ALTER TABLE `customer`
  MODIFY `cust_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `rent`
--
ALTER TABLE `rent`
  MODIFY `rent_id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `rent`
--
ALTER TABLE `rent`
  ADD CONSTRAINT `fk_carrent` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`),
  ADD CONSTRAINT `fk_custrent` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
