# ADMIN/Admin.py
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data_store.json")
DATA_FILE = os.path.abspath(DATA_FILE)

# struktur default
DEFAULT_STORE = {
    "artis": [],   # tiap artis: {"id": int, "nama": str, "genre": str, "is_verified": bool, "lagu": [ {judul,tahun,durasi,play_count,artist_name} ]}
    "users": []    # tiap user: {"id": int, "username": str, "password": str, "nama_playlist": str, "playlist": [ {judul,...} ] }
}

def _ensure_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_STORE, f, indent=2)

def load_store():
    _ensure_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_store(store):
    _ensure_file()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(store, f, indent=2, ensure_ascii=False)

# convenience getters
def get_artis_list():
    store = load_store()
    return store["artis"]

def get_user_list():
    store = load_store()
    return store["users"]

def set_artis_list(artis_list):
    store = load_store()
    store["artis"] = artis_list
    save_store(store)

def set_user_list(user_list):
    store = load_store()
    store["users"] = user_list
    save_store(store)
