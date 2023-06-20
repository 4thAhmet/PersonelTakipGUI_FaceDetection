#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Kütüphaneler #
import os,shutil as sh
import sqlite3 as sql
from tkinter import filedialog as fd
from CTkMessagebox import CTkMessagebox


import webbrowser as web
import cv2
import datetime

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Global değişkenler #
vt=sql.connect("scripts/Db/user_db.sqlite")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Fonksiyonlar #
def KullaniciSay():
        im=vt.cursor()
        im.execute("Select count(U_Id) as count from  Users")
        veri=im.fetchone()
        return veri[0]

def kIdFinder():
    im=vt.cursor()
    im.execute("Select MAX(U_Id) from Users")
    kullaniciID=im.fetchone()
    return kullaniciID[0]

def messageBox(title,message,icon,option):
    if len(option) == 1:
        msg=CTkMessagebox(title=title,message=message,icon=icon,option_1=option[0]) 
    elif len(option)==2:
        msg=CTkMessagebox(title=title,message=message,icon=icon,option_1=option[0],option_2=option[1])
    elif len(option)==3:
        msg=CTkMessagebox(title=title,message=message,icon=icon,option_1=option[0],option_2=option[1],option_3=option[2])
    else:
        msg=CTkMessagebox(title="ERROR",message="Hatalı Giriş Yapıldı!",icon="warning",option_1="OK")
    res=msg.get()
    return res

def kEkle(ad,soyad,tel,posta,did,pw): 
    im=vt.cursor()
    im1=vt.cursor()
    try:
        im.execute(f"Insert Into Users (U_ad,U_soyad,U_telefon,U_eposta,D_ID,P_pw) values ('{ad}','{soyad}','{tel}','{posta}',{did},'{pw}')")
        vt.commit()
        kId=kIdFinder()
        print(kId,"'li Kullanıcı eklendi!")
        msg=str(ad)+" "+str(soyad)+" Kullanıcısı sisteme eklendi"
        bilgiEkle(msg,kId)
        im1.execute(f"INSERT INTO PersonelDurum (K_no,Durum) values ({kId},{0})")
        vt.commit()
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

def kUpdate(no,ad,soyad,tel,posta,did,pw):
    im=vt.cursor()
    im.execute("Update Users SET U_ad='"+ad+"', U_soyad='"+soyad+"', U_telefon='"+tel+"', U_eposta='"+posta+"', D_ID="+did+", P_pw='"+pw+"' WHERE U_Id="+no)
    vt.commit()
    msg=str(no)+" ID numaralı kullanıcı bilgileri güncellendi"
    bilgiEkle(msg,no)
    print(no," İd'li Kullanıcı Düzenlendi")
    return 1

def kliste():
        cur2=vt.cursor()
        cur2.execute("Select * FROM DEPARTMAN")
        drows=cur2.fetchall()
        rows1=[]
        cur1 = vt.cursor()
        cur1.execute("SELECT U_Id,U_ad,U_soyad,U_telefon,U_eposta,D_ID,P_pw FROM Users")
        rows = cur1.fetchall()
        for row in rows:
            dizi=[row[0],row[1],row[2],row[3],row[4],str(row[5]),row[6]]
            did=row[5]
            for drow in drows:
                if int(did) in drow:
                    dizi[5]=drow[1]
                    break
                else:
                    dizi[5]="Bilinmeyen Departman"
            rows1.append(dizi)
        return rows1

def kDel(deleteid):
     cur=vt.cursor()
     cur.execute(f"Delete from Users where U_Id={deleteid}")
     vt.commit()
     print(f"Kullanıcı silindi! ID:{deleteid}")
     msg=str(deleteid)+" ID numaralı kullanıcı silindi."
     bilgiEkle(msg,deleteid)
     Resimsil(deleteid)

def Pliste():
    cur2=vt.cursor()
    cur2.execute("Select * FROM Users")
    drows=cur2.fetchall()
    rows1=[]
    im=vt.cursor()
    im.execute("SELECT * FROM SonIslemler")
    rows=im.fetchall()
    for row in rows:
        dizi=[row[0],row[1],row[2],row[3],str(row[4])]
        userid=row[4]
        for drow in drows:
            if int(userid) in drow:
                dizi[4]=drow[1]+" "+drow[2]
                break
            else:
                dizi[4]="Bilinmeyen Kullanıcı"
        rows1.append(dizi)
    return rows1

def bilgiEkle(islem,uid):
    an=datetime.datetime.now()
    tarih=datetime.datetime.strftime(an, '%d,%B,%Y')
    saat=datetime.date.strftime(an,'%X')
    cur=vt.cursor()
    cur.execute(f"insert into SonIslemler (islem,saat,tarih,userid) values ('{islem}','{saat}','{tarih}',{uid})")
    vt.commit()
    print("Bilgi Eklendi")

def bilgisil(id):
    try:
        cur=vt.cursor()
        cur.execute(f"delete from SonIslemler where id={id}")
        vt.commit()
        print(f"{id} numaralı işlem silindi")
        return 1
    except:
        return -1

def openPicture(path,winname):
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, 1000, 500)   # Move it to (x,y)
    res=cv2.imread(path,1)
    ress=cv2.resize(res, (400, 400))
    cv2.imshow(winname,ress)

def departmanGetir():
    cur=vt.cursor()
    cur.execute("SELECT * FROM DEPARTMAN")
    rows=cur.fetchall()
    return rows

def PersonelDurum(id):
    cur=vt.cursor()
    cur.execute(f"SELECT max(id),K_no,Durum FROM PersonelDurum where K_no={id}")
    rows=cur.fetchone()
    print(rows)
    return rows

def PersonelDurumEkle(id,Durum):
    curDate=datetime.datetime.now()
    date=datetime.datetime.strftime(curDate,'%d,%B,%Y')
    time=datetime.date.strftime(curDate,'%X')
    cur=vt.cursor()
    cur.execute(f"INSERT INTO PersonelDurum (K_no,Durum,Tarih,Saat) values ({id},{Durum},'{date}','{time}')")
    vt.commit()
    print("Eklendi")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # END #