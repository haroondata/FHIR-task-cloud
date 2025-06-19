CREATE TABLE IF NOT EXISTS `device` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `udicarrier` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `distinctidentifier` VARCHAR(255) DEFAULT NULL,
  `manufacturedate` VARCHAR(255) DEFAULT NULL,
  `expirationdate` VARCHAR(255) DEFAULT NULL,
  `lotnumber` VARCHAR(255) DEFAULT NULL,
  `serialnumber` VARCHAR(255) DEFAULT NULL,
  `devicename` VARCHAR(255) DEFAULT NULL,
  `type_coding` VARCHAR(255) DEFAULT NULL,
  `type_text` VARCHAR(255) DEFAULT NULL,
  `patient_reference` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;