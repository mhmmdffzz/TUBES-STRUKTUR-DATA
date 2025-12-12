import os
import time
from database.data_store import (
    artists_list,
    add_artist, get_artist, delete_artist, search_artist,
    add_song_to_artist, delete_song_from_artist,
    count_total_songs, get_artist_with_most_songs, get_all_artists_sorted_by_songs
) # Import fungsi dan struktur data dari data_store

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    width = 70
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()

def pause():
    input("\n[Tekan Enter untuk kembali ke menu...]")

def katalog_add_artist():
    print("\n--- TAMBAH ARTIS BARU ---\n")
    
    nama = input("Nama Artis: ").strip()
    if not nama:
        print("Nama artis tidak boleh kosong!")
        return
    
    if get_artist(nama):
        print(f"Artis '{nama}' sudah ada di database!")
        return
    
    genre = input("Genre: ").strip()
    if not genre:
        print("Genre tidak boleh kosong!")
        return
    
    try:
        tahun_debut = int(input("Tahun Debut: "))
    except ValueError:
        print("Tahun debut harus berupa angka!")
        return
    
    if add_artist(nama, genre, tahun_debut):
        print(f"\nArtis '{nama}' berhasil ditambahkan!")
        print(f"   Genre: {genre}")
        print(f"   Tahun Debut: {tahun_debut}")
    else:
        print("Gagal menambahkan artis!")


# ========================================
# FITUR 2: TAMBAH LAGU (INSERT CHILD)
# ========================================

def katalog_add_song():
  
    print("\n--- TAMBAH LAGU KE ARTIS ---\n")
    
    if not artists_list:
        print("Belum ada artis di database! Tambahkan artis terlebih dahulu.")
        return
    
    # Tampilkan daftar artis
    print("Daftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        print(f"   {i}. {artist.nama_artis} ({artist.genre}) - {artist.song_count()} lagu")
    
    # Pilih artis
    nama_artis = input("\nNama Artis: ").strip()
    artist = get_artist(nama_artis)
    
    if not artist:
        print(f"Artis '{nama_artis}' tidak ditemukan!")
        return
    
    # Input judul lagu (Child - tipe dasar String)
    judul_lagu = input("Judul Lagu: ").strip()
    if not judul_lagu:
        print("Judul lagu tidak boleh kosong!")
        return
    
    # Tambah lagu ke artis
    if add_song_to_artist(nama_artis, judul_lagu):
        print(f"\nLagu '{judul_lagu}' berhasil ditambahkan ke artis '{artist.nama_artis}'!")
        print(f"   Total lagu {artist.nama_artis}: {artist.song_count()}")
    else:
        print(f"Gagal menambahkan lagu! (Mungkin lagu sudah ada)")

def katalog_view_all():
 
    print("\n--- KATALOG ALBUM MUSIK LENGKAP ---\n")
    
    if not artists_list:
        print("(Katalog masih kosong)")
        return
    
    for i, artist in enumerate(artists_list, 1):
        print(f"{i}. {artist.nama_artis}")
        print(f"   Genre      : {artist.genre}")
        print(f"   Tahun Debut: {artist.tahun_debut}")
        print(f"   Jumlah Lagu: {artist.song_count()}")
        
        # Loop semua lagu artis (Children) - NESTED LOOP
        if artist.songs:
            print(f"   Daftar Lagu:")
            for j, judul_lagu in enumerate(artist.songs, 1):
                print(f"      {j}. {judul_lagu}")
        else:
            print(f"   (Belum ada lagu)")
        print()

def katalog_delete_song():

    print("\n--- HAPUS LAGU ---\n")
    
    if not artists_list:
        print("Belum ada artis di database!")
        return
    
    # Tampilkan daftar artis
    print("Daftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        print(f"   {i}. {artist.nama_artis} - {artist.song_count()} lagu")
    
    # Pilih artis
    nama_artis = input("\nNama Artis: ").strip()
    artist = get_artist(nama_artis)
    
    if not artist:
        print(f"Artis '{nama_artis}' tidak ditemukan!")
        return
    
    if not artist.songs:
        print(f"Artis '{artist.nama_artis}' belum memiliki lagu!")
        return
    
    # Tampilkan lagu-lagu artis
    print(f"\nLagu dari {artist.nama_artis}:")
    for j, judul_lagu in enumerate(artist.songs, 1):
        print(f"   {j}. {judul_lagu}")
    
    # Pilih lagu yang akan dihapus
    judul_lagu = input("\nJudul Lagu yang akan dihapus: ").strip()
    
    # Konfirmasi
    konfirmasi = input(f"Yakin hapus lagu '{judul_lagu}'? (y/n): ").lower()
    if konfirmasi != 'y':
        print("Batal menghapus.")
        return
    
    # Hapus lagu
    if delete_song_from_artist(nama_artis, judul_lagu):
        print(f"\nLagu '{judul_lagu}' berhasil dihapus dari '{artist.nama_artis}'!")
        print(f"   Sisa lagu: {artist.song_count()}")
    else:
        print(f"Lagu '{judul_lagu}' tidak ditemukan!")

def katalog_delete_artist():
    """
    Menghapus artis beserta semua lagunya (DELETE PARENT & CASCADE)
    """
    print("\n--- HAPUS ARTIS ---\n")
    
    if not artists_list:
        print("Belum ada artis di database!")
        return
    
    # Tampilkan daftar artis
    print("Daftar Artis:")
    for i, artist in enumerate(artists_list, 1):
        print(f"   {i}. {artist.nama_artis} ({artist.genre}) - {artist.song_count()} lagu")
    
    # Pilih artis
    nama_artis = input("\nNama Artis yang akan dihapus: ").strip()
    artist = get_artist(nama_artis)
    
    if not artist:
        print(f"Artis '{nama_artis}' tidak ditemukan!")
        return
    
    # Konfirmasi (karena akan menghapus semua lagu juga)
    print(f"\n PERHATIAN: Menghapus artis '{artist.nama_artis}' juga akan menghapus {artist.song_count()} lagu!")
    konfirmasi = input("Yakin hapus? (y/n): ").lower()
    
    if konfirmasi != 'y':
        print("Batal menghapus.")
        return
    
    # Hapus artis (cascade: lagu ikut terhapus)
    if delete_artist(nama_artis):
        print(f"\nArtis '{nama_artis}' dan semua lagunya berhasil dihapus!")
    else:
        print("Gagal menghapus artis!")

def katalog_search_artist():
    """
    Mencari artis berdasarkan nama (Sequential Search dengan partial match)
    """
    print("\n--- CARI ARTIS ---\n")
    
    keyword = input("Masukkan nama artis: ").strip()
    if not keyword:
        print("Kata kunci tidak boleh kosong!")
        return
    
    # Cari artis
    results = search_artist(keyword)
    
    if not results:
        print(f"\nTidak ditemukan artis dengan kata kunci '{keyword}'")
        return
    
    print(f"\nDitemukan {len(results)} artis:")
    for i, artist in enumerate(results, 1):
        print(f"\n{i}. {artist.nama_artis}")
        print(f"   Genre      : {artist.genre}")
        print(f"   Tahun Debut: {artist.tahun_debut}")
        print(f"   Jumlah Lagu: {artist.song_count()}")
        
        if artist.songs:
            print(f"   Daftar Lagu:")
            for j, judul_lagu in enumerate(artist.songs, 1):
                print(f"      {j}. {judul_lagu}")

def katalog_report():
    """
    Menampilkan laporan pengolahan MLL:
    - COUNTING: Hitung total lagu per artis dan total seluruh lagu
    - MAX: Cari artis dengan lagu paling banyak
    """
    print("\n--- LAPORAN KATALOG MUSIK ---\n")
    
    if not artists_list:
        print("(Katalog masih kosong)")
        return
    
    # === COUNTING: Total lagu seluruh database ===
    total_songs = count_total_songs()
    print(f"📊 STATISTIK KATALOG")
    print(f"   Total Artis: {len(artists_list)}")
    print(f"   Total Lagu : {total_songs}")
    print()
    
    # === COUNTING: Jumlah lagu per artis ===
    print(f"📋 JUMLAH LAGU PER ARTIS:")
    sorted_artists = get_all_artists_sorted_by_songs()
    for i, (artist, count) in enumerate(sorted_artists, 1):
        bar = "█" * count  # Visual bar chart
        print(f"   {i}. {artist.nama_artis}: {count} lagu {bar}")
    print()
    
    # === MAX: Artis dengan lagu terbanyak ===
    max_artist, max_count = get_artist_with_most_songs()
    if max_artist:
        print(f"🏆 ARTIS DENGAN LAGU TERBANYAK:")
        print(f"   {max_artist.nama_artis} dengan {max_count} lagu!")
        print(f"   Genre: {max_artist.genre}")
        print(f"   Tahun Debut: {max_artist.tahun_debut}")
        print(f"   Daftar Lagu:")
        for j, judul_lagu in enumerate(max_artist.songs, 1):
            print(f"      {j}. {judul_lagu}")

def menu_katalog():
    """
    Menu utama untuk mengelola katalog musik
    """
    while True:
        clear_screen()
        print_header("KATALOG ALBUM MUSIK")
        
        print("Menu Utama:")
        print()
        print("  1. Tambah Artis")
        print("  2. Tambah Lagu ke Artis")
        print("  3. Lihat Semua Data")
        print("  4. Hapus Lagu")
        print("  5. Hapus Artis")
        print("  6. Cari Artis")
        print("  7. Laporan (Counting & Max)")
        print("  0. Kembali ke Menu Utama")
        print()
        print("-" * 70)
        
        pilihan = input(">> Pilih menu (0-7): ").strip()
        
        if pilihan == '1':
            katalog_add_artist()
            pause()
        
        elif pilihan == '2':
            katalog_add_song()
            pause()
        
        elif pilihan == '3':
            katalog_view_all()
            pause()
        
        elif pilihan == '4':
            katalog_delete_song()
            pause()
        
        elif pilihan == '5':
            katalog_delete_artist()
            pause()
        
        elif pilihan == '6':
            katalog_search_artist()
            pause()
        
        elif pilihan == '7':
            katalog_report()
            pause()
        
        elif pilihan == '0':
            break
        
        else:
            print("\nPilihan tidak valid!")
            time.sleep(1)
