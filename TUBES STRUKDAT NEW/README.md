# 🎵 Aplikasi Katalog Album Musik

**Aplikasi Katalog Album Musik berbasis Command Line Interface (CLI)** yang dibangun dengan Python 3. Aplikasi ini menggunakan struktur data **Multi Linked List (MLL)** dengan konsep **Parent-Child Relationship** dimana Parent berupa Record (Class) dan Child berupa Tipe Dasar (String).

---

## 📋 Deskripsi Proyek

Aplikasi ini adalah sistem katalog musik sederhana untuk mencatat **Daftar Artis** dan **Judul Lagu** yang mereka miliki. Mirip seperti sampul belakang kaset/CD.

### Struktur Data MLL (Multi Linked List) 1-N:

| Komponen | Tipe | Atribut |
|----------|------|---------|
| **PARENT (Artis)** | Record (Class Object) | `nama_artis` (String), `genre` (String), `tahun_debut` (Integer), Pointer ke Child |
| **CHILD (Lagu)** | Tipe Dasar (String) | Judul lagu saja (contoh: "Hati-Hati di Jalan", "Monokrom", "Dan") |

### Keunggulan Struktur Ini:
- ✅ **Sesuai Syarat MLL**: Parent = Record, Child = Tipe Dasar
- ✅ **Kode Lebih Pendek**: Tidak perlu class Song, child hanya List of Strings
- ✅ **Mudah Dipahami**: Konsep Artis punya Lagu (1 ke N) yang intuitif

---

## 🚀 Fitur Aplikasi (7 Fitur)

| No | Fitur | Deskripsi | Konsep Teknis |
|----|-------|-----------|---------------|
| 1 | **Tambah Artis** | Menambahkan artis baru ke database | INSERT LAST (Parent) |
| 2 | **Tambah Lagu ke Artis** | Menambahkan judul lagu ke artis tertentu | INSERT CHILD (String) |
| 3 | **Lihat Semua Data** | Tampilkan semua artis & daftar lagunya | Nested Loop Traversal |
| 4 | **Hapus Lagu** | Hapus 1 judul lagu dari artis | DELETE CHILD |
| 5 | **Hapus Artis** | Hapus artis + semua lagunya otomatis | DELETE CASCADE |
| 6 | **Cari Artis** | Cari artis berdasarkan nama | Sequential Search |
| 7 | **Laporan** | Counting total lagu & Max artis terbanyak | Pengolahan MLL |

### Detail Fitur Laporan (Pengolahan MLL):
- **COUNTING**: Menghitung jumlah lagu per artis dan total seluruh lagu di database
- **MAX**: Mencari artis dengan jumlah lagu paling banyak

---

## 📁 Struktur Folder

```
TUBES STRUKDAT/
│
├── main.py                    # Entry point aplikasi (Load → Menu → Save)
│
├── database/
│   ├── __init__.py            # Package marker
│   ├── models.py              # Class Artist (Parent dengan List[str] songs)
│   ├── data_store.py          # Global storage & helper functions (CRUD)
│   └── music_db.json          # Database file (JSON format)
│
├── admin/
│   ├── __init__.py            # Package marker
│   └── menu_admin.py          # Menu katalog (7 fitur)
│
└── README.md                  # Dokumentasi ini
```

---

## 🔧 Cara Install & Run

### 1. **Requirement**
- Python 3.7 atau lebih baru
- Windows/Linux/Mac dengan terminal

### 2. **Cek Versi Python**
```bash
python --version
```

### 3. **Masuk ke Folder Project**
```bash
cd "d:\Struktur Data\TUBES STRUKDAT"
```

### 4. **Jalankan Aplikasi**
```bash
python main.py
```

### 5. **Navigasi Menu**
```
======================================================================
                      APLIKASI KATALOG ALBUM MUSIK
======================================================================

Selamat Datang di Katalog Album Musik!

Aplikasi ini menggunakan struktur MLL (Multi Linked List):
  - PARENT: Artis (Record dengan nama, genre, tahun debut)
  - CHILD : Lagu (Tipe Dasar String - judul lagu)

----------------------------------------------------------------------

  1. MASUK KE KATALOG MUSIK
  2. SIMPAN & KELUAR

----------------------------------------------------------------------
>> Pilih menu (1-2):
```

---

## 📊 Database Schema (JSON)

```json
{
  "artists": [
    {
      "nama_artis": "Sheila on 7",
      "genre": "Pop Rock",
      "tahun_debut": 1996,
      "songs": [
        "Dan",
        "Sephia",
        "Kita",
        "Melompat Lebih Tinggi"
      ]
    },
    {
      "nama_artis": "Tulus",
      "genre": "Pop",
      "tahun_debut": 2011,
      "songs": [
        "Hati-Hati di Jalan",
        "Monokrom",
        "Sepatu"
      ]
    }
  ]
}
```

**Penjelasan:**
- `nama_artis`: Nama artis (String) - KEY UNIK
- `genre`: Genre musik (String)
- `tahun_debut`: Tahun debut artis (Integer)
- `songs`: **List of String** (judul lagu saja, bukan object)

---

## 🎯 Flow Aplikasi

```
┌─────────────────────────────────────────┐
│  START: python main.py                  │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  load_database() dari music_db.json     │
│  • Load artists_list ke memory (RAM)    │
│  • Rebuild Artist objects               │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  MAIN MENU (while True)                 │
│  [1] Masuk ke Katalog Musik             │
│  [2] Simpan & Keluar                    │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  MENU KATALOG (7 Fitur)                 │
│  [1] Tambah Artis                       │
│  [2] Tambah Lagu ke Artis               │
│  [3] Lihat Semua Data                   │
│  [4] Hapus Lagu                         │
│  [5] Hapus Artis                        │
│  [6] Cari Artis                         │
│  [7] Laporan (Counting & Max)           │
│  [0] Kembali ke Menu Utama              │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  EXIT: save_database()                  │
│  • Convert Artist objects → dict        │
│  • Write to music_db.json               │
│  • Program terminate                    │
└─────────────────────────────────────────┘
```

---

## 💡 Konsep Teknis & Algoritma

### 1. **Struktur MLL (Multi Linked List) 1-N**

```
┌─────────────────────────────────────────────────────────────┐
│                    PARENT (Artist)                          │
│  ┌─────────────┬─────────────┬──────────────┬─────────┐    │
│  │ nama_artis  │    genre    │ tahun_debut  │  songs  │───►│
│  │ "Sheila on 7"│ "Pop Rock" │    1996      │  [...]  │    │
│  └─────────────┴─────────────┴──────────────┴─────────┘    │
└─────────────────────────────────────────────────────────────┘
                                                    │
                                                    ▼
                              ┌─────────────────────────────────┐
                              │        CHILD (List[str])        │
                              │  ┌───────────────────────────┐  │
                              │  │ "Dan"                     │  │
                              │  │ "Sephia"                  │  │
                              │  │ "Kita"                    │  │
                              │  │ "Melompat Lebih Tinggi"   │  │
                              │  └───────────────────────────┘  │
                              └─────────────────────────────────┘
```

**Kode:**
```python
class Artist:
    def __init__(self, nama_artis, genre, tahun_debut):
        self.nama_artis = nama_artis    # String
        self.genre = genre              # String
        self.tahun_debut = tahun_debut  # Integer
        self.songs = []                 # List of String (Child - Tipe Dasar)
```

### 2. **INSERT LAST (Tambah Artis)**
Artis baru ditambahkan di akhir list:
```python
def add_artist(nama_artis, genre, tahun_debut):
    new_artist = Artist(nama_artis, genre, tahun_debut)
    artists_list.append(new_artist)  # INSERT LAST
    return True
```

### 3. **INSERT CHILD (Tambah Lagu)**
Lagu (string) ditambahkan ke list songs artis:
```python
def add_song(self, judul_lagu):
    self.songs.append(judul_lagu)  # Child adalah String
```

### 4. **DELETE CASCADE (Hapus Artis)**
Saat artis dihapus, semua lagunya otomatis ikut terhapus:
```python
def delete_artist(name):
    artist = get_artist(name)
    artists_list.remove(artist)  # Lagu (child) ikut terhapus
    return True
```

### 5. **Sequential Search (Cari Artis)**
Mencari artis berdasarkan nama dengan partial match:
```python
def search_artist(keyword):
    results = []
    for artist in artists_list:
        if keyword.lower() in artist.nama_artis.lower():
            results.append(artist)
    return results
```

### 6. **COUNTING (Hitung Total Lagu)**
Menghitung total lagu di seluruh database:
```python
def count_total_songs():
    total = 0
    for artist in artists_list:
        total += artist.song_count()  # len(self.songs)
    return total
```

### 7. **MAX (Artis dengan Lagu Terbanyak)**
Mencari artis dengan jumlah lagu paling banyak:
```python
def get_artist_with_most_songs():
    max_artist = artists_list[0]
    max_count = max_artist.song_count()
    
    for artist in artists_list:
        if artist.song_count() > max_count:
            max_artist = artist
            max_count = artist.song_count()
    
    return (max_artist, max_count)
```

---

## 🧪 Testing & Contoh Penggunaan

### Test Case 1: Tambah Artis Baru
```
1. Pilih [1] Masuk ke Katalog Musik
2. Pilih [1] Tambah Artis
3. Input:
   - Nama Artis: "Dewa 19"
   - Genre: "Rock"
   - Tahun Debut: 1992
4. Hasil: Artis "Dewa 19" berhasil ditambahkan
```

### Test Case 2: Tambah Lagu ke Artis
```
1. Pilih [2] Tambah Lagu ke Artis
2. Pilih artis: "Dewa 19"
3. Input Judul Lagu: "Kangen"
4. Hasil: Lagu "Kangen" berhasil ditambahkan ke "Dewa 19"
```

### Test Case 3: Lihat Laporan
```
1. Pilih [7] Laporan (Counting & Max)
2. Hasil:
   📊 STATISTIK KATALOG
      Total Artis: 4
      Total Lagu : 12

   📋 JUMLAH LAGU PER ARTIS:
      1. Sheila on 7: 4 lagu ████
      2. Tulus: 3 lagu ███
      3. Raisa: 2 lagu ██
      4. Isyana Sarasvati: 2 lagu ██

   🏆 ARTIS DENGAN LAGU TERBANYAK:
      Sheila on 7 dengan 4 lagu!
```

### Test Case 4: DELETE CASCADE
```
1. Pilih [5] Hapus Artis
2. Pilih artis: "Tulus"
3. Konfirmasi: y
4. Hasil: Artis "Tulus" dan 3 lagunya berhasil dihapus
5. Cek [3] Lihat Semua Data → Tulus tidak ada lagi
```

---

## 📝 Penjelasan Kode Per File

### 📄 `main.py`
**Fungsi:** Entry point aplikasi  
**Alur:**
1. `load_database()` - Baca JSON, rebuild Artist objects di memory
2. `while True` loop - Menu utama (Katalog / Simpan & Keluar)
3. Route ke `menu_katalog()` untuk fitur katalog
4. `save_database()` saat exit - Simpan perubahan ke JSON

**Konsep Penting:**
- Load dilakukan 1x di awal (efficient)
- Save dilakukan 1x saat exit (efficient)
- Data di memory (RAM) selama aplikasi running

---

### 📄 `database/models.py`
**Fungsi:** Definisi class Artist (Parent)

**Class Artist:**
```python
class Artist:
    def __init__(self, nama_artis, genre, tahun_debut):
        self.nama_artis = nama_artis    # String - KEY UNIK
        self.genre = genre              # String
        self.tahun_debut = tahun_debut  # Integer
        self.songs = []                 # List[str] - Child (Tipe Dasar)
```

**Method Penting:**
| Method | Fungsi |
|--------|--------|
| `add_song(judul)` | INSERT CHILD - tambah judul lagu ke list |
| `remove_song(judul)` | DELETE CHILD - hapus judul lagu dari list |
| `song_count()` | COUNTING - hitung jumlah lagu |
| `has_song(judul)` | Cek apakah lagu sudah ada (validasi duplikat) |
| `to_dict()` | Convert object → dictionary (untuk JSON) |
| `from_dict(data)` | Convert dictionary → object (load JSON) |

---

### 📄 `database/data_store.py`
**Fungsi:** Global storage & helper functions  

**Global Variable:**
```python
artists_list = []  # List semua Artist objects
```

**Helper Functions:**

| Fungsi | Deskripsi | Return |
|--------|-----------|--------|
| `load_database()` | Baca JSON → Rebuild objects | void |
| `save_database()` | Convert objects → Write JSON | void |
| `add_artist(nama, genre, tahun)` | INSERT LAST artis | bool |
| `delete_artist(name)` | DELETE CASCADE artis | bool |
| `get_artist(name)` | Sequential Search artis | Artist/None |
| `search_artist(keyword)` | Partial match search | List[Artist] |
| `add_song_to_artist(artist, judul)` | INSERT CHILD lagu | bool |
| `delete_song_from_artist(artist, judul)` | DELETE CHILD lagu | bool |
| `count_total_songs()` | COUNTING total lagu | int |
| `get_artist_with_most_songs()` | MAX artis terbanyak | (Artist, int) |
| `get_all_artists_sorted_by_songs()` | Sort by song count | List[(Artist, int)] |

---

### 📄 `admin/menu_admin.py`
**Fungsi:** Menu katalog dengan 7 fitur

| Fungsi | Fitur |
|--------|-------|
| `katalog_add_artist()` | Tambah Artis (INSERT PARENT) |
| `katalog_add_song()` | Tambah Lagu ke Artis (INSERT CHILD) |
| `katalog_view_all()` | Lihat Semua Data (NESTED VIEW) |
| `katalog_delete_song()` | Hapus Lagu (DELETE CHILD) |
| `katalog_delete_artist()` | Hapus Artis (DELETE CASCADE) |
| `katalog_search_artist()` | Cari Artis (SEQUENTIAL SEARCH) |
| `katalog_report()` | Laporan (COUNTING & MAX) |
| `menu_katalog()` | Menu loop utama katalog |

**Contoh Nested View (Parent-Child):**
```python
def katalog_view_all():
    for i, artist in enumerate(artists_list, 1):  # Loop Parent
        print(f"{i}. {artist.nama_artis}")
        print(f"   Genre: {artist.genre}")
        print(f"   Tahun Debut: {artist.tahun_debut}")
        
        for j, judul_lagu in enumerate(artist.songs, 1):  # Loop Child
            print(f"      {j}. {judul_lagu}")
```

---

## 🎓 Ringkasan Konsep Struktur Data

| Konsep | Implementasi dalam Aplikasi |
|--------|---------------------------|
| **MLL (Multi Linked List)** | Artis (Parent) → List Judul Lagu (Child) |
| **Parent = Record** | Class Artist dengan atribut nama, genre, tahun debut |
| **Child = Tipe Dasar** | String (judul lagu) dalam List |
| **INSERT LAST** | `artists_list.append(new_artist)` |
| **INSERT CHILD** | `artist.songs.append(judul_lagu)` |
| **DELETE PARENT** | `artists_list.remove(artist)` |
| **DELETE CHILD** | `artist.songs.pop(index)` |
| **DELETE CASCADE** | Hapus artis = lagu ikut terhapus (child ada dalam parent) |
| **Sequential Search** | Loop `for artist in artists_list` |
| **COUNTING** | `sum(artist.song_count() for artist in artists_list)` |
| **MAX** | Loop cari `artist.song_count()` terbesar |

---

## 📌 Catatan Penting

1. **Data Tersimpan Permanen**: Perubahan disimpan ke `music_db.json` saat pilih "Simpan & Keluar"
2. **Case Insensitive**: Pencarian artis tidak case-sensitive ("tulus" = "Tulus")
3. **Validasi Duplikat**: Tidak bisa menambahkan artis atau lagu yang sudah ada
4. **Konfirmasi Hapus**: Selalu ada konfirmasi sebelum menghapus data

---

## 👥 Kontributor

- Mahasiswa Struktur Data

---

## 📜 Lisensi

Project ini dibuat untuk keperluan tugas mata kuliah Struktur Data.
