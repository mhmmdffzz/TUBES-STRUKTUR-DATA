import os
import time
# --- PENTING: MENGAMBIL DATA DARI FOLDER DATABASE ---
from database.data_store import users_list, artists_list
from database.models import User

# --- FUNGSI BANTUAN (Lokal di file ini) ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    width = 60
    print("=" * width)
    print(title.center(width))
    print("=" * width)

# ==========================================
# LOGIKA FITUR USER
# ==========================================

def user_add_song_logic(current_user):
    print("\n--- 🔍 CARI & TAMBAH LAGU ---")
    artist_name = input("Masukkan Nama Artis: ")
    
    # 1. Cari Artisnya dulu di List Global
    found_artist = None
    for artist in artists_list:
        if artist.name.lower() == artist_name.lower():
            found_artist = artist
            break
    
    if not found_artist:
        print(f"❌ Artis '{artist_name}' tidak ditemukan.")
        return

    # 2. Tampilkan lagu milik artis tersebut
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
        # (Kita cek apakah OBJEK lagu itu sudah ada di list user)
        if found_song in current_user.playlist:
            print(f"⚠ Lagu '{found_song.title}' sudah ada di playlistmu!")
        else:
            # --- INI INTI MLL ---
            # Kita memasukkan OBJEK yang sama ke list user (Pointer/Reference)
            current_user.playlist.append(found_song)
            print(f"✅ Berhasil! '{found_song.title}' masuk ke playlist.")
    else:
        print(f"❌ Lagu '{song_title}' tidak ditemukan pada artis {found_artist.name}.")

def user_play_logic(current_user):
    print("\n--- ▶ PUTAR LAGU ---")
    try:
        idx = int(input("Masukkan Nomor Urut (Indeks) Lagu: "))
        # Validasi indeks
        if 0 <= idx < len(current_user.playlist):
            song = current_user.playlist[idx]
            print(f"🎵 Sedang memutar: {song.title} - {song.artist_name}...")
            time.sleep(2) # Simulasi mendengarkan
            
            # Update Play Count (Karena ini objek yang sama dgn Artis, play count artis jg nambah)
            song.play_count += 1 
            print(f"   (Total diputar global: {song.play_count} kali)")
        else:
            print("❌ Lagu tidak ditemukan di nomor itu.")
    except ValueError:
        print("❌ Input harus angka.")

def user_swap_logic(current_user):
    print("\n--- ⇄ ATUR URUTAN LAGU ---")
    # Tampilkan indeks
    for i, song in enumerate(current_user.playlist):
        print(f"[{i}] {song.title}")
    
    try:
        idx1 = int(input("Masukkan Indeks Lagu 1 (Posisi Awal): "))
        idx2 = int(input("Masukkan Indeks Lagu 2 (Posisi Tujuan): "))
        
        limit = len(current_user.playlist)
        if 0 <= idx1 < limit and 0 <= idx2 < limit:
            # Proses SWAP
            current_user.playlist[idx1], current_user.playlist[idx2] = \
            current_user.playlist[idx2], current_user.playlist[idx1]
            print("✅ Urutan berhasil ditukar!")
        else:
            print("❌ Indeks tidak valid.")
    except ValueError:
        print("❌ Masukkan angka saja.")

# ==========================================
# MENU NAVIGASI USER
# ==========================================

def menu_user_dashboard(current_user):
    while True:
        clear_screen()
        print_header(f"🎧 DASHBOARD: {current_user.username}")
        print(f"Playlist: {current_user.playlist_name}")
        print(f"Jumlah Lagu: {len(current_user.playlist)}")
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
            if not current_user.playlist:
                print("Playlist kosong.")
            else:
                user_play_logic(current_user)
            input("\nEnter kembali...")

        elif pilihan == '4':
            if not current_user.playlist:
                print("Playlist kosong.")
            else:
                print("\n🔁 Memutar Playlist...")
                for song in current_user.playlist:
                    print(f"   ▶ Now Playing: {song.title}...")
                    song.play_count += 1
                    time.sleep(1)
                print("⏹ Selesai.")
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
                    removed = current_user.playlist.pop(idx)
                    print(f"🗑 '{removed.title}' dihapus dari playlist (Data artis tetap aman).")
                else:
                    print("❌ Indeks salah.")
            except ValueError:
                print("❌ Input salah.")
            input("\nEnter kembali...")

        elif pilihan == '0':
            break

def menu_user_auth():
    """Menu Login / Register Awal"""
    while True:
        clear_screen()
        print_header("🙋‍♂️ MENU PENGGUNA (PENDENGAR)")
        print("1. Daftar Baru (Create Playlist)")
        print("2. Masuk (Login)")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input(">> Pilih (0-2): ")

        if pilihan == '1':
            nama = input("Masukkan Username Baru: ")
            # Cek unik
            if any(u.username == nama for u in users_list):
                print("❌ Username sudah ada!")
                time.sleep(1)
            elif nama:
                # INSERT FIRST (Sesuai Spek Tugas: Insert di Depan)
                new_user = User(nama)
                users_list.insert(0, new_user) 
                print("✅ Akun berhasil dibuat!")
                time.sleep(1)
                # Langsung masuk dashboard
                menu_user_dashboard(new_user)

        elif pilihan == '2':
            nama = input("Masukkan Username: ")
            # SEARCH USER (Sequential Search)
            found_user = None
            for u in users_list:
                if u.username == nama:
                    found_user = u
                    break
            
            if found_user:
                print(f"✅ Login sukses! Halo {found_user.username}.")
                time.sleep(1)
                menu_user_dashboard(found_user)
            else:
                print("❌ User tidak ditemukan.")
                time.sleep(1)

        elif pilihan == '0':
            break
