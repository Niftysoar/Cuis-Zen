-- Table: Famille
CREATE TABLE `Famille` (
    `ID` INTEGER,
    `Nom` TEXT,
    `Image` TEXT,
    PRIMARY KEY(`ID` AUTOINCREMENT)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table: Recettes
CREATE TABLE `Recettes` (
    `ID` INTEGER,
    `Nom` TEXT,
    `Image` TEXT,
    `Nombre de personnes` INTEGER,
    `Preparation` INTEGER,
    `Cuisson` INTEGER,
    `Difficulte` TEXT,
    `ID_Famille` INTEGER,
    FOREIGN KEY(`ID_Famille`) REFERENCES `Famille`,
    PRIMARY KEY(`ID` AUTOINCREMENT)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table: EtapeDeRecette
CREATE TABLE `EtapeDeRecette` (
    `IP` INTEGER,
    `ID_recettes` INTEGER,
    `Numero` INTEGER,
    `Descriptif` TEXT,
    PRIMARY KEY(`IP` AUTOINCREMENT),
    FOREIGN KEY(`ID_recettes`) REFERENCES `Recettes`
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table: Ingredients
CREATE TABLE `Ingredients` (
    `ID` INTEGER,
    `Nom` TEXT,
    PRIMARY KEY(`ID` AUTOINCREMENT)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table: IngredientsDeRecette
CREATE TABLE `IngredientsDeRecette` (
    `ID` INTEGER,
    `ID_Recettes` INTEGER,
    `ID_ingrdients` INTEGER,
    `Quantite` REAL,
    `Unite` TEXT,
    PRIMARY KEY(`ID` AUTOINCREMENT),
    FOREIGN KEY(`ID_ingrdients`) REFERENCES `Ingredients`,
    FOREIGN KEY(`ID_Recettes`) REFERENCES `Recettes`
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;