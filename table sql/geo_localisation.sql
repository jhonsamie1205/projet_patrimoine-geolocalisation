-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 23 déc. 2025 à 11:55
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `geo_localisation`
--

-- --------------------------------------------------------

--
-- Structure de la table `patrimoines`
--

CREATE TABLE `patrimoines` (
  `id` int(11) NOT NULL,
  `Nom_Parimoine` varchar(200) NOT NULL,
  `Description_Patrimoine` text DEFAULT NULL,
  `Latitudes` double DEFAULT NULL,
  `Longitudes` double DEFAULT NULL,
  `Date_Creation` date NOT NULL,
  `id_Utilisateurs` int(11) DEFAULT NULL,
  `id_Villes` int(11) DEFAULT NULL,
  `id_Types_Patrimoines` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `types_patrimoines`
--

CREATE TABLE `types_patrimoines` (
  `id` int(11) NOT NULL,
  `Libelle` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

CREATE TABLE `utilisateurs` (
  `id` int(11) NOT NULL,
  `Nom` varchar(200) NOT NULL,
  `Prenom` varchar(200) NOT NULL,
  `Username` varchar(200) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `MotDePasse` varchar(30) NOT NULL,
  `Nbr_Tentative` int(11) DEFAULT NULL CHECK (`Nbr_Tentative` <= 3)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `villes`
--

CREATE TABLE `villes` (
  `id` int(11) NOT NULL,
  `Nom` varchar(200) NOT NULL,
  `Description` text DEFAULT NULL,
  `Latitude` double DEFAULT NULL,
  `Longitude` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `patrimoines`
--
ALTER TABLE `patrimoines`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_ id_Types_Patrimoines` (`id_Types_Patrimoines`),
  ADD KEY `fk_ id_Utilisateurs` (`id_Utilisateurs`),
  ADD KEY `fk_ id_Villes` (`id_Villes`);

--
-- Index pour la table `types_patrimoines`
--
ALTER TABLE `types_patrimoines`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Username` (`Username`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Index pour la table `villes`
--
ALTER TABLE `villes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `patrimoines`
--
ALTER TABLE `patrimoines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `types_patrimoines`
--
ALTER TABLE `types_patrimoines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `villes`
--
ALTER TABLE `villes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `patrimoines`
--
ALTER TABLE `patrimoines`
  ADD CONSTRAINT `fk_ id_Types_Patrimoines` FOREIGN KEY (`id_Types_Patrimoines`) REFERENCES `types_patrimoines` (`id`),
  ADD CONSTRAINT `fk_ id_Utilisateurs` FOREIGN KEY (`id_Utilisateurs`) REFERENCES `utilisateurs` (`id`),
  ADD CONSTRAINT `fk_ id_Villes` FOREIGN KEY (`id_Villes`) REFERENCES `villes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
