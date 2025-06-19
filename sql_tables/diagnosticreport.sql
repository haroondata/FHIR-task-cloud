CREATE TABLE IF NOT EXISTS `diagnosticreport` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `category` VARCHAR(255) DEFAULT NULL,
  `code_coding` VARCHAR(255) DEFAULT NULL,
  `subject_reference` VARCHAR(255) DEFAULT NULL,
  `encounter_reference` VARCHAR(255) DEFAULT NULL,
  `effectivedatetime` VARCHAR(255) DEFAULT NULL,
  `issued` VARCHAR(255) DEFAULT NULL,
  `performer` VARCHAR(255) DEFAULT NULL,
  `presentedform` VARCHAR(255) DEFAULT NULL,
  `code_text` VARCHAR(255) DEFAULT NULL,
  `result` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;