import sqlite3
from typing import List, Dict, Any, Optional

class BangerWaveDatabase:
    """Manages thread-safe SQLite transactions for user playlists and track caching."""
    def __init__(self, db_name: str = "bangerwave.db"):
        self.db_name = db_name
        self.initialize_schema()

    def _get_connection(self) -> sqlite3.Connection:
        """Opens a distinct, parameterized database connection handle."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row  # Enables column access by dictionary string keys
        return conn

    def initialize_schema(self) -> None:
        """Generates relational database tables safely if they don't exist yet."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Master Cache Table for Track Information
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tracks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    search_query TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    duration REAL NOT NULL
                )
            """)
            
            # Folder Index for Custom Playlists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS playlists (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Relational Junction Table mapping tracks to playlists with cascade protection
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS playlist_tracks (
                    playlist_id INTEGER,
                    track_id INTEGER,
                    PRIMARY KEY (playlist_id, track_id),
                    FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
                    FOREIGN KEY (track_id) REFERENCES tracks(id) ON DELETE CASCADE
                )
            """)
            conn.commit()

    def create_playlist(self, playlist_name: str) -> bool:
        """Inserts a new playlist record; returns False if name is a duplicate."""
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO playlists (name) VALUES (?)", (playlist_name.strip(),))
                return True
        except sqlite3.IntegrityError:
            return False
