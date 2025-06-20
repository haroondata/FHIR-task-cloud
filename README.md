# FHIR Data Engineering Pipeline

## Overview
This project transforms FHIR-compliant patient data (in JSON format) into relational database tables for analytical use. The pipeline:

1. Parses FHIR JSON files.
2. Flattens nested structures.
3. Creates SQL tables (only for this task; not in production).
4. Inserts cleaned data into MySQL.
5. Optionally writes CSVs for inspection.

---

## Getting Started

### Prerequisites
- Docker
- Docker Compose (optional)

### Environment Variables
Store your MySQL credentials in a `.env` file:
```env
DB_USERNAME=your_username
DB_PASSWORD=your_password_with_special_chars
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
.
├── data/                      # Input FHIR JSON files
├── output/                   # Output CSVs (optional)
├── src/
│   ├── tools/
│   │   ├── read_json_data.py
│   │   ├── flatten_json.py
│   │   ├── mysql_connection.py
│   │   └── insert_data_into_mysql.py
├── requirements.txt
├── Dockerfile
├── .env
└── main.py
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
