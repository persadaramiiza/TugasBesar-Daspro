# Buka file owca-dex.csv dalam mode baca
file = open("owca-dex.csv", "r")

# Baca semua baris di file
lines = file.readlines()

# Tutup file setelah membaca
file.close()

# Dictionary untuk menyimpan data monster
monsters = {}

# Proses setiap baris kecuali header
for line in lines[1:]:
    # Menghilangkan whitespace dan baris baru
    line = line.strip()

    # Inisialisasi variabel sementara untuk menyimpan bagian data
    current_data = ''
    parts = []
    comma = False

    # Manual parsing tiap karakter untuk handle koma sebagai pemisah
    for char in line:
        if char == ',' and not comma:
            parts.append(current_data)
            current_data = ''
        else:
            if char != ',':
                current_data += char
    parts.append(current_data)  # Tambahkan bagian terakhir

    # Mengambil data dari bagian yang telah dipisahkan
    monster_name = parts[0]
    monster_type = parts[2]
    atk_power = int(parts[3])
    def_power = int(parts[4])
    hp = int(parts[5])
    level = int(parts[6])

    # Simpan data ke dictionary
    monsters[monster_name] = {
        'Monster Type' : monster_type,
        'ATK Power': atk_power,
        'DEF Power': def_power,
        'HP': hp,
        'Level': level
    }

# Cetak data untuk verifikasi
for monster, stats in monsters.items():
    print(f"Monster: {monster}, Stats: {stats}")