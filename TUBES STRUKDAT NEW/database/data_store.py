# ========================================
# DATA STORE - Manajemen Database & Persistence
# ========================================
# File ini mengelola:
# - Global storage (RAM): artists_list
# - Load/Save ke JSON (Disk)
# - Helper functions untuk CRUD operations
# - Pengolahan MLL: Counting dan Max

import json
import os
from database.models import Artist

# ========================================
# GLOBAL DATA STORAGE (RAM)
# ========================================
artists_list = []  # List semua Artist objects

# Path ke file database JSON
DB_PATH = os.path.join(os.path.dirname(__file__), 'music_db.json')


# ========================================
# LOAD & SAVE DATABASE
# ========================================

def load_database():
    """
    Load data dari file JSON ke memory (RAM)
    Dipanggil saat aplikasi start
    """
    global artists_list
    
    # Cek apakah file JSON ada
    if not os.path.exists(DB_PATH):
        print("Database belum ada, membuat data awal...")
        initialize_default_data()
        save_database()
        return
    
    try:
        # Baca file JSON
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Load artists dari JSON
        artists_list = [Artist.from_dict(a) for a in data.get('artists', [])]
        
        # Hitung total lagu
        total_songs = sum(artist.song_count() for artist in artists_list)
        print(f"Database loaded: {len(artists_list)} artis, {total_songs} lagu")
    
    except Exception as e:
        print(f"Error loading database: {e}")
        initialize_default_data()


def save_database():
    """
    Simpan data dari memory (RAM) ke file JSON (Disk)
    Dipanggil saat aplikasi exit atau user request
    """
    try:
        # Konversi semua objek ke dictionary
        data = {
            'artists': [artist.to_dict() for artist in artists_list]
        }
        
        # Tulis ke file JSON dengan format yang rapi
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("Database berhasil disimpan!")
    
    except Exception as e:
        print(f"Error saving database: {e}")


def initialize_default_data():
    """
    Inisialisasi data default (sample data)
    Dipanggil saat database pertama kali dibuat
    """
    global artists_list
    
    # Sample artists dan lagu
    artists_list = []
    
    # Contoh artis 1
    tulus = Artist("Tulus", "Pop", 2011)
    tulus.add_song("Hati-Hati di Jalan")
    tulus.add_song("Monokrom")
    tulus.add_song("Sepatu")
    artists_list.append(tulus)
    
    # Contoh artis 2
    sheila = Artist("Sheila on 7", "Pop Rock", 1996)
    sheila.add_song("Dan")
    sheila.add_song("Sephia")
    sheila.add_song("Kita")
    sheila.add_song("Melompat Lebih Tinggi")
    artists_list.append(sheila)
    
    # Contoh artis 3
    raisa = Artist("Raisa", "R&B", 2011)
    raisa.add_song("Serba Salah")
    raisa.add_song("Mantan Terindah")
    artists_list.append(raisa)
    
    print("Data default berhasil dibuat!")


# ========================================
# ARTIST FUNCTIONS (CRUD PARENT)
# ========================================

def get_artist(name):
    """
    Cari artis berdasarkan nama (Sequential Search)
    Parameter: name (string)
    Return: objek Artist atau None jika tidak ditemukan
    """
    for artist in artists_list:
        if artist.nama_artis.lower() == name.lower():
            return artist
    return None


def add_artist(nama_artis, genre, tahun_debut):
    """
    Tambah artis baru ke database (INSERT LAST)
    Parameter: nama_artis (string), genre (string), tahun_debut (int)
    Return: True jika berhasil, False jika nama sudah ada
    """
    if get_artist(nama_artis):
        return False
    
    # INSERT LAST - append ke akhir list
    new_artist = Artist(nama_artis, genre, tahun_debut)
    artists_list.append(new_artist)
    return True


def delete_artist(name):
    """
    Hapus artis dan semua lagunya dari database (DELETE PARENT & CASCADE)
    Parameter: name (string)
    Return: True jika berhasil, False jika artis tidak ditemukan
    """
    artist = get_artist(name)
    if not artist:
        return False
    
    # Hapus artis dari list (lagu ikut terhapus karena child ada di dalam parent)
    artists_list.remove(artist)
    return True


# ========================================
# SONG FUNCTIONS (CRUD CHILD)
# ========================================

def add_song_to_artist(artist_name, judul_lagu):
    """
    Tambah lagu baru ke artis tertentu (INSERT CHILD)
    Parameter: artist_name (string), judul_lagu (string)
    Return: True jika berhasil, False jika artis tidak ditemukan atau lagu sudah ada
    """
    artist = get_artist(artist_name)
    if not artist:
        return False
    
    # Cek duplikasi lagu
    if artist.has_song(judul_lagu):
        return False
    
    # Tambah lagu ke child list artis
    artist.add_song(judul_lagu)
    return True


def delete_song_from_artist(artist_name, judul_lagu):
    """
    Hapus lagu tertentu dari artis (DELETE CHILD)
    Parameter: artist_name (string), judul_lagu (string)
    Return: True jika berhasil, False jika tidak ditemukan
    """
    artist = get_artist(artist_name)
    if not artist:
        return False
    
    return artist.remove_song(judul_lagu)


def search_artist(keyword):
    """
    Cari artis berdasarkan nama (Sequential Search dengan partial match)
    Parameter: keyword (string)
    Return: list of Artist yang cocok
    """
    results = []
    for artist in artists_list:
        if keyword.lower() in artist.nama_artis.lower():
            results.append(artist)
    return results


# ========================================
# PENGOLAHAN MLL: COUNTING & MAX
# ========================================

def count_total_songs():
    """
    Hitung total seluruh lagu di database (COUNTING)
    Return: integer - jumlah total lagu
    """
    total = 0
    for artist in artists_list:
        total += artist.song_count()
    return total


def get_artist_with_most_songs():
    """
    Cari artis dengan lagu paling banyak (MAX)
    Return: tuple (Artist, song_count) atau (None, 0) jika database kosong
    """
    if not artists_list:
        return (None, 0)
    
    max_artist = artists_list[0]
    max_count = max_artist.song_count()
    
    for artist in artists_list:
        if artist.song_count() > max_count:
            max_artist = artist
            max_count = artist.song_count()
    
    return (max_artist, max_count)


def get_all_artists_sorted_by_songs():
    """
    Dapatkan semua artis diurutkan berdasarkan jumlah lagu (descending)
    Return: list of (Artist, song_count)
    """
    artist_counts = [(artist, artist.song_count()) for artist in artists_list]
    
    # Sort berdasarkan jumlah lagu (descending) - Bubble Sort
    n = len(artist_counts)
    for i in range(n):
        for j in range(0, n-i-1):
            if artist_counts[j][1] < artist_counts[j+1][1]:
                artist_counts[j], artist_counts[j+1] = artist_counts[j+1], artist_counts[j]
    
    return artist_counts
