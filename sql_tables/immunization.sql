CREATE TABLE IF NOT EXISTS `immunization` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `vaccinecode_coding` VARCHAR(255) DEFAULT NULL,
  `vaccinecode_text` VARCHAR(255) DEFAULT NULL,
  `patient_reference` VARCHAR(255) DEFAULT NULL,
  `encounter_reference` VARCHAR(255) DEFAULT NULL,
  `occurrencedatetime` VARCHAR(255) DEFAULT NULL,
  `primarysource` BOOLEAN DEFAULT NULL,
  `location_reference` VARCHAR(255) DEFAULT NULL,
  `location_display` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;