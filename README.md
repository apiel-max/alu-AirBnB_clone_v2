# AirBnB Clone - The Console (v2)

## Description
This project is a clone of the AirBnB web application. Version 2 adds MySQL database storage via SQLAlchemy ORM alongside the existing file-based storage.

## Authors
- Project contributors

## Environment Variables
- `HBNB_ENV`: running environment (`dev` or `test`)
- `HBNB_MYSQL_USER`: MySQL username
- `HBNB_MYSQL_PWD`: MySQL password
- `HBNB_MYSQL_HOST`: MySQL hostname
- `HBNB_MYSQL_DB`: MySQL database name
- `HBNB_TYPE_STORAGE`: storage type (`file` or `db`)

## Usage
```bash
./console.py
```

## Storage Engines
- **FileStorage**: stores objects in a JSON file (`file.json`)
- **DBStorage**: stores objects in a MySQL database via SQLAlchemy

## Running Tests
```bash
python3 -m unittest discover tests
```
