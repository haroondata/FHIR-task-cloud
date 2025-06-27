CREATE TABLE IF NOT EXISTS `supplydelivery` (
  `resourcetype` VARCHAR(255) DEFAULT NULL,
  `id` VARCHAR(255) DEFAULT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `patient_reference` VARCHAR(255) DEFAULT NULL,
  `type_coding` VARCHAR(255) DEFAULT NULL,
  `supplieditem_quantity_value` BIGINT DEFAULT NULL,
  `supplieditem_itemcodeableconcept_coding` VARCHAR(255) DEFAULT NULL,
  `supplieditem_itemcodeableconcept_text` VARCHAR(255) DEFAULT NULL,
  `occurrencedatetime` VARCHAR(255) DEFAULT NULL,
  `patient_reference_uuid` VARCHAR(255) DEFAULT NULL,
  `created_at` VARCHAR(255) DEFAULT NULL,
  `updated_at` VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;