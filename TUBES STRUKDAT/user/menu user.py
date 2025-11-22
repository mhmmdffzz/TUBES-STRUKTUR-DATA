import os
import time

# 1. STRUKTUR DATA 

#wadah lagu
class Song:
    def __init__(self, title, year, duration):
        self.title = title
        self.year = year
        self.duration = duration
        self.play_count = 0  # Atribut yang bakal berubah kalau diputar User/nnti kalau lagu nya baru itu nilainya 0 karena blm pernah di putarz
        self.artist_name = "" # Helper biar tau ini lagu siapa

#wadah artis
class Artist:
    #
    def __init__(self, name, genre, verified=False):
        self.name = name
        self.genre = genre
        self.verified = verified
        self.songs = [] # List of Song Objects (Child)

#wadah user
class User:
    def __init__(self, username, playlist_name="My Favorites"):
        self.username = username
        self.playlist_name = playlist_name
        self.playlist = [] # List of Songs (Ref to Artist's songs)

# --- GLOBAL DATA (Database Sementara) ---
artists_list = [] 
users_list = []

# 2. FUNGSI BANTUAN (UTILITIES)

def clear_screen():    #buat bersihin layar/babu kalau program yang kita pakai udh selesai
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    width = 60
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()  # Tambahkan baris kosong setelah header

# 3. LOGIKA FITUR USER

def user_add_song_logic(current_user):
    print("\n--- 🔍 CARI & TAMBAH LAGU ---")
    artist_name = input("Masukkan Nama Artis: ")
    
    # 1. Cari Artisnya dulu
    found_artist = None
    for artist in artists_list:
        if artist.name.lower() == artist_name.lower():
            found_artist = artist
            break
    
    if not found_artist:
        print(f"❌ Artis '{artist_name}' tidak ditemukan.")
        return

    # 2. Tampilkan lagu milik artis tersebut (Biar user gampang milih)
    print(f"\nLagu dari {found_artist.name}:")
    if not found_artist.songs:
        print("   (Belum ada lagu)")
        return
        
    for i, song in enumerate(found_artist.songs, 1):
        print(f"   {i}. {song.title} ({song.year})")

    # 3. User pilih judul lagu
    song_title = input("\nMasukkan Judul Lagu yang mau ditambah: ")
    
    found_song = None
    for song in found_artist.songs:
        if song.title.lower() == song_title.lower():
            found_song = song
            break
            
    if found_song:
        # 4. Validasi: Cek apakah lagu sudah ada di playlist user?
        if found_song in current_user.playlist:
            print(f"⚠ Lagu '{found_song.title}' sudah ada di playlistmu!")
        else:
            # --- INI INTI MLL ---
            # Kita memasukkan OBJEK lagu yang sama ke list user
            current_user.playlist.append(found_song)
            print(f"✅ Berhasil! '{found_song.title}' masuk ke playlist.")
    else:
        print(f"❌ Lagu '{song_title}' tidak ditemukan pada artis {found_artist.name}.")

def user_play_all_logic(current_user):
    if not current_user.playlist:
        print("Playlist kosong.")
        return

    print(f"\n🔁 Memutar Playlist: {current_user.playlist_name}")
    for i, song in enumerate(current_user.playlist, 1):
        print(f"   ▶ Now Playing: {song.title} - {song.artist_name}...")
        song.play_count += 1 # Update data global
        time.sleep(1) # Simulasi durasi singkat
    print("\n⏹ Seluruh playlist selesai diputar.")

def user_swap_logic(current_user):
    print("\n--- ⇄ ATUR URUTAN LAGU ---")
    # Tampilkan dulu indexnya biar user tau
    for i, song in enumerate(current_user.playlist):
        print(f"[{i}] {song.title}")
    
    try:
        idx1 = int(input("Masukkan Indeks Lagu 1 (Posisi Awal): "))
        idx2 = int(input("Masukkan Indeks Lagu 2 (Posisi Tujuan): "))
        
        # Cek validitas indeks
        limit = len(current_user.playlist)
        if 0 <= idx1 < limit and 0 <= idx2 < limit:
            # Proses SWAP di Python (Simpel banget)
            current_user.playlist[idx1], current_user.playlist[idx2] = \
            current_user.playlist[idx2], current_user.playlist[idx1]
            print("✅ Urutan berhasil ditukar!")
        else:
            print("❌ Indeks tidak valid (di luar jangkauan).")
    except ValueError:
        print("❌ Masukkan angka saja.")

# ==========================================
# 4. MENU NAVIGASI USER
# ==========================================

def menu_user_dashboard(current_user):
    while True:
        clear_screen()
        print_header(f"🎧 DASHBOARD: {current_user.username}")
        print(f"Playlist: {current_user.playlist_name} | Total: {len(current_user.playlist)} Lagu")
        print("-" * 60)
        
        print("1. ➕ Tambah Lagu (Cari Artis -> Add)")
        print("2. 📜 Lihat Playlist Saya")
        print("3. ▶  Putar Lagu Tertentu")
        print("4. 🔁 Putar Semua (Loop)")
        print("5. ⇄  Tukar Urutan (Swap)")
        print("6. ❌ Hapus Lagu dari Playlist")
        print("0. 🔙 Logout")
        
        pilihan = input("\n>> Pilih menu (0-6): ")

        if pilihan == '1':
            user_add_song_logic(current_user)
            input("\nEnter kembali...")

        elif pilihan == '2':
            print(f"\n📜 Isi Playlist {current_user.username}:")
            if not current_user.playlist:
                print("(Kosong)")
            else:
                for i, song in enumerate(current_user.playlist):
                    print(f"   {i}. {song.title} - {song.artist_name} [{song.play_count} plays]")
            input("\nEnter kembali...")

        elif pilihan == '3':
            print("\n--- ▶ PUTAR LAGU ---")
            try:
                idx = int(input("Masukkan Nomor Urut (Indeks) Lagu: "))
                if 0 <= idx < len(current_user.playlist):
                    song = current_user.playlist[idx]
                    print(f"🎵 Sedang memutar: {song.title}...")
                    song.play_count += 1 # Update play count
                    print(f"   (Total diputar global: {song.play_count} kali)")
                else:
                    print("❌ Lagu tidak ditemukan.")
            except ValueError:
                print("❌ Input harus angka.")
            input("\nEnter kembali...")

        elif pilihan == '4':
            user_play_all_logic(current_user)
            input("\nEnter kembali...")

        elif pilihan == '5':
            if len(current_user.playlist) < 2:
                print("❌ Butuh minimal 2 lagu untuk tukar posisi.")
            else:
                user_swap_logic(current_user)
            input("\nEnter kembali...")

        elif pilihan == '6':
            print("\n--- HAPUS LAGU DARI PLAYLIST ---")
            try:
                idx = int(input("Masukkan Indeks Lagu yang mau dihapus: "))
                if 0 <= idx < len(current_user.playlist):
                    removed = current_user.playlist.pop(idx) # Hapus dari list user saja
                    print(f"🗑 '{removed.title}' dihapus dari playlist (Data artis tetap aman).")
                else:
                    print("❌ Indeks salah.")
            except:
                print("❌ Input salah.")
            input("\nEnter kembali...")

        elif pilihan == '0':
            break

def menu_user_auth():
    while True:
        clear_screen()
        print_header("🙋‍♂️ LOGIN / SIGN UP PENDENGAR")
        print("1. Daftar Baru (Create Playlist)")
        print("2. Masuk (Login)")
        print("0. Kembali")
        
        pilihan = input(">> Pilih (0-2): ")

        if pilihan == '1':
            nama = input("Masukkan Username Baru: ")
            # Cek unik
            if any(u.username == nama for u in users_list):
                print("❌ Username sudah ada!")
                time.sleep(1)
            elif nama:
                # INSERT FIRST (Sesuai Spek)
                new_user = User(nama)
                users_list.insert(0, new_user) 
                print("✅ Akun berhasil dibuat!")
                time.sleep(1)
                menu_user_dashboard(new_user)

        elif pilihan == '2':
            nama = input("Masukkan Username: ")
            # SEARCH USER
            found = next((u for u in users_list if u.username == nama), None)
            if found:
                menu_user_dashboard(found)
            else:
                print("❌ User tidak ditemukan.")
                time.sleep(1)

        elif pilihan == '0':
            break

# --- TESTING ---
if __name__ == "__main__":
    # Kita butuh Data Dummy Artis biar user bisa nambah lagu
    # Karena Admin belum dibuat, kita suntik manual dulu datanya
    
    # 1. Buat Artis
    a1 = Artist("Tulus", "Pop")
    a1.songs.append(Song("Hati-Hati di Jalan", 2022, 240))
    a1.songs[0].artist_name = "Tulus" # Helper
    
    a2 = Artist("Coldplay", "Rock")
    a2.songs.append(Song("Yellow", 2000, 260))
    a2.songs[0].artist_name = "Coldplay"

    artists_list.append(a1)
    artists_list.append(a2)

    # Jalankan Menu User
    menu_user_auth()
