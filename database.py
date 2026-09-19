import sqlite3

DB_NAME = "trips.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS trips(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver TEXT NOT NULL,
            from_location TEXT NOT NULL,
            to_location TEXT NOT NULL,
            date TEXT NOT NULL,
            seats_available INTEGER NOT NULL,
            price_per_seat REAL NOT NULL
        )
    """)   
    conn.commit()
    conn.close()


def add_trip(driver, from_location, to_location, date, seats_available, price_per_seat):
    conn = get_connection()
    conn.execute("""
        INSERT INTO trips (driver, from_location, to_location, date, seats_available, price_per_seat)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (driver, from_location, to_location, date, seats_available, price_per_seat))
    conn.commit()
    conn.close()


def get_all_trips():
    conn = get_connection()
    trips = conn.execute("SELECT * FROM trips").fetchall()
    conn.close()
    return trips


def book_seat(trip_id):
    conn = get_connection()
    conn.execute("""
        UPDATE trips
        SET seats_available = seats_available - 1
        WHERE id = ? AND seats_available > 0
    """, (trip_id,))
    conn.commit()
    conn.close()


