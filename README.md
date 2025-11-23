# 🎵 Music Streaming Platform - CLI Application

**Aplikasi Music Streaming berbasis Command Line Interface (CLI)** yang dibangun dengan Python 3. Aplikasi ini mengelola database musik dengan konsep **Parent-Child Relationship** dan **Memory Linked List (MLL)** untuk playlist management.

---

## 📋 Deskripsi Proyek

Aplikasi ini adalah sistem manajemen musik streaming yang memiliki 2 role user:
- **Admin** - Mengelola database musik (artis, lagu, analytics)
- **User** - Mengelola playlist pribadi dengan lagu-lagu dari database

### Konsep Utama:
1. **Parent 1 (Artist)** memiliki **Child (Songs)** - One-to-Many relationship
2. **Parent 2 (User)** memiliki **Playlist (MLL)** - Referensi ke Song objects, bukan copy
3. **JSON File Persistence** - Data tersimpan permanen di `music_db.json`

---

## 🚀 Fitur Aplikasi

### 👨‍💼 Menu Admin (9 Fitur)

| No | Fitur | Deskripsi | Konsep Teknis |
|----|-------|-----------|---------------|
| 1 | **Tambah Artis** | Menambahkan artis baru ke database | INSERT LAST (`append`) |
| 2 | **Tambah Lagu ke Artis** | Menambahkan lagu ke artis tertentu | INSERT CHILD (nested list) |
| 3 | **Lihat Semua Musik** | Tampilkan semua artis & lagu | Nested Loop Traversal |
| 4 | **Hapus Artis** | Hapus artis + semua lagunya | DELETE CASCADE |
| 5 | **Hapus Lagu** | Hapus 1 lagu dari artis | DELETE CHILD |
| 6 | **Top Artist** | Artis dengan lagu terbanyak | Max Finding Algorithm |
| 7 | **Cari Lagu** | Cari lagu berdasarkan keyword | Sequential Search |
| 8 | **Tambah Admin** | Menambahkan admin baru | User Management |
| 9 | **Analytics** | Trending songs, top artists, top users | Data Analysis |

### 👤 Menu User (8 Fitur)

| No | Fitur | Deskripsi | Konsep Teknis |
|----|-------|-----------|---------------|
| 1 | **Register** | Daftar user baru | INSERT FIRST (`insert(0)`) |
| 2 | **Login** | Masuk dengan username/password | Authentication |
| 3 | **Tambah Lagu** | Tambah lagu ke playlist | MLL Append (referensi) |
| 4 | **Putar Lagu** | Play lagu tertentu | Update play_count |
| 5 | **Hapus Lagu** | Hapus lagu dari playlist | List Remove |
| 6 | **Lihat Playlist** | Tampilkan playlist pribadi | List Traversal |
| 7 | **Pindah Urutan** | Swap posisi 2 lagu | Tuple Unpacking Swap |
| 8 | **Putar Semua** | Play all songs di playlist | Loop Iteration |

---

## 📁 Struktur Folder

```
TUBES STRUKDAT/
│
├── main.py                    # Entry point aplikasi (Load → Menu Loop → Save)
│
├── database/
│   ├── __init__.py
│   ├── models.py              # Class definitions (Song, Artist, User, Admin)
│   ├── data_store.py          # Global storage & helper functions (CRUD)
│   └── music_db.json          # Database file (JSON format)
│
├── admin/
│   ├── __init__.py
│   └── menu_admin.py          # 9 fitur admin
│
├── user/
│   ├── __init__.py
│   └── menu_user.py           # 8 fitur user
│
└── README.md                  # Dokumentasi ini
```

---

## 🔧 Cara Install & Run

### 1. **Requirement**
- Python 3.7 atau lebih baru
- Windows/Linux/Mac dengan terminal

### 2. **Install Python** (jika belum)
```bash
# Cek versi Python
python --version
```

### 3. **Download/Clone Project**
```bash
cd "d:\TUBES STRUKDAT"
```

### 4. **Jalankan Aplikasi**
```bash
python main.py
```

### 5. **Login Credentials**

**Admin Default:**
- Username: `admin` | Password: `admin123`
- Username: `manager` | Password: `manager123`

**User Default:**
- Username: `Budi` | Password: `budi123`
- Username: `Andi` | Password: `andi123`
- Username: `Dewi` | Password: `dewi456`
- ...atau register user baru

---

## 💡 Konsep Teknis & Algoritma

### 1. **Memory Linked List (MLL)**
Playlist user menyimpan **referensi** ke Song object, bukan copy:
```python
# Saat user tambah lagu ke playlist:
current_user.playlist.append(song)  # Simpan referensi

# Saat user play lagu:
song.play_count += 1  # Update object asli di database
```

**Keuntungan MLL:**
- Hemat memory (tidak duplikasi data)
- Update play_count langsung tereflek ke semua user
- Sinkronisasi data otomatis

### 2. **INSERT FIRST vs INSERT LAST**

**INSERT FIRST** (User Registration):
```python
users_list.insert(0, new_user)  # User baru di posisi pertama
```

**INSERT LAST** (Add Artist):
```python
artists_list.append(new_artist)  # Artist baru di posisi terakhir
```

### 3. **DELETE CASCADE**
Saat artis dihapus, semua referensi lagu di playlist user juga dihapus:
```python
for user in users_list:
    user.playlist = [song for song in user.playlist 
                     if song.artist_name != artist_name]
```

### 4. **Sequential Search**
Mencari lagu berdasarkan keyword:
```python
for artist in artists_list:
    for song in artist.songs:
        if keyword.lower() in song.title.lower():
            results.append(song)
```

### 5. **Swap dengan Tuple Unpacking**
Menukar posisi 2 lagu di playlist:
```python
playlist[idx1], playlist[idx2] = playlist[idx2], playlist[idx1]
```

---

## 📊 Database Schema (JSON)

```json
{
  "artists": [
    {
      "name": "Tulus",
      "genre": "Pop",
      "verified": true,
      "songs": [
        {
          "title": "Hati-Hati di Jalan",
          "year": 2022,
          "duration": 240,
          "artist_name": "Tulus",
          "play_count": 15
        }
      ]
    }
  ],
  "users": [
    {
      "username": "Budi",
      "password": "budi123",
      "playlist_name": "Playlist Budi",
      "playlist_refs": [
        {
          "title": "Hati-Hati di Jalan",
          "artist": "Tulus"
        }
      ]
    }
  ],
  "admins": [
    {
      "username": "admin",
      "password": "admin123"
    }
  ]
}
```

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
│  • Load artists_list                    │
│  • Load users_list (rebuild MLL)        │
│  • Load admins_list                     │
└─────────────┬───────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│  MAIN MENU LOOP (while True)            │
│  [1] Admin Login                        │
│  [2] User Login                         │
│  [3] User Register                      │
│  [4] Exit                               │
└─────────────┬───────────────────────────┘
              │
      ┌───────┴────────┐
      ▼                ▼
┌──────────┐    ┌──────────────┐
│  ADMIN   │    │     USER     │
│  MENU    │    │     MENU     │
│ (9 fitur)│    │  (8 fitur)   │
└──────────┘    └──────────────┘
      │                │
      └───────┬────────┘
              ▼
┌─────────────────────────────────────────┐
│  EXIT: save_database()                  │
│  • Convert objects to dict              │
│  • Write to music_db.json               │
│  • Program terminate                    │
└─────────────────────────────────────────┘
```

---

## 🧪 Testing & Debugging

### Test Case 1: Register User Baru
```
1. Pilih [3] User Register
2. Input username: "TestUser"
3. Input password: "test123"
4. Input nama playlist: "My Playlist"
5. Exit aplikasi
6. Cek music_db.json → user "TestUser" harus ada di array "users"
```

### Test Case 2: MLL Concept
```
1. Login sebagai user
2. Tambah lagu "Dan" dari Sheila on 7
3. Play lagu tersebut (play_count naik)
4. Login sebagai user lain
5. Tambah lagu "Dan" yang sama
6. Play lagu tersebut (play_count naik lagi)
7. Exit & cek JSON → play_count "Dan" harus terakumulasi
```

### Test Case 3: DELETE CASCADE
```
1. Login sebagai admin
2. Hapus artis "Tulus"
3. Exit aplikasi
4. Login sebagai user yang punya lagu Tulus di playlist
5. Lihat playlist → lagu Tulus harus hilang otomatis
```

---

## 📝 Penjelasan Kode Per File

### 📄 `main.py`
**Fungsi:** Entry point aplikasi  
**Alur:**
1. `load_database()` - Baca JSON, rebuild objects di memory
2. `while True` loop - Menu utama
3. Route ke admin/user menu berdasarkan pilihan
4. `save_database()` saat exit - Simpan perubahan ke JSON

**Konsep Penting:**
- Load dilakukan 1x di awal (efficient)
- Save dilakukan 1x saat exit (efficient)
- Data di memory selama aplikasi running

---

### 📄 `database/models.py`
**Fungsi:** Definisi class untuk semua entitas  

**Class yang ada:**
1. **Song** - Representasi 1 lagu (title, year, duration, play_count)
2. **Artist** - Representasi 1 artis (name, genre, verified, songs[])
3. **User** - Representasi 1 user (username, password, playlist[])
4. **Admin** - Representasi 1 admin (username, password)

**Method Penting:**
- `to_dict()` - Convert object → dictionary (untuk save ke JSON)
- `from_dict()` - Convert dictionary → object (saat load dari JSON)
- `song_count()` - Hitung jumlah lagu (Artist/User)

---

### 📄 `database/data_store.py`
**Fungsi:** Global storage & helper functions  

**Global Variables:**
```python
artists_list = []  # List semua artis
users_list = []    # List semua user
admins_list = []   # List semua admin
```

**Helper Functions:**
- `load_database()` - Baca JSON → Rebuild objects
- `save_database()` - Convert objects → Write JSON
- `add_artist()` - INSERT LAST artis
- `add_user()` - INSERT FIRST user
- `delete_artist()` - DELETE CASCADE artis + cleanup playlist
- `search_song()` - Sequential search lagu
- `get_trending_songs()` - Sort by play_count
- `verify_admin()` - Check credentials admin
- `get_user()` - Find user by username

**Konsep MLL di sini:**
```python
# Saat load users dari JSON:
for song_ref in data['playlist_refs']:
    # Cari song object yang sesuai dari artists_list
    found_song = search_song_object(song_ref['title'], song_ref['artist'])
    if found_song:
        user.playlist.append(found_song)  # Simpan REFERENSI
```

---

### 📄 `admin/menu_admin.py`
**Fungsi:** Semua fitur admin (9 fitur)  

**Fitur Utama:**
1. **admin_add_artist()** - INSERT LAST dengan validasi duplikasi
2. **admin_add_song()** - INSERT CHILD ke artist.songs[]
3. **admin_view_all_music()** - Nested loop (artist → songs)
4. **admin_delete_artist()** - DELETE CASCADE + cleanup playlist
5. **admin_delete_song()** - DELETE CHILD + cleanup playlist
6. **admin_top_artist()** - Find max song_count()
7. **admin_search_song()** - Sequential search dengan keyword
8. **admin_add_admin()** - User management
9. **admin_analytics()** - Trending songs, top artists, top users

**Contoh Kode DELETE CASCADE:**
```python
def admin_delete_artist():
    # 1. Hapus dari artists_list
    artists_list.remove(found_artist)
    
    # 2. Cleanup playlist semua user (CASCADE)
    for user in users_list:
        user.playlist = [s for s in user.playlist 
                         if s.artist_name != artist_name]
```

---

### 📄 `user/menu_user.py`
**Fungsi:** Semua fitur user (8 fitur)  

**Fitur Utama:**
1. **user_register()** - INSERT FIRST ke users_list
2. **user_login()** - Authentication dengan password
3. **user_add_song()** - MLL append dengan validasi duplikasi
4. **user_play_song()** - Update play_count (karena MLL, global ikut update)
5. **user_remove_song()** - Remove dari playlist (tidak hapus dari database)
6. **user_view_playlist()** - Tampilkan playlist pribadi
7. **user_swap_songs()** - Swap dengan tuple unpacking
8. **user_play_all()** - Loop semua lagu dengan animasi

**Contoh Kode MLL:**
```python
def user_add_song(current_user):
    # Cari song object dari database
    found_song = search_song_in_artists(title, artist)
    
    # Tambahkan REFERENSI ke playlist (bukan copy)
    current_user.playlist.append(found_song)
    
    # Ketika user play lagu:
    found_song.play_count += 1  # Object asli di database terupdate
```

**Contoh Kode Swap:**
```python
def user_swap_songs(current_user):
    idx1 = int(input("Posisi lagu 1: ")) - 1
    idx2 = int(input("Posisi lagu 2: ")) - 1
    
    # Tuple unpacking swap (Python way)
    current_user.playlist[idx1], current_user.playlist[idx2] = \
        current_user.playlist[idx2], current_user.playlist[idx1]
```

---

## 🛡️ Error Handling

Aplikasi ini memiliki validasi di setiap input:
- ✅ Validasi duplikasi (artis, lagu, user)
- ✅ Validasi index (saat pilih dari list)
- ✅ Validasi file JSON (error handling load/save)
- ✅ Validasi password (login)
- ✅ Validasi empty list (cek sebelum akses)

---

## 🎓 Konsep Struktur Data yang Digunakan

| Konsep | Implementasi | Lokasi |
|--------|--------------|--------|
| **List (Array)** | `artists_list`, `users_list`, `playlist` | Semua file |
| **INSERT FIRST** | `users_list.insert(0, user)` | `menu_user.py` |
| **INSERT LAST** | `artists_list.append(artist)` | `menu_admin.py` |
| **DELETE CASCADE** | Hapus parent + cleanup children | `data_store.py` |
| **Sequential Search** | Loop cari keyword | `data_store.py` |
| **Nested Loop** | Loop artist → loop songs | `menu_admin.py` |
| **MLL (Memory Linked List)** | Playlist simpan referensi | `models.py` |
| **Sorting** | `sorted(songs, key=lambda x: x.play_count)` | `data_store.py` |
| **Max Finding** | `max(artists, key=lambda x: x.song_count())` | `menu_admin.py` |

---

## 📞 Support & Troubleshooting

### Problem 1: "File not found" saat run
**Solusi:** Pastikan Anda di folder `TUBES STRUKDAT` saat run `python main.py`

### Problem 2: Data tidak tersimpan setelah exit
**Solusi:** Pastikan pilih **[4] Exit** di menu, jangan force close (Ctrl+C)

### Problem 3: Play count tidak terupdate
**Solusi:** Ini bug jika MLL tidak diimplementasi benar. Cek `User.from_dict()` di `models.py`

### Problem 4: JSON error saat load
**Solusi:** Cek format JSON di `music_db.json`, pastikan valid (gunakan JSON validator)

---

## 🎉 Kesimpulan

Aplikasi Music Streaming Platform ini mendemonstrasikan:
✅ **Parent-Child Relationship** (Artist-Song, User-Playlist)  
✅ **Memory Linked List** (Playlist referensi, bukan copy)  
✅ **CRUD Operations** (Create, Read, Update, Delete)  
✅ **JSON Persistence** (Load/Save dari file)  
✅ **Sequential Search & Sorting**  
✅ **DELETE CASCADE** (Hapus parent + cleanup children)  
✅ **INSERT FIRST & INSERT LAST**  
✅ **Authentication System**  

Semua konsep Struktur Data diimplementasikan dengan real-world use case! 🚀

---

**Dibuat dengan ❤️ untuk Tugas Besar Struktur Data**  
**© 2025 Music Streaming Platform CLI**
