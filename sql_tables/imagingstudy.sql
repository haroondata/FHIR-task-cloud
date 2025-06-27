CREATE TABLE IF NOT EXISTS `imagingstudy` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `identifier` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `subject_reference` VARCHAR(255) DEFAULT NULL,
  `encounter_reference` VARCHAR(255) DEFAULT NULL,
  `started` VARCHAR(255) DEFAULT NULL,
  `numberofseries` BIGINT DEFAULT NULL,
  `numberofinstances` BIGINT DEFAULT NULL,
  `procedurecode` VARCHAR(255) DEFAULT NULL,
  `location_reference` VARCHAR(255) DEFAULT NULL,
  `location_display` VARCHAR(255) DEFAULT NULL,
  `series` VARCHAR(255) DEFAULT NULL,
  `patient_reference_uuid` VARCHAR(255) DEFAULT NULL,
  `created_at` VARCHAR(255) DEFAULT NULL,
  `updated_at` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;