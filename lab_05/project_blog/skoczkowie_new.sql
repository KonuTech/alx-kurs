--CREATE SCHEMA `skoczkowie` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci;

USE SCHEMA `skoczkowie`;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Baza danych: `skoczkowie5`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `kibice`
--

CREATE TABLE `kibice` (
  `id` int NOT NULL,
  `imie_k` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `nazwisko_k` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `kraj` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `wzrost` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `kibice`
--

INSERT INTO `kibice` (`id`, `imie_k`, `nazwisko_k`, `kraj`, `wzrost`) VALUES
(1, 'Jan', 'Kowalski', 'POL', NULL),
(2, 'John', 'Smith', NULL, 172),
(3, 'Anna', 'Zawadzka', NULL, NULL);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `skocznie`
--

CREATE TABLE `skocznie` (
  `id` int NOT NULL,
  `id_skoczni` int DEFAULT NULL,
  `miasto` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `kraj_s` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `nazwa` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `k` int DEFAULT NULL,
  `sedz` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `skocznie`
--

INSERT INTO `skocznie` (`id`, `id_skoczni`, `miasto`, `kraj_s`, `nazwa`, `k`, `sedz`) VALUES
(1, 1, 'Zakopane', 'POL', 'Wielka Krokiew', 120, 134),
(2, 2, 'Garmisch-Partenkirchen', 'GER', 'Wielka Skocznia Olimpijska', 115, 125),
(3, 4, 'Oberstdorf', 'GER', 'Skocznia Heiniego Klopfera', 185, 211),
(4, 3, 'Oberstdorf', 'GER', 'Grosse Schattenberg', 120, 134),
(5, 5, 'Willingen', 'GER', 'Grosse Muhlenkopfschanze', 130, 145),
(6, 6, 'Kuopio', 'FIN', 'Puijo', 120, 131),
(7, 7, 'Lahti', 'FIN', 'Salpausselka', 116, 128),
(8, 8, 'Trondheim', 'NOR', 'Granasen', 120, 132);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `trenerzy`
--

CREATE TABLE `trenerzy` (
  `id` int NOT NULL,
  `kraj` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `imie_t` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `nazwisko_t` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `data_ur_t` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `trenerzy`
--

INSERT INTO `trenerzy` (`id`, `kraj`, `imie_t`, `nazwisko_t`, `data_ur_t`) VALUES
(1, 'AUT', 'Alexander', 'Pointner', NULL),
(2, 'FIN', 'Tommi', 'Nikunen', NULL),
(3, 'NOR', 'Mika', 'Kojonkoski', '1963-04-19'),
(4, 'POL', 'Heinz', 'Kuttin', '1971-01-05'),
(5, 'GER', 'Wolfang', 'Steiert', '1963-04-19'),
(6, 'JPN', 'Hirokazu', 'Yagi', NULL);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zawodnicy`
--

CREATE TABLE `zawodnicy` (
  `id` int NOT NULL,
  `imie` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `nazwisko` text CHARACTER SET utf8 COLLATE utf8_polish_ci,
  `kraj` char(3) CHARACTER SET utf8 COLLATE utf8_polish_ci DEFAULT NULL,
  `data_ur` date DEFAULT NULL,
  `wzrost` int DEFAULT NULL,
  `waga` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zawodnicy`
--

INSERT INTO `zawodnicy` (`id`, `imie`, `nazwisko`, `kraj`, `data_ur`, `wzrost`, `waga`) VALUES
(1, 'Adam', 'MAŁYSZ', 'POL', '1977-12-03', 169, 60),
(2, 'Marcin', 'BACHLEDA', 'POL', '1982-09-04', 166, 56),
(3, 'Robert', 'MATEJA', 'POL', '1974-10-05', 180, 63),
(4, 'Alexander', 'HERR', 'GER', '1978-10-04', 173, 65),
(5, 'Stephan', 'HOCKE', 'GER', '1983-10-20', 178, 59),
(6, 'Martin', 'SCHMITT', 'GER', '1978-01-29', 181, 64),
(7, 'Michael', 'UHRMANN', 'GER', '1978-09-09', 184, 64),
(8, 'Georg', 'SPAETH', 'GER', '1981-02-24', 187, 68),
(9, 'Matti', 'HAUTAMAEKI', 'FIN', '1981-07-14', 174, 57),
(10, 'Tami', 'KIURU', 'FIN', '1976-09-13', 183, 59),
(11, 'Janne', 'AHONEN', 'FIN', '1977-05-11', 184, 67),
(12, 'Martin', 'HOELLWARTH', 'AUT', '1974-04-13', 182, 67),
(13, 'Thomas', 'MORGENSTERN', 'AUT', '1986-10-30', 174, 57),
(14, 'Alan', 'ALBORN', 'USA', '1980-12-13', 177, 57),
(15, 'Tommy', 'INGEBRIGTSEN', 'NOR', '1977-08-08', 179, 56),
(16, 'Bjoern-Einar', 'ROMOEREN', 'NOR', '1981-04-01', 182, 63),
(17, 'Roar', 'LJOEKELSOEY', 'NOR', '1976-05-31', 175, 62);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zawody`
--

CREATE TABLE `zawody` (
  `id` int NOT NULL,
  `id_skoczni` int DEFAULT NULL,
  `data` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zawody`
--

INSERT INTO `zawody` (`id`, `id_skoczni`, `data`) VALUES
(1, 1, '2017-01-23'),
(2, 7, '2016-11-15'),
(3, 3, '2016-12-26');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `kibice`
--
ALTER TABLE `kibice`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `skocznie`
--
ALTER TABLE `skocznie`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `trenerzy`
--
ALTER TABLE `trenerzy`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `zawodnicy`
--
ALTER TABLE `zawodnicy`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `zawody`
--
ALTER TABLE `zawody`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `kibice`
--
ALTER TABLE `kibice`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT dla tabeli `skocznie`
--
ALTER TABLE `skocznie`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT dla tabeli `trenerzy`
--
ALTER TABLE `trenerzy`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT dla tabeli `zawodnicy`
--
ALTER TABLE `zawodnicy`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT dla tabeli `zawody`
--
ALTER TABLE `zawody`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;
