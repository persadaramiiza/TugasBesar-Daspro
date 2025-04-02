

from F15 import save


#fungsi untuk keluar dari program
def exit(user,monster,monster_shop,monster_inventory,item_shop,item_inventory):
    exit=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") #fungsi akan meminta input 
    while True: #perulangan diperlukan untuk mengecek apakah input dari pengguna valid
        if exit=="Y" or exit=="y": #pegguna ingin menyimpan file ditandai dengan string 'Y' atau 'y'
            save(user,monster,monster_inventory,monster_shop,item_inventory,item_shop) #jalankan fungsi save untuk menyimpan data
            print("Anda telah keluar dari permainan") #fungsi memberikan informasi
            break #hentikan perulangan karena semua langkah langkah telah dilakukan 
        elif exit=="N" or exit=="n": #pengguna ingin keluar tetapi tidak ingin menyimpan perubahan
            print("Data tidak disimpan") #fungsi memberikan informasi 
            print("Anda telah keluar dari permainan")
            break #hentikan perulangan karena semua langkah langkah telah dilakukan
        else: exit=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
            #perintah yang dilakukan ketika pengguna memasukan nilai yang tidak sesuai
