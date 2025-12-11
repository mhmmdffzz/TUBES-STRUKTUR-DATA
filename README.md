# ========================================
# MAIN - Entry Point Aplikasi Katalog Album Musik
# ========================================
# File ini adalah controller utama aplikasi
# Mengatur flow: Load DB -> Menu Katalog -> Save DB
#
# Struktur MLL (Multi Linked List) 1-N:
# - PARENT (Artis): Record dengan atribut nama_artis, genre, tahun_debut
# - CHILD (Lagu): Tipe Dasar String (judul lagu saja)
#
# Fitur Utama:
# 1. CRUD Artis (Tambah/Hapus Parent)
# 2. CRUD Lagu (Tambah/Hapus Child)
# 3. Search Artis
# 4. Laporan: Counting (total lagu) & Max (artis dengan lagu terbanyak)

import os
import time
from database.data_store import load_database, save_database
from admin.menu_admin import menu_katalog

# ========================================
# FUNGSI UTILITY
# ========================================

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J", end="")

def print_header(title):
    """Cetak header dengan border"""
    width = 70
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()

# ========================================
# PROGRAM UTAMA
# ========================================

def main():
    """
    Fungsi utama aplikasi
    Flow: Load Database -> Menu Loop -> Save Database
    """
    
    # === STEP 1: LOAD DATABASE ===
    print("Loading database...")
    load_database()
    print()
    time.sleep(1)
    
    # === STEP 2: MENU LOOP ===
    while True:
        clear_screen()
        print_header("APLIKASI KATALOG ALBUM MUSIK")
        
        print("Selamat Datang di Katalog Album Musik!")
        print()
        print("Aplikasi ini menggunakan struktur MLL (Multi Linked List):")
        print("  - PARENT: Artis (Record dengan nama, genre, tahun debut)")
        print("  - CHILD : Lagu (Tipe Dasar String - judul lagu)")
        print()
        print("-" * 70)
        print()
        print("  1. MASUK KE KATALOG MUSIK")
        print("  2. SIMPAN & KELUAR")
        print()
        print("-" * 70)
        
        pilihan = input(">> Pilih menu (1-2): ").strip()
        
        # === MENU 1: KATALOG MUSIK ===
        if pilihan == '1':
            menu_katalog()
        
        # === MENU 2: SAVE & EXIT ===
        elif pilihan == '2':
            clear_screen()
            print_header("SIMPAN & KELUAR")
            
            print("Menyimpan semua perubahan ke database...")
            
            # === STEP 3: SAVE DATABASE ===
            save_database()
            
            print("\nSemua data berhasil disimpan!")
            print("\nTerima kasih telah menggunakan Katalog Album Musik!")
            print("Sampai jumpa lagi!")
            time.sleep(2)
            
            break
        
        else:
            print("\nPilihan tidak valid!")
            time.sleep(1)


# ========================================
# ENTRY POINT
# ========================================

if __name__ == "__main__":
    main()
