CREATE TABLE IF NOT EXISTS `careteam` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `subject_reference` VARCHAR(255) DEFAULT NULL,
  `encounter_reference` VARCHAR(255) DEFAULT NULL,
  `period_start` VARCHAR(255) DEFAULT NULL,
  `participant` VARCHAR(255) DEFAULT NULL,
  `reasoncode` VARCHAR(255) DEFAULT NULL,
  `managingorganization` VARCHAR(255) DEFAULT NULL,
  `period_end` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;