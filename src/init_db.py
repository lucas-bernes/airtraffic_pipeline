from database import get_connection


def run_schema():
    conn = get_connection()
    cursor = conn.cursor()

    with open("database/schema.sql", "r", encoding="utf-8") as file:
        sql_script = file.read()

    # Split and execute multiple SQL statements
    statements = sql_script.split(";")

    for statement in statements:
        statement = statement.strip()
        if statement:
            cursor.execute(statement)

    conn.commit()
    cursor.close()
    conn.close()

    print("Database schema executed successfully.")


if __name__ == "__main__":
    run_schema()
