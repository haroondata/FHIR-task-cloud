# FHIR Data Engineering Pipeline

## Overview
This project transforms FHIR-compliant patient data (in JSON format) into relational database tables for analytical use. The pipeline:

1. Parses FHIR JSON files.
2. Flattens nested structures.
3. Creates SQL tables (only for this task; not in production).
4. Inserts cleaned data into MySQL.
5. Writes CSVs for inspection.

---

## Getting Started

### Prerequisites
- Docker
- Docker Compose (optional)

### Environment Variables
Store your MySQL credentials in a `.env` file:
```env
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_HOST=your_db_host
DB_NAME=your_database_name
```

---

## How to Run

### Docker Only
```bash
docker build -t fhir-task .
docker run --env-file .env fhir-task
```

### With Docker Compose (recommended)
```bash
docker-compose up --build
```

---

## Project Structure
```
./
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── docs
│   └── info.txt
├── logs
├── main.py
├── output
│   ├── AllergyIntolerance_flat.csv
│   ├── CarePlan_flat.csv
│   ├── CareTeam_flat.csv
│   ├── Claim_flat.csv
│   ├── Condition_flat.csv
│   ├── Device_flat.csv
│   ├── DiagnosticReport_flat.csv
│   ├── DocumentReference_flat.csv
│   ├── Encounter_flat.csv
│   ├── ExplanationOfBenefit_flat.csv
│   ├── ImagingStudy_flat.csv
│   ├── Immunization_flat.csv
│   ├── MedicationAdministration_flat.csv
│   ├── MedicationRequest_flat.csv
│   ├── Medication_flat.csv
│   ├── Observation_flat.csv
│   ├── Patient_flat.csv
│   ├── Procedure_flat.csv
│   ├── Provenance_flat.csv
│   └── SupplyDelivery_flat.csv
├── requirements.txt
├── sql_tables
│   ├── allergyintolerance.sql
│   ├── careplan.sql
│   ├── careteam.sql
│   ├── claim.sql
│   ├── condition.sql
│   ├── device.sql
│   ├── diagnosticreport.sql
│   ├── documentreference.sql
│   ├── encounter.sql
│   ├── explanationofbenefit.sql
│   ├── imagingstudy.sql
│   ├── immunization.sql
│   ├── medication.sql
│   ├── medicationadministration.sql
│   ├── medicationrequest.sql
│   ├── observation.sql
│   ├── patient.sql
│   ├── procedure.sql
│   ├── provenance.sql
│   └── supplydelivery.sql
├── src
│   ├── info.txt
│   └── tools
│       ├── db
│       │   ├── check_connection.py
│       │   ├── db_inserter.py
│       │   ├── execute_schema_queries.py
│       │   └── mysql_connection.py
│       ├── etl
│       │   ├── create_sql_schema.py
│       │   ├── creates_csv_file.py
│       │   ├── generate_sql_create_queries.py
│       │   ├── prepare_and_load_to_mysql.py
│       │   └── read_json_data.py
│       ├── info.txt
│       ├── logger.py
│       └── utils
│           ├── df_preprocessor.py
│           └── helper_function_cleaning_df.py
└── test
    ├── test_extract_patient.py
    ├── test_flatten.py
    └── test_schema.py
```

---

## Notes
- **Table Creation:** For this assessment, SQL table schemas are generated from inferred DataFrame schemas. This is not run every time in production.
- **NaN Handling:** Python `NaN` values are converted to SQL `NULL` using `df.where(pd.notnull(df), None)` before insertion.

---

## Tests
Run tests from the root:
```bash
pytest tests/
```

## License
MIT
