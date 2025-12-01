# ========================================
# MENU USER - Manajemen Playlist Pribadi
# ========================================
# File ini berisi semua fitur untuk user:
# 1. Register (Create Playlist) - INSERT FIRST
# 2. Login
# 3. Add Song to Playlist (dengan validasi)
# 4. Play Song (update play count)
# 5. Remove Song
# 6. View My Playlist
# 7. Move Song Order (Swap)
# 8. Play All (Loop)

import os
import time
from database.data_store import artists_list, users_list, add_user, get_user
from database.models import User

# ========================================
# FUNGSI UTILITY
# ========================================

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J", end="")  # ANSI escape code backup

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
# FITUR 1: ADD SONG TO PLAYLIST
# ========================================

def user_add_song(current_user):
    """
    Menambahkan lagu ke playlist user (MLL - Memory Linked List)
    User mencari lagu dari database artis, lalu menambahkan REFERENSI ke playlist
    Validasi: Lagu tidak boleh duplikat di playlist
    """
    print("\n--- TAMBAH LAGU KE PLAYLIST ---")
    
    if not artists_list:
        print("Belum ada artis di database!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Flow: return -> pause() -> while True (loop menu user)
        return
    
    # STEP 1: Tampilkan daftar artis
    print("\nDaftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        verified_badge = "[V]" if artist.verified else ""
        print(f"   {i}. {artist.name} {verified_badge} - {artist.song_count()} lagu")
    
    # STEP 2: Pilih artis (Sequential Search)
    artist_name = input("\nNama Artis: ").strip()
    found_artist = None
    
    for artist in artists_list:
        if artist.name.lower() == artist_name.lower():
            found_artist = artist
            break
    
    if not found_artist:
        print(f"Artis '{artist_name}' tidak ditemukan!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Sequential search gagal menemukan artis
        return
    
    # STEP 3: Tampilkan lagu-lagu artis
    if not found_artist.songs:
        print(f"Artis '{found_artist.name}' belum memiliki lagu!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Artis ada tapi belum punya lagu
        return
    
    print(f"\nLagu dari {found_artist.name}:")
    for i, song in enumerate(found_artist.songs, 1):
        minutes = song.duration // 60
        seconds = song.duration % 60
        print(f"   {i}. {song.title} ({song.year}) - {minutes}:{seconds:02d}")
    
    # STEP 4: Pilih lagu (Sequential Search)
    song_title = input("\nJudul Lagu yang mau ditambah: ").strip()
    found_song = None
    
    for song in found_artist.songs:
        if song.title.lower() == song_title.lower():
            found_song = song
            break
    
    if not found_song:
        print(f"Lagu '{song_title}' tidak ditemukan!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Lagu tidak ada di list artis
        return
    
    # STEP 5: Validasi duplikasi
    if found_song in current_user.playlist:
        print(f"Lagu '{found_song.title}' sudah ada di playlist Anda!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Validasi duplikasi: lagu sudah ada di playlist user
        return
    
    # STEP 6: Tambahkan REFERENSI lagu ke playlist (MLL)
    # Bukan copy, tapi pointer/referensi ke objek yang sama
    current_user.playlist.append(found_song)
    print(f"'{found_song.title}' berhasil ditambahkan ke playlist!")
    print(f"   Total lagu di playlist: {current_user.playlist_count()}")


# ========================================
# FITUR 2: PLAY SONG
# ========================================

def user_play_song(current_user):
    """
    Memutar lagu tertentu dari playlist
    Update play_count lagu (karena MLL, data global juga terupdate)
    """
    print("\n--- PUTAR LAGU ---")
    
    if not current_user.playlist:
        print("Playlist Anda masih kosong!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Tidak ada lagu yang bisa diputar
        return
    
    # Tampilkan playlist dengan indeks
    print(f"\n{current_user.playlist_name}:")
    for i, song in enumerate(current_user.playlist):
        print(f"   [{i}] {song.title} - {song.artist_name}")
    
    try:
        idx = int(input("\nMasukkan nomor lagu [0-{}]: ".format(len(current_user.playlist)-1)))
        
        # Validasi indeks
        if 0 <= idx < len(current_user.playlist):
            song = current_user.playlist[idx]
            
            # Simulasi pemutaran
            minutes = song.duration // 60
            seconds = song.duration % 60
            print(f"\nNow Playing: {song.title} - {song.artist_name}")
            print(f"   Durasi: {minutes}:{seconds:02d}")
            print(f"   ... memutar lagu ...")
            time.sleep(2)
            
            # === UPDATE PLAY COUNT ===
            # Karena ini referensi ke objek yang sama (MLL),
            # play_count di database global artis juga ikut terupdate!
            song.play_count += 1
            
            print(f"Selesai diputar!")
            print(f"   Total diputar: {song.play_count} kali")
        else:
            print("Nomor tidak valid!")
    
    except ValueError:
        print("Input harus berupa angka!")


# ========================================
# FITUR 3: REMOVE SONG
# ========================================

def user_remove_song(current_user):
    """
    Menghapus lagu dari playlist pribadi
    PENTING: Hanya menghapus dari playlist user, tidak menghapus dari database artis
    """
    print("\n--- HAPUS LAGU DARI PLAYLIST ---")
    
    if not current_user.playlist:
        print("Playlist Anda masih kosong!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Tidak ada lagu yang bisa dihapus
        return
    
    # Tampilkan playlist
    print(f"\n{current_user.playlist_name}:")
    for i, song in enumerate(current_user.playlist):
        print(f"   [{i}] {song.title} - {song.artist_name}")
    
    try:
        idx = int(input("\nMasukkan nomor lagu yang akan dihapus [0-{}]: ".format(len(current_user.playlist)-1)))
        
        # Validasi indeks
        if 0 <= idx < len(current_user.playlist):
            # pop() menghapus dan mengembalikan elemen
            removed_song = current_user.playlist.pop(idx)
            print(f"'{removed_song.title}' dihapus dari playlist!")
            print(f"   (Data lagu di database artis tetap aman)")
            print(f"   Sisa lagu di playlist: {current_user.playlist_count()}")
        else:
            print("Nomor tidak valid!")
    
    except ValueError:
        print("Input harus berupa angka!")


# ========================================
# FITUR 4: VIEW MY PLAYLIST
# ========================================

def user_view_playlist(current_user):
    """
    Menampilkan semua lagu dalam playlist user secara terurut
    """
    print(f"\n--- {current_user.playlist_name.upper()} ---\n")
    
    if not current_user.playlist:
        print("(Playlist masih kosong)")
        print("\nTip: Gunakan menu 'Tambah Lagu' untuk menambahkan lagu!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Playlist kosong, tampilkan tips lalu kembali
        return
    
    print(f"Total: {current_user.playlist_count()} lagu\n")
    
    # Tampilkan detail setiap lagu
    for i, song in enumerate(current_user.playlist):
        minutes = song.duration // 60
        seconds = song.duration % 60
        print(f"   [{i}] {song.title}")
        print(f"       Artis: {song.artist_name}")
        print(f"       Tahun: {song.year}")
        print(f"       Durasi: {minutes}:{seconds:02d}")
        print(f"       Play Count: {song.play_count}")
        print()


# ========================================
# FITUR 5: MOVE SONG ORDER (SWAP)
# ========================================

def user_swap_songs(current_user):
    """
    Menukar posisi 2 lagu dalam playlist
    Menggunakan teknik swap dengan tuple unpacking
    """
    print("\n--- ATUR URUTAN LAGU ---")
    
    if len(current_user.playlist) < 2:
        print("Butuh minimal 2 lagu untuk swap posisi!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Swap butuh minimal 2 elemen
        return
    
    # Tampilkan playlist dengan indeks
    print(f"\n{current_user.playlist_name}:")
    for i, song in enumerate(current_user.playlist):
        print(f"   [{i}] {song.title}")
    
    try:
        idx1 = int(input("\nPosisi lagu pertama [0-{}]: ".format(len(current_user.playlist)-1)))
        idx2 = int(input("Posisi lagu kedua [0-{}]: ".format(len(current_user.playlist)-1)))
        
        # Validasi indeks
        if 0 <= idx1 < len(current_user.playlist) and 0 <= idx2 < len(current_user.playlist):
            # === SWAP menggunakan Python Tuple Unpacking ===
            # Menukar posisi 2 elemen dalam list secara simultan
            current_user.playlist[idx1], current_user.playlist[idx2] = \
                current_user.playlist[idx2], current_user.playlist[idx1]
            
            print(f"Posisi berhasil ditukar!")
            print(f"   [{idx1}] sekarang: {current_user.playlist[idx1].title}")
            print(f"   [{idx2}] sekarang: {current_user.playlist[idx2].title}")
        else:
            print("Nomor tidak valid!")
    
    except ValueError:
        print("Input harus berupa angka!")


# ========================================
# FITUR 6: PLAY ALL (LOOP)
# ========================================

def user_play_all(current_user):
    """
    Memutar semua lagu dalam playlist secara berurutan (Loop)
    Setiap lagu yang diputar, play_count-nya bertambah
    """
    print("\n--- PUTAR SEMUA LAGU ---")
    
    if not current_user.playlist:
        print("Playlist masih kosong!")
        # return None -> dikembalikan ke menu_user_dashboard()
        # Tidak ada lagu yang bisa diputar
        return
    
    print(f"\nMemutar {current_user.playlist_count()} lagu dari {current_user.playlist_name}...\n")
    
    # Loop semua lagu dalam playlist
    for i, song in enumerate(current_user.playlist, 1):
        minutes = song.duration // 60
        seconds = song.duration % 60
        
        print(f"[{i}/{current_user.playlist_count()}] > {song.title} - {song.artist_name} ({minutes}:{seconds:02d})")
        
        # Simulasi pemutaran
        time.sleep(1)
        
        # Update play count (MLL - data global terupdate)
        song.play_count += 1
    
    print(f"\nSelesai! Semua lagu telah diputar.")


# ========================================
# MENU USER DASHBOARD
# ========================================

def menu_user_dashboard(current_user):
    """
    Dashboard user setelah login
    Berisi semua fitur manajemen playlist
    """
    while True:
        clear_screen()
        print_header(f"{current_user.username.upper()}'S MUSIC PLAYER")
        
        print(f"Playlist: {current_user.playlist_name}")
        print(f"Jumlah Lagu: {current_user.playlist_count()}")
        print("-" * 70)
        
        print("\nMANAJEMEN PLAYLIST:")
        print("  1. Tambah Lagu ke Playlist")
        print("  2. Lihat Playlist Saya")
        print("  3. Putar Lagu Tertentu")
        print("  4. Putar Semua Lagu (Loop)")
        print("  5. Atur Urutan Lagu (Swap)")
        print("  6. Hapus Lagu dari Playlist")
        print()
        print("  0. Logout")
        print("-" * 70)
        
        pilihan = input(">> Pilih menu (0-6): ").strip()
        
        if pilihan == '1':
            user_add_song(current_user)
            pause()
        
        elif pilihan == '2':
            user_view_playlist(current_user)
            pause()
        
        elif pilihan == '3':
            user_play_song(current_user)
            pause()
        
        elif pilihan == '4':
            user_play_all(current_user)
            pause()
        
        elif pilihan == '5':
            user_swap_songs(current_user)
            pause()
        
        elif pilihan == '6':
            user_remove_song(current_user)
            pause()
        
        elif pilihan == '0':
            print(f"\nLogout dari {current_user.username}...")
            time.sleep(1)
            break
        
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)


# ========================================
# MENU LOGIN & REGISTER
# ========================================

def menu_user_auth():
    """
    Menu autentikasi user: Register & Login
    Register menggunakan INSERT FIRST (user baru di posisi 0)
    """
    while True:
        clear_screen()
        print_header("USER - MUSIC STREAMING")
        
        print("1. DAFTAR BARU (Register)")
        print("2. MASUK (Login)")
        print("0. Kembali ke Menu Utama")
        print("-" * 70)
        
        pilihan = input(">> Pilih (0-2): ").strip()
        
        # === REGISTER (INSERT FIRST) ===
        if pilihan == '1':
            print("\n--- REGISTRASI USER BARU ---")
            
            username = input("Username: ").strip()
            if not username:
                print("Username tidak boleh kosong!")
                time.sleep(1)
                continue
            
            # Cek apakah username sudah ada (validasi unik)
            if get_user(username):
                print(f"Username '{username}' sudah digunakan!")
                time.sleep(1)
                continue
            
            password = input("Password (kosongkan jika tidak ingin password): ").strip()
            
            # Tambah user baru (INSERT FIRST - posisi 0)
            new_user = add_user(username, password)
            
            if new_user:
                print(f"\nAkun berhasil dibuat!")
                print(f"   Username: {username}")
                print(f"   Playlist: {new_user.playlist_name}")
                time.sleep(2)
                
                # Langsung masuk ke dashboard
                menu_user_dashboard(new_user)
            else:
                print("Gagal membuat akun!")
                time.sleep(1)
        
        # === LOGIN ===
        elif pilihan == '2':
            print("\n--- LOGIN USER ---")
            
            username = input("Username: ").strip()
            
            # Cari user (Sequential Search)
            found_user = get_user(username)
            
            if not found_user:
                print(f"User '{username}' tidak ditemukan!")
                time.sleep(1)
                continue
            
            # Cek password jika user punya password
            if found_user.password:
                password = input("Password: ").strip()
                if password != found_user.password:
                    print("Password salah!")
                    time.sleep(1)
                    continue
            
            # Login berhasil
            print(f"\nLogin berhasil! Selamat datang, {found_user.username}!")
            time.sleep(1)
            
            # Masuk ke dashboard
            menu_user_dashboard(found_user)
        
        # === KEMBALI ===
        elif pilihan == '0':
            break
        
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)
