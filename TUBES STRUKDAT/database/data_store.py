# ========================================
# DATA STORE - Manajemen Database & Persistence
# ========================================
# File ini mengelola:
# - Global storage (RAM): artists_list, users_list, admins_list
# - Load/Save ke JSON (Disk)
# - Helper functions untuk CRUD operations

import json
import os
from database.models import Artist, Song, User, Admin

# ========================================
# GLOBAL DATA STORAGE (RAM)
# ========================================
artists_list = []  # List semua Artist objects
users_list = []    # List semua User objects
admins_list = []   # List semua Admin objects

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
    global artists_list, users_list, admins_list
    
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
        
        # Load artists terlebih dahulu (karena users butuh referensi ke songs)
        artists_list = [Artist.from_dict(a) for a in data.get('artists', [])]
        
        # Load users (dengan referensi ke songs di artists_list - MLL)
        users_list = [User.from_dict(u, artists_list) for u in data.get('users', [])]
        
        # Load admins
        admins_list = [Admin.from_dict(a) for a in data.get('admins', [])]
        
        print(f"Database loaded: {len(artists_list)} artis, {len(users_list)} user, {len(admins_list)} admin")
    
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
            'artists': [artist.to_dict() for artist in artists_list],
            'users': [user.to_dict() for user in users_list],
            'admins': [admin.to_dict() for admin in admins_list]
        }
        
        # Tulis ke file JSON dengan format yang rapi
        with open(DB_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("Database berhasil disimpan!")
    
    except Exception as e:
        print(f"Error saving database: {e}")


def initialize_default_data():
    """
    Inisialisasi data default (admin dan sample data)
    Dipanggil saat database pertama kali dibuat
    """
    global artists_list, users_list, admins_list
    
    # Buat admin default
    admins_list = [
        Admin("admin", "admin123"),
        Admin("manager", "manager123")
    ]
    
    # Sample artists dan lagu
    artists_list = []
    users_list = []
    
    print("Data default berhasil dibuat!")


# ========================================
# ADMIN FUNCTIONS
# ========================================

def get_admin(username):
    """
    Cari admin berdasarkan username (Sequential Search)
    Parameter: username (string)
    Return: objek Admin atau None jika tidak ditemukan
    """
    for admin in admins_list:
        if admin.username == username:
            # return admin -> dikembalikan ke pemanggil (verify_admin atau menu)
            # Mengembalikan objek Admin yang ditemukan
            return admin
    # return None -> dikembalikan ke pemanggil
    # Admin tidak ditemukan dalam list
    return None


def verify_admin(username, password):
    """
    Verifikasi login admin
    Parameter: username (string), password (string)
    Return: True jika valid, False jika tidak
    """
    admin = get_admin(username)
    if admin and admin.password == password:
        # return True -> dikembalikan ke main.py bagian login admin
        # Login berhasil, user bisa masuk ke menu_admin()
        return True
    # return False -> dikembalikan ke main.py
    # Login gagal, tampilkan pesan error
    return False


def add_admin(username, password):
    """
    Tambah admin baru ke database
    Parameter: username (string), password (string)
    Return: True jika berhasil, False jika username sudah ada
    """
    if get_admin(username):
        # return False -> dikembalikan ke admin_add_new_admin()
        # Username sudah ada, gagal menambahkan
        return False
    
    admins_list.append(Admin(username, password))
    # return True -> dikembalikan ke admin_add_new_admin()
    # Admin berhasil ditambahkan
    return True


# ========================================
# ARTIST FUNCTIONS
# ========================================

def get_artist(name):
    """
    Cari artis berdasarkan nama (Sequential Search)
    Parameter: name (string)
    Return: objek Artist atau None jika tidak ditemukan
    """
    for artist in artists_list:
        if artist.name.lower() == name.lower():
            # return artist -> dikembalikan ke pemanggil (admin_add_artist, dll)
            # Mengembalikan objek Artist yang ditemukan
            return artist
    # return None -> dikembalikan ke pemanggil
    # Artis tidak ditemukan
    return None


def add_artist(name, genre, verified=False):
    """
    Tambah artis baru ke database (INSERT LAST)
    Parameter: name (string), genre (string), verified (bool)
    Return: True jika berhasil, False jika nama sudah ada
    """
    if get_artist(name):
        # return False -> dikembalikan ke admin_add_artist()
        # Artis sudah ada, gagal menambahkan (validasi duplikasi)
        return False
    
    # INSERT LAST - append ke akhir list
    artists_list.append(Artist(name, genre, verified))
    # return True -> dikembalikan ke admin_add_artist()
    # Artis berhasil ditambahkan
    return True


def delete_artist(name):
    """
    Hapus artis dan semua lagunya dari database (DELETE PARENT & CASCADE)
    PENTING: Juga hapus referensi lagu dari playlist user
    
    Parameter: name (string)
    Return: True jika berhasil, False jika artis tidak ditemukan
    """
    artist = get_artist(name)
    if not artist:
        # return False -> dikembalikan ke admin_delete_artist()
        # Artis tidak ditemukan, gagal menghapus
        return False
    
    # Hapus referensi lagu artis dari semua playlist user (CASCADE)
    for user in users_list:
        # Filter playlist: hapus lagu yang artisnya sama dengan yang dihapus
        user.playlist = [song for song in user.playlist if song.artist_name != artist.name]
    
    # Hapus artis dari list
    artists_list.remove(artist)
    # return True -> dikembalikan ke admin_delete_artist()
    # Artis dan semua lagunya berhasil dihapus
    return True


def get_top_artists(limit=5):
    """
    Dapatkan artis dengan jumlah lagu terbanyak
    Parameter: limit (int) - jumlah artis yang ditampilkan
    Return: list of (Artist, song_count) sorted descending
    """
    # Buat list tuple (artist, jumlah_lagu)
    artist_counts = [(artist, artist.song_count()) for artist in artists_list]
    
    # Sort berdasarkan jumlah lagu (descending)
    artist_counts.sort(key=lambda x: x[1], reverse=True)
    
    # return list[:limit] -> dikembalikan ke admin_view_top_artists()
    # Mengembalikan list tuple (Artist, song_count) yang sudah diurutkan
    return artist_counts[:limit]


# ========================================
# SONG FUNCTIONS
# ========================================

def search_song(title):
    """
    Cari lagu berdasarkan judul di semua artis (Sequential Search)
    Parameter: title (string)
    Return: list of (Artist, Song) yang cocok
    """
    results = []
    for artist in artists_list:
        for song in artist.songs:
            if title.lower() in song.title.lower():
                results.append((artist, song))
    # return results -> dikembalikan ke admin_search_song()
    # Mengembalikan list hasil pencarian (bisa kosong jika tidak ada)
    return results


def add_song_to_artist(artist_name, title, year, duration):
    """
    Tambah lagu baru ke artis tertentu (INSERT CHILD)
    Parameter: artist_name, title, year, duration
    Return: True jika berhasil, False jika artis tidak ditemukan
    """
    artist = get_artist(artist_name)
    if not artist:
        # return False -> dikembalikan ke admin_add_song()
        # Artis tidak ditemukan, gagal menambahkan lagu
        return False
    
    # Buat objek Song baru
    new_song = Song(title, year, duration, artist_name)
    
    # Tambah ke child list artis
    artist.add_song(new_song)
    # return True -> dikembalikan ke admin_add_song()
    # Lagu berhasil ditambahkan ke artis
    return True


def delete_song_from_artist(artist_name, song_title):
    """
    Hapus lagu tertentu dari artis (DELETE CHILD)
    PENTING: Juga hapus referensi dari playlist user
    
    Parameter: artist_name (string), song_title (string)
    Return: True jika berhasil, False jika tidak ditemukan
    """
    artist = get_artist(artist_name)
    if not artist:
        # return False -> dikembalikan ke admin_delete_song()
        # Artis tidak ditemukan
        return False
    
    # Cari lagu di list songs artis
    song_to_delete = None
    for song in artist.songs:
        if song.title.lower() == song_title.lower():
            song_to_delete = song
            break
    
    if not song_to_delete:
        # return False -> dikembalikan ke admin_delete_song()
        # Lagu tidak ditemukan di artis tersebut
        return False
    
    # Hapus referensi lagu dari semua playlist user (CASCADE)
    for user in users_list:
        if song_to_delete in user.playlist:
            user.playlist.remove(song_to_delete)
    
    # Hapus lagu dari artis
    artist.songs.remove(song_to_delete)
    # return True -> dikembalikan ke admin_delete_song()
    # Lagu berhasil dihapus
    return True


def get_trending_songs(limit=5):
    """
    Dapatkan lagu dengan play count tertinggi
    Parameter: limit (int) - jumlah lagu yang ditampilkan
    Return: list of (Song, Artist) sorted by play_count descending
    """
    all_songs = []
    
    # Kumpulkan semua lagu dari semua artis
    for artist in artists_list:
        for song in artist.songs:
            all_songs.append((song, artist))
    
    # Sort berdasarkan play_count (descending)
    all_songs.sort(key=lambda x: x[0].play_count, reverse=True)
    
    # return list[:limit] -> dikembalikan ke admin_view_analytics()
    # Mengembalikan list tuple (Song, Artist) yang sudah diurutkan
    return all_songs[:limit]


# ========================================
# USER FUNCTIONS
# ========================================

def get_user(username):
    """
    Cari user berdasarkan username (Sequential Search)
    Parameter: username (string)
    Return: objek User atau None jika tidak ditemukan
    """
    for user in users_list:
        if user.username == username:
            # return user -> dikembalikan ke pemanggil (menu_user_auth, dll)
            # Mengembalikan objek User yang ditemukan
            return user
    # return None -> dikembalikan ke pemanggil
    # User tidak ditemukan
    return None


def verify_user(username, password):
    """
    Verifikasi login user
    Parameter: username (string), password (string)
    Return: True jika valid, False jika tidak
    """
    user = get_user(username)
    if user and user.password == password:
        # return True -> dikembalikan ke pemanggil
        # Login user valid
        return True
    # return False -> dikembalikan ke pemanggil
    # Login gagal (user tidak ada atau password salah)
    return False


def add_user(username, password=""):
    """
    Tambah user baru (INSERT FIRST - user baru di depan)
    Parameter: username (string), password (string)
    Return: objek User baru atau None jika username sudah ada
    """
    if get_user(username):
        # return None -> dikembalikan ke menu_user_auth() bagian register
        # Username sudah ada, gagal register
        return None
    
    new_user = User(username, password)
    # INSERT FIRST - insert di posisi 0
    users_list.insert(0, new_user)
    # return new_user -> dikembalikan ke menu_user_auth()
    # User baru berhasil dibuat, return objek User untuk langsung login
    return new_user


def get_top_users(limit=5):
    """
    Dapatkan user dengan playlist terbanyak
    Parameter: limit (int) - jumlah user yang ditampilkan
    Return: list of (User, playlist_count) sorted descending
    """
    # Buat list tuple (user, jumlah_lagu)
    user_counts = [(user, user.playlist_count()) for user in users_list]
    
    # Sort berdasarkan jumlah lagu (descending)
    user_counts.sort(key=lambda x: x[1], reverse=True)
    
    # return list[:limit] -> dikembalikan ke admin_view_analytics()
    # Mengembalikan list tuple (User, playlist_count) yang sudah diurutkan
    return user_counts[:limit]
