import os 
import time 
import sys


def save(user,monster,monster_shop,monster_inventory,item_shop,item_inventory):
    #menyimpan semua data ke csv
    nama_folder=input("Masukkan nama folder:") #fungsi meminta input nama folder
    path=os.path.join("..","data",nama_folder)
    if not os.path.exists(path):
        print(f"membuat folder data {nama_folder}")
    animate_saving(nama_folder)
    if not os.path.exists(path): # jika nama folder belum ada, maka buat folder baru
        os.mkdir(path)
    makecsvfile(nama_folder,user,"user.csv") #simpan semua data dalam bentuk csv ke folder tersebut
    makecsvfile(nama_folder,monster,"monster.csv")
    makecsvfile(nama_folder,monster_shop,"monster_shop.csv")
    makecsvfile(nama_folder,monster_inventory,"monster_inventory.csv")
    makecsvfile(nama_folder,item_shop,"item_shop.csv")
    makecsvfile(nama_folder,item_inventory,"item_inventory.csv")


    
def dicttocsv(dict): #fungsi yang mengubah dictionary ke csv
    dict_csv=[i for i in list(dict.keys())] #isi list awal dengan keys dari dictionary
    #list yang menyimpan seluruh komponnen (keys dan values) dari dictionary

    for i in range(int(len(list(dict[dict_csv[0]])))):
        for j in list(dict.keys()):
            dict_csv.append(dict[j][i]) #isi list dengan values dari dictionary secara bergantian berdasarkan keys
    field='' #inisiasi string kosong
    fields=[] #inisiasi array kosong
    if int(len(list(dict.keys())))==5: #mengubah list biasa menjadi list berbentuk seperti struktur data csv
        for i in range (0,len(dict_csv),5): #perulangan dengan kelipatan lima dari 0 sampai jumlah seluruh elemen list
            for j in range(i,i+5): #perulangan sebanyak lima kali 
                field+=dict_csv[j] #tambahkan setiap elemen list ke variabel string
                field+=';' #tambahkan ';' setiap akhir elemen untuk digunakan pada fungsi makecsvfile
            field+='\n' #tulis'\n' setiap akhir kelipatan lima untuk digunakan pada fungsi makecsvfile
            fields.append(field) #tambahkan nilai pada variabel field ke array fields
            field=''
    else: #perintah yang dilakukan untuk data yang keys nya 3 (selain user dan monster)
        for i in range (0,len(dict_csv),3):
            for j in range(i,i+3):
                field+=dict_csv[j]
                field+=';'
            field=field[:-1]+'\n'
            fields.append(field)
            field=''
    return fields            


def makecsvfile(nama_folder,dictionary,nama_file): #fungsi yang menulis csv pada suatu folder
    folder_path= os.path.join("..","data",nama_folder) 
    if (os.path.exists(folder_path)): #mengecek apakah folder ada
        csv=dicttocsv(dictionary) #variabel untuk menyimpan list berbentuk seperti struktur data csv
        with open(os.path.join("..","data",nama_folder,nama_file),'w') as f: #membuka file csv yang ingin ditulis 
            field='' #program akan menulis csv berdasarkan baris yang sama terlebih dahulu baru dilanjutkan baris selanjutnya 
            for i in csv:
                for j in i:
                    if j==';': #jika bertemu ';' maka penulisan akan dilanjutkan di kolom selanjutnya
                        f.write(field) #tulis keseluruhan string yang tersimpan pada variabel field pada baris csv
                        f.write(';') #perintah agar penulisan dilanjutkan ke kolom selanjutnya
                        field='' # kembalikan variabel field ke string kosong untuk menyimpan data selanjutnya
                    elif j=='\n': #jika bertemu '\n' maka penulisan dilanjutkan pada baris selanjutnya
                        f.write(field) #tulis keseluruhan string yang tersimpan pada variabel field pada baris csv
                        f.write('\n') #perintah agar penulisan dilanjutkan ke baris selanjutnya
                        field='' # kembalikan variabel field ke string kosong untuk menyimpan data selanjutnya
                    else:
                        field+=j #tambahkan setiap huruf pada setiap elemen list hingga membentuk suatu kesatuan nilai string
            
def animate_saving(a): #fungsi untuk menampilkan animasi saving
    text = "Saving"
    max_dots = 5
    iterations = 2
    for _ in range(iterations):
        for i in range(max_dots + 1):
            sys.stdout.write("\r" + text + "." * i)
            sys.stdout.flush()
            time.sleep(0.5)
        
        sys.stdout.write("\r" + text + " " * max_dots)
        sys.stdout.flush()
        time.sleep(0.5)

    print(f"\nBerhasil menyimpan data di folder {a}")

print()




                    

            
                            

                    





        
            



            

