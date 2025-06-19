CREATE TABLE IF NOT EXISTS `medicationrequest` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `meta_profile_0` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `intent` VARCHAR(255) DEFAULT NULL,
  `medicationcodeableconcept_coding` VARCHAR(255) DEFAULT NULL,
  `medicationcodeableconcept_text` VARCHAR(255) DEFAULT NULL,
  `subject_reference` VARCHAR(255) DEFAULT NULL,
  `encounter_reference` VARCHAR(255) DEFAULT NULL,
  `authoredon` VARCHAR(255) DEFAULT NULL,
  `requester_reference` VARCHAR(255) DEFAULT NULL,
  `requester_display` VARCHAR(255) DEFAULT NULL,
  `reasonreference` VARCHAR(255) DEFAULT NULL,
  `dosageinstruction` VARCHAR(255) DEFAULT NULL,
  `medicationreference_reference` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;