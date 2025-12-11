# ========================================
# MODELS - Definisi Struktur Data
# ========================================
# File ini berisi class untuk entitas dalam sistem:
# - Artist (Parent): Artis yang memiliki daftar lagu
# - Lagu (Child): Tipe dasar String (hanya judul lagu)
#
# Struktur MLL (Multi Linked List) 1-N:
# PARENT (Artis) -> CHILD (List of String judul lagu)

class Artist:
    """
    Model untuk ARTIS (Parent Entity)
    Artis memiliki list lagu (child) berupa List of String (judul lagu saja)
    
    Struktur sesuai syarat:
    - Parent berupa Record (Class Object)
    - Child berupa Tipe Dasar (String)
    """
    def __init__(self, nama_artis, genre, tahun_debut):
        self.nama_artis = nama_artis    # Nama artis - KEY UNIK (string)
        self.genre = genre              # Genre musik (string)
        self.tahun_debut = tahun_debut  # Tahun debut (integer)
        self.songs = []                 # Pointer ke child list: List of String (judul lagu)
    
    def add_song(self, judul_lagu):
        """
        Tambah lagu ke child list artis (INSERT CHILD)
        Parameter: judul_lagu (string) - judul lagu yang akan ditambahkan
        """
        self.songs.append(judul_lagu)
    
    def remove_song(self, judul_lagu):
        """
        Hapus lagu dari child list artis (DELETE CHILD)
        Parameter: judul_lagu (string) - judul lagu yang akan dihapus
        Return: True jika berhasil, False jika tidak ditemukan
        """
        for i, song in enumerate(self.songs):
            if song.lower() == judul_lagu.lower():
                self.songs.pop(i)
                return True
        return False
    
    def song_count(self):
        """
        Hitung jumlah lagu yang dimiliki artis (COUNTING)
        Return: integer - jumlah lagu
        """
        return len(self.songs)
    
    def has_song(self, judul_lagu):
        """
        Cek apakah artis memiliki lagu tertentu
        Parameter: judul_lagu (string)
        Return: True jika ada, False jika tidak
        """
        for song in self.songs:
            if song.lower() == judul_lagu.lower():
                return True
        return False
    
    def to_dict(self):
        """
        Konversi objek Artist ke dictionary untuk disimpan ke JSON
        Return: dict dengan semua atribut artis
        """
        return {
            'nama_artis': self.nama_artis,
            'genre': self.genre,
            'tahun_debut': self.tahun_debut,
            'songs': self.songs  # List of string, langsung disimpan
        }
    
    @staticmethod
    def from_dict(data):
        """
        Buat objek Artist dari dictionary (saat load dari JSON)
        Parameter: data (dict) - dictionary berisi data artis
        Return: objek Artist
        """
        artist = Artist(
            data['nama_artis'],
            data['genre'],
            data.get('tahun_debut', 2000)
        )
        # Load child list songs (list of string)
        artist.songs = data.get('songs', [])
        return artist
