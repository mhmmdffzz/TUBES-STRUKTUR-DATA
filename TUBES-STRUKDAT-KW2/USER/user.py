# USER/user.py

import time
from ADT.adt import Lagu, User as UserClass, Artis
from ADMIN.Admin import load_store, save_store, get_user_list, set_user_list, get_artis_list, set_artis_list

def register_user():
    users = get_user_list()
    uname = input("Masukkan username baru: ").strip()
    if any(u["username"] == uname for u in users):
        print("❌ Username sudah ada.")
        return
    pwd = input("Masukkan password: ").strip()
    nama_playlist = input("Nama playlist default: ").strip() or "My Playlist"

    new_id = max([u["id"] for u in users], default=0) + 1
    new_user = {
        "id": new_id,
        "username": uname,
        "password": pwd,
        "nama_playlist": nama_playlist,
        "playlist": []
    }
    users.append(new_user)
    set_user_list(users)
    print(f"✅ User '{uname}' berhasil dibuat.")

def login_user():
    users = get_user_list()
    uname = input("Username: ").strip()
    pwd = input("Password: ").strip()
    found = next((u for u in users if u["username"] == uname and u["password"] == pwd), None)
    if not found:
        print("❌ Login gagal.")
        return None
    print(f"✅ Login berhasil. Selamat datang, {uname}!")
    return found  # dict

def user_dashboard(user_dict):
    # user_dict is dict representation
    while True:
        print(f"\n🎧 DASHBOARD: {user_dict['username']}")
        print("1. Cari lagu & tambah ke playlist")
        print("2. Lihat playlist")
        print("3. Putar lagu (pilih)")
        print("4. Play all (loop)")
        print("0. Logout")
        choice = input("Pilihan: ").strip()
        store = load_store()
        artis_list = store["artis"]
        if choice == "1":
            query = input("Cari judul (substring): ").strip().lower()
            hits = []
            for a in artis_list:
                for l in a.get("lagu", []):
                    if query in l["judul"].lower():
                        hits.append((a, l))
            if not hits:
                print("🔍 Tidak ditemukan.")
                continue
            for i, (a, l) in enumerate(hits, 1):
                print(f"{i}. {l['judul']} - {a['nama']} ({l.get('play_count',0)} plays)")
            try:
                idx = int(input("Pilih nomor lagu (0 batal): "))
                if idx == 0:
                    continue
                sel = hits[idx-1][1]
                # tambahkan ke playlist user (simpan copy of song dict)
                # Hindari duplikat: pakai judul+artist
                pl = user_dict.get("playlist", [])
                key = (sel["judul"].lower(), hits[idx-1][0]["nama"].lower())
                exists = any((song["judul"].lower(), song.get("artist_name","").lower()) == key for song in pl)
                if exists:
                    print("❗ Lagu sudah ada di playlist.")
                    continue
                copy_song = dict(sel)
                copy_song["artist_name"] = hits[idx-1][0]["nama"]
                pl.append(copy_song)
                user_dict["playlist"] = pl
                # save back
                users = store["users"]
                for u in users:
                    if u["id"] == user_dict["id"]:
                        u["playlist"] = pl
                save_store(store)
                print(f"✅ '{copy_song['judul']}' ditambahkan ke playlist.")
            except (ValueError, IndexError):
                print("Input tidak valid.")
        elif choice == "2":
            print(f"\n🎵 Playlist: {user_dict.get('nama_playlist','My Playlist')}")
            pl = user_dict.get("playlist", [])
            if not pl:
                print("(Kosong)")
            for i, s in enumerate(pl, 1):
                print(f"{i}. {s['judul']} - {s.get('artist_name','')}")
        elif choice == "3":
            pl = user_dict.get("playlist", [])
            if not pl:
                print("Playlist kosong.")
                continue
            for i, s in enumerate(pl, 1):
                print(f"{i}. {s['judul']} - {s.get('artist_name','')} ({s.get('play_count',0)} plays)")
            try:
                idx = int(input("Pilih nomor lagu: "))
                sel = pl[idx-1]
                # increment play_count in global store (find song in artis and increment)
                for a in store["artis"]:
                    for l in a.get("lagu", []):
                        if l["judul"] == sel["judul"] and a["nama"] == sel.get("artist_name",""):
                            l["play_count"] = l.get("play_count", 0) + 1
                # also increment in playlist copy
                sel["play_count"] = sel.get("play_count", 0) + 1
                save_store(store)
                print(f"▶ Memutar: {sel['judul']}")
            except (ValueError, IndexError):
                print("Input tidak valid.")
        elif choice == "4":
            pl = user_dict.get("playlist", [])
            if not pl:
                print("Playlist kosong.")
                continue
            print("▶ Memutar semua lagu...")
            for sel in pl:
                # increment global
                for a in store["artis"]:
                    for l in a.get("lagu", []):
                        if l["judul"] == sel["judul"] and a["nama"] == sel.get("artist_name",""):
                            l["play_count"] = l.get("play_count", 0) + 1
                sel["play_count"] = sel.get("play_count", 0) + 1
                print(f"   ▶ {sel['judul']}")
                time.sleep(0.3)
            save_store(store)
            print("⏹ Selesai.")
        elif choice == "0":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid.")
