import sqlite3

class BangerWaveDatabase:
    def __init__(self, db_name: str = "tunein.db"):
        self.db_name = db_name
        self.initialize_schema()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_name)
        # Forces columns to map directly to text string dictionary keys
        conn.row_factory = sqlite3.Row  
        return conn

    def create_playlist(self, playlist_name: str) -> bool:
   
        """Inserts a new playlist track record; returns False  if name is duplicate."""
        try: 
            with self._get_connection() as conn:
                 cursor = conn.cursor()
                 cursor.execute("INSERT INTO playlists (name) VALUES (?)", (playlist_name,))


              
            return True
        except sqlite3.IntegrityError:
            return False

    def initialize_schema(self): 
        """Creates the playlists table if it doesn't exist."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
  #Master cache Table for Tracking Info
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tracks ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    search_query TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    duration REAL NOT NULL
                )
            """) 
     #Folder Table for Playlists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS playlists (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """) 
     #Relational TAble mapping tracks to playlist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS playlist_tracks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    playlist_id INTEGER NOT NULL,
                    track_id INTEGER NOT NULL,
                    FOREIGN KEY (playlist_id) REFERENCES playlists (id) ON DELETE CASCADE,
                    FOREIGN KEY (track_id) REFERENCES tracks (id) ON DELETE CASCADE
                )
            """) 

#TODO try to fix any errors and bugs and work on the next steps or ui