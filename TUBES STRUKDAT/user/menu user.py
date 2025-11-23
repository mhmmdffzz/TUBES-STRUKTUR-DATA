import os  # Untuk operasi sistem seperti clear screen
import time  # Untuk delay/simulasi

# Import data global dari database
from database.data_store import users_list, artists_list  # List global artis & user
from database.models import User  # Class untuk membuat objek User

def clear_screen():
    """Membersihkan layar terminal (cls untuk Windows, clear untuk Linux/Mac)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Cetak judul dengan border yang rapi"""
    width = 60
    print("=" * width)  # Border atas
    print(title.center(width))  # Teks di tengah
    print("=" * width)  # Border bawah
    print()  # Baris kosong

# === LOGIKA FITUR USER ===

def user_add_song_logic(current_user):
    """Fitur mencari dan menambahkan lagu ke playlist user"""
    print("\n--- 🔍 CARI & TAMBAH LAGU ---")
    artist_name = input("Masukkan Nama Artis: ")
    
    # STEP 1: Cari artis di database (Sequential Search)
    found_artist = None  # Inisialisasi variabel pencarian
    for artist in artists_list:  # Loop semua artis
        if artist.name.lower() == artist_name.lower():  # Bandingkan nama (case-insensitive)
            found_artist = artist  # Artis ditemukan
            break  # Keluar dari loop
    
    # Validasi: Artis tidak ditemukan
    if not found_artist:
        print(f"❌ Artis '{artist_name}' tidak ditemukan.")
        return  # Keluar dari fungsi

    # STEP 2: Tampilkan semua lagu dari artis tersebut
    print(f"\nLagu dari {found_artist.name}:")
    if not found_artist.songs:  # Cek jika artis belum punya lagu
        print("   (Belum ada lagu)")
        return
    
    # Loop untuk menampilkan list lagu dengan nomor urut
    for i, song in enumerate(found_artist.songs, 1):  # enumerate mulai dari 1
        print(f"   {i}. {song.title} ({song.year})")

    # STEP 3: User memilih lagu yang mau ditambahkan
    song_title = input("\nMasukkan Judul Lagu yang mau ditambah: ")
    
    # Cari lagu berdasarkan judul (Sequential Search)
    found_song = None
    for song in found_artist.songs:  # Loop semua lagu artis
        if song.title.lower() == song_title.lower():  # Bandingkan judul (case-insensitive)
            found_song = song  # Lagu ditemukan
            break  # Keluar dari loop
            
    # STEP 4: Validasi dan tambahkan ke playlist
    if found_song:
        # Cek duplikasi: Apakah lagu sudah ada di playlist user?
        if found_song in current_user.playlist:  # Python cek referensi objek
            print(f"⚠ Lagu '{found_song.title}' sudah ada di playlistmu!")
        else:
            # === KONSEP MLL (Memory Linked List) ===
            # Menambahkan REFERENSI/POINTER objek lagu yang sama
            # Bukan copy baru, tapi objek yang sama dengan di artists_list
            # Jadi kalau play_count berubah, data global artis juga ikut berubah!
            current_user.playlist.append(found_song)
            print(f"✅ Berhasil! '{found_song.title}' masuk ke playlist.")
    else:
        print(f"❌ Lagu '{song_title}' tidak ditemukan pada artis {found_artist.name}.")

def user_play_logic(current_user):
    """Fitur memutar lagu tertentu berdasarkan indeks"""
    print("\n--- ▶ PUTAR LAGU ---")
    try:
        # Input indeks dari user (convert string ke integer)
        idx = int(input("Masukkan Nomor Urut (Indeks) Lagu: "))
        
        # Validasi: Cek apakah indeks valid (0 sampai panjang playlist - 1)
        if 0 <= idx < len(current_user.playlist):
            song = current_user.playlist[idx]  # Ambil objek lagu dari playlist
            print(f"🎵 Sedang memutar: {song.title} - {song.artist_name}...")
            time.sleep(2)  # Simulasi durasi mendengarkan (2 detik)
            
            # Update play count
            # Karena ini referensi ke objek yang sama dengan di artists_list,
            # maka data global artis juga otomatis terupdate!
            song.play_count += 1 
            print(f"   (Total diputar global: {song.play_count} kali)")
        else:
            print("❌ Lagu tidak ditemukan di nomor itu.")
    except ValueError:  # Error handling jika input bukan angka
        print("❌ Input harus angka.")

def user_swap_logic(current_user):
    """Fitur menukar posisi 2 lagu dalam playlist"""
    print("\n--- ⇄ ATUR URUTAN LAGU ---")
    
    # Tampilkan semua lagu dengan indeksnya
    for i, song in enumerate(current_user.playlist):  # enumerate untuk dapatkan index
        print(f"[{i}] {song.title}")
    
    try:
        # Input 2 indeks yang mau ditukar
        idx1 = int(input("Masukkan Indeks Lagu 1 (Posisi Awal): "))
        idx2 = int(input("Masukkan Indeks Lagu 2 (Posisi Tujuan): "))
        
        limit = len(current_user.playlist)  # Batas maksimal indeks
        
        # Validasi: Kedua indeks harus dalam range yang valid
        if 0 <= idx1 < limit and 0 <= idx2 < limit:
            # === SWAP dengan Python Tuple Unpacking ===
            # Menukar posisi 2 elemen dalam list secara simultan
            current_user.playlist[idx1], current_user.playlist[idx2] = \
            current_user.playlist[idx2], current_user.playlist[idx1]
            print("✅ Urutan berhasil ditukar!")
        else:
            print("❌ Indeks tidak valid.")
    except ValueError:  # Error handling untuk input non-numerik
        print("❌ Masukkan angka saja.")


# === MENU NAVIGASI ===

def menu_user_dashboard(current_user):
    """Dashboard utama user setelah login - Menu CRUD playlist"""
    while True:  # Loop menu sampai user logout
        clear_screen()  # Bersihkan layar
        
        # Header dengan info user
        print_header(f"🎧 DASHBOARD: {current_user.username}")
        print(f"Playlist: {current_user.playlist_name}")
        print(f"Jumlah Lagu: {len(current_user.playlist)}")
        print("-" * 60)
        
        # Tampilkan menu opsi
        print("1. ➕ Tambah Lagu (Cari Artis -> Add)")
        print("2. 📜 Lihat Playlist Saya")
        print("3. ▶  Putar Lagu Tertentu")
        print("4. 🔁 Putar Semua (Loop)")
        print("5. ⇄  Tukar Urutan (Swap)")
        print("6. ❌ Hapus Lagu dari Playlist")
        print("0. 🔙 Logout")
        
        pilihan = input("\n>> Pilih menu (0-6): ")

        # MENU 1: Tambah Lagu
        if pilihan == '1':
            user_add_song_logic(current_user)  # Panggil fungsi tambah lagu
            input("\nEnter kembali...")  # Pause sebelum kembali ke menu

        # MENU 2: Lihat Playlist
        elif pilihan == '2':
            print(f"\n📜 Isi Playlist {current_user.username}:")
            if not current_user.playlist:  # Cek jika playlist kosong
                print("(Kosong)")
            else:
                # Tampilkan semua lagu dengan detail
                for i, song in enumerate(current_user.playlist):
                    print(f"   {i}. {song.title} - {song.artist_name} [{song.play_count} plays]")
            input("\nEnter kembali...")

        # MENU 3: Putar Lagu Tertentu
        elif pilihan == '3':
            if not current_user.playlist:  # Validasi playlist tidak kosong
                print("Playlist kosong.")
            else:
                user_play_logic(current_user)  # Panggil fungsi play
            input("\nEnter kembali...")

        # MENU 4: Putar Semua Lagu (Loop)
        elif pilihan == '4':
            if not current_user.playlist:
                print("Playlist kosong.")
            else:
                print("\n🔁 Memutar Playlist...")
                # Loop semua lagu dalam playlist
                for song in current_user.playlist:
                    print(f"   ▶ Now Playing: {song.title}...")
                    song.play_count += 1  # Update play count tiap lagu
                    time.sleep(1)  # Delay 1 detik per lagu
                print("⏹ Selesai.")
            input("\nEnter kembali...")

        # MENU 5: Swap Urutan Lagu
        elif pilihan == '5':
            # Validasi: Minimal 2 lagu untuk bisa swap
            if len(current_user.playlist) < 2:
                print("❌ Butuh minimal 2 lagu untuk tukar posisi.")
            else:
                user_swap_logic(current_user)  # Panggil fungsi swap
            input("\nEnter kembali...")

        # MENU 6: Hapus Lagu
        elif pilihan == '6':
            print("\n--- HAPUS LAGU DARI PLAYLIST ---")
            try:
                idx = int(input("Masukkan Indeks Lagu yang mau dihapus: "))
                # Validasi indeks
                if 0 <= idx < len(current_user.playlist):
                    # pop(idx) menghapus dan mengembalikan elemen di indeks tersebut
                    removed = current_user.playlist.pop(idx)
                    print(f"🗑 '{removed.title}' dihapus dari playlist (Data artis tetap aman).")
                else:
                    print("❌ Indeks salah.")
            except ValueError:
                print("❌ Input salah.")
            input("\nEnter kembali...")

        # MENU 0: Logout
        elif pilihan == '0':
            break  # Keluar dari loop while, kembali ke menu auth

def menu_user_auth():
    """Menu Login/Register untuk user"""
    while True:  # Loop menu sampai user kembali ke main
        clear_screen()
        print_header("🙋‍♂️ MENU PENGGUNA (PENDENGAR)")
        print("1. Daftar Baru (Create Playlist)")
        print("2. Masuk (Login)")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input(">> Pilih (0-2): ")

        # MENU 1: Register/Daftar Baru
        if pilihan == '1':
            nama = input("Masukkan Username Baru: ")
            
            # Validasi: Cek apakah username sudah ada (harus unik)
            # any() mengembalikan True jika ada minimal 1 yang cocok
            if any(u.username == nama for u in users_list):
                print("❌ Username sudah ada!")
                time.sleep(1)
            elif nama:  # Jika username valid dan belum ada
                # Input password (opsional)
                password = input("Buat Password (kosongkan jika tidak ingin password): ")
                
                # === INSERT FIRST ===
                # Buat objek User baru
                new_user = User(nama, password)
                # Insert di posisi 0 (depan list) - user terbaru di awal
                users_list.insert(0, new_user) 
                print("✅ Akun berhasil dibuat!")
                time.sleep(1)
                # Langsung masuk ke dashboard user
                menu_user_dashboard(new_user)

        # MENU 2: Login
        elif pilihan == '2':
            nama = input("Masukkan Username: ")
            
            # === SEQUENTIAL SEARCH ===
            # Cari user berdasarkan username
            found_user = None  # Inisialisasi hasil pencarian
            for u in users_list:  # Loop semua user
                if u.username == nama:  # Bandingkan username
                    found_user = u  # User ditemukan
                    break  # Keluar dari loop
            
            # Validasi hasil pencarian
            if found_user:
                # Cek apakah user punya password
                if found_user.password:  # Jika password tidak kosong
                    password = input("Masukkan Password: ")
                    # Verifikasi password
                    if password != found_user.password:
                        print("❌ Password salah!")
                        time.sleep(1)
                        continue  # Kembali ke awal loop (menu auth)
                
                # Login berhasil
                print(f"✅ Login sukses! Halo {found_user.username}.")
                time.sleep(1)
                menu_user_dashboard(found_user)  # Masuk ke dashboard
            else:
                print("❌ User tidak ditemukan.")
                time.sleep(1)

        # MENU 0: Kembali ke Menu Utama
        elif pilihan == '0':
            break  # Keluar dari loop, kembali ke main.py
