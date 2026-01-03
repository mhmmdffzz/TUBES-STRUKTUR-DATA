#ifndef KATALOG_H
#define KATALOG_H

//  LIBRARY YANG DIGUNAKAN 
#include <iostream>     // Library untuk input/output: cout, cin, endl
#include <fstream>      // Library untuk file I/O: ifstream (baca file), ofstream (tulis file)
#include <sstream>      // Library untuk string parsing: stringstream, getline dengan delimiter
#include <string>       // Library untuk manipulasi string: string class, getline, operasi string
#include <algorithm>    // Library untuk algoritma: transform (case conversion), sort, search
#include <limits>       // Library untuk konstanta numerik: numeric_limits (clear input buffer)

using namespace std;

// SPESIFIKASI TUBES STRUKDAT 
// 1.a BST/MLL 1-N: IMPLEMENTASI MLL 1-N
// - Data pada node berupa tipe bentukan (record): infoArtis
// - Satu atribut berupa array tipe dasar: string* laguArray
// - List parent dan anak tidak boleh sama: Artis (parent) vs Lagu (child array)

//  DEFINISI STRUKTUR DATA MLL 1-N 
struct infoArtis {    // SPESIFIKASI 1.a: Tipe bentukan (record)
    string nama;
    string genre;
    int tahunDebut;
};

struct elmArtis {     // SPESIFIKASI 1.a: Node MLL dengan record + array tipe dasar
    infoArtis info;         // Record (tipe bentukan)
    string* laguArray;      // SPESIFIKASI 1.a: Array tipe dasar (string)
    int jumlahLagu;         // Current number of songs
    int kapasitas;          // Array capacity
    struct elmArtis* next;  // SPESIFIKASI 1.a: Pointer ke node berikutnya
};

struct List {         // SPESIFIKASI 1.a: List parent
    elmArtis* first;
};

typedef elmArtis* adrArtis;

//  SPESIFIKASI TUBES: FUNGSIONALITAS 
// 2. Fungsionalitas:
// a. Dasar: CRUD + Search`
// b. Pengolahan MLL: Counting, dll

//  PROTOTYPES OPERASI DASAR 
adrArtis createElementArtis(const string &nama, const string &genre, int tahun);

// PROTOTYPES CRUD + SEARCH (SPESIFIKASI 2.a) 
void createList(List &L);                    // CREATE: Inisialisasi list
void insertLastArtis(List &L, adrArtis P, const string &filename = "music_db.csv");  // CREATE: Tambah artis
adrArtis searchArtis(List L, const string &nama);     // SEARCH: Cari artis
void deleteArtis(List &L, const string &nama, const string &filename = "music_db.csv");  // DELETE: Hapus artis
void updateArtisInfo(List &L, const string &nama, const string &genreBaru, int tahunBaru, const string &filename = "music_db.csv");  // UPDATE: Edit info artis

//  PROTOTYPES OPERASI LAGU (CHILD ELEMENT) 
void insertLagu(adrArtis P, const string &judul, List &L, const string &filename = "music_db.csv");    // CREATE: Tambah lagu
void deleteLagu(adrArtis P, const string &judul, List &L, const string &filename = "music_db.csv");    // DELETE: Hapus lagu

// Support functions (no auto-save)
void insertLaguNoSave(adrArtis P, const string &judul);
void insertLastArtisNoSave(List &L, adrArtis P);

// PROTOTYPES UTILITY LIST 
bool isListEmpty(List L);
void deallocateList(List &L);

// PROTOTYPES DISPLAY 
void showAllData(List L);                    // READ: Tampil semua data
void displayMenu();                          // Display main menu with better UI
void displaySubMenu();                       // Display sub-menu untuk kelola data
void displaySubMenuHapus();                  // Display sub-menu untuk hapus data
void showReport(List L);                     // Show system report with statistics
void exitProgram(const string &filename);   // Exit program with cleanup message

// PROTOTYPES PENGOLAHAN MLL (SPESIFIKASI 2.b) 
int countTotalLagu(List L);                  // Counting total lagu
int countTotalArtis(List L);                 // Counting total artis

// PROTOTYPES FILE I/O 
bool loadFromCSV(const string &filename, List &L);
bool saveToCSV(List L, const string &filename);

// PROTOTYPES UTILITY 
int getMenuChoice();

//  UTILITY FUNCTIONS UNTUK UI 

inline void clearScreen() {
    system("cls");
    // Reset any ANSI colors
    cout << "\033[0m";
}

inline void displayHeader(const string &title) {
    cout << "\n  +";
    for(int i=0; i<60; i++) cout << "=";
    cout << "+" << endl;
    int padding = (60 - title.length()) / 2;
    cout << "  |" << string(padding, ' ');
    cout << title;
    cout << string(60 - padding - title.length(), ' ') << "|" << endl;
    cout << "  +";
    for(int i=0; i<60; i++) cout << "=";
    cout << "+";
    cout << endl;
}

inline void displaySubHeader(const string &subtitle) {
    cout << "\n  +";
    for(int i=0; i<58; i++) cout << "-";
    cout << "+" << endl;
    cout << "  | ";
    cout << subtitle;
    cout << string(56 - subtitle.length(), ' ') << " |" << endl;
    cout << "  +";
    for(int i=0; i<58; i++) cout << "-";
    cout << "+";
    cout << endl;
}

inline void waitForEnter() {
    cout << "\n  >>  Tekan ENTER untuk melanjutkan...";
    cin.ignore();
}

inline string readString(const string &prompt) {
    string input;
    bool valid = false;
    
    while (!valid) {
        cout << prompt;
        getline(cin, input);
        
        // Trim whitespace
        input.erase(0, input.find_first_not_of(" \t\n\r\f\v"));
        input.erase(input.find_last_not_of(" \t\n\r\f\v") + 1);
        
        if (!input.empty()) {
            valid = true;
        } else {
            cout << "  ERROR: Input tidak boleh kosong!" << endl;
        }
    }
    return input;
}

inline int readInteger(const string &prompt) {
    int value;
    bool valid = false;
    
    while (!valid) {
        cout << prompt;
        if (cin >> value) {
            valid = true;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        } else {
            cout << "  ERROR: Input tidak valid! Masukkan angka yang benar." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }
    return value;
}

inline int readMenuChoice() {
    return getMenuChoice();
}

#endif