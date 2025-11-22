import os #guna untuk membersihkan layar
import time #untuk jeda waktu

# IMPORT FUNGSI DARI FOLDER LAIN
# Kita panggil fungsi yang ada di folder 'database', 'admin', dan 'user'
# Pastikan nama folder dan filenya sesuai ya!

from database.data_store import load_database, save_database
from admin.admin_menu import menu_admin
from user.user_menu import menu_user_auth

# --- FUNGSI BANTUAN (UTILITIES) ---
# Kita taruh clear_screen di sini atau bisa bikin file utils.py terpisah
# Biar gampang, kita taruh sini dulu aja buat Main Menu.
def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear') #untuk membersihkan layar/terminal

def print_header(title): #untuk mencetak header
    width = 60
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()  # Tambahkan baris kosong setelah header

# --- PROGRAM UTAMA ---
def main():
    # 1. LOAD DATA (Penting! Baca data dari Hard Disk ke RAM)
    load_database()

    while True:
        clear_screen()
        print_header("🎵 APLIKASI MUSIC STREAMING (TUGAS BESAR) 🎵")
        
        print("Selamat Datang! Silakan pilih peran anda:")
        print("-" * 60)
        print("1. 👨‍🔧 Masuk sebagai ADMIN (Label Manager)")
        print("2. 🙋‍♂️ Masuk sebagai USER (Pendengar)")
        print("3. 💾 KELUAR (Save & Exit)")
        print("-" * 60)
        
        pilihan = input(">> Pilih menu (1-3): ")

        if pilihan == '1':
            # Masuk ke Folder Admin
            # Kita kasih password sederhana di sini biar aman
            pw = input("\n🔐 Masukkan Password Admin: ")
            if pw == "admin123": 
                print("✅ Akses Diterima!")
                time.sleep(1)
                menu_admin() # Panggil fungsi dari file admin/admin_menu.py
            else:
                print("❌ Password Salah!")
                time.sleep(1)

        elif pilihan == '2':
            # Masuk ke Folder User
            menu_user_auth() # Panggil fungsi dari file user/user_menu.py

        elif pilihan == '3':
            # 2. SAVE DATA (Penting! Simpan RAM ke Hard Disk)
            print("\nSedang menyimpan data database...")
            save_database() 
            print("✅ Data tersimpan. Terima kasih telah menggunakan aplikasi ini!")
            break
            
        else:
            print("❌ Pilihan tidak valid!")
            time.sleep(1)

# --- TOMBOL START ---
if __name__ == "__main__":
    main()