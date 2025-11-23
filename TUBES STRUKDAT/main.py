import os
import time

# --- IMPORT MODUL DARI FOLDER LAIN ---
# Perhatikan cara penulisannya: dari folder.nama_file import nama_fungsi
from database.data_store import load_database, save_database
from admin.admin_menu import menu_admin
from user.user_menu import menu_user_auth

# --- FUNGSI BANTUAN UI ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    width = 60
    print("=" * width)
    print(title.center(width))
    print("=" * width)

# --- PROGRAM UTAMA (CONTROLLER) ---
def main():
    # 1. LOAD DATA (WAJIB DULUAN!)
    # Sebelum menu muncul, kita baca dulu file JSON biar RAM terisi.
    load_database()

    while True:
        clear_screen()
        print_header("🎵 APLIKASI MUSIC STREAMING (TUGAS BESAR) 🎵")
        
        print("Selamat Datang! Silakan pilih peran anda:")
        print("-" * 60)
        print("1. 👨‍🔧 Masuk sebagai ADMIN (Label Manager)")
        print("2. 🙋‍♂️ Masuk sebagai USER (Pendengar)")
        print("3. 💾 SIMPAN & KELUAR (Save & Exit)")
        print("-" * 60)
        
        pilihan = input(">> Pilih menu (1-3): ")

        if pilihan == '1':
            # --- LOGIN ADMIN ---
            # Kita kasih password sederhana biar aman dikit
            pw = input("\n🔐 Masukkan Password Admin: ")
            
            if pw == "admin123": 
                print("✅ Akses Diterima!")
                time.sleep(1)
                # Pindah ke file admin/admin_menu.py
                menu_admin() 
            else:
                print("❌ Password Salah!")
                time.sleep(1)

        elif pilihan == '2':
            # --- LOGIN USER ---
            # Pindah ke file user/user_menu.py
            menu_user_auth() 

        elif pilihan == '3':
            # --- SAVE & EXIT ---
            print("\n💾 Sedang menyimpan perubahan ke Database JSON...")
            
            # Pindahkan data dari RAM (List) ke File (Hard Disk)
            save_database() 
            
            print("✅ Data tersimpan aman.")
            print("Terima kasih! Sampai jumpa lagi.")
            time.sleep(2)
            break # Keluar dari loop while, program berhenti.
            
        else:
            print("❌ Pilihan tidak valid!")
            time.sleep(1)

# --- TOMBOL START ---
# Ini titik awal program berjalan
if __name__ == "__main__":
    main()
