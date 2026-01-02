# 📋 CHEATSHEET - KATALOG MUSIK (MLL 1-N)

## 📌 STRUKTUR DATA

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
