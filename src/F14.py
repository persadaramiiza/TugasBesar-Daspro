import argparse
import os
import sys 
import time


def animate():
#prosedure untuk menampilkan animasi loading pada terminal
    for i in range (11):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rSelesai!     ')
    print(" ")

def load (): #fungsi untuk memvalidasi apakah folder yang diberikan pengguna ada, dan mengopen file csv jika 
    #folder memang ada 
    parser=argparse.ArgumentParser(usage="")
    parser.add_argument("namafolder",nargs='?',help="Nama folder di dalam parent 'data' ")
    args=parser.parse_args()
    animate() #program menampilkan animasi loading 
    if args.namafolder is None: #nama folder tidak diberikan
        print("Tidak ada nama foder yang diberikan!")
        sys.exit()
    folder_path= os.path.join("..","data",args.namafolder)
    if (os.path.exists(folder_path)): #folder ada di directory
        #program selanjutnya membuka file csv yang ada pada folder dan mengubah ke dictionary
        with open (os.path.join("..","data",args.namafolder,"user.csv"),'r') as file :
            user=dictionary_csv("user.csv",args.namafolder)
        with open (os.path.join("..","data",args.namafolder,"monster.csv"),'r') as file :
            monster=dictionary_csv("monster.csv",args.namafolder)
        with open (os.path.join("..","data",args.namafolder,"monster_shop.csv"),'r') as file :
            monster_shop=dictionary_csv("monster_shop.csv",args.namafolder)
        with open (os.path.join("..","data",args.namafolder,"monster_inventory.csv"),'r') as file :
            monster_inventory=dictionary_csv("monster_inventory.csv",args.namafolder)
        with open (os.path.join("..","data",args.namafolder,"item_shop.csv"),'r') as file :
            item_shop=dictionary_csv("item_shop.csv",args.namafolder)
        with open (os.path.join("..","data",args.namafolder,"item_inventory.csv"),'r') as file :
            item_inventory=dictionary_csv("item_inventory.csv",args.namafolder)
        sambutan()
        return user,monster,monster_shop,monster_inventory,item_shop,item_inventory,True
        #fungsi memberikan keluaran berupa dictionary dari beberapa file csv yang telah diubah     
           
            

        
    else : #jika nama folder sudah diberikan tapi tidak ditemukan
        print (f"folder {args.namafolder} tidak ditemukan")
        return False




    



def fungsisplit(bariscsv):
     fields=[] #inisialisasi list kosong
     field='' #inisialisasi string kosong
     for baris in bariscsv: #loop melalui setiap baris pada csv
        for karakter in baris: #loop melalui setiap karakter pada baris 
            if karakter==';':  # Jika karakter adalah titik koma, tambahkan field saat ini ke dalam list fields
                fields.append(field) 
                field=''
            else:
                field+=karakter  # Tambahkan karakter ke dalam field saat ini
        if field.endswith('\n'):
            field=field[:-1]  # Jika field berakhir dengan newline, hilangkan newline tersebut
        fields.append(field)
        field=''
     return fields


def dictionary_csv(file_csv,nama_folder): #fungsi untuk mengubah csv ke dictionary
    csv=open(os.path.join("..","data",nama_folder,file_csv)) #buka file csv
    if file_csv =="user.csv" or file_csv=="monster.csv": 
        array_test=[i for i in csv]
        array_csv=fungsisplit(array_test)[5:] #ubah csv ke list dengan menghilangkan header
        header=fungsisplit(array_test)[:5] #simpan header dari csv tersebut
        data=[array_csv[i:i+5] for i in range (0,len(array_csv),5)] #memecah array_csv menjadi 5 bagian
        array_final={} #inisialisasi
        for i in header: #iterasi setiap elemen pada header
            # Membuat entri dalam dictionary array_final dengan nama kolom sebagai kunci
            array_final[i]=[ j[header.index(i)] for j in data]
    else: #perintah yang akan dilakukan jika file csv selain 'user.csv' dan 'monster.csv'
        array_test=[i for i in csv]
        array_csv=fungsisplit(array_test)[3:]
        header=fungsisplit(array_test)[:3]
        data=[array_csv[i:i+3] for i in range (0,len(array_csv),3)]
        array_final={}
        for i in header:
            array_final[i]=[j[header.index(i)] for j in data]

    return array_final

def sambutan():
    print("""
  _____        ______    _    
 / _ \ \      / / ___|  / \   
| | | \ \ /\ / / |     / _ \  
| |_| |\ V  V /| |___ / ___ \ 
 \___/  \_/\_/  \____/_/   \_\
          
  selamat datang di OWCA!!     
          
          """)
a,b,c,d,e,f,g=load()
print(a)                  
          


