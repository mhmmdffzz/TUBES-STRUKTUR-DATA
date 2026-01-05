# 📚 TUGAS BESAR STRUKTUR DATA - KATALOG MUSIK DIGITAL

## 📋 IDENTITAS PROGRAM
**Topik**: Manajemen Katalog Musik (Artis & Lagu)  
**Struktur Data**: Multi Linked List (MLL) 1-N  
**Bahasa Pemrograman**: C++  
**Database**: CSV File (music_db.csv)

---

## ✅ PEMENUHAN SPESIFIKASI TUGAS BESAR MLL 1-N

### **📌 SPESIFIKASI b. MLL 1-N**

Berdasarkan ketentuan tugas besar, program harus memenuhi 3 kriteria:

---

### **1️⃣ KRITERIA: List Parent dan Anak Tidak Boleh Sama**
**✓ STATUS: TERPENUHI**

#### **Kode Implementasi:**

**Parent menggunakan LINKED LIST:**
```cpp
// File: katalog.h, Baris 35-37
struct List {         // SPESIFIKASI 1.a: List parent
    elmArtis* first;  // Pointer ke node pertama (LINKED LIST)
};

// File: katalog.h, Baris 27-33
struct elmArtis {     // Node Linked List
    infoArtis info;         
    string* laguArray;      
    int jumlahLagu;         
    int kapasitas;          
    struct elmArtis* next;  // POINTER next untuk LINKED LIST ✓
};
```

**Child menggunakan ARRAY:**
```cpp
// File: katalog.h, Baris 29
string* laguArray;      // ARRAY DINAMIS untuk child (BUKAN linked list) ✓
```

**Bukti Operasi Berbeda:**
```cpp
// PARENT (Linked List) - Traversal menggunakan POINTER
// File: katalog.cpp, Baris 255-282
void showAllData(List L) {
    adrArtis P = L.first;
    while (P != nullptr) {           // Traversal dengan POINTER ✓
        // ... tampilkan data ...
        P = P->next;                 // Pindah ke node berikutnya ✓
    }
}

// CHILD (Array) - Akses menggunakan INDEX
// File: katalog.cpp, Baris 272-275
for (int i = 0; i < P->jumlahLagu; i++) {    // Loop dengan INDEX ✓
    cout << P->laguArray[i] << endl;         // Akses dengan [i] ✓
}
```

**✓ KESIMPULAN:**
- **Parent (Artis)**: Linked List dengan pointer `next`
- **Child (Lagu)**: Array dinamis dengan akses index `[i]`
- **BERBEDA** ✓

---

### **2️⃣ KRITERIA: Data Elemen Parent Berupa Tipe Bentukan (Record)**
**✓ STATUS: TERPENUHI**

#### **Kode Implementasi:**

**Definisi Record:**
```cpp
// File: katalog.h, Baris 21-25
struct infoArtis {    // TIPE BENTUKAN (RECORD) ✓
    string nama;      // Field 1
    string genre;     // Field 2  
    int tahunDebut;   // Field 3
};
```

**Penggunaan Record di Parent:**
```cpp
// File: katalog.h, Baris 27-33
struct elmArtis {     // Elemen Parent
    infoArtis info;         // DATA PARENT = TIPE BENTUKAN ✓
    string* laguArray;      // Child (array)
    int jumlahLagu;         
    int kapasitas;          
    struct elmArtis* next;  
};
```

**Bukti Akses Field Record:**
```cpp
// File: katalog.cpp, Baris 10-19
adrArtis createElementArtis(const string &nama, const string &genre, int tahun) {
    adrArtis P = new elmArtis;
    P->info.nama = nama;           // Akses field record.nama ✓
    P->info.genre = genre;         // Akses field record.genre ✓
    P->info.tahunDebut = tahun;    // Akses field record.tahunDebut ✓
    P->laguArray = new string[5];
    P->jumlahLagu = 0;
    P->kapasitas = 5;
    P->next = nullptr;
    return P;
}

// File: katalog.cpp, Baris 267-269 (Tampil Data)
cout << "  [" << counter << "] " << P->info.nama << endl;     // ✓
cout << "      Genre: " << P->info.genre << endl;             // ✓
cout << "      Debut: " << P->info.tahunDebut << endl;        // ✓
```

**✓ KESIMPULAN:**
- Data parent = `struct infoArtis` (record dengan 3 field)
- Bukan tipe dasar, tapi **tipe bentukan** ✓

---

### **3️⃣ KRITERIA: Data Elemen Child Berupa Tipe Dasar**
**✓ STATUS: TERPENUHI**

#### **Kode Implementasi:**

**Definisi Child sebagai Tipe Dasar:**
```cpp
// File: katalog.h, Baris 29
string* laguArray;      // ARRAY TIPE DASAR (string) ✓
```

**Alokasi Array Tipe Dasar:**
```cpp
// File: katalog.cpp, Baris 15
P->laguArray = new string[5];  // Alokasi array TIPE DASAR ✓
```

**Insert Data ke Array Tipe Dasar:**
```cpp
// File: katalog.cpp, Baris 151-152
P->laguArray[P->jumlahLagu] = judul;  // Simpan string langsung ✓
P->jumlahLagu++;
```

**Resize Array Tipe Dasar:**
```cpp
// File: katalog.cpp, Baris 136-148
if (P->jumlahLagu >= P->kapasitas) {
    int newKapasitas = P->kapasitas * 2;
    string* newArray = new string[newKapasitas];  // Array TIPE DASAR ✓
    
    // Copy data
    for (int i = 0; i < P->jumlahLagu; i++) {
        newArray[i] = P->laguArray[i];  // Copy string langsung ✓
    }
    
    delete[] P->laguArray;
    P->laguArray = newArray;
    P->kapasitas = newKapasitas;
}
```

**Akses Data Array Tipe Dasar:**
```cpp
// File: katalog.cpp, Baris 272-275
for (int i = 0; i < P->jumlahLagu; i++) {
    cout << "        + " << P->laguArray[i] << endl;  // Akses string ✓
}
```

**✓ KESIMPULAN:**
- Child = array tipe dasar `string`
- Bukan record/struct, tapi **tipe dasar** ✓

---

### **📊 RINGKASAN PEMENUHAN SPESIFIKASI MLL 1-N**

| **Kriteria** | **Implementasi** | **Lokasi Kode** | **Status** |
|-------------|------------------|-----------------|------------|
| **List parent ≠ child** | Parent: Linked List, Child: Array | katalog.h:27-37 | ✓ TERPENUHI |
| **Data parent = tipe bentukan** | `struct infoArtis` (3 field) | katalog.h:21-25 | ✓ TERPENUHI |
| **Data child = tipe dasar** | `string* laguArray` | katalog.h:29 | ✓ TERPENUHI |

**✅ SEMUA SPESIFIKASI MLL 1-N TERPENUHI**

---

## 📌 FUNGSIONALITAS PROGRAM

### **2. Fungsionalitas**

---

### **a. Dasar: CRUD + Search**

#### **🔹 C - CREATE (Tambah Data)**
**✓ STATUS: TERPENUHI**

**1️⃣ CREATE Artis Baru:**
```cpp
// File: katalog.cpp, Baris 10-20
// FUNCTION - return pointer artis baru
adrArtis createElementArtis(const string &nama, const string &genre, int tahun) {
    adrArtis P = new elmArtis;                    // Alokasi node MLL
    P->info.nama = nama;                          // Set record field 1
    P->info.genre = genre;                        // Set record field 2
    P->info.tahunDebut = tahun;                   // Set record field 3
    P->laguArray = new string[5];                 // Alokasi array tipe dasar
    P->jumlahLagu = 0;
    P->kapasitas = 5;
    P->next = nullptr;
    return P;
}

// File: katalog.cpp, Baris 30-44
// PROCEDURE - tambah artis ke list
void insertLastArtis(List &L, adrArtis P, const string &filename) {
    if (L.first == nullptr) {
        L.first = P;                              // Insert node pertama
    } else {
        adrArtis Q = L.first;
        while (Q->next != nullptr) {              // Traversal ke akhir
            Q = Q->next;
        }
        Q->next = P;                              // Insert di akhir
    }
    cout << "  Artis berhasil ditambahkan!" << endl;
    saveToCSV(L, filename);                       // Auto-save
}
```

**2️⃣ CREATE Lagu ke Artis:**
```cpp
// File: katalog.cpp, Baris 131-158
// PROCEDURE - tambah lagu ke array artis
void insertLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    // Auto-resize jika array penuh
    if (P->jumlahLagu >= P->kapasitas) {
        int newKapasitas = P->kapasitas * 2;
        string* newArray = new string[newKapasitas];
        
        for (int i = 0; i < P->jumlahLagu; i++) {
            newArray[i] = P->laguArray[i];        // Copy existing
        }
        
        delete[] P->laguArray;
        P->laguArray = newArray;
        P->kapasitas = newKapasitas;
    }
    
    P->laguArray[P->jumlahLagu] = judul;          // Insert ke array
    P->jumlahLagu++;
    
    cout << "  Lagu '" << judul << "' berhasil ditambahkan!" << endl;
    saveToCSV(L, filename);
}
```

**Implementasi di Main Program:**
```cpp
// File: main.cpp, Baris 45-96
case 1: {
    // CREATE Artis Baru
    nama = readString("  Nama artis: ");
    genre = readString("  Genre: ");
    tahun = readInteger("  Tahun debut: ");
    
    adrArtis newArtis = createElementArtis(nama, genre, tahun);  // CREATE
    insertLastArtis(L, newArtis, filename);                      // INSERT
}
```

---

#### **🔹 R - READ (Tampilkan Data)**
**✓ STATUS: TERPENUHI**

```cpp
// File: katalog.cpp, Baris 255-287
// PROCEDURE - tampilkan semua data katalog
void showAllData(List L) {
    displayHeader("*** DATA KATALOG MUSIK ***");
    
    if (L.first == nullptr) {
        cout << "\n  Tidak ada data artis." << endl;
        return;
    }

    int artistCount = 0;
    int totalSongs = 0;
    
    adrArtis P = L.first;
    while (P != nullptr) {                        // TRAVERSAL Linked List
        artistCount++;
        cout << "\n  [" << artistCount << "] " << P->info.nama << endl;
        cout << "      Genre  : " << P->info.genre << endl;
        cout << "      Debut  : " << P->info.tahunDebut << endl;
        cout << "      Lagu   : ";

        if (P->jumlahLagu == 0) {
            cout << "(kosong)" << endl;
        } else {
            cout << "(" << P->jumlahLagu << " lagu)" << endl;
            for (int i = 0; i < P->jumlahLagu; i++) {  // TRAVERSAL Array
                cout << "         - " << P->laguArray[i] << endl;
                totalSongs++;
            }
        }
        P = P->next;                              // Pindah ke node berikutnya
    }
    
    cout << "\n  Total: " << artistCount << " artis, " << totalSongs << " lagu" << endl;
}
```

**Implementasi di Main Program:**
```cpp
// File: main.cpp, Baris 172-176
case 2: {
    // READ - Tampil semua data
    clearScreen();
    showAllData(L);                              // READ operation
    break;
}
```

---

#### **🔹 U - UPDATE (Ubah Data)**
**✓ STATUS: TERPENUHI**

```cpp
// File: katalog.cpp, Baris 109-124
// PROCEDURE - update info artis
void updateArtisInfo(List &L, const string &nama, const string &genreBaru, 
                     int tahunBaru, const string &filename) {
    adrArtis P = searchArtis(L, nama);            // SEARCH dulu
    
    if (P != nullptr) {
        P->info.genre = genreBaru;                // UPDATE field record
        P->info.tahunDebut = tahunBaru;           // UPDATE field record
        
        cout << "  Info artis '" << nama << "' berhasil diupdate!" << endl;
        
        if (saveToCSV(L, filename)) {             // AUTO-SAVE
            cout << "  Data disimpan ke " << filename << endl;
        }
    } else {
        cout << "  Artis tidak ditemukan!" << endl;
    }
}
```

**Implementasi di Main Program:**
```cpp
// File: main.cpp, Baris 268-275
case 6: {
    // UPDATE Info Artis
    clearScreen();
    displayHeader("UPDATE INFO ARTIS");
    nama = readString(">> Nama Artis: ");
    genre = readString(">> Genre Baru: ");
    tahun = readInteger(">> Tahun Debut Baru: ");
    
    updateArtisInfo(L, nama, genre, tahun, filename);  // UPDATE operation
    break;
}
```

---

#### **🔹 D - DELETE (Hapus Data)**
**✓ STATUS: TERPENUHI**

**1️⃣ DELETE Artis:**
```cpp
// File: katalog.cpp, Baris 76-107
// PROCEDURE - hapus artis dari list
void deleteArtis(List &L, const string &nama, const string &filename) {
    adrArtis P = searchArtis(L, nama);            // SEARCH dulu
    
    if (P == nullptr) {
        cout << "  Artis tidak ditemukan!" << endl;
        return;
    }
    
    // Cari node sebelumnya
    adrArtis prev = nullptr;
    adrArtis current = L.first;
    while (current != nullptr && current != P) {
        prev = current;
        current = current->next;
    }
    
    delete[] P->laguArray;                        // Dealokasi array child
    
    // Hapus artis dari list
    if (prev == nullptr) {
        L.first = P->next;                        // Hapus node pertama
    } else {
        prev->next = P->next;                     // Hapus node tengah/akhir
    }
    
    delete P;                                     // Dealokasi node
    cout << "  Artis '" << nama << "' berhasil dihapus!" << endl;
    saveToCSV(L, filename);
}
```

**2️⃣ DELETE Lagu:**
```cpp
// File: katalog.cpp, Baris 160-195
// PROCEDURE - hapus lagu dari array artis
void deleteLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    if (P == nullptr || P->jumlahLagu == 0) {
        cout << "  Lagu tidak ditemukan!" << endl;
        return;
    }
    
    // Cari index lagu (case-insensitive)
    string judulLower = judul;
    transform(judulLower.begin(), judulLower.end(), judulLower.begin(), ::tolower);
    
    int index = -1;
    for (int i = 0; i < P->jumlahLagu; i++) {
        string laguLower = P->laguArray[i];
        transform(laguLower.begin(), laguLower.end(), laguLower.begin(), ::tolower);
        if (laguLower == judulLower) {
            index = i;
            break;
        }
    }
    
    if (index == -1) {
        cout << "  Lagu tidak ditemukan!" << endl;
        return;
    }
    
    // Shift array ke kiri
    for (int i = index; i < P->jumlahLagu - 1; i++) {
        P->laguArray[i] = P->laguArray[i + 1];
    }
    
    P->jumlahLagu--;
    cout << "  Lagu '" << judul << "' berhasil dihapus!" << endl;
    saveToCSV(L, filename);
}
```

**Implementasi di Main Program:**
```cpp
// File: main.cpp, Baris 211-217
case 2: {
    // DELETE Artis
    clearScreen();
    displayHeader("HAPUS ARTIS");
    nama = readString("  Nama Artis yang dihapus: ");
    deleteArtis(L, nama, filename);              // DELETE operation
    break;
}
```

---

#### **🔍 SEARCH (Pencarian Data)**
**✓ STATUS: TERPENUHI**

```cpp
// File: katalog.cpp, Baris 47-73
// FUNCTION - return pointer artis hasil pencarian
adrArtis searchArtis(List L, const string &nama) {
    string namaLower = nama;
    
    // Trim whitespace
    namaLower.erase(namaLower.find_last_not_of(" \t\n\r\f\v") + 1);
    namaLower.erase(0, namaLower.find_first_not_of(" \t\n\r\f\v"));
    
    // Convert to lowercase (CASE-INSENSITIVE)
    transform(namaLower.begin(), namaLower.end(), namaLower.begin(), ::tolower);
    
    adrArtis P = L.first;
    while (P != nullptr) {                        // SEQUENTIAL SEARCH
        string storedName = P->info.nama;
        
        // Trim & lowercase
        storedName.erase(storedName.find_last_not_of(" \t\n\r\f\v") + 1);
        storedName.erase(0, storedName.find_first_not_of(" \t\n\r\f\v"));
        transform(storedName.begin(), storedName.end(), storedName.begin(), ::tolower);
        
        if (storedName == namaLower) {
            return P;                             // FOUND
        }
        P = P->next;
    }
    return nullptr;                               // NOT FOUND
}
```

**Implementasi di Main Program:**
```cpp
// File: main.cpp, Baris 237-258
case 4: {
    // SEARCH Artis
    clearScreen();
    displayHeader("CARI ARTIS");
    nama = readString(">> Nama Artis: ");
    pFound = searchArtis(L, nama);               // SEARCH operation
    
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
```

---

### **b. Pengolahan MLL: Counting, dll.**

#### **📊 COUNTING Operations**
**✓ STATUS: TERPENUHI**

**1️⃣ Count Total Artis:**
```cpp
// File: katalog.cpp, Baris 362-372
// FUNCTION - return jumlah total artis
int countTotalArtis(List L) {
    int count = 0;
    adrArtis P = L.first;
    
    while (P != nullptr) {                        // TRAVERSAL semua node
        count++;                                  // INCREMENT counter
        P = P->next;
    }
    
    return count;                                 // RETURN hasil counting
}
```

**2️⃣ Count Total Lagu:**
```cpp
// File: katalog.cpp, Baris 351-361
// FUNCTION - return jumlah total lagu
int countTotalLagu(List L) {
    int total = 0;
    adrArtis P = L.first;
    
    while (P != nullptr) {                        // TRAVERSAL semua artis
        total += P->jumlahLagu;                   // AKUMULASI lagu per artis
        P = P->next;
    }
    
    return total;                                 // RETURN total lagu
}
```

**3️⃣ Laporan Statistik (Menggunakan Counting):**
```cpp
// File: katalog.cpp, Baris 317-342
// PROCEDURE - tampilkan laporan statistik
void showReport(List L) {
    displayHeader("*** LAPORAN SISTEM KATALOG MUSIK ***");
    
    int totalArtis = countTotalArtis(L);          // COUNTING artis
    int totalLagu = countTotalLagu(L);            // COUNTING lagu
    
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
            cout << "  " << counter << ". " << P->info.nama 
                 << " (" << P->jumlahLagu << " lagu)" << endl;  // COUNTING per artis
            P = P->next;
            counter++;
        }
    }
}
```

**Implementasi di Main Program:**
```cpp
// File: main.cpp, Baris 260-265
case 5: {
    // LAPORAN dengan COUNTING
    clearScreen();
    showReport(L);                               // Tampil statistik + counting
    break;
}

// File: main.cpp, Baris 95
cout << "  Total artis: " << countTotalArtis(L) << endl;  // Counting setelah insert
```

---

### **📊 RINGKASAN PEMENUHAN FUNGSIONALITAS**

| **Fungsionalitas** | **Fungsi/Procedure** | **Lokasi Kode** | **Status** |
|-------------------|---------------------|-----------------|------------|
| **CREATE Artis** | `createElementArtis()`, `insertLastArtis()` | katalog.cpp:10, 30 | ✓ TERPENUHI |
| **CREATE Lagu** | `insertLagu()` | katalog.cpp:131 | ✓ TERPENUHI |
| **READ Data** | `showAllData()` | katalog.cpp:255 | ✓ TERPENUHI |
| **UPDATE Artis** | `updateArtisInfo()` | katalog.cpp:109 | ✓ TERPENUHI |
| **DELETE Artis** | `deleteArtis()` | katalog.cpp:76 | ✓ TERPENUHI |
| **DELETE Lagu** | `deleteLagu()` | katalog.cpp:160 | ✓ TERPENUHI |
| **SEARCH Artis** | `searchArtis()` (case-insensitive) | katalog.cpp:47 | ✓ TERPENUHI |
| **COUNT Artis** | `countTotalArtis()` | katalog.cpp:362 | ✓ TERPENUHI |
| **COUNT Lagu** | `countTotalLagu()` | katalog.cpp:351 | ✓ TERPENUHI |
| **REPORT** | `showReport()` (dengan counting) | katalog.cpp:317 | ✓ TERPENUHI |

**✅ SEMUA FUNGSIONALITAS TERPENUHI**

---

## �️ STRUKTUR FILE

```
TUBES STRUKDAT CPP/
├── katalog.h           # Header file (prototype & struct)
├── katalog.cpp         # Implementasi fungsi
├── main.cpp            # Program utama
├── music_db.csv        # Database (auto-generated)
├── README.md           # Dokumentasi ini
└── CHEATSHEET.md       # Panduan singkat
```

---

## 🔧 CARA KOMPILASI & MENJALANKAN

### **Kompilasi:**
```bash
g++ -o katalog main.cpp katalog.cpp
```

### **Menjalankan:**
```bash
./katalog
```

---

## 📝 FORMAT DATABASE (CSV)

File `music_db.csv` menggunakan format:
```
nama;genre;tahun;judul_lagu
```

**Contoh:**
```csv
Taylor Swift;Pop;2006;Love Story
Ed Sheeran;Pop;2011;Shape of You
Coldplay;Rock;1998;Belum Ada Lagu
```

---

**✅ SEMUA SPESIFIKASI TUGAS BESAR TERPENUHI**

---

**Dibuat untuk memenuhi Tugas Besar Struktur Data**  
**Implementasi: Multi Linked List 1-N dengan CRUD + Search + Counting**
