CREATE TABLE IF NOT EXISTS `medicationadministration` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `medicationcodeableconcept_coding` VARCHAR(255) DEFAULT NULL,
  `medicationcodeableconcept_text` VARCHAR(255) DEFAULT NULL,
  `subject_reference` VARCHAR(255) DEFAULT NULL,
  `context_reference` VARCHAR(255) DEFAULT NULL,
  `effectivedatetime` VARCHAR(255) DEFAULT NULL,
  `reasonreference` VARCHAR(255) DEFAULT NULL,
  `dosage_dose_value` FLOAT DEFAULT NULL,
  `dosage_ratequantity_value` FLOAT DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;