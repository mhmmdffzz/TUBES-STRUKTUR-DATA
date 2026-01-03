# 📋 CHEATSHEET - KATALOG MUSIK (MLL 1-N)

## 🆕 UPDATE TERBARU v2.0 - NESTED MENU SYSTEM

### ⭐ **APA YANG BERUBAH?**

#### 🔄 **PERUBAHAN 1: Nested Menu (Menu Bertingkat)**

**SEBELUM (Versi Lama):**
```
Menu Utama (Flat - 8 pilihan):
[1] Tambah Artis Baru & Lagu
[2] Lihat Semua Data Katalog
[3] Hapus Lagu dari Artis
[4] Hapus Artis dari Katalog
[5] Cari Artis di Katalog
[6] Lihat Laporan Statistik
[7] Update Info Artis
[0] Keluar
```

**SESUDAH (Versi Baru):**
```
Menu Utama (Nested - 6 pilihan):
[1] Kelola Data Artis & Lagu   → SUB-MENU
    ↳ [1] Tambah Artis Baru
    ↳ [2] Tambah Lagu ke Artis Lama
    ↳ [0] Kembali ke Menu Utama
    
[2] Lihat Semua Data Katalog

[3] Hapus Data Artis & Lagu    → SUB-MENU
    ↳ [1] Hapus Lagu dari Artis
    ↳ [2] Hapus Artis dari Katalog
    ↳ [0] Kembali ke Menu Utama
    
[4] Cari Artis di Katalog
[5] Lihat Laporan Statistik
[6] Update Info Artis
[0] Keluar
```

**Implementasi di katalog.cpp:**
```cpp
// Fungsi baru yang ditambahkan:
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
```

---

#### 🔄 **PERUBAHAN 2: Logika Khusus Tanda "-" untuk Skip Lagu Pertama**

**SEBELUM:**
```cpp
// Di menu Tambah Artis:
// User WAJIB input lagu atau manual skip
// Tidak ada logika khusus
```

**SESUDAH:**
```cpp
// Di sub-menu [1] Tambah Artis Baru:
cout << "  Masukkan Lagu Pertama (atau ketik '-' untuk lewati): ";
getline(cin, judul);

// LOGIKA PENTING: Cek tanda strip "-"
if (judul == "-") {
    // Array lagu dibiarkan kosong (jumlahLagu = 0)
    cout << "\n  Artis ditambahkan tanpa lagu." << endl;
} else if (!judul.empty()) {
    // Masukkan lagu ke array
    newArtis->laguArray[0] = judul;
    newArtis->jumlahLagu = 1;
}
```

**Contoh Output:**
```
Masukkan Lagu Pertama (atau ketik '-' untuk lewati): -
Artis 'Michael Jackson' ditambahkan tanpa lagu.
```

---

#### 🔄 **PERUBAHAN 3: Loop Input Lagu Tanpa Batas**

**SEBELUM:**
```cpp
// Menu [2] Tambah Lagu ke Artis:
// - User input SATU lagu
// - Keluar dari menu
// - Kalau mau tambah lagi, harus masuk menu lagi
```

**SESUDAH:**
```cpp
// Sub-menu [2] Tambah Lagu ke Artis Lama:
// LOOP sampai user ketik "0"
while (true) {
    cout << "  Judul lagu [" << (pFound->jumlahLagu + 1) << "]: ";
    getline(cin, judul);
    
    if (judul == "0") {
        cout << "\n  Selesai menambahkan lagu." << endl;
        break;
    }
    
    if (judul.empty()) {
        cout << "  Input tidak boleh kosong! (Ketik '0' untuk selesai)" << endl;
        continue;
    }
    
    // Tambahkan lagu (array akan auto-expand jika penuh)
    insertLagu(pFound, judul, L, filename);
}
```

**Contoh Output:**
```
TAMBAH LAGU (Ketik '0' untuk selesai)
Judul lagu [1]: Shape of You
Lagu 'Shape of You' berhasil ditambahkan!
Judul lagu [2]: Perfect
Lagu 'Perfect' berhasil ditambahkan!
Judul lagu [3]: Thinking Out Loud
Lagu 'Thinking Out Loud' berhasil ditambahkan!
Judul lagu [4]: 0

Selesai menambahkan lagu.
Total lagu untuk 'Ed Sheeran': 3
```

---

### 📊 **PERBANDINGAN VERSI LAMA vs BARU**

| Aspek | Versi Lama | Versi Baru (v2.0) |
|-------|-----------|-------------------|
| **Menu Utama** | 8 menu flat | 6 menu + 2 sub-menu |
| **Tambah Artis** | Langsung dari menu utama | Dalam sub-menu "Kelola Data" |
| **Tambah Lagu** | Menu terpisah, 1 lagu per eksekusi | Sub-menu dengan loop unlimited |
| **Hapus Data** | 2 menu terpisah di utama | 1 menu dengan 2 sub-pilihan |
| **Lagu Pertama** | Input manual, tidak bisa skip clean | Ketik "-" untuk skip dengan logika |
| **Jumlah Input Lagu** | 1 lagu → keluar → masuk lagi | Unlimited sampai ketik "0" |
| **User Flow** | Banyak navigasi berulang | Efisien, semua di dalam sub-menu |
| **Kode Main.cpp** | Switch-case sederhana | Nested switch-case + loop |

---

### 🔧 **KODE YANG BERUBAH**

#### **File: katalog.h**
```cpp
// TAMBAHAN PROTOTYPE:
void displaySubMenuHapus();  // Sub-menu untuk hapus data
```

#### **File: katalog.cpp**
```cpp
// FUNGSI BARU:
void displaySubMenuHapus() {
    displaySubHeader("SUB-MENU: HAPUS DATA");
    cout << "\n  [1] Hapus Lagu dari Artis" << endl;
    cout << "  [2] Hapus Artis dari Katalog" << endl;
    cout << "  [0] Kembali ke Menu Utama" << endl;
    cout << "\n  >> Pilihan: ";
}

// FUNGSI DIUPDATE:
void displayMenu() {
    displayHeader("*** KATALOG MUSIK DIGITAL ***");
    cout << "\n  [1] Kelola Data Artis & Lagu" << endl;  // ← BARU
    cout << "  [2] Lihat Semua Data Katalog" << endl;
    cout << "  [3] Hapus Data Artis & Lagu" << endl;     // ← BARU
    cout << "  [4] Cari Artis di Katalog" << endl;
    cout << "  [5] Lihat Laporan Statistik" << endl;
    cout << "  [6] Update Info Artis" << endl;
    cout << "  [0] Keluar dari Program" << endl;
    cout << "\n  >> Pilihan: ";
}
```

#### **File: main.cpp - Case 1 (Nested Menu Kelola Data)**
```cpp
case 1: {
    // SUB-MENU: Kelola Data Artis & Lagu
    int subPilihan;
    do {
        clearScreen();
        displaySubMenu();
        subPilihan = readMenuChoice();
        
        switch (subPilihan) {
            case 1: {
                // Tambah Artis Baru
                // ... (lihat kode lengkap di main.cpp)
                
                // LOGIKA BARU: Tanda "-" untuk skip lagu
                cout << "  Masukkan Lagu Pertama (atau ketik '-' untuk lewati): ";
                getline(cin, judul);
                
                if (judul == "-") {
                    cout << "  Artis ditambahkan tanpa lagu." << endl;
                } else if (!judul.empty()) {
                    newArtis->laguArray[0] = judul;
                    newArtis->jumlahLagu = 1;
                }
                break;
            }
            
            case 2: {
                // Tambah Lagu ke Artis Lama
                // LOGIKA BARU: Loop input lagu
                while (true) {
                    cout << "  Judul lagu [" << (pFound->jumlahLagu + 1) << "]: ";
                    getline(cin, judul);
                    
                    if (judul == "0") {
                        break;
                    }
                    
                    insertLagu(pFound, judul, L, filename);
                }
                break;
            }
            
            case 0: {
                // Kembali ke menu utama
                break;
            }
        }
        
        if (subPilihan != 0) {
            waitForEnter();
        }
        
    } while (subPilihan != 0);
    break;
}
```

#### **File: main.cpp - Case 3 (Nested Menu Hapus Data)**
```cpp
case 3: {
    // SUB-MENU: Hapus Data Artis & Lagu
    int subPilihan;
    do {
        clearScreen();
        displaySubMenuHapus();
        subPilihan = readMenuChoice();
        
        switch (subPilihan) {
            case 1: {
                // Hapus Lagu dari Artis
                // ... (kode seperti versi lama)
                break;
            }
            
            case 2: {
                // Hapus Artis dari Katalog
                // ... (kode seperti versi lama)
                break;
            }
            
            case 0: {
                // Kembali ke menu utama
                break;
            }
        }
        
        if (subPilihan != 0) {
            waitForEnter();
        }
        
    } while (subPilihan != 0);
    break;
}
```

---

### 🎯 **KEUNTUNGAN UPDATE INI**

| Keuntungan | Penjelasan |
|-----------|------------|
| **✅ Organisasi Lebih Baik** | Fitur serupa (tambah/hapus) dikelompokkan dalam sub-menu |
| **✅ User Experience** | User bisa tambah 10, 20, 50 lagu tanpa keluar-masuk menu |
| **✅ Fleksibilitas** | Artis bisa dibuat tanpa lagu (ketik "-") |
| **✅ Efisiensi** | Tidak perlu re-navigate menu berkali-kali |
| **✅ Code Organization** | Nested pattern yang konsisten di semua menu |
| **✅ Array Unlimited** | Auto-expand tetap bekerja (5→10→20→40...) |

---

### 💡 **TIPS MODIFIKASI LANJUTAN**

#### **Skenario 1: Tambah Validasi di Loop Input Lagu**
```cpp
// Contoh: Cek lagu duplikat
bool isDuplicate = false;
for (int i = 0; i < pFound->jumlahLagu; i++) {
    if (pFound->laguArray[i] == judul) {
        isDuplicate = true;
        break;
    }
}

if (isDuplicate) {
    cout << "  ERROR: Lagu sudah ada dalam daftar!" << endl;
    continue; // Skip ke input berikutnya
}
```

#### **Skenario 2: Konfirmasi Sebelum Kembali**
```cpp
case 0: {
    char konfirmasi;
    cout << "  Kembali ke menu utama? (y/n): ";
    cin >> konfirmasi;
    cin.ignore();
    
    if (konfirmasi == 'y' || konfirmasi == 'Y') {
        kembali = true;
    }
    break;
}
```

#### **Skenario 3: Batasi Jumlah Lagu Per Sesi**
```cpp
// Di loop input lagu:
int maxLaguPerSesi = 10;
int counter = 0;

while (true && counter < maxLaguPerSesi) {
    // ... input lagu ...
    counter++;
}

if (counter >= maxLaguPerSesi) {
    cout << "  Batas maksimal " << maxLaguPerSesi << " lagu per sesi tercapai!" << endl;
}
```

---

## 📂 STRUKTUR FILE PROJECT

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

### Skenario 5️⃣: "Cari Artis Paling Produktif"

**Permintaan Dosen:**
> "Mas, saya penasaran siapa artis yang paling rajin bikin lagu (jumlah lagunya paling banyak). Tolong buatkan satu menu kecil atau fungsi untuk menampilkan satu nama artis dengan lagu terbanyak."

**Analisa:** Kamu butuh algoritma **Maximum Value Search**. Kamu harus looping dari awal sampai akhir, sambil memegang satu variabel penampung "Juara Sementara".

**Kunci Jawaban:**
```cpp
void showMostProductive(List L) {
    if (L.first == nullptr) {
        cout << "Data Kosong." << endl;
        return;
    }

    adrArtis P = L.first;
    adrArtis Juara = L.first; // Anggap orang pertama itu juara sementara

    while (P != nullptr) {
        // Jika nemu yang lagunya lebih banyak dari Juara saat ini
        if (P->jumlahLagu > Juara->jumlahLagu) {
            Juara = P; // Pemenang diganti
        }
        P = P->next;
    }

    cout << "Artis Terajin: " << Juara->info.nama 
         << " (" << Juara->jumlahLagu << " lagu)" << endl;
}
```

**Cara Implementasi:**
1. Tambahkan prototype di `katalog.h`: `void showMostProductive(List L);`
2. Implementasi fungsi di `katalog.cpp`
3. Tambahkan menu baru di `main.cpp` atau panggil dari menu statistik

---

### Skenario 6️⃣: "Hapus Lagu Terakhir (Undo)"

**Permintaan Asisten:**
> "Mas, kalau saya salah input lagu ke-5, masa saya harus hapus artisnya? Tolong buatkan fitur untuk menghapus hanya lagu terakhir yang baru saja dimasukkan ke artis tertentu."

**Analisa:** Ini jebakan. Kamu **TIDAK PERLU** menghapus string-nya dari memori array secara fisik. Kamu cukup mengurangi counter `jumlahLagu`. Data lama akan tertimpa sendiri kalau nanti ada input baru.

**Kunci Jawaban:**
```cpp
void deleteLastSong(adrArtis P, List &L, const string &filename) {
    if (P == nullptr) {
        cout << "Artis tidak valid." << endl;
        return;
    }
    
    if (P->jumlahLagu > 0) {
        // CUKUP KURANGI COUNTERNYA
        P->jumlahLagu--; 
        
        cout << "Lagu terakhir berhasil dihapus (di-undo)." << endl;
        cout << "Jumlah lagu sekarang: " << P->jumlahLagu << endl;
        
        // Secara teknis datanya masih ada di array, 
        // tapi tidak akan tampil karena loop tampilan dibatasi 'jumlahLagu'
        saveToCSV(L, filename); // Save perubahan
    } else {
        cout << "Artis ini belum punya lagu." << endl;
    }
}
```

**Cara Pakai:**
```cpp
// Di main.cpp, tambah menu baru:
case X: {
    clearScreen();
    displayHeader("UNDO LAGU TERAKHIR");
    nama = readString("  Nama artis: ");
    pFound = searchArtis(L, nama);
    
    if (pFound != nullptr) {
        deleteLastSong(pFound, L, filename);
    } else {
        cout << "  Artis tidak ditemukan!" << endl;
    }
    break;
}
```

---

### Skenario 7️⃣: "Insert After (Sisip Tengah)"

**Permintaan Dosen:**
> "Mas, InsertLast itu biasa. Saya mau kalau nambah Artis baru, posisinya harus setelah Artis yang saya tentukan. Misal: Masukkan 'Tulus' setelah 'Noah'."

**Analisa:** Ini mainan **Pointer Next**. Kamu perlu pointer `P` (Artis Baru) dan `Prec` (Artis Sebelumnya/Predecessor).

**Kunci Jawaban:**
```cpp
void insertAfterArtis(List &L, adrArtis Prec, adrArtis P, const string &filename) {
    if (Prec == nullptr || P == nullptr) {
        cout << "Pointer tidak valid!" << endl;
        return;
    }
    
    // Logika: P disambung ke kanannya Prec, baru Prec disambung ke P
    P->next = Prec->next;
    Prec->next = P;
    
    cout << "Artis '" << P->info.nama << "' berhasil disisipkan setelah '" 
         << Prec->info.nama << "'" << endl;
    saveToCSV(L, filename);
}
```

**Cara Panggil di Main:**
```cpp
// Contoh penggunaan:
// 1. Buat P (createElementArtis) -> 'Tulus'
adrArtis newArtis = createElementArtis("Tulus", "Pop", 2011);

// 2. Cari Prec (searchArtis) -> 'Noah'
adrArtis predecessor = searchArtis(L, "Noah");

if (predecessor != nullptr) {
    // 3. insertAfterArtis(L, Prec, P, filename);
    insertAfterArtis(L, predecessor, newArtis, filename);
} else {
    cout << "Artis 'Noah' tidak ditemukan!" << endl;
}
```

---

### Skenario 8️⃣: "Rename Artis (Update Data)"

**Permintaan Asisten:**
> "Mas, ini nama artisnya typo. 'Noah' ditulis 'Noak'. Saya gak mau hapus dan bikin ulang karena lagunya udah banyak. Bikin fitur Ganti Nama Artis dong."

**Analisa:** Ini sangat simpel tapi sering bikin panik. Kamu cuma butuh **Search** lalu **Assign** nilai baru. Tidak perlu ubah pointer.

**Kunci Jawaban:**
```cpp
void updateNamaArtis(List L, const string &namaLama, const string &namaBaru, const string &filename) {
    adrArtis P = searchArtis(L, namaLama);
    
    if (P != nullptr) {
        P->info.nama = namaBaru; // <--- CUMA INI KUNCINYA
        cout << "Nama berhasil diubah dari '" << namaLama 
             << "' menjadi '" << namaBaru << "'" << endl;
        saveToCSV(L, filename);
    } else {
        cout << "Artis '" << namaLama << "' tidak ditemukan." << endl;
    }
}
```

**Implementasi di Menu:**
```cpp
case X: {
    clearScreen();
    displayHeader("RENAME ARTIS");
    string namaLama = readString("  Nama artis saat ini: ");
    string namaBaru = readString("  Nama baru: ");
    
    updateNamaArtis(L, namaLama, namaBaru, filename);
    break;
}
```

---

### Skenario 9️⃣: "Validasi Lagu Kembar (Anti Duplikat)"

**Permintaan Dosen:**
> "Mas, coba lihat array lagumu. Kalau saya input lagu 'Separuh Aku' dua kali ke artis 'Noah', dia mau masuk kan? Itu bug. Tolong cegah lagu kembar dalam satu artis."

**Analisa:** Sebelum baris `P->laguArray[P->jumlahLagu] = judul`, kamu harus melakukan **Looping kecil** (Sequential Search) di dalam array si Artis itu.

**Kunci Jawaban - Modifikasi di fungsi insertLagu:**
```cpp
void insertLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    if (P == nullptr) return;
    
    // CEK DUPLIKASI DULU
    for (int i = 0; i < P->jumlahLagu; i++) {
        if (P->laguArray[i] == judul) {
            cout << "  [ERROR] Lagu '" << judul << "' sudah ada! Gagal menambahkan." << endl;
            return; // Langsung keluar fungsi
        }
    }

    // Check if array needs to be resized
    if (P->jumlahLagu >= P->kapasitas) {
        int newKapasitas = P->kapasitas * 2;
        string* newArray = new string[newKapasitas];
        
        for (int i = 0; i < P->jumlahLagu; i++) {
            newArray[i] = P->laguArray[i];
        }
        
        delete[] P->laguArray;
        P->laguArray = newArray;
        P->kapasitas = newKapasitas;
    }
    
    // Kalau lolos validasi duplikasi, baru masukkan
    P->laguArray[P->jumlahLagu] = judul;
    P->jumlahLagu++;
    
    cout << "  Lagu '" << judul << "' berhasil ditambahkan!" << endl;
    saveToCSV(L, filename);
}
```

**Penjelasan:**
- Loop `for` dari `i = 0` sampai `i < P->jumlahLagu`
- Jika ada yang sama, langsung `return` (keluar dari fungsi)
- Jika lolos semua pengecekan, baru data masuk ke array

---

### Skenario 🔟: "Reset Lagu (Clear Array)"

**Permintaan Asisten:**
> "Mas, artis ini pindah label rekaman. Semua lagunya ditarik. Saya mau hapus SEMUA lagunya si artis itu, tapi Artisnya jangan dihapus dari list. Jadi jumlah lagunya balik jadi 0."

**Analisa:** Kamu harus me-reset counter `jumlahLagu` jadi 0. Untuk nilai plus, kamu bisa melakukan **dealokasi array lama** dan buat array baru (biar bersih memori), tapi mereset counter saja seringkali sudah cukup diterima.

**Kunci Jawaban:**
```cpp
void clearLaguArtis(adrArtis P, List &L, const string &filename) {
    if (P == nullptr) {
        cout << "Artis tidak valid!" << endl;
        return;
    }
    
    // Cara PRO (Bersih Memori):
    delete[] P->laguArray;        // Hancurkan array lama
    P->laguArray = new string[5]; // Bikin wadah baru yang fresh
    P->kapasitas = 5;
    P->jumlahLagu = 0;            // Reset hitungan
    
    cout << "Semua lagu milik '" << P->info.nama << "' telah dihapus." << endl;
    cout << "Artis tetap ada dalam katalog dengan 0 lagu." << endl;
    saveToCSV(L, filename);
}
```

**Cara Pakai di Menu:**
```cpp
case X: {
    clearScreen();
    displayHeader("RESET SEMUA LAGU ARTIS");
    nama = readString("  Nama artis: ");
    pFound = searchArtis(L, nama);
    
    if (pFound != nullptr) {
        char konfirmasi;
        cout << "\n  PERINGATAN: Semua lagu akan dihapus!" << endl;
        cout << "  Lanjutkan? (y/n): ";
        cin >> konfirmasi;
        cin.ignore();
        
        if (konfirmasi == 'y' || konfirmasi == 'Y') {
            clearLaguArtis(pFound, L, filename);
        } else {
            cout << "  Operasi dibatalkan." << endl;
        }
    } else {
        cout << "  Artis tidak ditemukan!" << endl;
    }
    break;
}
```

---

### Skenario 1️⃣1️⃣: "Tampilkan Hanya Artis Kosong"

**Permintaan Dosen:**
> "Saya mau bersih-bersih data. Coba tampilkan Artis mana saja yang TIDAK PUNYA lagu sama sekali (lagunya 0), biar nanti saya hapus."

**Analisa:** Mirip skenario filter tahun debut, tapi kondisinya mengecek `jumlahLagu`.

**Kunci Jawaban:**
```cpp
void showEmptyArtis(List L) {
    adrArtis P = L.first;
    bool ada = false;
    int counter = 0;

    displayHeader("DAFTAR ARTIS TANPA LAGU");
    
    while (P != nullptr) {
        // LOGIKA FILTER:
        if (P->jumlahLagu == 0) {
            counter++;
            cout << "  " << counter << ". " << P->info.nama 
                 << " (Genre: " << P->info.genre 
                 << ", Debut: " << P->info.tahunDebut << ")" << endl;
            ada = true;
        }
        P = P->next;
    }
    
    if (!ada) {
        cout << "\n  Tidak ada artis kosong. Semua artis punya lagu!" << endl;
    } else {
        cout << "\n  Total artis tanpa lagu: " << counter << endl;
    }
}
```

**Implementasi di Menu:**
```cpp
case X: {
    clearScreen();
    showEmptyArtis(L);
    break;
}
```

**Bonus - Hapus Semua Artis Kosong:**
```cpp
void deleteAllEmptyArtis(List &L, const string &filename) {
    adrArtis P = L.first;
    adrArtis prev = nullptr;
    int deleted = 0;
    
    while (P != nullptr) {
        if (P->jumlahLagu == 0) {
            adrArtis temp = P;
            
            // Update link
            if (prev == nullptr) {
                L.first = P->next;
                P = L.first;
            } else {
                prev->next = P->next;
                P = P->next;
            }
            
            // Delete node
            delete[] temp->laguArray;
            delete temp;
            deleted++;
        } else {
            prev = P;
            P = P->next;
        }
    }
    
    cout << "Berhasil menghapus " << deleted << " artis kosong." << endl;
    saveToCSV(L, filename);
}
```

---

## 💡 TIPS MENGHADAPI SKENARIO DOSEN

| Tipe Modifikasi | File yang Berubah | Tingkat Kesulitan |
|----------------|-------------------|-------------------|
| Ubah logika insert/delete | katalog.cpp | ⭐⭐ |
| Filter data tampilan | katalog.cpp (showAllData) | ⭐ |
| Batasi kapasitas array | katalog.cpp (insertLagu) | ⭐⭐ |
| Tambah field struct | katalog.h + katalog.cpp + main.cpp | ⭐⭐⭐⭐ |
| Maximum/Minimum search | katalog.cpp | ⭐⭐ |
| Validasi duplikat | katalog.cpp (insertLagu) | ⭐⭐ |
| Insert After/Before | katalog.cpp | ⭐⭐⭐ |
| Clear/Reset data | katalog.cpp | ⭐⭐ |

**Prinsip Emas:**
1. **Pahami struktur data** → Tahu dimana data disimpan
2. **Trace alur fungsi** → Tahu fungsi mana yang dipanggil
3. **Test step by step** → Jangan langsung run semua
4. **Backup sebelum ubah** → Copy file dulu sebelum modif

---

**Last Updated:** January 3, 2026  
**Structure:** Multi-Linked List (MLL) 1-N with Dynamic Array
