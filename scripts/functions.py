#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Kütüphaneler #
import os,shutil as sh
import sqlite3 as sql
from tkinter import filedialog as fd
import webbrowser as web

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Global değişkenler #
vt=sql.connect("C:/Users/AHMET/Desktop/PythonProje/scripts/Db/user_db.sqlite")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Fonksiyonlar #
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
        im.execute(f"Insert Into Users values ({id},'{ad}','{soyad}','{tel}','{posta}',{did},'{pw}')")
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
    imgpath=fd.askopenfilenames(filetypes=files,defaultextension=files)
    for pth in imgpath:
         sh.move(pth,pathnew)
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
     sh.rmtree(pth)
       
def calistir(self):
    os.system("python Face_Detect.py")
    
def socialmedia(secim):
    if secim == 1:
        web.open_new("www.facebook.com")
    elif secim == 2: 
        web.open_new("www.instagram.com")
    elif secim == 3:
        web.open_new("www.twitter.com")
    else:
        print("hata ",secim)

def kUpdate(no,ad,soyad,tel,posta,did,dad,pw):
    im=vt.cursor()
    im.execute("Update Users SET U_ad='"+ad+"', U_soyad='"+soyad+"', U_telefon='"+tel+"', U_eposta='"+posta+"', D_ID="+did+", P_pw='"+pw+"' WHERE U_Id="+no)
    vt.commit()
    print(no," İd'li Kullanıcı Düzenlendi")
    return 1

def kliste():
        cur1 = vt.cursor()
        cur1.execute("SELECT U_Id,U_ad,U_soyad,U_telefon,U_eposta,D_ID,P_pw FROM Users")
        rows = cur1.fetchall() 
        return rows

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # END #