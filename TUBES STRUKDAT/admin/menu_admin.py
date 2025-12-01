# ========================================
# MENU ADMIN - Manajemen Database Musik
# ========================================
# File ini berisi semua fitur untuk admin:
# 1. Insert Last Artis
# 2. Insert Lagu (Child)
# 3. View All Music (Nested)
# 4. Delete Artis (Parent & Cascade)
# 5. Delete Lagu (Child)
# 6. View Top Artist
# 7. Search Lagu
# 8. Add Admin
# 9. View Analytics (Trending & Top User)

import os
import time
#untuk mengakses data store.py, kita perlu mengimpor fungsi dan variabel yang diperlukan
from database.data_store import (
    artists_list, users_list, admins_list,
    add_artist, get_artist, delete_artist, get_top_artists,
    add_song_to_artist, delete_song_from_artist, search_song,
    add_admin, get_trending_songs, get_top_users
)
#untuk mengakses dat base models.py
from database.models import Song 

# ========================================
# FUNGSI UTILITY
# ========================================

def clear_screen():
    """Membersihkan layar terminal"""
    # Metode 1: os.system (standard)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Metode 2: ANSI escape code (backup jika os.system gagal)
    print("\033[H\033[J", end="")

def print_header(title):
    """Cetak header dengan border"""
    width = 70
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()

def pause():
    """Pause dan tunggu user tekan Enter"""
    input("\n[Tekan Enter untuk kembali ke menu...]")


# ========================================
# FITUR 1: INSERT LAST ARTIS
# ========================================

def admin_add_artist():
    """
    Menambahkan artis baru ke database (INSERT LAST)
    Artis ditambahkan di akhir list menggunakan append
    """
    print("\n--- TAMBAH ARTIS BARU ---") #ini akan di tampilkan di tittle menu admin
    
    # Input data artis
    name = input("Nama Artis: ").strip() #strip untuk menghilangkan spasi di awal dan akhir
    if not name:
        print("Nama artis tidak boleh kosong!")
        # return tanpa nilai = return None
        # Dikembalikan ke: menu_admin() -> baris yang memanggil admin_add_artist()
        # Setelah return, lanjut ke pause() lalu loop while kembali tampilkan menu
        return
    
    # Cek apakah artis sudah ada (validasi duplikasi)
    if get_artist(name): 
        print(f"Artis '{name}' sudah ada di database!")
        # return tanpa nilai = return None
        # Dikembalikan ke: menu_admin() baris 'admin_add_artist()'
        # Flow: return -> pause() -> while True (loop menu admin)
        return 
    
    genre = input("Genre: ").strip()
    verified_input = input("Verified? (y/n): ").lower()
    verified = True if verified_input == 'y' else False
    
    # Tambah artis menggunakan fungsi helper (INSERT LAST)
    if add_artist(name, genre, verified):
        print(f"Artis '{name}' berhasil ditambahkan ke database!")
        print(f"   Genre: {genre}, Verified: {'Ya' if verified else 'Tidak'}")
    else:
        print("Gagal menambahkan artis!")


# ========================================
# FITUR 2: INSERT LAGU (CHILD)
# ========================================

def admin_add_song():

    print("\n--- TAMBAH LAGU KE ARTIS ---")
    
    # Tampilkan daftar artis yang ada
    if not artists_list:
        print("Belum ada artis di database! Tambahkan artis terlebih dahulu.")
        # return tanpa nilai     = return None
        # Dikembalikan ke: menu_admin() baris 'admin_add_song()'
        # Flow: return -> pause() -> while True (loop menu admin)
        return
    
    print("\nDaftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        print(f"   {i}. {artist.name} ({artist.genre}) - {artist.song_count()} lagu")
    
    # Pilih artis
    artist_name = input("\nNama Artis: ").strip()#menghilangkan spasi di awal dan akhir
    artist = get_artist(artist_name)#mengambil objek artis berdasarkan nama
    
    if not artist:
        print(f"Artis '{artist_name}' tidak ditemukan!")
        # return tanpa nilai = return None
        # Dikembalikan ke: menu_admin() -> setelah admin_add_song() selesai
        # Flow: return -> pause() -> loop menu admin
        return
    
    # Input data lagu
    title = input("Judul Lagu: ").strip()
    if not title:
        print("Judul lagu tidak boleh kosong!")
        # return None -> dikembalikan ke menu_admin()
        # Flow: return -> pause() -> loop menu admin
        return
    
    try: 
        year = int(input("Tahun Rilis: ")) 
        duration = int(input("Durasi (detik): "))
    except ValueError:
        print("Tahun dan durasi harus berupa angka!")
        # return None -> dikembalikan ke menu_admin()
        # Keluar dari fungsi karena input tidak valid
        return
    
    # Tambah lagu ke artis (INSERT CHILD)
    if add_song_to_artist(artist_name, title, year, duration):
        print(f"Lagu '{title}' berhasil ditambahkan ke artis '{artist_name}'!")
        print(f"   Total lagu {artist_name}: {artist.song_count()}")
    else:
        print("Gagal menambahkan lagu!")


# ========================================
# FITUR 3: VIEW ALL MUSIC (NESTED)
# ========================================

def admin_view_all_music():
  
    print("\n--- DATABASE MUSIK LENGKAP ---\n")
    
    if not artists_list:
        print("(Database masih kosong)")
        # return None -> dikembalikan ke menu_admin()
        # Tidak ada yang ditampilkan, langsung kembali ke menu
        return
    
    # Loop semua artis (Parent)
    for i, artist in enumerate(artists_list, 1):
        # Tampilkan info artis
        verified_badge = "[V]" if artist.verified else ""
        print(f"{i}. {artist.name} {verified_badge}")
        print(f"   Genre: {artist.genre}")
        print(f"   Jumlah Lagu: {artist.song_count()}")
        print(f"   Total Plays: {artist.total_plays()}")
        
        # Loop semua lagu artis (Children) - NESTED LOOP
        if artist.songs:
            print(f"   Daftar Lagu:")
            for j, song in enumerate(artist.songs, 1):
                minutes = song.duration // 60
                seconds = song.duration % 60
                print(f"      {j}. {song.title} ({song.year}) - {minutes}:{seconds:02d} [{song.play_count} plays]")
        else:
            print(f"   (Belum ada lagu)")
        print()


# ========================================
# FITUR 4: DELETE ARTIS (CASCADE)
# ========================================

def admin_delete_artist():
    """
    Menghapus artis beserta semua lagunya (DELETE PARENT & CASCADE)
    PENTING: Lagu yang ada di playlist user juga dihapus
    """
    print("\n--- HAPUS ARTIS ---")
    
    if not artists_list:
        print("Belum ada artis di database!")
        # return None -> dikembalikan ke menu_admin()
        # Flow: return -> pause() -> loop menu admin
        return
    
    # Tampilkan daftar artis
    print("\nDaftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        print(f"   {i}. {artist.name} - {artist.song_count()} lagu")
    
    artist_name = input("\nNama Artis yang akan dihapus: ").strip()
    artist = get_artist(artist_name)
    
    if not artist:
        print(f"Artis '{artist_name}' tidak ditemukan!")
        # return None -> dikembalikan ke menu_admin()
        # Artis tidak ada, batalkan operasi
        return
    
    # Konfirmasi penghapusan (karena ini akan menghapus semua lagu juga)
    print(f"\nPERINGATAN:")
    print(f"   - Artis: {artist_name}")
    print(f"   - Jumlah lagu yang akan dihapus: {artist.song_count()}")
    print(f"   - Lagu di playlist user juga akan dihapus (CASCADE)")
    
    confirm = input("\nApakah Anda yakin? (yes/no): ").lower()
    if confirm != 'yes':
        print("Penghapusan dibatalkan.")
        # return None -> dikembalikan ke menu_admin()
        # User membatalkan, kembali ke menu tanpa menghapus
        return
    
    # Hapus artis dan cascade ke user playlists
    if delete_artist(artist_name):
        print(f"Artis '{artist_name}' dan semua lagunya berhasil dihapus!")
    else:
        print("Gagal menghapus artis!")


# ========================================
# FITUR 5: DELETE LAGU (CHILD)
# ========================================

def admin_delete_song():
    """
    Menghapus lagu tertentu dari artis (DELETE CHILD)
    PENTING: Referensi lagu di playlist user juga dihapus
    """
    print("\n--- HAPUS LAGU ---")
    
    artist_name = input("Nama Artis: ").strip()
    artist = get_artist(artist_name)
    
    if not artist:
        print(f"Artis '{artist_name}' tidak ditemukan!")
        # return None -> dikembalikan ke menu_admin()
        # Flow: return -> pause() -> loop menu admin
        return
    
    # Tampilkan lagu-lagu artis
    if not artist.songs:
        print(f"Artis '{artist_name}' belum memiliki lagu!")
        # return None -> dikembalikan ke menu_admin()
        # Tidak ada lagu yang bisa dihapus
        return
    
    print(f"\nLagu dari {artist_name}:")
    for i, song in enumerate(artist.songs, 1):
        print(f"   {i}. {song.title} ({song.year})")
    
    song_title = input("\nJudul Lagu yang akan dihapus: ").strip()
    
    # Konfirmasi
    confirm = input(f"Hapus '{song_title}' dari {artist_name}? (yes/no): ").lower()
    if confirm != 'yes':
        print("Penghapusan dibatalkan.")
        # return None -> dikembalikan ke menu_admin()
        # User membatalkan penghapusan
        return
    
    # Hapus lagu dan cascade ke user playlists
    if delete_song_from_artist(artist_name, song_title):
        print(f"Lagu '{song_title}' berhasil dihapus!")
        print(f"   Sisa lagu {artist_name}: {artist.song_count()}")
    else:
        print(f"Lagu '{song_title}' tidak ditemukan!")


# ========================================
# FITUR 6: VIEW TOP ARTIST
# ========================================

def admin_view_top_artists():
    """
    Menampilkan artis dengan jumlah lagu terbanyak
    """
    print("\n--- TOP ARTIS (BERDASARKAN JUMLAH LAGU) ---\n")
    
    if not artists_list:
        print("(Belum ada artis)")
        # return None -> dikembalikan ke menu_admin()
        # Tidak ada data untuk ditampilkan
        return
    
    # Dapatkan top artis (sorted by song count)
    top_artists = get_top_artists(limit=10)
    
    for i, (artist, song_count) in enumerate(top_artists, 1):
        verified_badge = "[V]" if artist.verified else ""
        print(f"{i}. {artist.name} {verified_badge}")
        print(f"   Jumlah Lagu: {song_count}")
        print(f"   Genre: {artist.genre}")
        print(f"   Total Plays: {artist.total_plays()}")
        print()


# ========================================
# FITUR 7: SEARCH LAGU
# ========================================

def admin_search_song():
    """
    Mencari lagu berdasarkan judul (Sequential Search)
    Menampilkan info lagu dan artisnya
    """
    print("\n--- CARI LAGU ---")
    
    keyword = input("Masukkan judul lagu (atau sebagian): ").strip()
    if not keyword:
        print("Keyword tidak boleh kosong!")
        # return None -> dikembalikan ke menu_admin()
        # Input tidak valid, kembali ke menu
        return
    
    # Cari lagu (Sequential Search di semua artis)
    results = search_song(keyword)
    
    if not results:
        print(f"Tidak ada lagu yang cocok dengan '{keyword}'")
        # return None -> dikembalikan ke menu_admin()
        # Pencarian tidak menemukan hasil
        return
    
    print(f"\nDitemukan {len(results)} lagu:\n")
    for i, (artist, song) in enumerate(results, 1):
        minutes = song.duration // 60
        seconds = song.duration % 60
        print(f"{i}. {song.title}")
        print(f"   Artis: {artist.name}")
        print(f"   Tahun: {song.year}")
        print(f"   Durasi: {minutes}:{seconds:02d}")
        print(f"   Play Count: {song.play_count}")
        print()


# ========================================
# FITUR 8: ADD ADMIN
# ========================================

def admin_add_new_admin():
    """
    Menambahkan admin baru ke sistem
    Hanya admin yang sudah login yang bisa menambah admin baru
    """
    print("\n--- TAMBAH ADMIN BARU ---")
    
    username = input("Username Admin Baru: ").strip()
    if not username:
        print("Username tidak boleh kosong!")
        # return None -> dikembalikan ke menu_admin()
        # Input tidak valid
        return
    
    # Cek apakah username sudah ada
    if any(a.username == username for a in admins_list):
        print(f"Username '{username}' sudah digunakan!")
        # return None -> dikembalikan ke menu_admin()
        # Username duplikat, batalkan
        return
    
    password = input("Password: ").strip()
    if not password:
        print("Password tidak boleh kosong!")
        # return None -> dikembalikan ke menu_admin()
        # Password wajib diisi untuk admin
        return
    
    # Tambah admin baru
    if add_admin(username, password):
        print(f"Admin '{username}' berhasil ditambahkan!")
        print(f"   Total admin: {len(admins_list)}")
    else:
        print("Gagal menambahkan admin!")


# ========================================
# FITUR 9: VIEW ANALYTICS
# ========================================

def admin_view_analytics():
    """
    Menampilkan analisis data:
    - Trending Song (lagu dengan play count tertinggi)
    - Top User (user dengan playlist terbanyak)
    """
    clear_screen()
    print_header("ANALISIS DATA")
    
    # === TRENDING SONGS ===
    print("TRENDING SONGS (Play Count Tertinggi)\n")
    trending = get_trending_songs(limit=5)
    
    if not trending:
        print("   (Belum ada data)")
    else:
        for i, (song, artist) in enumerate(trending, 1):
            print(f"{i}. {song.title} - {artist.name}")
            print(f"   Play Count: {song.play_count}")
            print()
    
    print("-" * 70)
    
    # === TOP USERS ===
    print("\nTOP USERS (Playlist Terbanyak)\n")
    top_users = get_top_users(limit=5)
    
    if not top_users:
        print("   (Belum ada user)")
    else:
        for i, (user, playlist_count) in enumerate(top_users, 1):
            print(f"{i}. {user.username}")
            print(f"   Playlist: {user.playlist_name}")
            print(f"   Jumlah Lagu: {playlist_count}")
            print()


# ========================================
# MENU UTAMA ADMIN
# ========================================

def menu_admin():
    """
    Menu dashboard admin dengan semua fitur
    """
    while True:
        clear_screen()
        print_header("ADMIN DASHBOARD - MUSIC MANAGEMENT")
        
        print("MANAJEMEN ARTIS & LAGU:")
        print("  1. Tambah Artis Baru (Insert Last)")
        print("  2. Tambah Lagu ke Artis (Insert Child)")
        print("  3. Lihat Semua Musik (View Nested)")
        print("  4. Hapus Artis (Delete Parent & Cascade)")
        print("  5. Hapus Lagu Tertentu (Delete Child)")
        print()
        print("INFORMASI & ANALISIS:")
        print("  6. Lihat Artis Terpopuler")
        print("  7. Cari Lagu")
        print("  8. Analisis Data (Trending & Top User)")
        print()
        print("PENGATURAN:")
        print("  9. Tambah Admin Baru")
        print("  0. Logout")
        print("-" * 70)
        
        pilihan = input(">> Pilih menu (0-9): ").strip()
        
        if pilihan == '1':
            admin_add_artist() 
            pause() #tunggu user tekan enter sebelum kembali ke menu admin
        
        elif pilihan == '2':
            admin_add_song()
            pause()
        
        elif pilihan == '3':
            admin_view_all_music()
            pause()
        
        elif pilihan == '4':
            admin_delete_artist()
            pause()
        
        elif pilihan == '5':
            admin_delete_song()
            pause()
        
        elif pilihan == '6':
            admin_view_top_artists()
            pause()
        
        elif pilihan == '7':
            admin_search_song()
            pause()
        
        elif pilihan == '8':
            admin_view_analytics()
            pause()
        
        elif pilihan == '9':
            admin_add_new_admin()
            pause()
        
        elif pilihan == '0':
            print("\nLogout dari Admin Dashboard...")
            time.sleep(1)
            break
        
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)
