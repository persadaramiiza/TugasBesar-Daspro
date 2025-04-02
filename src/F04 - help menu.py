def help_before_login():
    print("=========== HELP ===========")
    print("Login belum dilakukan,silahkan logi terlebih dahulu.")
    print("1. Login: Masuk ke dalam akun yang sudah terdaftar")
    print("2. Register: Membuat akun baru")

    print("\nFootnote:")
    print("Silahkan masukan fungsi yang terdaftar dalam menggunakan aplikasi")
    print("Pastikan input yang dimasukkan valid")

        
def help_admin():
    print("=========== HELP ===========")
    print("Selamat datang, Admin. Berikut adalah hal- hal yang dapat kamu lakukan:")
    print("1. Logout: Keluar dari akun yang sedang digunakan")
    print("2. Shop Management: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
    print("3. Monster Management: Melakukan manajemen Monster")
    print("4. Save: Menyimpan progress Anda")
    print("5. Exit: Keluar dari game")

    print("\nFootnote:")
    print("Silahkan masukan fungsi yang terdaftar dalam menggunakan aplikasi")
    print("Pastikan input yang dimasukkan valid")
        
def help_agent(username: str):
    print("=========== HELP ===========")
    print(f"Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
    print("1.  Logout: Keluar dari akun yang sedang digunakan")
    print("2.  Inventory: Melihat owca-dex yang dimiliki oleh Agent")
    print("3.  Shop: Membeli potion atau monster")
    print("4.  Battle: Bertarung melawan monster!")
    print("5.  Arena: Latih dan tingkatkan kemampuan agen dan para monstermu!")
    print("6.  Laboratory: Upgrade monster yang kamu miliki")
    print("7.  Jackpot: Uji keberuntunganmu di sini!")
    print("8.  Legenda: Melihat peta kota Denville")
    print("9.  Save: Menyimpan progress Anda")
    print("10. Exit: Keluar dari game")

    print("\nFootnote:")
    print("Silahkan masukan fungsi yang terdaftar dalam menggunakan aplikasi")
    print("Pastikan input yang dimasukkan valid")
def menu():
    print("""
        ====================== KOTA MONSTERTOPIA  ========================
      || ----------------------------------------------------------- ||
      ||              Selamat datang di kota MonsterTopia            ||
      ||                                                             ||
      ||    ~~ mulai petualangan dan kalahkan musuh musuh       ~~   ||
      ||                                                             ||
        =============================================================
          
                    (Ketik HELP untuk mendapat bantuan) 
          

""")