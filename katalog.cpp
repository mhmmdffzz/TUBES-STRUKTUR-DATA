#include "katalog.h"

//   IMPLEMENTASI SPESIFIKASI TUBES STRUKDAT   
// SPESIFIKASI 1.a: MLL 1-N dengan:
// - Record (tipe bentukan): infoArtis
// - Array tipe dasar: string* laguArray
// - Parent: List Artis, Child: Array Lagu

//  OPERASI DASAR ELEMENT   
adrArtis createElementArtis(const string &nama, const string &genre, int tahun) {  //membuat wadah artis baru
    adrArtis P = new elmArtis;                    // SPESIFIKASI 1.a: Alokasi node MLL
    P->info.nama = nama;                          // Record field 1
    P->info.genre = genre;                        // Record field 2  
    P->info.tahunDebut = tahun;                   // Record field 3
    P->laguArray = new string[5];                 // SPESIFIKASI 1.a: Array tipe dasar dinamis
    P->jumlahLagu = 0;
    P->kapasitas = 5;
    P->next = nullptr;                            // SPESIFIKASI 1.a: Pointer next
    return P;
}

// SPESIFIKASI 2.a: CRUD + SEARCH

//  OPERASI CREATE 
void createList(List &L) {
    L.first = nullptr;                            // SPESIFIKASI 2.a: CREATE - Inisialisasi list
}

void insertLastArtis(List &L, adrArtis   P, const string &filename) {   
    // SPESIFIKASI 2.a: CREATE - Tambah artis baru ke list
    if (L.first == nullptr) { //check apakah list masih kosong
        L.first = P;
    } else {
        adrArtis Q = L.first; 
        while (Q->next != nullptr) {              // Traversal ke akhir list
            Q = Q->next;
        }
        Q->next = P;                              // Insert di akhir
    }
    
    cout << "  Artis '" << P->info.nama << "' berhasil ditambahkan!" << endl;
    saveToCSV(L, filename);
}

//  OPERASI SEARCH 
adrArtis searchArtis(List L, const string &nama) {
    // SPESIFIKASI 2.a: SEARCH - Pencarian dengan case insensitive
    // Trim whitespace and convert input to lowercase for case insensitive search
    string namaLower = nama;
    // Remove leading/trailing whitespace
    namaLower.erase(namaLower.find_last_not_of(" \t\n\r\f\v") + 1);
    namaLower.erase(0, namaLower.find_first_not_of(" \t\n\r\f\v"));
    // Convert to lowercase
    transform(namaLower.begin(), namaLower.end(), namaLower.begin(), ::tolower);
    
    adrArtis P = L.first;
    while (P != nullptr) {                        // Traversal sequential search
        // Convert stored name to lowercase and trim for comparison
        string storedName = P->info.nama;
        // Remove leading/trailing whitespace
        storedName.erase(storedName.find_last_not_of(" \t\n\r\f\v") + 1);
        storedName.erase(0, storedName.find_first_not_of(" \t\n\r\f\v"));
        // Convert to lowercase
        transform(storedName.begin(), storedName.end(), storedName.begin(), ::tolower);
        
        if (storedName == namaLower) {
            return P;                             // SEARCH berhasil
        }
        P = P->next;
    }
    return nullptr;                               // SEARCH tidak ditemukan
}

//  OPERASI DELETE 
void deleteArtis(List &L, const string &nama, const string &filename) {
    // SPESIFIKASI 2.a: DELETE - Hapus artis dari list
    adrArtis P = searchArtis(L, nama);            // Cari dulu dengan SEARCH
    
    if (P == nullptr) {
        cout << "  Artis tidak ditemukan!" << endl;
        return;
    }
    
    // Find the previous node to update links
    adrArtis prev = nullptr;
    adrArtis current = L.first;
    while (current != nullptr && current != P) {
        prev = current;
        current = current->next;
    }
    
    // Hapus array lagu (dealokasi array tipe dasar)
    delete[] P->laguArray;
    
    // Hapus artis dari list (update pointer)
    if (prev == nullptr) {
        L.first = P->next;                        // Hapus node pertama
    } else {
        prev->next = P->next;                     // Hapus node tengah/akhir
    }
    
    delete P;                                     // Dealokasi node
    cout << "  Artis '" << nama << "' berhasil dihapus!" << endl;
    saveToCSV(L, filename);
}

//  OPERASI UPDATE 
void updateArtisInfo(List &L, const string &nama, const string &genreBaru, int tahunBaru, const string &filename) {
    // SPESIFIKASI 2.a: UPDATE - Edit informasi artis
    adrArtis P = searchArtis(L, nama);            // Cari dulu dengan SEARCH
    if (P != nullptr) {
        P->info.genre = genreBaru;                // Update field record
        P->info.tahunDebut = tahunBaru;           // Update field record
        cout << "  Info artis '" << nama << "' berhasil diupdate!" << endl;
        
        // Auto-save ke CSV
        if (saveToCSV(L, filename)) {
            cout << "  Data disimpan ke " << filename << endl;
        } else {
            cout << "  Gagal menyimpan ke file!" << endl;
        }
    } else {
        cout << "  Artis tidak ditemukan!" << endl;
    }
}

//  OPERASI ARRAY TIPE DASAR (CHILD) 
// SPESIFIKASI 1.a: Array tipe dasar (string) dalam record

void insertLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    // SPESIFIKASI 1.a: Operasi pada array tipe dasar dinamis
    if (P == nullptr) return;
    
    // Check if array needs to be resized (dynamic array management)
    if (P->jumlahLagu >= P->kapasitas) {
        // Resize array (double the capacity)
        int newKapasitas = P->kapasitas * 2;
        string* newArray = new string[newKapasitas];  // Alokasi array baru
        
        // Copy existing songs
        for (int i = 0; i < P->jumlahLagu; i++) {
            newArray[i] = P->laguArray[i];            // Copy elemen
        }
        
        // Delete old array and update pointer
        delete[] P->laguArray;                        // Dealokasi array lama
        P->laguArray = newArray;                      // Update pointer
        P->kapasitas = newKapasitas;
    }
    
    // Add new song
    P->laguArray[P->jumlahLagu] = judul;              // INSERT ke array
    P->jumlahLagu++;
    
    cout << "  Lagu '" << judul << "' berhasil ditambahkan!" << endl;
    saveToCSV(L, filename);
}

void deleteLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    if (P == nullptr || P->jumlahLagu == 0) {
        cout << "  Lagu tidak ditemukan!" << endl;
        return;
    }
    
    // Find song index
    int index = -1;
    for (int i = 0; i < P->jumlahLagu; i++) {
        if (P->laguArray[i] == judul) {
            index = i;
            break;
        }
    }
    
    if (index == -1) {
        cout << "  Lagu tidak ditemukan!" << endl;
        return;
    }
    
    // Shift elements left to remove song
    for (int i = index; i < P->jumlahLagu - 1; i++) {
        P->laguArray[i] = P->laguArray[i + 1];
    }
    
    P->jumlahLagu--;
    cout << "  Lagu '" << judul << "' berhasil dihapus!" << endl;
    saveToCSV(L, filename);
}

// Fungsi insertLagu tanpa auto-save untuk loading dari CSV
void insertLaguNoSave(adrArtis P, const string &judul) {
    if (P == nullptr) return;
    
    // Check if array needs to be resized
    if (P->jumlahLagu >= P->kapasitas) {
        // Resize array (double the capacity)
        int newKapasitas = P->kapasitas * 2;
        string* newArray = new string[newKapasitas];
        
        // Copy existing songs
        for (int i = 0; i < P->jumlahLagu; i++) {
            newArray[i] = P->laguArray[i];
        }
        
        // Delete old array and update pointer
        delete[] P->laguArray;
        P->laguArray = newArray;
        P->kapasitas = newKapasitas;
    }
    
    // Add new song
    P->laguArray[P->jumlahLagu] = judul;
    P->jumlahLagu++;
}

// Fungsi insertLastArtis tanpa auto-save untuk loading dari CSV
void insertLastArtisNoSave(List &L, adrArtis P) {
    if (L.first == nullptr) {
        L.first = P;
    } else {
        adrArtis Q = L.first;
        while (Q->next != nullptr) {
            Q = Q->next;
        }
        Q->next = P;
    }
}

bool isListEmpty(List L) {
    return L.first == nullptr;
}

void deallocateList(List &L) {
    adrArtis P = L.first;
    while (P != nullptr) {
        adrArtis temp = P;
        P = P->next;
        
        // Deallocate song array
        delete[] temp->laguArray;
        
        // Deallocate artist node
        delete temp;
    }
    L.first = nullptr;
}

//  OPERASI DISPLAY 
void showAllData(List L) {
    displayHeader("*** DATA KATALOG MUSIK ***");
    
    if (L.first == nullptr) {
        cout << "\n  Tidak ada data artis." << endl;
        return;
    }

    int artistCount = 0;
    int totalSongs = 0;
    
    adrArtis P = L.first;
    while (P != nullptr) {
        artistCount++;
        cout << "\n  [" << artistCount << "] " << P->info.nama << endl;
        cout << "      Genre  : " << P->info.genre << endl;
        cout << "      Debut  : " << P->info.tahunDebut << endl;
        cout << "      Lagu   : ";
        
        if (P->jumlahLagu == 0) {
            cout << "(kosong)" << endl;
        } else {
            cout << "(" << P->jumlahLagu << " lagu)" << endl;
            for (int i = 0; i < P->jumlahLagu; i++) {
                cout << "         - " << P->laguArray[i] << endl;
                totalSongs++;
            }
        }
        P = P->next;
    }
    
    cout << "\n  Total: " << artistCount << " artis, " << totalSongs << " lagu" << endl;
}

void displayMenu() {
    displayHeader("*** KATALOG MUSIK DIGITAL ***");
    cout << "\n  [1] Kelola Data Artis & Lagu" << endl;
    cout << "  [2] Lihat Semua Data Katalog" << endl;
    cout << "  [3] Hapus Data Artis & Lagu" << endl;
    cout << "  [4] Cari Artis di Katalog" << endl;
    cout << "  [5] Lihat Laporan Statistik" << endl;
    cout << "  [6] Update Info Artis" << endl;
    cout << "  [0] Keluar dari Program" << endl;
    cout << "\n  >> Pilihan: ";
}

void displaySubMenu() {
    displaySubHeader("SUB-MENU: KELOLA DATA");
    cout << "\n  [1] Tambah Artis Baru" << endl;
    cout << "  [2] Tambah Lagu ke Artis Lama" << endl;
    cout << "  [0] Kembali ke Menu Utama" << endl;
    cout << "\n  >> Pilihan: ";
}

void displaySubMenuHapus() {
    displaySubHeader("SUB-MENU: HAPUS DATA");
    cout << "\n  [1] Hapus Lagu dari Artis" << endl;
    cout << "  [2] Hapus Artis dari Katalog" << endl;
    cout << "  [0] Kembali ke Menu Utama" << endl;
    cout << "\n  >> Pilihan: ";
}

void showReport(List L) {
    displayHeader("*** LAPORAN SISTEM KATALOG MUSIK ***");
    
    int totalArtis = countTotalArtis(L);
    int totalLagu = countTotalLagu(L);
    
    cout << "\n  STATISTIK GLOBAL" << endl;
    cout << "  Total Artis: " << totalArtis << endl;
    cout << "  Total Lagu : " << totalLagu << endl;
    
    cout << "\n  DETAIL PER ARTIS" << endl;
    
    if (L.first == nullptr) {
        cout << "  (tidak ada data)" << endl;
    } else {
        adrArtis P = L.first;
        int counter = 1;
        while (P != nullptr) {
            cout << "  " << counter << ". " << P->info.nama << " (" << P->jumlahLagu << " lagu)" << endl;
            P = P->next;
            counter++;
        }
    }
}

void exitProgram(const string &filename) {
    displayHeader("*** TERIMA KASIH ***");
    cout << "\n  Data berhasil disimpan: " << filename << endl;
    cout << "  Sampai jumpa lagi!" << endl;
}

// SPESIFIKASI 2.b: PENGOLAHAN MLL 
// Counting, Min Max, dll.

int countTotalLagu(List L) {
    // SPESIFIKASI 2.b: Counting total lagu di seluruh MLL
    int total = 0;
    adrArtis P = L.first;
    while (P != nullptr) {                        // Traversal semua artis
        total += P->jumlahLagu;                   // Akumulasi jumlah lagu
        P = P->next;
    }
    return total;
}

int countTotalArtis(List L) {
    // SPESIFIKASI 2.b: Counting total artis dalam MLL
    int count = 0;
    adrArtis P = L.first;
    while (P != nullptr) {                        // Traversal dan counting
        count++;
        P = P->next;
    }
    return count;
}

//  FILE I/O OPERATIONS 
bool loadFromCSV(const string &filename, List &L) {
    ifstream file(filename);
    if (!file.is_open()) {
        return false;
    }
    
    string line;
    while (getline(file, line)) {
        if (line.empty()) continue;
        
        stringstream ss(line);
        string nama, genre, tahunStr, judul;
        
        if (getline(ss, nama, ';') && 
            getline(ss, genre, ';') && 
            getline(ss, tahunStr, ';') && 
            getline(ss, judul)) {
            
            try {
                int tahun = stoi(tahunStr);
                
                adrArtis P = searchArtis(L, nama);
                if (P == nullptr) {
                    P = createElementArtis(nama, genre, tahun);
                    insertLastArtisNoSave(L, P);
                }
                
                // Skip jika judul = "Belum Ada Lagu" (placeholder untuk artis tanpa lagu)
                if (judul != "Belum Ada Lagu") {
                    insertLaguNoSave(P, judul);
                }
            } catch (const exception& e) {
                // Skip invalid lines silently
            }
        }
    }
    
    file.close();
    return true;
}

bool saveToCSV(List L, const string &filename) {
    ofstream file(filename);
    if (!file.is_open()) {
        return false;
    }
    
    adrArtis P = L.first;
    while (P != nullptr) {
        if (P->jumlahLagu == 0) {
            file << P->info.nama << ";" << P->info.genre << ";" 
                 << P->info.tahunDebut << ";Belum Ada Lagu" << endl;
        } else {
            for (int i = 0; i < P->jumlahLagu; i++) {
                file << P->info.nama << ";" << P->info.genre << ";" 
                     << P->info.tahunDebut << ";" << P->laguArray[i] << endl;
            }
        }
        P = P->next;
    }
    
    file.close();
    return true;
}

//  UTILITY FUNCTIONS 
int getMenuChoice() {
    int choice;
    bool valid = false;
    
    while (!valid) {
        if (cin >> choice) {
            valid = true; //kalau inputnya benar ke sini
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        } else {
            cout << "  [ERROR] Input tidak valid! Masukkan angka pilihan menu." << endl;
            cout << "  Pilihan: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); //kalau salah ke sini dan dia bakal ngulang terus
        }
    }
    return choice;
}