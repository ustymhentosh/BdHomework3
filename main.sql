-- -----------------------------------------------------
-- Schema Photography
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Photography` DEFAULT CHARACTER SET utf8 ;
USE `Photography` ;

-- -----------------------------------------------------
-- Table `Photography`.`PhotographyAgencies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`PhotographyAgencies` (
  `agencyID` INT NOT NULL,
  `agencyName` VARCHAR(45) NOT NULL,
  `agencySpecializetion` VARCHAR(45) NULL,
  PRIMARY KEY (`agencyID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`Photographers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`Photographers` (
  `photographerID` INT NOT NULL,
  `agencyID` INT NULL,
  `photographerName` MEDIUMTEXT NOT NULL,
  `photographerType` VARCHAR(45) NULL,
  `experiance` INT ZEROFILL NULL,
  `style` SET("sharp", "elegant", "modern") NULL,
  PRIMARY KEY (`photographerID`),
  INDEX `fk_Photographers_PhotographyAgencies_idx` (`agencyID` ASC) VISIBLE,
  CONSTRAINT `fk_Photographers_PhotographyAgencies`
    FOREIGN KEY (`agencyID`)
    REFERENCES `Photography`.`PhotographyAgencies` (`agencyID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`Storages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`Storages` (
  `storageID` VARCHAR(45) NOT NULL,
  `ownerID` INT NULL,
  `storageType` VARCHAR(45) NOT NULL,
  `storageSize` INT NOT NULL,
  `properties` MEDIUMTEXT GENERATED ALWAYS AS (CONCAT(storageType, ' | ', storageSize)) VIRTUAL,
  `status` TINYINT NOT NULL,
  PRIMARY KEY (`storageID`),
  INDEX `fk_Storage_Photographers1_idx` (`ownerID` ASC) VISIBLE,
  CONSTRAINT `fk_Storage_Photographers1`
    FOREIGN KEY (`ownerID`)
    REFERENCES `Photography`.`PhotographyAgencies` (`agencyID`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`Instruments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`Instruments` (
  `serialNum` INT NOT NULL,
  `ownerID` INT NULL,
  `cameraType` VARCHAR(45) NOT NULL,
  `modelName` VARCHAR(45) NULL,
  `aperture` FLOAT NULL,
  `exposure` INT NULL,
  `settings` VARCHAR(45) GENERATED ALWAYS AS (CONCAT(aperture, ' | ', exposure)) VIRTUAL,
  `status` TINYINT NOT NULL,
  PRIMARY KEY (`serialNum`),
  INDEX `fk_Instrument_Photographers1_idx` (`ownerID` ASC) VISIBLE,
  CONSTRAINT `fk_Instrument_Photographers1`
    FOREIGN KEY (`ownerID`)
    REFERENCES `Photography`.`PhotographyAgencies` (`agencyID`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`Locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`Locations` (
  `location` VARCHAR(64) NOT NULL,
  `country` VARCHAR(45) NULL,
  `mtrAboveSeaLevel` INT NULL,
  `temperature_celsius` INT NULL,
  `weatherCondition` VARCHAR(45) NULL,
  PRIMARY KEY (`location`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`Orders` (
  `orderID` INT NOT NULL,
  `agencyID` INT NOT NULL,
  `totalPrice` VARCHAR(45) NOT NULL,
  `clientID` VARCHAR(45) NOT NULL,
  `description` VARCHAR(45) NULL,
  `status` VARCHAR(45) NOT NULL,
  `assignedPhotographer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`orderID`, `agencyID`),
  INDEX `agencyID_idx` (`agencyID` ASC) VISIBLE,
  CONSTRAINT `agencyID`
    FOREIGN KEY (`agencyID`)
    REFERENCES `Photography`.`PhotographyAgencies` (`agencyID`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`Images`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`Images` (
  `imgID` VARCHAR(45) NOT NULL,
  `geodata` VARCHAR(64) NOT NULL,
  `instrumentSerialNum` INT NULL,
  `storageID` VARCHAR(45) NOT NULL,
  `orderID` INT NULL,
  `resolution` VARCHAR(45) NULL,
  `time` TIME NULL,
  `date` DATE NULL,
  `title` VARCHAR(45) NULL,
  PRIMARY KEY (`imgID`, `geodata`, `storageID`),
  INDEX `fk_Image_Storage1_idx` (`storageID` ASC) VISIBLE,
  INDEX `fk_Image_Instrument1_idx` (`instrumentSerialNum` ASC) VISIBLE,
  INDEX `order_to_image_conn_idx` (`orderID` ASC) VISIBLE,
  CONSTRAINT `fk_Image_Storage1`
    FOREIGN KEY (`storageID`)
    REFERENCES `Photography`.`Storages` (`storageID`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Image_Instrument1`
    FOREIGN KEY (`instrumentSerialNum`)
    REFERENCES `Photography`.`Instruments` (`serialNum`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Image_Locations1`
    FOREIGN KEY (`geodata`)
    REFERENCES `Photography`.`Locations` (`location`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `order_to_image_conn`
    FOREIGN KEY (`orderID`)
    REFERENCES `Photography`.`Orders` (`orderID`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`PhotographySubjects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`PhotographySubjects` (
  `subjectName` VARCHAR(45) NOT NULL,
  `location` VARCHAR(64) NOT NULL,
  `person` TINYINT NULL,
  PRIMARY KEY (`subjectName`, `location`),
  CONSTRAINT `fk_Subjects_Locations1`
    FOREIGN KEY (`location`)
    REFERENCES `Photography`.`Locations` (`location`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Photography`.`Prices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Photography`.`Prices` (
  `style` VARCHAR(45) NOT NULL,
  `agencyID` INT NOT NULL,
  `pricePerOnePhoto` INT NULL,
  PRIMARY KEY (`style`, `agencyID`),
  INDEX `for_which_agency_idx` (`agencyID` ASC) VISIBLE,
  CONSTRAINT `for_which_agency`
    FOREIGN KEY (`agencyID`)
    REFERENCES `Photography`.`PhotographyAgencies` (`agencyID`)
    ON UPDATE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;