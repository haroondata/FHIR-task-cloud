CREATE TABLE IF NOT EXISTS `procedure` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `code_coding` VARCHAR(255) DEFAULT NULL,
  `code_text` VARCHAR(255) DEFAULT NULL,
  `subject_reference` VARCHAR(255) DEFAULT NULL,
  `encounter_reference` VARCHAR(255) DEFAULT NULL,
  `performedperiod_start` VARCHAR(255) DEFAULT NULL,
  `performedperiod_end` VARCHAR(255) DEFAULT NULL,
  `location_reference` VARCHAR(255) DEFAULT NULL,
  `location_display` VARCHAR(255) DEFAULT NULL,
  `reasonreference` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;