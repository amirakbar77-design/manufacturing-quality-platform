import psycopg

connection = psycopg.connect(
    "dbname=manufacturing_quality"
)

print("Connected to PostgreSQL!")

connection.close()
