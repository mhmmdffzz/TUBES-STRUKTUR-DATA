# ========================================
# MODELS - Definisi Struktur Data
# ========================================
# File ini berisi class untuk semua entitas dalam sistem:
# - Song (Child): Lagu yang dimiliki Artis dan bisa ada di Playlist User
# - Artist (Parent 1): Penyanyi/Band yang memiliki lagu
# - User (Parent 2): Pendengar yang memiliki playlist
# - Admin: Pengelola sistem

class Song:
    """
    Model untuk LAGU (Child Entity)
    Lagu ini milik Artis (parent) dan bisa direferensikan oleh User (MLL)
    """
    def __init__(self, title, year, duration, artist_name=""):
        self.title = title              # Judul lagu (string)
        self.year = year                # Tahun rilis (integer)
        self.duration = duration        # Durasi dalam detik (integer)
        self.artist_name = artist_name  # Nama artis pemilik (string)
        self.play_count = 0             # Jumlah kali diputar (integer)
    
    def to_dict(self):
        """
        Konversi objek Song ke dictionary untuk disimpan ke JSON
        Return: dict dengan semua atribut lagu
        """
        return {
            'title': self.title,
            'year': self.year,
            'duration': self.duration,
            'artist_name': self.artist_name,
            'play_count': self.play_count
        }
    
    @staticmethod
    def from_dict(data):
        """
        Buat objek Song dari dictionary (saat load dari JSON)
        Parameter: data (dict) - dictionary berisi data lagu
        Return: objek Song
        """
        song = Song(
            data['title'], 
            data['year'], 
            data.get('duration', 180),
            data.get('artist_name', "")
        )
        song.play_count = data.get('play_count', 0)
        return song


class Artist:
    """
    Model untuk ARTIS (Parent 1)
    Artis memiliki list lagu (child) sebagai pointer ke children
    """
    def __init__(self, name, genre, verified=False):
        self.name = name            # Nama artis - KEY UNIK (string)
        self.genre = genre          # Genre utama (string)
        self.verified = verified    # Status verified (boolean)
        self.songs = []             # Pointer ke child list: List objek Song
    
    def add_song(self, song):
        """
        Tambah lagu ke child list artis (INSERT CHILD)
        Parameter: song (Song) - objek lagu yang akan ditambahkan
        """
        self.songs.append(song)
    
    def song_count(self):
        """
        Hitung jumlah lagu yang dimiliki artis
        Return: integer - jumlah lagu
        """
        return len(self.songs)
    
    def total_plays(self):
        """
        Hitung total play count dari semua lagu artis
        Return: integer - jumlah total pemutaran
        """
        return sum(song.play_count for song in self.songs)
    
    def to_dict(self):
        """
        Konversi objek Artist ke dictionary untuk JSON
        Return: dict dengan data artis dan semua lagunya
        """
        return {
            'name': self.name,
            'genre': self.genre,
            'verified': self.verified,
            'songs': [song.to_dict() for song in self.songs]
        }
    
    @staticmethod
    def from_dict(data):
        """
        Buat objek Artist dari dictionary (saat load dari JSON)
        Parameter: data (dict) - dictionary berisi data artis
        Return: objek Artist
        """
        artist = Artist(
            data['name'], 
            data['genre'],
            data.get('verified', False)
        )
        # Rebuild child list songs
        artist.songs = [Song.from_dict(s) for s in data.get('songs', [])]
        return artist


class User:
    """
    Model untuk USER (Parent 2)
    User memiliki playlist berisi referensi ke lagu-lagu (MLL - Memory Linked List)
    """
    def __init__(self, username, password="", playlist_name=None):
        self.username = username                      # Username - KEY UNIK (string)
        self.password = password                      # Password untuk autentikasi (string)
        
        if playlist_name:
            self.playlist_name = playlist_name
        else:
            self.playlist_name = f"Playlist {username}"
        
        self.playlist = []                            # Pointer ke child list: List referensi Song (MLL)
    
    def playlist_count(self):
        """
        Hitung jumlah lagu di playlist user
        Return: integer - jumlah lagu
        """
        return len(self.playlist)
    
    def to_dict(self):
        """
        Konversi objek User ke dictionary untuk JSON
        Playlist disimpan sebagai referensi (title + artist_name) bukan objek penuh
        Return: dict dengan data user dan referensi playlist
        """
        return {
            'username': self.username,
            'password': self.password,
            'playlist_name': self.playlist_name,
            'playlist_refs': [
                {'title': song.title, 'artist': song.artist_name}
                for song in self.playlist
            ]
        }
    
    @staticmethod
    def from_dict(data, artists_list):
        """
        Buat objek User dari dictionary (saat load dari JSON)
        PENTING: Rebuild playlist dengan mencari referensi ke objek Song di artists_list (MLL)
        
        Parameter: 
            data (dict) - dictionary berisi data user
            artists_list (list) - list semua artis untuk mencari referensi lagu
        Return: objek User
        """
        user = User(
            data['username'], 
            data.get('password', ''),
            data.get('playlist_name')
        )
        
        # === REBUILD MLL (Memory Linked List) ===
        # Playlist hanya menyimpan REFERENSI ke objek Song yang sama dengan di artists_list
        # Jadi jika play_count berubah, semua referensi terupdate
        for song_ref in data.get('playlist_refs', []):
            for artist in artists_list:
                for song in artist.songs:
                    # Cari song yang cocok berdasarkan title dan artist
                    if song.title == song_ref['title'] and song.artist_name == song_ref['artist']:
                        user.playlist.append(song)  # Tambahkan referensi, bukan copy
                        break
        
        return user


class Admin:
    """
    Model untuk ADMIN
    Admin mengelola database musik (artis dan lagu)
    """
    def __init__(self, username, password):
        self.username = username  # Username admin - KEY UNIK (string)
        self.password = password  # Password untuk autentikasi (string)
    
    def to_dict(self):
        """
        Konversi objek Admin ke dictionary untuk JSON
        Return: dict dengan username dan password
        """
        return {
            'username': self.username,
            'password': self.password
        }
    
    @staticmethod
    def from_dict(data):
        """
        Buat objek Admin dari dictionary (saat load dari JSON)
        Parameter: data (dict) - dictionary berisi data admin
        Return: objek Admin
        """
        return Admin(data['username'], data['password'])
