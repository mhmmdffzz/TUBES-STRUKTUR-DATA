# MAIN/main.py

from ADMIN.Admin import load_store, save_store, get_artis_list, set_artis_list, get_user_list, set_user_list
from ADT.adt import Lagu, Artis, User
from USER.user import register_user, login_user, user_dashboard
import os

def print_main_menu():
    print("\n=== APLIKASI MANAJEMEN MUSIK ===")
    print("1. Admin - Tambah Artis")
    print("2. Admin - Tambah Lagu ke Artis")
    print("3. Admin - Lihat Semua Musik")
    print("4. Admin - Hapus Artis")
    print("5. Admin - Lihat Top Artist (by number of songs)")
    print("6. Registrasi User")
    print("7. Login User")
    print("8. Trending Song (by plays)")
    print("0. Keluar")

# helper admin functions here for simple CRUD using store
def admin_add_artis():
    store = load_store()
    nama = input("Nama artis: ").strip()
    genre = input("Genre: ").strip()
    isv = input("Verified? (y/n): ").strip().lower() == 'y'
    new_id = max([a["id"] for a in store["artis"]], default=0) + 1
    artis = {"id": new_id, "nama": nama, "genre": genre, "is_verified": isv, "lagu": []}
    store["artis"].append(artis)
    save_store(store)
    print(f"✅ Artis '{nama}' ditambahkan.")

def admin_add_lagu():
    store = load_store()
    if not store["artis"]:
        print("Belum ada artis, tambahkan artis dulu.")
        return
    print("Pilih artis (ketik id):")
    for a in store["artis"]:
        print(f"{a['id']}. {a['nama']} [{a['genre']}]")
    try:
        aid = int(input("ID artis: "))
    except ValueError:
        print("Input tidak valid.")
        return
    artis = next((x for x in store["artis"] if x["id"] == aid), None)
    if not artis:
        print("Artis tidak ditemukan.")
        return
    judul = input("Judul lagu: ").strip()
    try:
        tahun = int(input("Tahun rilis: "))
        dur = int(input("Durasi (detik): "))
    except ValueError:
        print("Tahun/durasi harus angka.")
        return
    lagu = {"judul": judul, "tahun": tahun, "durasi": dur, "play_count": 0, "artist_name": artis["nama"]}
    artis["lagu"].append(lagu)
    save_store(store)
    print(f"✅ Lagu '{judul}' ditambahkan ke artis {artis['nama']}.")

def admin_view_all_music():
    store = load_store()
    if not store["artis"]:
        print("(Database kosong)")
        return
    for a in store["artis"]:
        v = "✔" if a.get("is_verified") else ""
        print(f"\n🎤 {a['nama']} [{a['genre']}] {v}")
        if not a.get("lagu"):
            print("   (Belum ada lagu)")
        else:
            for i, l in enumerate(a["lagu"], 1):
                print(f"   {i}. {l['judul']} - {l.get('play_count',0)} plays")

def admin_delete_artis():
    store = load_store()
    for a in store["artis"]:
        print(f"{a['id']}. {a['nama']}")
    try:
        aid = int(input("Pilih ID artis untuk dihapus: "))
    except ValueError:
        print("Input tidak valid.")
        return
    target = next((x for x in store["artis"] if x["id"] == aid), None)
    if not target:
        print("Artis tidak ditemukan.")
        return
    # remove songs from user playlists
    for song in target.get("lagu", []):
        for u in store["users"]:
            u["playlist"] = [s for s in u.get("playlist", []) if not (s["judul"] == song["judul"] and s.get("artist_name","") == target["nama"])]
    store["artis"] = [x for x in store["artis"] if x["id"] != aid]
    save_store(store)
    print("✅ Artis dihapus.")

def admin_top_artist():
    store = load_store()
    if not store["artis"]:
        print("Data kosong.")
        return
    top = max(store["artis"], key=lambda x: len(x.get("lagu", [])))
    print(f"👑 Top Artist: {top['nama']} ({len(top.get('lagu', []))} lagu)")

def view_trending():
    store = load_store()
    semua = []
    for a in store["artis"]:
        for l in a.get("lagu", []):
            semua.append((a, l))
    if not semua:
        print("Belum ada lagu.")
        return
    top = max(semua, key=lambda x: x[1].get("play_count", 0))
    a, l = top
    print("\n📈 TRENDING SONG")
    print(f"🔥 {l['judul']} oleh {a['nama']}")
    print(f"Total plays: {l.get('play_count',0)}")

def main():
    # ensure data file exists
    _ = load_store()
    while True:
        print_main_menu()
        pilihan = input("Pilihan: ").strip()
        if pilihan == "1":
            admin_add_artis()
        elif pilihan == "2":
            admin_add_lagu()
        elif pilihan == "3":
            admin_view_all_music()
        elif pilihan == "4":
            admin_delete_artis()
        elif pilihan == "5":
            admin_top_artist()
        elif pilihan == "6":
            register_user()
        elif pilihan == "7":
            user = login_user()
            if user:
                user_dashboard(user)
        elif pilihan == "8":
            view_trending()
        elif pilihan == "0":
            print("Selesai. Bye!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
