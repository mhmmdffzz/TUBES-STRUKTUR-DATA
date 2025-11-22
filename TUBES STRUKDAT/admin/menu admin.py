import os #untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# RUMUSNYA (Pakai variabel 'title')
def print_header(title):
    width = 50 
    print("=" * width)
    print(title.center(width))  # Di sini dia pakai variabel 'title'
    print("=" * width)

def menu_admin():
    while True:
        print("\n---  MENU ADMIN (LABEL/MANAGER) ---")
        print("1. Tambah Artis Baru (Insert Last)")
        print("2. Tambah Lagu ke Artis (Insert Child)")
        print("3. Lihat Semua Musik (View Nested)")
        print("4. Hapus Artis (Delete Parent & Cascade)")
        print("5. Hapus Lagu (Delete Child)")
        print("6. Cari Lagu")
        print("7. Lihat Artis Terpopuler (Top Artist)")
        print("8. Analisis: Trending Song & Top User")
        print("0. Logout (Kembali ke Menu Utama)")
        
        pilihan = input(">> Pilih menu (0-8): ")
        
        if pilihan == '1':
            print("[Sistem] Masuk ke fitur Tambah Artis...")
        elif pilihan == '2':
            print("[Sistem] Masuk ke fitur Tambah Lagu...")
        elif pilihan == '3':
            print("[Sistem] Menampilkan seluruh database...")
        elif pilihan == '4':
            print("[Sistem] Menghapus artis...")
        elif pilihan == '5':
            print("[Sistem] Menghapus lagu...")
        elif pilihan == '6':
            print("[Sistem] Mencari lagu...")
        elif pilihan == '7':
            print("[Sistem] Menampilkan artis dengan lagu terbanyak...")
        elif pilihan == '8':
            print("[Sistem] Menampilkan data analisis...")
        elif pilihan == '0':
            print("Logout dari Admin...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_admin()