import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Allow override for Render Disk: set DATABASE_PATH=/var/data/spc_monitoring.db
DATABASE_NAME = os.environ.get(
    "DATABASE_PATH",
    os.path.join(BASE_DIR, "database", "spc_monitoring.db"),
)


def get_connection():

    os.makedirs(os.path.dirname(DATABASE_NAME), exist_ok=True)
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