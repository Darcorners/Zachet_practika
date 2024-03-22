-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Мар 22 2024 г., 16:04
-- Версия сервера: 5.7.39-log
-- Версия PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Phone_station`
--
CREATE DATABASE IF NOT EXISTS `Phone_station` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `Phone_station`;

-- --------------------------------------------------------

--
-- Структура таблицы `Cities`
--

CREATE TABLE `Cities` (
  `id` int(11) NOT NULL,
  `city` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fare` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `Cities`
--

INSERT INTO `Cities` (`id`, `city`, `fare`) VALUES
(1, 'Москва', 5),
(2, 'Санкт-петербург', 20);

-- --------------------------------------------------------

--
-- Структура таблицы `History`
--

CREATE TABLE `History` (
  `id` int(11) NOT NULL,
  `time_start` time NOT NULL,
  `city` int(11) NOT NULL,
  `time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `History`
--

INSERT INTO `History` (`id`, `time_start`, `city`, `time`) VALUES
(1, '18:15:00', 1, 5),
(2, '18:30:00', 2, 7),
(3, '18:45:00', 1, 15);

-- --------------------------------------------------------

--
-- Дублирующая структура для представления `phone_history`
-- (См. Ниже фактическое представление)
--
CREATE TABLE `phone_history` (
`id` int(11)
,`Город` varchar(50)
,`Тариф` int(11)
,`Время начала` time
,`Время разговора` int(11)
,`Сумма` bigint(21)
);

-- --------------------------------------------------------

--
-- Структура для представления `phone_history`
--
DROP TABLE IF EXISTS `phone_history`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `phone_history`  AS SELECT `history`.`id` AS `id`, `cities`.`city` AS `Город`, `cities`.`fare` AS `Тариф`, `history`.`time_start` AS `Время начала`, `history`.`time` AS `Время разговора`, (`history`.`time` * `cities`.`fare`) AS `Сумма` FROM (`history` join `cities` on((`cities`.`id` = `history`.`city`)))  ;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Cities`
--
ALTER TABLE `Cities`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `History`
--
ALTER TABLE `History`
  ADD PRIMARY KEY (`id`),
  ADD KEY `city` (`city`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Cities`
--
ALTER TABLE `Cities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `History`
--
ALTER TABLE `History`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `History`
--
ALTER TABLE `History`
  ADD CONSTRAINT `history_ibfk_1` FOREIGN KEY (`city`) REFERENCES `Cities` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
