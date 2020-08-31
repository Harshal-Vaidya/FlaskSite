-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 31, 2020 at 03:17 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thoughtstrivial`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `message` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `message`, `date`, `email`) VALUES
(1, 'first value', '123445678', 'first message', '2020-08-20 13:56:57', 'first@gmail.com'),
(2, 'Harshal Vaidya', '08223046953', 'hahahahha', '2020-08-20 14:17:52', 'harshalvaidya18@gmail.com'),
(3, 'Harshal Vaidya', '08223046953', 'babababababbab', '2020-08-24 14:37:38', 'harshalvaidya18@gmail.com'),
(4, 'Harshal Vaidya', '08223046953', 'babababababbab', '2020-08-24 14:50:21', 'harshalvaidya18@gmail.com'),
(5, 'Harshal Vaidya', '08223046953', 'babababbababbaba', '2020-08-24 14:50:50', 'harshalvaidya18@gmail.com'),
(6, 'Harshal Vaidya', '08223046953', 'babubabubabubabubabubabu', '2020-08-24 14:52:01', 'harshalvaidya18@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `subtitle` varchar(50) NOT NULL,
  `content` varchar(300) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `slug` varchar(50) NOT NULL,
  `img_file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `subtitle`, `content`, `date`, `slug`, `img_file`) VALUES
(1, 'Agriculture', 'My first post on agriculture', 'Agriculture is the science and art of cultivating plants and livestock.[1] Agriculture was the key development in the rise of sedentary human civilization, whereby farming of domesticated species created food surpluses that enabled people to live in cities. The history of agriculture began thousands', '2020-08-24 16:49:28', 'first-post', 'post-bg.jpg'),
(2, 'Horticulture', 'blog number dwitiya', 'Horticulture has a very long history.[8] The study and science of horticulture dates all the way back to the times of Cyrus the Great of ancient Persia, and has been going on ever since, with present-day horticulturists such as Freeman S. Howlett and Luther Burbank. The practice of horticulture can ', '2020-08-24 21:19:59', 'secong-blog', ''),
(3, 'Gardenting', 'ghar ki kheti', 'Gardening is the practice of growing and cultivating plants as part of horticulture. In gardens, ornamental plants are often grown for their flowers, foliage, or overall appearance; useful plants, such as root vegetables, leaf vegetables, fruits, and herbs, are grown for consumption, for use as dyes', '2020-08-24 21:21:32', 'third-blog', ''),
(4, 'Chaha chaudhary', 'sabo ko god lene walw uncle', 'bjkopp', '2020-08-24 21:23:26', 'fourth-blog', ''),
(5, 'Cube ', 'rubiks cube', 'dhakitikir dhakitikir dhakkitikitr lkdzjfkdjklmkldjfzddfiosdjojgiodjlgj', '2020-08-24 21:24:25', 'fifth-blog', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
