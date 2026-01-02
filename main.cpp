#include "katalog.h"

//  PROGRAM UTAMA TUBES STRUKDAT 
// IMPLEMENTASI: MLL 1-N dengan CRUD + Search + Pengolahan MLL
// Konteks: Katalog Musik (Artis -> Lagu)

int main() {
    List L;                                       // SPESIFIKASI 1.a: Deklarasi MLL
    createList(L);                                // SPESIFIKASI 2.a: CREATE list
    
    string filename = "music_db.csv";
    
    // Load existing data
    bool loaded = loadFromCSV(filename, L);
    if (!loaded) {
        // Start with empty database - no message needed
    }

    int pilihan;
    string nama, genre, judul;
    int tahun;
    adrArtis pFound;

    do {
        clearScreen();
        displayMenu();                                // Improved menu display

        pilihan = readMenuChoice();

        switch (pilihan) {
            case 1: {
                // SPESIFIKASI 2.a: CRUD - CREATE Artis Baru
                clearScreen();
                displayHeader("TAMBAH ARTIS");
                nama = readString("  Nama: ");
                genre = readString("  Genre: ");
                tahun = readInteger("  Tahun debut: ");
                
                insertLastArtis(L, createElementArtis(nama, genre, tahun), filename);  // CREATE operation
                cout << "  Total artis: " << countTotalArtis(L) << endl;   // SPESIFIKASI 2.b: Counting
                break;
            }

            case 2: {
                // SPESIFIKASI 2.a: CRUD - CREATE Lagu (child element)
                clearScreen();
                displayHeader("TAMBAH LAGU");
                nama = readString("  Nama artis: ");
                pFound = searchArtis(L, nama);            // SEARCH operation
                
                if (pFound != nullptr) {
                    judul = readString("  Judul lagu: ");
                    insertLagu(pFound, judul, L, filename);  // CREATE lagu ke array
                } else {
                    cout << "  Artis tidak ditemukan" << endl;
                }
                break;
            }

            case 3: {
                // SPESIFIKASI 2.a: CRUD - READ (Tampil semua data)
                clearScreen();
                showAllData(L);                           // READ operation dengan traversal MLL
                break;
            }

            case 4: {
                // SPESIFIKASI 2.a: CRUD - DELETE Lagu (dari array)
                clearScreen();
                displayHeader("HAPUS LAGU");
                nama = readString("  Nama artis: ");
                pFound = searchArtis(L, nama);            // SEARCH operation
                
                if (pFound != nullptr) {
                    cout << "\n  Lagu " << pFound->info.nama << ":" << endl;
                    for (int i = 0; i < pFound->jumlahLagu; i++) {
                        cout << "    + " << pFound->laguArray[i] << endl;
                    }
                    
                    judul = readString("\n  Hapus lagu: ");
                    deleteLagu(pFound, judul, L, filename);  // DELETE dari array
                } else {
                    cout << "  Artis tidak ditemukan" << endl;
                }
                break;
            }

            case 5: {
                // SPESIFIKASI 2.a: CRUD - DELETE Artis (dari MLL)
                clearScreen();
                displayHeader("HAPUS ARTIS");
                nama = readString(">> Nama Artis yang dihapus: ");
                deleteArtis(L, nama, filename);          // DELETE operation
                break;
            }

            case 6: {
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

            case 7: {
                // SPESIFIKASI 2.b: LAPORAN - Wrapped Report Function
                clearScreen();
                showReport(L);                          // Wrapped report function
                break;
            }

            case 8: {
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
                cout << "  Pilihan tidak valid (0-8)" << endl;
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