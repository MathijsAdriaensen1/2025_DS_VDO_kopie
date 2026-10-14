import psycopg2
from app import app
from contextlib import contextmanager
from psycopg2.extras import RealDictCursor


DB_CONFIG = {
    'host': app.config['DB_HOST'],
    'database': app.config['DB_NAME'],
    'user': app.config['DB_USER'],
    'password': app.config['DB_PASS'],
    'port': app.config['DB_PORT']
}

def get_connection():
    """Maak een connectie met de db"""
    return psycopg2.connect(**DB_CONFIG)


@contextmanager
def get_cursor (commit=False):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        yield cursor
        if commit:
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def execute_query(query, params=None, fetch=False, fetchone=False, commit=False):
    """
    Simpele query executor

    Args:
        query: SQL query string
        params: Query parameters (tuple of dict)
        fetch: Return all results
        fetchone: Return single result
        commit: Commit transaction
    """
    with get_cursor(commit=commit) as cursor:
        cursor.execute(query, params)

        if fetchone:
            return cursor.fetchone()
        elif fetch:
            return cursor.fetchall()
        else:
            return cursor.rowcount

