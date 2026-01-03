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

## 🎯 SKENARIO MODIFIKASI DOSEN

### Skenario 1️⃣: "Ubah Posisi Masuk (Insert First)"

**Permintaan Dosen:**
> "Mas Hanif, ini insertLastArtis kan masukin datanya ke belakang terus. Saya mau Artis yang baru diinput langsung jadi urutan nomor 1 (Masuk Depan). Ubah kodingannya sekarang."

**Analisa:** Kamu harus mengubah logika dari "Looping sampai ujung" menjadi "Langsung tembak depan".

**Langkah:**
1. Buka [katalog.cpp](katalog.cpp)
2. Cari fungsi `void insertLastArtis`
3. HAPUS/KOMENTAR semua logika `while` yang panjang itu
4. Ganti dengan logika Insert First yang simpel

**Kunci Jawaban:**
```cpp
void insertLastArtis(List &L, adrArtis P, const string &filename) {
    // LOGIKA LAMA (MATIKAN INI):
    /*
    if (L.first == nullptr) {
        L.first = P;
    } else {
        adrArtis Q = L.first;
        while (Q->next != nullptr) {
            Q = Q->next;
        }
        Q->next = P;
    }
    */

    // GANTI JADI INI (INSERT FIRST):
    P->next = L.first; // 1. Sambungkan P ke node pertama lama
    L.first = P;       // 2. Pindahkan bendera First ke P
    
    cout << "  Artis '" << P->info.nama << "' ditambahkan di DEPAN" << endl;
    saveToCSV(L, filename);
}
```

---

### Skenario 2️⃣: "Filter Tampilan (Hanya Artis Senior)"

**Permintaan Dosen:**
> "Mas, di menu 'Lihat Semua Data', saya pusing liatnya kebanyakan. Tolong tampilkan CUMA artis yang debut sebelum tahun 2000."

**Analisa:** Kamu tidak perlu hapus data, cuma memfilter apa yang di-cout.

**Langkah:**
1. Buka [katalog.cpp](katalog.cpp)
2. Cari fungsi `void showAllData`
3. Lihat loop `while (P != nullptr)`
4. Selipkan `if` sebelum melakukan `cout`

**Kunci Jawaban:**
```cpp
void showAllData(List L) {
    // ... (kode header) ...
    adrArtis P = L.first;
    while (P != nullptr) {
        // TAMBAHKAN IF INI:
        if (P->info.tahunDebut < 2000) {  // <--- KUNCINYA DISINI
            
            // Masukkan semua kodingan cout di dalam kurung kurawal if ini
            artistCount++;
            cout << "\n  [" << artistCount << "] " << P->info.nama << endl;
            cout << "     Genre: " << P->info.genre << endl;
            cout << "     Tahun Debut: " << P->info.tahunDebut << endl;
            // ... dst ...
        }
        
        P = P->next; // P->next WAJIB DI LUAR IF, biar loop jalan terus
    }
    // ...
}
```

---

### Skenario 3️⃣: "Batasi Jumlah Lagu (Array Logic)"

**Permintaan Dosen:**
> "Mas, ini lagu kok bisa nambah terus sampai ribuan (resize)? Saya mau hemat memori. Ubah kodingannya: Maksimal 1 artis cuma boleh punya 5 lagu. Kalau user input lagu ke-6, tolak!"

**Analisa:** Ini menyerang kelemahan Dynamic Array kamu. Dosen minta logika resize-nya dimatikan.

**Langkah:**
1. Buka [katalog.cpp](katalog.cpp)
2. Cari fungsi `void insertLagu`
3. Lihat bagian `if (P->jumlahLagu >= P->kapasitas)` → Itu logika resize
4. Matikan resize, ganti dengan logika batas

**Kunci Jawaban:**
```cpp
void insertLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    if (P == nullptr) return;

    // LOGIKA LAMA (RESIZE) - MATIKAN INI:
    /*
    if (P->jumlahLagu >= P->kapasitas) {
       // ... kode resize panjang ...
    }
    */

    // GANTI JADI LOGIKA BATAS (FIXED):
    if (P->jumlahLagu >= 5) { // Atau pakai P->kapasitas
        cout << "  [ERROR] Memori Penuh! Maksimal 5 lagu." << endl;
        return; // Stop fungsi, jangan lanjut
    }

    // Lanjut ke bawah (P->laguArray[P->jumlahLagu] = judul; ...)
    P->laguArray[P->jumlahLagu] = judul;
    P->jumlahLagu++;
    cout << "  Lagu '" << judul << "' ditambahkan" << endl;
    saveToCSV(L, filename);
}
```

---

### Skenario 4️⃣: "Tambah Data Negara (Modifikasi Struct)"

**Permintaan Dosen:**
> "Tambahkan data 'Negara Asal' untuk setiap artis. Ubah struct, input, dan tampilannya."

**Analisa:** Ini paling capek karena harus ubah 3 file (.h, .cpp, main). Tapi logikanya gampang.

**Langkah (Ikuti urutan ini biar gak error):**

**1. Buka [katalog.h](katalog.h) (Struct):**
```cpp
struct infoArtis {
    string nama;
    string genre;
    int tahunDebut;
    string negara; // <--- TAMBAH INI
};
```

**2. Buka [katalog.cpp](katalog.cpp) (Create Element):**
- Ubah parameter fungsi: `createElementArtis(..., int tahun, string negara)`
- Di dalam fungsi tambah: `P->info.negara = negara;`

```cpp
adrArtis createElementArtis(string nama, string genre, int tahun, string negara) {
    adrArtis P = new elmArtis;
    P->info.nama = nama;
    P->info.genre = genre;
    P->info.tahunDebut = tahun;
    P->info.negara = negara; // <--- TAMBAH INI
    P->next = nullptr;
    P->laguArray = new string[100];
    P->jumlahLagu = 0;
    P->kapasitas = 100;
    return P;
}
```

**3. Buka [main.cpp](main.cpp) (Menu 1):**
```cpp
// Di case 1:
nama = readString("  Nama: ");
genre = readString("  Genre: ");
string negara = readString("  Negara: "); // <--- TAMBAH INPUT
tahun = readInteger("  Tahun debut: ");

// Masukkan ke parameter
insertLastArtis(L, createElementArtis(nama, genre, tahun, negara), filename);
```

**4. Buka [katalog.cpp](katalog.cpp) (Show Data):**
- Tambahkan cout negara di fungsi `showAllData`:

```cpp
void showAllData(List L) {
    // ...
    while (P != nullptr) {
        artistCount++;
        cout << "\n  [" << artistCount << "] " << P->info.nama << endl;
        cout << "     Genre: " << P->info.genre << endl;
        cout << "     Tahun Debut: " << P->info.tahunDebut << endl;
        cout << "     Negara: " << P->info.negara << endl; // <--- TAMBAH INI
        // ...
    }
}
```

**5. Update CSV Loading:**
- Di `loadFromCSV()`, tambah parsing untuk negara:
```cpp
// Parsing line → tambahkan getline untuk negara
getline(ss, nama, ',');
getline(ss, genre, ',');
ss >> tahun; ss.ignore();
getline(ss, negara, ','); // <--- TAMBAH INI
```

---

## 💡 TIPS MENGHADAPI SKENARIO DOSEN

| Tipe Modifikasi | File yang Berubah | Tingkat Kesulitan |
|----------------|-------------------|-------------------|
| Ubah logika insert/delete | katalog.cpp | ⭐⭐ |
| Filter data tampilan | katalog.cpp (showAllData) | ⭐ |
| Batasi kapasitas array | katalog.cpp (insertLagu) | ⭐⭐ |
| Tambah field struct | katalog.h + katalog.cpp + main.cpp | ⭐⭐⭐⭐ |

**Prinsip Emas:**
1. **Pahami struktur data** → Tahu dimana data disimpan
2. **Trace alur fungsi** → Tahu fungsi mana yang dipanggil
3. **Test step by step** → Jangan langsung run semua
4. **Backup sebelum ubah** → Copy file dulu sebelum modif

---

**Last Updated:** January 3, 2026  
**Structure:** Multi-Linked List (MLL) 1-N with Dynamic Array
