# 📋 CHEATSHEET - KATALOG MUSIK (MLL 1-N)

## � STRUKTUR FILE PROJECT

### 1️⃣ **katalog.h** (Header File - 151 baris)
**Fungsi:** Deklarasi struktur data, prototype fungsi, dan utility functions

**Isi:**
```cpp
// STRUCT DEFINITIONS
- infoArtis          // Record: nama, genre, tahunDebut
- elmArtis           // Node: info + laguArray + jumlahLagu + next
- List               // Parent list: first pointer

// TYPEDEF
- adrArtis           // Pointer ke elmArtis

// FUNCTION PROTOTYPES (Deklarasi saja, tanpa implementasi)
- createList()
- createElementArtis()
- insertLastArtis()
- searchArtis()
- deleteArtis()
- insertLagu()
- deleteLagu()
- loadFromCSV()
- saveToCSV()
- showAllData()
- dll... (semua fungsi dideklarasikan di sini)

// INLINE UTILITY FUNCTIONS (Langsung ada implementasi)
- clearScreen()      // system("cls")
- displayHeader()    // Tampilkan header dengan border
- readString()       // Input string dari user
- readInteger()      // Input integer dari user
- waitForEnter()     // Tunggu user tekan enter
- readMenuChoice()   // Baca pilihan menu 0-8
```

**Kenapa perlu file ini?**
- Supaya file lain bisa tahu struktur data apa yang ada
- Supaya main.cpp tahu fungsi apa aja yang bisa dipanggil
- Cukup `#include "katalog.h"` → semua deklarasi langsung tersedia

---

### 2️⃣ **katalog.cpp** (Implementation File - 436 baris)
**Fungsi:** Implementasi SEMUA fungsi yang dideklarasikan di katalog.h

**Isi:**
```cpp
#include "katalog.h"    // Ambil deklarasi dari header

// IMPLEMENTASI FUNGSI DASAR
createList()            // Set L.first = nullptr
createElementArtis()    // new elmArtis + alokasi laguArray[100]
insertLastArtis()       // Traverse sampai last → insert → saveToCSV()

// IMPLEMENTASI CRUD - READ
searchArtis()           // Loop + case-insensitive compare
showAllData()           // Tampilkan semua artis + lagu
showReport()            // Statistik total artis & lagu

// IMPLEMENTASI CRUD - UPDATE
updateArtisInfo()       // Cari → update info → saveToCSV()

// IMPLEMENTASI CRUD - DELETE
deleteArtis()           // Hapus node + delete[] laguArray
deleteLagu()            // Cari index → shift array kiri
deallocateList()        // Loop semua node → delete satu-satu

// IMPLEMENTASI FILE I/O
loadFromCSV()           // Baca file → parse → insert ke list
saveToCSV()             // Loop list → tulis ke file

// IMPLEMENTASI INSERT LAGU
insertLagu()            // Tambah ke laguArray[jumlahLagu]
insertLaguNoSave()      // Sama tapi tanpa save (untuk loading)

// IMPLEMENTASI COUNTING
countTotalArtis()       // Hitung jumlah node
countTotalLagu()        // Sum semua jumlahLagu dari tiap artis

// IMPLEMENTASI HELPER
displayMenu()           // Cetak menu 0-8
exitProgram()           // Pesan exit + saveToCSV()
```

**Kenapa perlu file ini?**
- Memisahkan deklarasi (katalog.h) dengan implementasi (katalog.cpp)
- File jadi lebih terorganisir dan mudah di-maintain
- Kalau mau ubah cara kerja fungsi, cukup edit di sini

---

### 3️⃣ **main.cpp** (Main Program - 169 baris)
**Fungsi:** Entry point program, menu loop, dan orchestrator

**Isi:**
```cpp
#include "katalog.h"    // Biar bisa pakai semua fungsi

int main() {
    // DEKLARASI VARIABEL
    List L;                      // List utama
    string filename = "music_db.csv";
    int pilihan;                 // Input menu user
    string nama, genre, judul;   // Input data dari user
    int tahun;
    adrArtis pFound;             // Pointer hasil search
    
    // INISIALISASI
    createList(L);               // L.first = nullptr
    loadFromCSV(L, filename);    // Load data dari file
    
    // MENU LOOP (do-while)
    do {
        clearScreen();
        displayMenu();
        pilihan = readMenuChoice();
        
        switch (pilihan) {
            case 1:  // Tambah Artis
                input data → createElementArtis() → insertLastArtis()
                
            case 2:  // Tambah Lagu
                input nama → searchArtis() → insertLagu()
                
            case 3:  // Hapus Artis
                input nama → deleteArtis()
                
            case 4:  // Hapus Lagu
                input nama → searchArtis() → 
                verifikasi jumlahLagu > 0 → deleteLagu()
                
            case 5:  // Lihat Semua
                showAllData()
                
            case 6:  // Cari Artis
                input nama → searchArtis() → tampilkan detail
                
            case 7:  // Statistik
                showReport()
                
            case 8:  // Update Artis
                input data → updateArtisInfo()
                
            case 0:  // Keluar
                exitProgram()
                
            default:
                "Pilihan tidak valid"
        }
        
        if (pilihan != 0) {
            waitForEnter();      // Pause sebelum loop lagi
        }
        
    } while (pilihan != 0);      // Loop sampai user pilih 0
    
    // CLEANUP
    deallocateList(L);           // Hapus semua memory
    return 0;
}
```

**Kenapa perlu file ini?**
- Entry point: program dimulai dari `int main()`
- Mengatur alur program (inisialisasi → loop menu → cleanup)
- Menghubungkan user input dengan fungsi-fungsi yang ada

---

### 4️⃣ **music_db.csv** (Data File)
**Fungsi:** Penyimpanan data persisten

**Format:**
```
NamaArtis;Genre;TahunDebut;JudulLagu
Taylor Swift;Pop;2006;Love Story
Taylor Swift;Pop;2006;Shake It Off
Taylor Swift;Pop;2006;Anti-Hero
Drake;Hip-Hop;2006;Hotline Bling
Ariana Grande;Pop;2011;Belum Ada Lagu
```

**Aturan:**
- Delimiter: `;` (semicolon)
- 1 baris = 1 lagu
- Artis tanpa lagu ditulis sebagai: `NamaArtis;Genre;Tahun;Belum Ada Lagu`
- Kalau artis punya 3 lagu → 3 baris dengan nama artis yang sama

**Kapan file ini diakses?**
- **Load:** Saat program start (`loadFromCSV()`)
- **Save:** Setiap kali ada perubahan data (insert, update, delete)

---

## 🔗 HUBUNGAN ANTAR FILE

```
┌─────────────────────────────────────────────────────────────┐
│                        main.cpp                             │
│  - Entry point program                                      │
│  - Menu loop (do-while)                                     │
│  - Panggil fungsi-fungsi dari katalog.h/cpp                │
└────────────────────────┬────────────────────────────────────┘
                         │ #include "katalog.h"
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                       katalog.h                             │
│  - Deklarasi struct (infoArtis, elmArtis, List)            │
│  - Prototype fungsi (createList, insertLagu, dll)          │
│  - Inline utility functions (clearScreen, readString)      │
└────────────────────────┬────────────────────────────────────┘
                         │ #include "katalog.h"
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                      katalog.cpp                            │
│  - Implementasi SEMUA fungsi                                │
│  - CRUD operations                                          │
│  - File I/O (loadFromCSV, saveToCSV)                       │
│  - Memory management (deallocateList)                       │
└────────────────────────┬────────────────────────────────────┘
                         │ read/write
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                    music_db.csv                             │
│  - Data storage (artis + lagu)                             │
│  - Format: Nama;Genre;Tahun;Judul                          │
│  - Auto-save setiap perubahan                              │
└─────────────────────────────────────────────────────────────┘
```

---

## �📌 STRUKTUR DATA

### Parent (Artis) - Linked List
```cpp
struct elmArtis {
    infoArtis info;      // Nama, genre, tahunDebut
    string* laguArray;   // Array dinamis untuk lagu
    int jumlahLagu;      // Counter lagu
    adrArtis next;       // Pointer ke artis berikutnya
};
```

### Child (Lagu) - Array Dinamis
- Setiap artis punya **array dinamis** (maks 100 lagu)
- Lagu disimpan sebagai `string` di dalam `laguArray`

---

## 🔧 FUNGSI UTAMA

### CREATE
| Fungsi | Parameter | Return | Keterangan |
|--------|-----------|--------|------------|
| `createList(L)` | `List &L` | `void` | Inisialisasi list kosong |
| `createElementArtis(nama, genre, tahun)` | `string, string, int` | `adrArtis` | Buat node artis baru |
| `insertLastArtis(L, P, file)` | `List &L, adrArtis P, string` | `void` | Insert artis + auto-save |
| `insertLagu(P, judul, L, file)` | `adrArtis P, string, List, string` | `void` | Tambah lagu ke array |

### READ
| Fungsi | Parameter | Return | Keterangan |
|--------|-----------|--------|------------|
| `searchArtis(L, nama)` | `List L, string` | `adrArtis` | Cari artis (case-insensitive) |
| `showAllData(L)` | `List L` | `void` | Tampilkan semua data |
| `showReport(L)` | `List L` | `void` | Laporan statistik |

### UPDATE
| Fungsi | Parameter | Return | Keterangan |
|--------|-----------|--------|------------|
| `updateArtisInfo(L, nama, genre, tahun, file)` | `List &L, string, string, int, string` | `void` | Update info artis + save |

### DELETE
| Fungsi | Parameter | Return | Keterangan |
|--------|-----------|--------|------------|
| `deleteArtis(L, nama, file)` | `List &L, string, string` | `void` | Hapus artis + semua lagunya |
| `deleteLagu(P, judul, L, file)` | `adrArtis P, string, List, string` | `void` | Hapus 1 lagu dari array |
| `deallocateList(L)` | `List &L` | `void` | Bersihkan memory sebelum exit |

### FILE I/O
| Fungsi | Parameter | Return | Keterangan |
|--------|-----------|--------|------------|
| `loadFromCSV(L, file)` | `List &L, string` | `void` | Load data dari CSV |
| `saveToCSV(L, file)` | `List L, string` | `void` | Save data ke CSV |

### COUNTING
| Fungsi | Parameter | Return | Keterangan |
|--------|-----------|--------|------------|
| `countTotalArtis(L)` | `List L` | `int` | Hitung jumlah artis |
| `countTotalLagu(L)` | `List L` | `int` | Hitung total semua lagu |

---

## 🎯 MENU PROGRAM

| No | Menu | Operasi CRUD |
|----|------|--------------|
| 1 | Tambah Artis | **CREATE** artis |
| 2 | Tambah Lagu | **CREATE** lagu (child) |
| 3 | Hapus Artis | **DELETE** artis + lagu |
| 4 | Hapus Lagu | **DELETE** lagu dari array |
| 5 | Lihat Semua Data | **READ** all |
| 6 | Cari Artis | **READ** specific |
| 7 | Statistik | **READ** report |
| 8 | Update Info Artis | **UPDATE** artis |
| 0 | Keluar | Auto-save + deallocate |

---

## ⚙️ CARA KERJA PROGRAM

### 1. Inisialisasi
```cpp
List L;
createList(L);           // L.first = nullptr
loadFromCSV(L, file);    // Load data dari CSV
```

### 2. Loop Menu (do-while)
```cpp
do {
    displayMenu();       // Tampilkan menu
    pilihan = input();   // User pilih 0-8
    switch (pilihan) {   // Proses pilihan
        case 1: ...      // Tambah artis
        case 0: ...      // Exit
    }
    waitForEnter();      // Tunggu enter (kecuali exit)
} while (pilihan != 0);  // Loop sampai pilih 0
```

### 3. Cleanup
```cpp
deallocateList(L);       // Hapus semua node + array
return 0;                // Exit program
```

---

## 🔍 VERIFIKASI 2 LANGKAH

### Contoh: Delete Lagu
```cpp
// LANGKAH 1: Cek artis ada?
pFound = searchArtis(L, nama);
if (pFound != nullptr) {
    
    // LANGKAH 2: Cek punya lagu?
    if (pFound->jumlahLagu == 0) {
        cout << "Belum memiliki lagu";
    } else {
        deleteLagu(pFound, judul, L, file);
    }
}
```

---

## 📁 FORMAT CSV

```
NamaArtis;Genre;TahunDebut;JudulLagu
Taylor Swift;Pop;2006;Love Story
Taylor Swift;Pop;2006;Shake It Off
Drake;Hip-Hop;2006;Belum Ada Lagu
```

**Aturan:**
- Delimiter: `;`
- 1 baris = 1 lagu
- Artis tanpa lagu: `Belum Ada Lagu`

---

## 💡 TIPS

### Pointer vs Reference
```cpp
void func(List &L)      // Reference: ubah langsung
void func(List L)       // Copy: tidak ubah original
```

### Default Parameter
```cpp
void save(List L, string file = "music_db.csv")
// Bisa dipanggil: save(L) atau save(L, "custom.csv")
```

### Inline Function
```cpp
inline void clearScreen() { system("cls"); }
// Fungsi kecil, compiled langsung tanpa overhead
```

### Dynamic Memory
```cpp
adrArtis p = new elmArtis;      // Alokasi
p->laguArray = new string[100]; // Alokasi array
delete[] p->laguArray;          // Dealokasi array
delete p;                       // Dealokasi node
```

---

## ⚠️ COMMON ERRORS

| Error | Penyebab | Solusi |
|-------|----------|--------|
| Segmentation Fault | Akses pointer `nullptr` | Cek `if (p != nullptr)` |
| Memory Leak | Lupa `delete` | Panggil `deallocateList()` |
| File not found | CSV tidak ada | Program auto-create |
| Lagu tidak muncul | "Belum Ada Lagu" masuk array | Fixed: cek `judul != "Belum Ada Lagu"` |

---

## 📊 KOMPLEKSITAS

| Operasi | Kompleksitas |
|---------|--------------|
| Insert Last Artis | O(n) - traverse sampai last |
| Search Artis | O(n) - linear search |
| Delete Artis | O(n) - search + delete |
| Insert Lagu | O(1) - langsung ke index |
| Delete Lagu | O(m) - shift array (m = jumlah lagu) |
| Count Artis | O(n) - traverse semua |
| Count Lagu | O(n) - traverse + sum array |

---

**Last Updated:** January 2, 2026  
**Structure:** Multi-Linked List (MLL) 1-N with Dynamic Array
