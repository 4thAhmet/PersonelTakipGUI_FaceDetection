import os,csv
import sqlite3 as sql
from tkinter import filedialog
import shutil
vt=sql.connect("C:/Users/AHMET/Desktop/PythonProje/scripts/Db/user_db.sqlite")
# Kayıtlı kullanıcı sayısını bulan fonksiyon#
"""def KullaniciSay():
        count=0
        csvpath="dataFace/dataBase.csv"
        if os.path.exists(csvpath):
            f=open(csvpath,mode='r')
        else:
            return -1
        with f as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if len(row) == 0:
                    continue
                count+=1
        f.close()
        return count"""


def KullaniciSay():
        count=0
        im=vt.cursor()
        im.execute("Select count(U_Id) as count from  Users")
        veri=im.fetchone()
        return veri[0]


def Kliste():
    klistid=[]
    klistname=[]
    klistid.clear()
    klistname.clear()
    im=vt.cursor()
    im.execute("Select * from Users")
    veri=im.fetchall()
    for data in veri:
        klistid.append(data[0])
        klistname.append(data[1])
    return klistid,klistname

def kSil(deleteid):
     im=vt.cursor()
     im.execute(f"Delete from Users where U_Id={deleteid}")
     vt.commit()
     Resimsil(deleteid)
     

def kEkle(id,ad,soyad,tel,posta,did,dad,pw): 
    im=vt.cursor()
    try:
        im.execute(f"Insert Into Users values ({id},'{ad}','{soyad}','{tel}','{posta}','{did}','{pw}')")
        vt.commit()
        print(id,"'li Kullanıcı eklendi!")
        return 1
    except sql.IntegrityError:
        print("Kullanıcı ID daaha önce kullanılmış!")
        return -1
     

def filedialog_show(uid):
    files=[('Resim Dosyaları','*.jpg')]
    os.makedirs(f"dataFace/{uid}",mode=0o755, exist_ok=True)
    pathnew =f'dataFace/{uid}'
    imgpath=filedialog.askopenfilenames(filetypes=files,defaultextension=files)
    for pth in imgpath:
         shutil.move(pth,pathnew)
         print(pth,' tasındı.')
    imagePaths = [os.path.join(pathnew,f) for f in os.listdir(pathnew)]
    say=0
    for p in imagePaths:
        pfoto=p.split('.')
        if(say!=pfoto):
            os.rename(p,f'{pathnew}/{say}.jpg')
        say+=1
    say=0
    print("Fotoğraflar Yüklendi! Eğitimi Tekrar Başlatın!")

def Resimsil(uid):
     pth='dataFace/'+str(uid)
     shutil.rmtree(pth)
     


#Kayıtlı kullanıcıların id ve numarasını dizi olarak geri döndüren fonksiyon#
"""def Kliste():
        klistid=[]
        klistname=[]
        csvpath="dataFace/dataBase.csv"
        if os.path.exists(csvpath):
            f=open(csvpath,mode='r')
        else:
            return klistid,klistname
        with f as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if len(row) == 0:
                    continue
                else:
                    klistid.append(row[0])
                    klistname.append(row[1])
        f.close()
        return klistid,klistname"""
"""def kSil(deleteid,idlist,name):
    indexCount =0
    csvpath="dataFace/dataBase.csv"
    #if os.path.exists(csvpath):
    f=open(csvpath,mode='w')
    #else:
         #print("Silme Hatası")
    for d in idlist:
        if d==deleteid:
            idlist.remove(d)
            name.pop(indexCount)
        indexCount+=1
    indexCount=0
    d=""
    print(idlist)
    print(name)
    with f as csv_file:
        c=0
        writer1=csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONE)
        for idyaz in idlist:
            writer1.writerow([idyaz,f'ID: {idyaz}'])
    idlist.clear()
    name.clear()
    f.close()
    return idlist,name"""
    
                         
                        
     
def calistir(self):
    os.system("python Face_Detect.py")
    