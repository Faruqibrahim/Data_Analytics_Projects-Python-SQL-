# Data Analytics Project

## Overview

This repository contains the code for a data analytics project that involves processing sales data using Python and SQL. The project demonstrates how to clean, manipulate, and load data into an SQL Server database and then perform analytical queries to derive insights.

## Files

### 1. `Data Analytics.py`
This Python script performs the following tasks:
- **Data Loading**: Reads a CSV file containing sales data using pandas.
- **Data Cleaning and Transformation**:
  - Renames columns to follow a consistent format.
  - Handles missing values and performs calculations to create new columns (`discount`, `sale_price`, `profit`).
  - Converts date columns from string to datetime format.
  - Drops unnecessary columns that are not needed for analysis.
- **Database Interaction**: 
  - Establishes a connection to a local SQL Server instance.
  - Creates a table in the SQL Server database and loads the processed data into this table.

### 2. `SQL.sql`
This SQL script includes:
- **Table Creation**: SQL statements to create tables in the SQL Server database.
- **Data Insertion**: Queries to insert data into the tables.
- **Data Analysis**:
  - Aggregates sales data by region and product.
  - Compares sales across different years to identify trends.
  - Uses Common Table Expressions (CTEs) and window functions to perform more complex queries.

## How to Use

### Prerequisites
- Python 3.x
- Pandas library
- SQLAlchemy library
- Microsoft SQL Server
- ODBC Driver 17 for SQL Server

### Steps to Run the Project

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```
2. **Run the Python Script**:
   - Ensure the path to the CSV file is correct in the script.
   - Execute the script to load the data into your SQL Server database.

3. **Execute SQL Queries**:
   - Run the SQL script (`SQL.sql`) in SQL Server Management Studio (SSMS) or using SQLCMD to create the necessary tables and perform the analyses.

## Project Insights
- This project showcases how to integrate Python and SQL for data analytics tasks.
- The data transformation process in Python ensures that the data is clean and in the right format for SQL analysis.
- SQL queries are used to perform complex analyses that are crucial for business decision-making.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any queries, please contact [your_email@example.com](mailto:your_email@example.com).

---

You can copy this content into a `README.md` file in your GitHub repository. Adjust the links and contact details as necessary. If you want to upload this file to your repository, create a file named `README.md` in the root of your project directory and paste the content there.
