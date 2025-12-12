import os
import time
from database.data_store import load_database, save_database #import fungsi load dan save database
from admin.menu_admin import menu_katalog #import menu katalog musik

def clear_screen():
   
    os.system('cls' if os.name == 'nt' else 'clear') #untuk membersihkan terminal
    print("\033[H\033[J", end="")

def print_header(title):

    width = 70
    print("=" * width)
    print(title.center(width)) #untuk mencetak judul di tengah suaya engga spam di (====) di print
    print("=" * width)
    print()

def main():    
 
    print("Loading database...")
    load_database()
    print()
    time.sleep(1)
    
 
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
        
        if pilihan == '1':
            menu_katalog()
        
        elif pilihan == '2':
            clear_screen()
            print_header("SIMPAN & KELUAR")
            
            print("Menyimpan semua perubahan ke database...")
            
            save_database()
            
            print("\nSemua data berhasil disimpan!")
            print("\nTerima kasih telah menggunakan Katalog Album Musik!")
            print("Sampai jumpa lagi!")
            time.sleep(2)
            
            break
        
        else:
            print("\nPilihan tidak valid!")
            time.sleep(1)


if __name__ == "__main__":
    main()
