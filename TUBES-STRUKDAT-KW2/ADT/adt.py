# ADT/adt.py

class Lagu:
    def __init__(self, judul, tahun, durasi):
        self.judul = judul
        self.tahun = int(tahun)
        self.durasi = int(durasi)
        self.play_count = 0
        self.artist_name = ""

    def to_dict(self):
        return {
            "judul": self.judul,
            "tahun": self.tahun,
            "durasi": self.durasi,
            "play_count": self.play_count,
            "artist_name": self.artist_name
        }

    @staticmethod
    def from_dict(d):
        l = Lagu(d["judul"], d["tahun"], d["durasi"])
        l.play_count = d.get("play_count", 0)
        l.artist_name = d.get("artist_name", "")
        return l

    def __repr__(self):
        m = self.durasi // 60
        s = self.durasi % 60
        return f"'{self.judul}' ({m}:{s:02d}) - {self.play_count} plays"

class Artis:
    def __init__(self, id_, nama, genre, is_verified=False, daftar_lagu=None):
        self.id = id_
        self.nama = nama
        self.genre = genre
        self.is_verified = is_verified
        self.daftar_lagu = daftar_lagu or []  # list of Lagu objects

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "genre": self.genre,
            "is_verified": self.is_verified,
            "lagu": [l.to_dict() for l in self.daftar_lagu]
        }

    @staticmethod
    def from_dict(d):
        lagu_objs = [Lagu.from_dict(ld) for ld in d.get("lagu", [])]
        a = Artis(d["id"], d["nama"], d["genre"], d.get("is_verified", False), lagu_objs)
        # set artist_name for songs
        for l in a.daftar_lagu:
            l.artist_name = a.nama
        return a

class User:
    def __init__(self, id_, username, password, nama_playlist, playlist=None):
        self.id = id_
        self.username = username
        self.password = password
        self.nama_playlist = nama_playlist
        self.playlist = playlist or []  # list of Lagu objects

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "nama_playlist": self.nama_playlist,
            "playlist": [l.to_dict() for l in self.playlist]
        }

    @staticmethod
    def from_dict(d):
        pl = [Lagu.from_dict(ld) for ld in d.get("playlist", [])]
        u = User(d["id"], d["username"], d["password"], d.get("nama_playlist", ""), pl)
        return u
