# ========================================
# MAIN - Entry Point Aplikasi
# ========================================
# File ini adalah controller utama aplikasi
# Mengatur flow: Load DB -> Menu -> Save DB
# Menu: Admin Login, User Register/Login, Exit

import os
import time
from database.data_store import load_database, save_database, verify_admin
from admin.menu_admin import menu_admin
from user.menu_user import menu_user_auth

# ========================================
# FUNGSI UTILITY
# ========================================

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear') #'nt'=windows , else 'clear'=linux/mac
    print("\033[H\033[J", end="")  # ANSI escape code backup 

def print_header(title): #print_header akan di tampilkan di sini
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
    # Membaca data dari file JSON ke memory (RAM)
    # Harus dilakukan sebelum menu muncul
    print("Loading database...")
    load_database()
    print()
    time.sleep(1)
    
    # === STEP 2: MENU LOOP ===
    while True:
        clear_screen()
        print_header("MUSIC STREAMING PLATFORM") #print_headernya akan di tampilkan ketika di jalankan main.py
        
        print("Selamat Datang! Pilih peran Anda:")
        print()
        print("  1. ADMIN - Manajemen Database Musik")
        print("  2. USER - Playlist & Streaming")
        print("  3. SIMPAN & KELUAR")
        print()
        print("-" * 70)
        
        pilihan = input(">> Pilih menu (1-3): ").strip()
        
        # === MENU 1: ADMIN LOGIN ===
        if pilihan == '1':
            clear_screen()
            print_header("LOGIN ADMIN")
            
            # Input kredensial admin
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            # Verifikasi menggunakan fungsi dari data_store
            # fungsi verify_admin akan melakukan Sequential Search untuk cari admin
            if verify_admin(username, password):
                print(f"\nLogin berhasil! Selamat datang, {username}.")
                time.sleep(1) #(1 detik)
                
                # Masuk ke Admin Dashboard
                menu_admin()
            else:
                print("\nUsername atau password salah!")
                time.sleep(2) #tunggu 2 detik sebelum kembali ke menu utama
        
        # === MENU 2: USER REGISTER/LOGIN ===
        elif pilihan == '2':
            # Pindah ke menu user auth (register/login)
            menu_user_auth()
        
        # === MENU 3: SAVE & EXIT ===
        elif pilihan == '3':
            clear_screen()
            print_header("SIMPAN & KELUAR")
            
            print("Menyimpan semua perubahan ke database...")
            
            # === STEP 3: SAVE DATABASE ===
            # Menyimpan data dari memory (RAM) ke file JSON (Disk)
            # Semua perubahan (artis, lagu, user, playlist, play count) disimpan
            save_database()
            
            print("\nSemua data berhasil disimpan!")
            print("\nTerima kasih telah menggunakan Music Streaming Platform!")
            print("Sampai jumpa lagi!")
            time.sleep(2)
            
            # Keluar dari loop, program selesai
            break
        
        else:
            print("\nPilihan tidak valid!")
            time.sleep(1)


# ========================================
# ENTRY POINT
# ========================================
# Ini adalah titik awal program berjalan
# Python akan menjalankan fungsi main() saat file ini dieksekusi

if __name__ == "__main__":
    main() #maksudnaya adalah ketika file main.py di jalankan, maka program akan mengeksekusi fungsi main() jika tidak maka fiel tersebut ngg di jalankan

