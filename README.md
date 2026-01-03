# KATALOG MUSIK DIGITAL

## Deskripsi Program
Program Katalog Musik adalah aplikasi manajemen data musik berbasis **Multi Linked List (MLL) 1-N** yang diimplementasikan dengan C++ sesuai spesifikasi Tugas Besar Struktur Data. Program ini memungkinkan pengelolaan data artis dan lagu-lagunya dengan database CSV.

---

## 🆕 UPDATE TERBARU - MENU NESTED & FITUR ENHANCEMENT

### **Versi 2.0 - Peningkatan User Experience**

#### ⭐ **PERUBAHAN UTAMA:**

#### 1. **Nested Menu System** (Menu Bertingkat)
Program sekarang menggunakan **nested menu** untuk organisasi yang lebih baik:

**MENU UTAMA BARU:**
```
[1] Kelola Data Artis & Lagu    → Sub-menu untuk tambah data
[2] Lihat Semua Data Katalog
[3] Hapus Data Artis & Lagu     → Sub-menu untuk hapus data
[4] Cari Artis di Katalog
[5] Lihat Laporan Statistik
[6] Update Info Artis
[0] Keluar dari Program
```

**SUB-MENU 1: KELOLA DATA**
```
[1] Tambah Artis Baru
[2] Tambah Lagu ke Artis Lama
[0] Kembali ke Menu Utama
```

**SUB-MENU 3: HAPUS DATA**
```
[1] Hapus Lagu dari Artis
[2] Hapus Artis dari Katalog
[0] Kembali ke Menu Utama
```

#### 2. **Logika Khusus Tanda "-" untuk Skip Lagu Pertama**
Saat menambah artis baru, user bisa:
- **Ketik judul lagu**: Lagu langsung masuk ke `laguArray[0]`, `jumlahLagu = 1`
- **Ketik "-"**: Array lagu dibiarkan kosong, `jumlahLagu = 0`

```cpp
// Contoh implementasi:
cout << "  Masukkan Lagu Pertama (atau ketik '-' untuk lewati): ";
getline(cin, judul);

if (judul == "-") {
    // Array lagu dibiarkan kosong (jumlahLagu = 0)
    cout << "  Artis ditambahkan tanpa lagu." << endl;
} else if (!judul.empty()) {
    // Masukkan lagu ke array
    newArtis->laguArray[0] = judul;
    newArtis->jumlahLagu = 1;
}
```

#### 3. **Loop Input Lagu Tanpa Batas**
Di sub-menu "Tambah Lagu ke Artis Lama", user bisa menambahkan lagu **sebanyak apapun** dalam satu sesi:

```
TAMBAH LAGU (Ketik '0' untuk selesai)
Judul lagu [1]: Shape of You
Lagu 'Shape of You' berhasil ditambahkan!
Judul lagu [2]: Perfect
Lagu 'Perfect' berhasil ditambahkan!
Judul lagu [3]: Thinking Out Loud
Lagu 'Thinking Out Loud' berhasil ditambahkan!
Judul lagu [4]: 0  ← Ketik 0 untuk selesai

Selesai menambahkan lagu.
Total lagu untuk 'Ed Sheeran': 3
```

**Fitur:**
- Input lagu terus berulang sampai user ketik `"0"`
- Tidak ada batasan jumlah lagu per sesi
- Array akan auto-expand jika penuh (5 → 10 → 20 → 40 → ...)

#### 4. **Array Dinamis Auto-Expand** (Sudah Ada Sebelumnya)
Array lagu menggunakan **dynamic resizing** seperti `std::vector`:

**Mekanisme:**
```
Kapasitas Awal: 5
Lagu ke-6 ditambah → Resize ke kapasitas 10
Lagu ke-11 ditambah → Resize ke kapasitas 20
Lagu ke-21 ditambah → Resize ke kapasitas 40
... dan seterusnya (tidak ada batasan!)
```

**Implementasi:**
```cpp
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
```

---

### **PERBEDAAN VERSI LAMA vs BARU**

| Aspek | Versi Lama | Versi Baru (2.0) |
|-------|-----------|------------------|
| **Menu Structure** | Flat menu (7 pilihan) | Nested menu (3 + sub-menu) |
| **Tambah Artis & Lagu** | Satu menu gabungan | Terpisah di sub-menu |
| **Hapus Data** | 2 menu terpisah | 1 menu dengan sub-menu |
| **Input Lagu Pertama** | Wajib input atau skip manual | Logika khusus tanda "-" |
| **Tambah Lagu ke Artis** | Input satu-satu, keluar & masuk lagi | Loop terus sampai ketik "0" |
| **Jumlah Lagu per Sesi** | 1 lagu per eksekusi menu | Unlimited (sampai user ketik 0) |
| **Kapasitas Array** | Fixed resize (sudah ada) | Fixed resize (tetap sama) |
| **User Flow** | Kurang terorganisir | Lebih terstruktur & intuitif |

---

### **KEUNTUNGAN UPDATE INI:**

✅ **Organisasi Menu Lebih Baik**: Fitur serupa dikelompokkan dalam sub-menu  
✅ **User Experience Lebih Smooth**: Bisa input banyak lagu tanpa keluar-masuk menu  
✅ **Fleksibilitas Tinggi**: Artis bisa dibuat tanpa lagu (pakai "-")  
✅ **Efisiensi Waktu**: Tidak perlu re-navigate menu berkali-kali  
✅ **Konsistensi Kode**: Nested menu pattern yang sama untuk kelola & hapus data  

---

## PEMENUHAN SPESIFIKASI TUGAS BESAR

### SPESIFIKASI 1.a: Struktur Data MLL 1-N

#### ✅ KRITERIA 1: Data pada Node Berupa Tipe Bentukan (Record)
**Status: TERPENUHI**

Program menggunakan `struct infoArtis` sebagai tipe bentukan (record) yang menyimpan informasi artis:

```cpp
struct infoArtis {    // Tipe bentukan (record)
    string nama;      // Field 1: Nama artis
    string genre;     // Field 2: Genre musik
    int tahunDebut;   // Field 3: Tahun debut
};
```

**Implementasi di Node:**
```cpp
struct elmArtis {
    infoArtis info;         // Record yang menyimpan data artis
    string* laguArray;      // Array untuk child
    int jumlahLagu;
    int kapasitas;
    elmArtis* next;
};
```

**Bukti Penggunaan:**
```cpp
// File: katalog.cpp, baris 10-19
adrArtis createElementArtis(const string &nama, const string &genre, int tahun) {
    adrArtis P = new elmArtis;
    P->info.nama = nama;           // Akses field record
    P->info.genre = genre;         // Akses field record
    P->info.tahunDebut = tahun;    // Akses field record
    P->laguArray = new string[5];
    P->jumlahLagu = 0;
    P->kapasitas = 5;
    P->next = nullptr;
    return P;
}
```

---

#### ✅ KRITERIA 2: Satu Atribut Berupa Array Tipe Dasar
**Status: TERPENUHI**

Program menggunakan **array dinamis tipe dasar `string`** untuk menyimpan lagu:

```cpp
struct elmArtis {
    infoArtis info;
    string* laguArray;    // ARRAY TIPE DASAR (string*)
    int jumlahLagu;       // Counter jumlah lagu
    int kapasitas;        // Kapasitas maksimal array
    elmArtis* next;
};
```

**Alokasi Dinamis Array:**
```cpp
// File: katalog.cpp, baris 15
P->laguArray = new string[5];  // Alokasi array tipe dasar dinamis
```

**Resize Array Otomatis:**
```cpp
// File: katalog.cpp, baris 129-138
void insertLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    if (P->jumlahLagu >= P->kapasitas) {
        // Resize array jika penuh
        int newCapacity = P->kapasitas * 2;
        string* newArray = new string[newCapacity];
        
        for (int i = 0; i < P->jumlahLagu; i++) {
            newArray[i] = P->laguArray[i];
        }
        
        delete[] P->laguArray;
        P->laguArray = newArray;
        P->kapasitas = newCapacity;
    }
    
    P->laguArray[P->jumlahLagu] = judul;
    P->jumlahLagu++;
}
```

---

#### ✅ KRITERIA 3: List Parent dan Child Tidak Boleh Sama
**Status: TERPENUHI**

**Parent (Artis):** Menggunakan **Linked List** dengan pointer `next`
**Child (Lagu):** Menggunakan **Array Tipe Dasar** `string*`

```cpp
struct List {
    elmArtis* first;  // Parent: Linked List Artis
};

struct elmArtis {
    infoArtis info;
    string* laguArray;  // Child: ARRAY (bukan linked list)
    int jumlahLagu;
    int kapasitas;
    elmArtis* next;     // Pointer untuk linked list parent
};
```

**Perbedaan Struktur:**
- **Parent (Artis):** Linked list dengan traversal menggunakan pointer `next`
- **Child (Lagu):** Array dengan akses menggunakan index `[i]`

---

### SPESIFIKASI 2.a: Fungsionalitas Dasar - CRUD + Search

#### ✅ KRITERIA 1: CREATE (Tambah Data)
**Status: TERPENUHI**

**1. Create List:**
```cpp
// File: katalog.cpp, baris 25-27
void createList(List &L) {
    L.first = nullptr;  // Inisialisasi list kosong
}
```

**2. Create Element Artis:**
```cpp
// File: katalog.cpp, baris 10-20
adrArtis createElementArtis(const string &nama, const string &genre, int tahun) {
    adrArtis P = new elmArtis;
    P->info.nama = nama;
    P->info.genre = genre;
    P->info.tahunDebut = tahun;
    P->laguArray = new string[5];
    P->jumlahLagu = 0;
    P->kapasitas = 5;
    P->next = nullptr;
    return P;
}
```

**3. Insert Artis ke List:**
```cpp
// File: katalog.cpp, baris 29-44
void insertLastArtis(List &L, adrArtis P, const string &filename) {
    if (L.first == nullptr) {
        L.first = P;
    } else {
        adrArtis Q = L.first;
        while (Q->next != nullptr) {
            Q = Q->next;
        }
        Q->next = P;
    }
    cout << "  Artis '" << P->info.nama << "' ditambahkan" << endl;
    saveToCSV(L, filename);
}
```

**4. Insert Lagu ke Array:**
```cpp
// File: katalog.cpp, baris 127-149
void insertLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    if (P->jumlahLagu >= P->kapasitas) {
        int newCapacity = P->kapasitas * 2;
        string* newArray = new string[newCapacity];
        for (int i = 0; i < P->jumlahLagu; i++) {
            newArray[i] = P->laguArray[i];
        }
        delete[] P->laguArray;
        P->laguArray = newArray;
        P->kapasitas = newCapacity;
    }
    P->laguArray[P->jumlahLagu] = judul;
    P->jumlahLagu++;
    saveToCSV(L, filename);
}
```

---

#### ✅ KRITERIA 2: READ (Tampilkan Data)
**Status: TERPENUHI**

**Tampilkan Semua Data dengan Traversal:**
```cpp
// File: katalog.cpp, baris 248-282
void showAllData(List L) {
    displayHeader("DATA KATALOG MUSIK");
    
    if (L.first == nullptr) {
        cout << "\n  Tidak ada data artis." << endl;
        return;
    }

    int artistCount = 0;
    int totalSongs = 0;
    
    adrArtis P = L.first;
    while (P != nullptr) {  // Traversal linked list
        artistCount++;
        cout << "\n  [" << artistCount << "] " << P->info.nama << endl;
        cout << "      Genre: " << P->info.genre << endl;
        cout << "      Debut: " << P->info.tahunDebut << endl;
        cout << "      Lagu: ";
        
        if (P->jumlahLagu == 0) {
            cout << "(kosong)" << endl;
        } else {
            cout << endl;
            for (int i = 0; i < P->jumlahLagu; i++) {  // Traversal array
                cout << "        + " << P->laguArray[i] << endl;
                totalSongs++;
            }
        }
        cout << endl;
        P = P->next;  // Pindah ke node berikutnya
    }
    
    cout << "  Total: " << artistCount << " artis, " << totalSongs << " lagu" << endl;
}
```

---

#### ✅ KRITERIA 3: UPDATE (Ubah Data)
**Status: TERPENUHI**

```cpp
// File: katalog.cpp, baris 107-125
void updateArtisInfo(List &L, const string &nama, const string &newGenre, 
                     int newTahun, const string &filename) {
    adrArtis P = searchArtis(L, nama);  // Cari artis dulu
    
    if (P == nullptr) {
        cout << "  Artis tidak ditemukan" << endl;
        return;
    }
    
    // Simpan data lama untuk ditampilkan
    string oldGenre = P->info.genre;
    int oldTahun = P->info.tahunDebut;
    
    // Update data
    P->info.genre = newGenre;
    P->info.tahunDebut = newTahun;
    
    cout << "  Data artis '" << P->info.nama << "' berhasil diupdate" << endl;
    cout << "  Genre: " << oldGenre << " -> " << newGenre << endl;
    cout << "  Tahun: " << oldTahun << " -> " << newTahun << endl;
    
    saveToCSV(L, filename);
}
```

---

#### ✅ KRITERIA 4: DELETE (Hapus Data)
**Status: TERPENUHI**

**1. Delete Artis dari List:**
```cpp
// File: katalog.cpp, baris 74-105
void deleteArtis(List &L, const string &nama, const string &filename) {
    adrArtis P = searchArtis(L, nama);
    
    if (P == nullptr) {
        cout << "  Artis tidak ditemukan" << endl;
        return;
    }
    
    // Cari node sebelumnya
    adrArtis prev = nullptr;
    adrArtis current = L.first;
    while (current != nullptr && current != P) {
        prev = current;
        current = current->next;
    }
    
    // Hapus array lagu (dealokasi memori)
    delete[] P->laguArray;
    
    // Hapus artis dari list
    if (prev == nullptr) {
        L.first = P->next;  // Hapus node pertama
    } else {
        prev->next = P->next;  // Hapus node tengah/akhir
    }
    
    delete P;  // Dealokasi node
    cout << "  Artis '" << nama << "' berhasil dihapus" << endl;
    saveToCSV(L, filename);
}
```

**2. Delete Lagu dari Array:**
```cpp
// File: katalog.cpp, baris 151-179
void deleteLagu(adrArtis P, const string &judul, List &L, const string &filename) {
    int index = -1;
    
    // Cari index lagu
    for (int i = 0; i < P->jumlahLagu; i++) {
        if (P->laguArray[i] == judul) {
            index = i;
            break;
        }
    }
    
    if (index == -1) {
        cout << "  Lagu tidak ditemukan" << endl;
        return;
    }
    
    // Shift array ke kiri
    for (int i = index; i < P->jumlahLagu - 1; i++) {
        P->laguArray[i] = P->laguArray[i + 1];
    }
    
    P->jumlahLagu--;
    cout << "  Lagu '" << judul << "' berhasil dihapus" << endl;
    saveToCSV(L, filename);
}
```

---

#### ✅ KRITERIA 5: SEARCH (Pencarian Data)
**Status: TERPENUHI**

**Case-Insensitive Search dengan Whitespace Trimming:**
```cpp
// File: katalog.cpp, baris 47-72
adrArtis searchArtis(List L, const string &nama) {
    string namaLower = nama;
    
    // Trim whitespace
    namaLower.erase(namaLower.find_last_not_of(" \t\n\r\f\v") + 1);
    namaLower.erase(0, namaLower.find_first_not_of(" \t\n\r\f\v"));
    
    // Convert to lowercase
    transform(namaLower.begin(), namaLower.end(), namaLower.begin(), ::tolower);
    
    adrArtis P = L.first;
    while (P != nullptr) {  // Sequential search dengan traversal
        string storedName = P->info.nama;
        
        // Trim whitespace
        storedName.erase(storedName.find_last_not_of(" \t\n\r\f\v") + 1);
        storedName.erase(0, storedName.find_first_not_of(" \t\n\r\f\v"));
        
        // Convert to lowercase
        transform(storedName.begin(), storedName.end(), storedName.begin(), ::tolower);
        
        if (storedName == namaLower) {
            return P;  // Ditemukan
        }
        P = P->next;
    }
    return nullptr;  // Tidak ditemukan
}
```

---

### SPESIFIKASI 2.b: Pengolahan MLL - Counting & Analisis

#### ✅ KRITERIA: Operasi Counting
**Status: TERPENUHI**

**1. Count Total Artis:**
```cpp
// File: katalog.cpp, baris 181-190
int countTotalArtis(List L) {
    int count = 0;
    adrArtis P = L.first;
    
    while (P != nullptr) {
        count++;
        P = P->next;
    }
    
    return count;
}
```

**2. Count Total Lagu:**
```cpp
// File: katalog.cpp, baris 192-201
int countTotalLagu(List L) {
    int totalLagu = 0;
    adrArtis P = L.first;
    
    while (P != nullptr) {
        totalLagu += P->jumlahLagu;  // Akumulasi jumlah lagu dari setiap artis
        P = P->next;
    }
    
    return totalLagu;
}
```

**3. Laporan Statistik:**
```cpp
// File: katalog.cpp, baris 297-322
void showReport(List L) {
    displayHeader("LAPORAN SISTEM KATALOG MUSIK");
    
    int totalArtis = countTotalArtis(L);  // Menggunakan counting
    int totalLagu = countTotalLagu(L);    // Menggunakan counting
    
    cout << "\n  Statistik:" << endl;
    cout << "  + Artis: " << totalArtis << endl;
    cout << "  + Lagu: " << totalLagu << endl;
    
    cout << "\n  Detail per artis:" << endl;
    
    if (L.first == nullptr) {
        cout << "  (tidak ada data)" << endl;
    } else {
        adrArtis P = L.first;
        int counter = 1;
        while (P != nullptr) {
            cout << "  " << counter << ". " << P->info.nama 
                 << " (" << P->jumlahLagu << " lagu)" << endl;
            P = P->next;
            counter++;
        }
    }
}
```

---

### FITUR TAMBAHAN

#### ✅ Persistensi Data dengan CSV
**Load dari CSV:**
```cpp
// File: katalog.cpp, baris 345-391
bool loadFromCSV(const string &filename, List &L) {
    ifstream file(filename);
    if (!file.is_open()) {
        return false;
    }
    
    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string nama, genre, tahunStr, judul;
        
        // Parse dengan delimiter semicolon
        getline(ss, nama, ';');
        getline(ss, genre, ';');
        getline(ss, tahunStr, ';');
        getline(ss, judul, ';');
        
        try {
            int tahun = stoi(tahunStr);
            
            adrArtis P = searchArtis(L, nama);
            if (P == nullptr) {
                P = createElementArtis(nama, genre, tahun);
                insertLastArtisNoSave(L, P);
            }
            
            insertLaguNoSave(P, judul);
        } catch (const exception& e) {
            // Skip invalid lines
        }
    }
    
    file.close();
    return true;
}
```

**Save ke CSV:**
```cpp
// File: katalog.cpp, baris 397-420
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
```

#### ✅ Validasi Input dengan Loop
```cpp
// File: katalog.h, baris 107-121
inline int readInteger(const string &prompt) {
    int value;
    bool valid = false;
    
    while (!valid) {
        cout << prompt;
        if (cin >> value) {
            valid = true;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        } else {
            cout << "  [ERROR] Input tidak valid! Masukkan angka yang benar." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
    }
    return value;
}
```

---

## KESIMPULAN PEMENUHAN SPESIFIKASI

### ✅ Semua Kriteria TERPENUHI:

1. **Spesifikasi 1.a - Struktur Data:**
   - ✅ Data node berupa record (`infoArtis`)
   - ✅ Array tipe dasar (`string* laguArray`)
   - ✅ Parent (Linked List) ≠ Child (Array)

2. **Spesifikasi 2.a - CRUD + Search:**
   - ✅ CREATE: `createList`, `createElementArtis`, `insertLastArtis`, `insertLagu`
   - ✅ READ: `showAllData` dengan traversal lengkap
   - ✅ UPDATE: `updateArtisInfo`
   - ✅ DELETE: `deleteArtis`, `deleteLagu`
   - ✅ SEARCH: `searchArtis` dengan case-insensitive

3. **Spesifikasi 2.b - Pengolahan MLL:**
   - ✅ COUNTING: `countTotalArtis`, `countTotalLagu`
   - ✅ ANALISIS: `showReport` dengan statistik

4. **Fitur Tambahan:**
   - ✅ Persistensi data CSV (load/save)
   - ✅ Validasi input robust
   - ✅ Memory management proper
   - ✅ User-friendly interface

---

## Struktur Data

### Spesifikasi MLL 1-N
Program menggunakan **Multi Linked List 1-N** dengan:
- **Parent (Artis)**: Linked List dari node artis
- **Child (Lagu)**: Array dinamis tipe dasar (string) untuk menyimpan lagu
- **Record**: Tipe bentukan `infoArtis` yang menyimpan nama, genre, dan tahun debut

### Definisi Struktur
```cpp
struct infoArtis {
    string nama;
    string genre; 
    int tahunDebut;
};

struct elmArtis {
    infoArtis info;           // Record (tipe bentukan)
    string* laguArray;        // Array tipe dasar dinamis
    int jumlahLagu;           // Jumlah lagu saat ini
    int kapasitas;            // Kapasitas array
    elmArtis* next;           // Pointer ke artis berikutnya
};

struct List {
    elmArtis* first;          // Pointer ke artis pertama
};
```

## Fitur Program

### CRUD Operations (Create, Read, Update, Delete)
1. **[1] Tambah Artis Baru ke Katalog** - Menambahkan artis dengan informasi genre dan tahun debut
2. **[2] Tambah Lagu ke Artis** - Menambahkan lagu ke dalam array lagu artis
3. **[3] Lihat Semua Data Katalog** - Menampilkan seluruh data artis dan lagu
4. **[4] Hapus Lagu dari Artis** - Menghapus lagu tertentu dari array lagu artis
5. **[5] Hapus Artis dari Katalog** - Menghapus artis beserta semua lagunya
6. **[8] Update Info Artis** - Mengubah informasi genre dan tahun debut artis

### Search Operations
7. **[6] Cari Artis di Katalog** - Pencarian artis dengan nama (case-insensitive)

### Reporting & Statistics
8. **[7] Lihat Laporan Statistik** - Menampilkan:

## Cara Kompilasi dan Menjalankan Program

### Kompilasi:
```bash
g++ -o katalog_musik.exe main.cpp katalog.cpp
```

### Menjalankan:
```bash
.\katalog_musik.exe
```

### Catatan:
- Pastikan compiler C++ (g++/MinGW) sudah terinstall
- Program menggunakan C++ standard library
- Database otomatis dibuat jika belum ada

## Database & Persistensi Data

### Format File CSV
- **Nama File**: `music_db.csv`
- **Delimiter**: Semicolon (`;`)
- **Format**: `NamaArtis;Genre;TahunDebut;JudulLagu`
- **Auto-save**: Setiap operasi CRUD otomatis menyimpan ke database

### Contoh Data CSV:
```csv
Taylor Swift;Pop;2006;Love Story
Taylor Swift;Pop;2006;Shake It Off
Ed Sheeran;Pop;2011;Perfect
The Weeknd;R&B;2010;Blinding Lights
```

## Validasi Input

Program memiliki validasi input yang robust:
- **Input Integer**: Loop sampai mendapat angka yang valid
- **Input String**: Tidak boleh kosong, otomatis trim whitespace
- **Input Menu**: Validasi pilihan menu dengan error handling
- **Error Message**: Pesan error yang jelas dan informatif

## Struktur File Program

```
D:\Struktur Data\TUBES STRUKDAT CPP\
├── katalog.h            # Header file dengan definisi struct dan prototype
├── katalog.cpp          # Implementasi semua fungsi
├── main.cpp             # Program utama dengan menu interface
├── music_db.csv         # Database musik (CSV)
├── katalog_musik.exe    # Executable program
└── README.md            # Dokumentasi program
```

## Fungsi-Fungsi Utama

### Operasi Artis
- `createElementArtis()` - Membuat node artis baru
- `insertLastArtis()` - Menambah artis ke akhir list
- `searchArtis()` - Mencari artis (case-insensitive)
- `deleteArtis()` - Menghapus artis dan semua lagunya
- `updateArtisInfo()` - Update info genre dan tahun debut

### Operasi Lagu
- `insertLagu()` - Menambah lagu ke array artis
- `deleteLagu()` - Menghapus lagu dari array artis
- Array lagu menggunakan alokasi dinamis dengan resize otomatis

### Operasi Tampilan
- `showAllData()` - Menampilkan semua data katalog
- `showReport()` - Menampilkan laporan statistik
- `displayMenu()` - Menampilkan menu utama
- `displayHeader()` - Menampilkan header dengan border

### Operasi Database
- `loadFromCSV()` - Membaca data dari file CSV
- `saveToCSV()` - Menyimpan data ke file CSV
- Auto-save setiap perubahan data

### Operasi Counting
- `countTotalArtis()` - Menghitung total artis
- `countTotalLagu()` - Menghitung total lagu di semua artis

## Fitur Pencarian

### Smart Search
- **Case Insensitive**: "taylor swift" = "Taylor Swift" = "TAYLOR SWIFT"
- **Whitespace Trimming**: Menghapus spasi di awal dan akhir
- **Sequential Search**: Traversal list untuk menemukan data

## Error Handling

Program dilengkapi dengan:
- Validasi tipe data input (integer vs string)
- Loop retry untuk input yang salah
- Pesan error yang deskriptif
- Handle file tidak ditemukan
- Memory cleanup yang proper

## Cara Penggunaan

1. **Jalankan Program**: Eksekusi `katalog_musik.exe`
2. **Auto-load**: Database otomatis dimuat dari CSV
3. **Pilih Menu**: Masukkan nomor [0-8]
4. **Input Data**: Ikuti instruksi untuk setiap operasi
5. **Auto-save**: Perubahan otomatis tersimpan

### Contoh Penggunaan:

**Tambah Artis:**
```
[1] Tambah Artis Baru ke Katalog
Nama: Taylor Swift
Genre: Pop
Tahun debut: 2006
```

**Tambah Lagu:**
```
[2] Tambah Lagu ke Artis  
Nama artis: Taylor Swift
Judul lagu: Love Story
```

**Lihat Data:**
```
[3] Lihat Semua Data Katalog
Menampilkan semua artis dan lagu mereka
```

## Spesifikasi Teknis

### Kompleksitas Algoritma
- **Insert Artis**: O(n) - insert di akhir list
- **Search Artis**: O(n) - sequential search
- **Delete Artis**: O(n) - traversal untuk cari node
- **Insert Lagu**: O(1) amortized - array dengan resize
- **Delete Lagu**: O(n) - shift array setelah delete

### Memory Management
- Dynamic memory allocation untuk array lagu
- Proper deallocation saat hapus artis
- Resize array otomatis saat kapasitas penuh

## Library yang Digunakan
```cpp
#include <iostream>     // I/O stream operations
#include <fstream>      // File input/output
#include <sstream>      // String stream parsing
#include <string>       // String class dan operations
#include <algorithm>    // Transform, manipulasi string
#include <limits>       // Numeric limits untuk input validation
```

---

**Dibuat untuk memenuhi Tugas Besar Struktur Data**
**Implementasi: Multi Linked List 1-N dengan Array Dinamis**
