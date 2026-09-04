import psycopg
from psycopg.rows import dict_row


def get_db_connection():
    return psycopg.connect("dbname=manufacturing_quality")


def insert_machine_records(record):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
    INSERT INTO machine_readings (udi,
        product_id,
        type,
        air_temperature,
        process_temperature,
        rotational_speed,
        torque,
        tool_wear)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """,
                (
                    record["udi"],
                    record["product_id"],
                    record["type"],
                    record["air_temperature"],
                    record["process_temperature"],
                    record["rotational_speed"],
                    record["torque"],
                    record["tool_wear"])
            )


def get_machine_record_by_udi(udi):
    with get_db_connection() as connection:
        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """
            SELECT * FROM machine_readings
            WHERE udi = %s
                """,

                (udi,)
            )

            row = cursor.fetchone()
            return row


def delete_machine_record_by_udi(udi):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM machine_readings
                WHERE udi = %s
                """,

                (udi,)
            )


def update_machine_tool_wear(udi, tool_wear):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE machine_readings
                SET tool_wear = %s
                WHERE udi = %s;



                """,
                (tool_wear, udi)
            )


def insert_machine_records_bulk(records):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            for record in records:
                cursor.execute(
                    """
                    INSERT INTO machine_readings (
                        udi,
                        product_id,
                        type,
                        air_temperature,
                        process_temperature,
                        rotational_speed,
                        torque,
                        tool_wear
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
                    ON CONFLICT (udi) DO NOTHING
                    """,
                    (
                        record["udi"],
                        record["product_id"],
                        record["type"],
                        record["air_temperature"],
                        record["process_temperature"],
                        record["rotational_speed"],
                        record["torque"],
                        record["tool_wear"],
                    ),
                )
