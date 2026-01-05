#include "katalog.h"
// IMPLEMENTASI: MLL 1-N dengan CRUD + Search + Pengolahan MLL
// Konteks: Katalog Musik (Artis -> Lagu)

int main() {
    List L;                                       // SPESIFIKASI 1.a: Deklarasi MLL
    createList(L);                                // SPESIFIKASI 2.a: CREATE list
    
    //  KONEKSI DATABASE (CSV FILE) 
    string filename = "music_db.csv";             // DATABASE: Nama file CSV sebagai storage
    
    // DATABASE: Load/baca data dari CSV ke memory (MLL)
    bool loaded = loadFromCSV(filename, L);       // KONEKSI: Read dari file ke struktur data
    if (!loaded) {
        // Start with empty database - no message needed
    }

    // Variabel untuk menyimpan input user
    int pilihan;                // Menyimpan pilihan menu user (0-8)
    string nama;                // Menyimpan nama artis dari input user
    string genre;               // Menyimpan genre musik dari input user
    string judul;               // Menyimpan judul lagu dari input user
    string negara;
    int tahun;                  // Menyimpan tahun debut artis dari input user
    adrArtis pFound;            // Menyimpan alamat/pointer artis hasil pencarian

    do {
        clearScreen();
        displayMenu();                               

        pilihan = readMenuChoice();

        switch (pilihan) {
            case 1: {
                // SUB-MENU: Kelola Data Artis & Lagu
                int subPilihan;
                do {
                    clearScreen();
                    displaySubMenu();
                    subPilihan = readMenuChoice();
                    
                    switch (subPilihan) {
                            case 1: {
                                // SPESIFIKASI 2.a: CRUD - CREATE Artis Baru
                                clearScreen();
                                displayHeader("TAMBAH ARTIS BARU");
                                
                                // Input nama artis
                                nama = readString("  Nama artis: ");
                                
                                // VERIFIKASI: Cek apakah artis sudah ada
                                adrArtis cekArtis = searchArtis(L, nama);
                                
                                if (cekArtis != nullptr) {
                                    cout << "\n  [!] ERROR: Artis '" << nama << "' sudah ada dalam katalog!" << endl;
                                    break;
                                }
                                
                            // kalau artis belum ada, lanjut input data lain
                            genre = readString("  Genre: ");
                            tahun = readInteger("  Tahun debut: ");
                            
                            // Buat element artis
                            adrArtis newArtis = createElementArtis(nama, genre, tahun);
                            
                            // Input lagu pertama (opsional dengan tanda "-")
                            cout << "\n  Masukkan Lagu Pertama (atau ketik '-' untuk lewati): ";
                            getline(cin, judul);
                            
                            // Trim whitespace
                            judul.erase(0, judul.find_first_not_of(" \t\n\r\f\v"));
                            judul.erase(judul.find_last_not_of(" \t\n\r\f\v") + 1);
                            
                            // LOGIKA PENTING: Cek tanda strip "-"
                            if (judul == "-") {
                                // Array lagu dibiarkan kosong (jumlahLagu = 0)
                                cout << "\n  Artis '" << nama << "' ditambahkan tanpa lagu." << endl;
                            } else if (!judul.empty()) {
                                // Masukkan lagu ke array
                                newArtis->laguArray[0] = judul;
                                newArtis->jumlahLagu = 1;
                                cout << "\n  Lagu '" << judul << "' berhasil ditambahkan!" << endl;
                            }
                            
                            // Insert artis ke list
                            insertLastArtis(L, newArtis, filename);
                            
                            cout << "  Total artis: " << countTotalArtis(L) << endl;
                            break;
                        }
                        
                        case 2: {
                            // Tambah Lagu ke Artis Lama
                            clearScreen();
                            displayHeader("TAMBAH LAGU KE ARTIS LAMA");
                            
                            nama = readString("  Nama artis yang dicari: ");
                            
                            // Pencarian (searching)
                            pFound = searchArtis(L, nama);
                            
                            if (pFound != nullptr) {
                                // Artis ditemukan
                                cout << "\n  [DITEMUKAN]" << endl;
                                cout << "  Artis: " << pFound->info.nama << endl;
                                cout << "  Genre: " << pFound->info.genre << endl;
                                cout << "  Jumlah lagu saat ini: " << pFound->jumlahLagu << endl;
                                
                                // Loop tambah lagu sampai user ketik 0
                                cout << "\n  TAMBAH LAGU (Ketik '0' untuk selesai)" << endl;
                                
                                while (true) {
                                    cout << "  Judul lagu [" << (pFound->jumlahLagu + 1) << "]: ";
                                    getline(cin, judul);
                                    
                                    // Trim whitespace
                                    judul.erase(0, judul.find_first_not_of(" \t\n\r\f\v"));
                                    judul.erase(judul.find_last_not_of(" \t\n\r\f\v") + 1);
                                    
                                    // Cek jika user input "0" untuk berhenti
                                    if (judul == "0") {
                                        cout << "\n  Selesai menambahkan lagu." << endl;
                                        break;
                                    }
                                    
                                    // Cek jika input kosong
                                    if (judul.empty()) {
                                        cout << "  Input tidak boleh kosong! (Ketik '0' untuk selesai)" << endl;
                                        continue;
                                    }
                                    
                                    // Tambahkan lagu (array akan auto-expand jika penuh)
                                    insertLagu(pFound, judul, L, filename);
                                }
                                
                                cout << "  Total lagu untuk '" << pFound->info.nama << "': " << pFound->jumlahLagu << endl;
                            } else {
                                // Artis tidak ditemukan
                                cout << "\n  [!] ERROR: Artis '" << nama << "' tidak ditemukan dalam katalog!" << endl;
                            }
                            break;
                        }
                        
                        case 0: {
                            // Kembali ke menu utama
                            cout << "\n  Kembali ke menu utama..." << endl;
                            break;
                        }
                        
                        default: {
                            cout << "\n  Pilihan tidak valid! Silakan pilih 0-2." << endl;
                            break;
                        }
                    }
                    
                    if (subPilihan != 0) {
                        waitForEnter();
                    }
                    
                } while (subPilihan != 0);
                break;
            }

            case 2: {
                // SPESIFIKASI 2.a: CRUD - READ (Tampil semua data)
                clearScreen();
                showAllData(L);                           // READ operation dengan traversal MLL
                break;
            }

            case 3: {
                // SUB-MENU: Hapus Data Artis & Lagu
                int subPilihan;
                do {
                    clearScreen();
                    displaySubMenuHapus();
                    subPilihan = readMenuChoice();
                    
                    switch (subPilihan) {
                        case 1: {
                            // SPESIFIKASI 2.a: CRUD - DELETE Lagu (dari array)
                            clearScreen();
                            displayHeader("HAPUS LAGU");
                            nama = readString("  Nama artis: ");
                            pFound = searchArtis(L, nama);            // SEARCH operation
                            
                            if (pFound != nullptr) {
                                // Validasi: cek apakah artis punya lagu
                                if (pFound->jumlahLagu == 0) {
                                    cout << "\n  [!] Artis '" << pFound->info.nama << "' belum memiliki lagu" << endl;
                                    cout << "  Tidak ada lagu yang bisa dihapus" << endl;
                                } else {
                                    cout << "\n  Lagu " << pFound->info.nama << ":" << endl;
                                    for (int i = 0; i < pFound->jumlahLagu; i++) {
                                        cout << "    + " << pFound->laguArray[i] << endl;
                                    }
                                    
                                    judul = readString("\n  Hapus lagu: ");
                                    deleteLagu(pFound, judul, L, filename);  // DELETE dari array
                                }
                            } else {
                                cout << "  Artis tidak ditemukan" << endl;
                            }
                            break;
                        }
                        
                        case 2: {
                            // SPESIFIKASI 2.a: CRUD - DELETE Artis (dari MLL)
                            clearScreen();
                            displayHeader("HAPUS ARTIS");
                            nama = readString("  Nama Artis yang dihapus: ");
                            deleteArtis(L, nama, filename);          // DELETE operation
                            break;
                        }
                        
                        case 0: {
                            // Kembali ke menu utama
                            cout << "\n  Kembali ke menu utama..." << endl;
                            break;
                        }
                        
                        default: {
                            cout << "\n  Pilihan tidak valid! Silakan pilih 0-2." << endl;
                            break;
                        }
                    }
                    
                    if (subPilihan != 0) {
                        waitForEnter();
                    }
                    
                } while (subPilihan != 0);
                break;
            }

            case 4: {
                // SPESIFIKASI 2.a: SEARCH - Cari artis dalam MLL
                clearScreen();
                displayHeader("CARI ARTIS");
                nama = readString(">> Nama Artis: ");
                pFound = searchArtis(L, nama);            // SEARCH operation
                
                if (pFound != nullptr) {
                    cout << "\n[DITEMUKAN]" << endl;
                    cout << "Nama       : " << pFound->info.nama << endl;
                    cout << "Genre      : " << pFound->info.genre << endl;
                    cout << "Tahun Debut: " << pFound->info.tahunDebut << endl;
                    cout << "Jumlah Lagu: " << pFound->jumlahLagu << endl;
                    
                    if (pFound->jumlahLagu > 0) {
                        cout << "\n>> Lagu-lagu:" << endl;
                        for (int i = 0; i < pFound->jumlahLagu; i++) {
                            cout << "  - " << (i + 1) << ". " << pFound->laguArray[i] << endl;
                        }
                    }
                } else {
                    cout << "[X] Artis tidak ditemukan!" << endl;
                }
                break;
            }

            case 5: {
                // SPESIFIKASI 2.b: LAPORAN - Wrapped Report Function
                clearScreen();
                showReport(L);                          // Wrapped report function
                break;
            }

            case 6: {
                // SPESIFIKASI 2.a: CRUD - UPDATE Info Artis
                clearScreen();
                displayHeader("UPDATE INFO ARTIS");
                nama = readString(">> Nama Artis: ");
                genre = readString(">> Genre Baru: ");
                tahun = readInteger(">> Tahun Debut Baru: ");
                
                updateArtisInfo(L, nama, genre, tahun, filename);  // UPDATE operation
                break;
            }

            case 0: {
                exitProgram(filename);                   // Wrapped exit function
                break;
            }

            default: {
                cout << "  Pilihan tidak valid (0-6)" << endl; //untuk menangkap pilihan diluar menu
                break;
            }
        }

        if (pilihan != 0) {
            waitForEnter();
        }

    } while (pilihan != 0);

    // Cleanup
    deallocateList(L);
    return 0;
}