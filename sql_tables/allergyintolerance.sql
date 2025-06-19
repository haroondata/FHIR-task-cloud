CREATE TABLE IF NOT EXISTS `allergyintolerance` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `clinicalstatus_coding` VARCHAR(255) DEFAULT NULL,
  `verificationstatus_coding` VARCHAR(255) DEFAULT NULL,
  `type` VARCHAR(255) DEFAULT NULL,
  `category_0` VARCHAR(255) DEFAULT NULL,
  `criticality` VARCHAR(255) DEFAULT NULL,
  `code_coding` VARCHAR(255) DEFAULT NULL,
  `code_text` VARCHAR(255) DEFAULT NULL,
  `patient_reference` VARCHAR(255) DEFAULT NULL,
  `recordeddate` VARCHAR(255) DEFAULT NULL,
  `reaction` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;