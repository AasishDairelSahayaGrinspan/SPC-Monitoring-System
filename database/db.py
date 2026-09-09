import sqlite3


DATABASE_NAME = "database/spc_monitoring.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_NAME)

    return connection



def create_tables():

    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alarms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL NOT NULL,
            reason TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)


    connection.commit()

    connection.close()


def save_measurement(value):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO measurements (value)
        VALUES (?)
        """,
        (value,)
    )


    connection.commit()

    connection.close()


def save_alarm(value, reason):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO alarms (value, reason)
        VALUES (?, ?)
        """,
        (value, reason)
    )


    connection.commit()

    connection.close()


def get_recent_alarms(limit=10):

    connection = get_connection()

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            id,
            value,
            reason,
            created_at
        FROM alarms
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )


    rows = cursor.fetchall()


    connection.close()


    return [
        dict(row)
        for row in rows
    ]



def get_recent_measurements(limit=50):

    connection = get_connection()

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            id,
            value,
            created_at
        FROM measurements
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )


    rows = cursor.fetchall()


    connection.close()


    return [
        dict(row)
        for row in rows
    ]