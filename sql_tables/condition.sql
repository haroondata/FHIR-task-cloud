CREATE TABLE IF NOT EXISTS `condition` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `clinicalstatus_coding` VARCHAR(255) DEFAULT NULL,
  `verificationstatus_coding` VARCHAR(255) DEFAULT NULL,
  `category` VARCHAR(255) DEFAULT NULL,
  `code_coding` VARCHAR(255) DEFAULT NULL,
  `code_text` VARCHAR(255) DEFAULT NULL,
  `subject_reference` VARCHAR(255) DEFAULT NULL,
  `encounter_reference` VARCHAR(255) DEFAULT NULL,
  `onsetdatetime` VARCHAR(255) DEFAULT NULL,
  `recordeddate` VARCHAR(255) DEFAULT NULL,
  `abatementdatetime` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;