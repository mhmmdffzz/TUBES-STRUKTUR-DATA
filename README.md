# KATALOG MUSIK DIGITAL

## Deskripsi Program
Program Katalog Musik adalah aplikasi manajemen data musik berbasis **Multi Linked List (MLL) 1-N** yang diimplementasikan dengan C++ sesuai spesifikasi Tugas Besar Struktur Data. Program ini memungkinkan pengelolaan data artis dan lagu-lagunya dengan database CSV.

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

**© 2026 - Katalog Musik Efficient Version**  
*Implementasi Multi Linked List 1-N dengan C++ Standard Library*