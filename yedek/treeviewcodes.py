import customtkinter
from tkinter import ttk
import tkinter as tk
import os
import cv2
from PIL import Image
from scripts import functions

#eklenecek
from datetime import datetime, timezone


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_default_color_theme('scripts/theme.json')
        self.title("Personel Takip Uygulaması")
        self.geometry("1050x720")
        self.iconbitmap(default="images/logo1.ico")
        self.treeView()
        self.tree1.bind('<Double-1>', self.tik)
        self.tree1.bind("<ButtonRelease-1>",self.dene)
    def dene(self,it):
        print("+ ya cift tiklama")
    def treeView(self):
        style=ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        self.tree1=ttk.Treeview(self)
        self.tree1["columns"]=("one","two","three","four","five","six")
        self.tree1.heading("#0",text=" ",anchor=tk.W)
        self.tree1.column("#0",width=100)
        self.tree1.heading("one", text="Ad",anchor=tk.W)
        self.tree1.heading("two", text="Soyad",anchor=tk.W)
        self.tree1.heading("three", text="telefon",anchor=tk.W)
        self.tree1.heading("four", text="E-Posta",anchor=tk.W)
        self.tree1.heading("five", text="Depertman",anchor=tk.W)
        rows=functions.kliste()
        kBilgiler=[]
        altbilgiId=[]
        ind=[]
        i=0   
        for row in rows:
            path="dataFace/"+str(row[0])
            kBilgiler.append(row)
            altbilgiId.append(row[0])
            ind.append(i)
            ind[i]=self.tree1.insert("",3,text=row[0],values=(row[1],row[2],row[3],row[4],row[5])) 
            #print("Alt Bilgi :",altbilgiId,"\n")
            #print("KBilgiler :",kBilgiler,"\n")
            #print("ind :",ind,"\n")
            list=[os.path.join(path,f) for f in os.listdir(path)]
            for p in list:
                al=p.split("\\")[1]
                print(p.split("\\")[1],"\n")
                dosya=os.stat(p)
                print("Oluşturma Tarihi: ",dosya.st_ctime)
                print(" Boyutu:",dosya.st_size)
                print(" uzantı ",al.split('.')[1])
                tip=al.split('.')[1]+" File"
                b=(dosya.st_size/1024)
                boyut=str(float("{:.2f}".format(b)))+"Kb"
                otarih=datetime.fromtimestamp(dosya.st_ctime, tz=timezone.utc).strftime('%Y-%m-%d %H:%M')
                self.tree1.insert(ind[i],"end",text=al,values=(otarih,tip,boyut),tags="child")
        i+=1
        self.tree1.tag_configure('child',background='#DFDFDF')
        self.tree1.grid(row=1,column=0,padx=(30,30),pady=0,sticky="n")
        

    def tik(self,a):
        item=self.tree1.selection()
        iid=self.tree1.selection()[0]
        parentid=self.tree1.parent(iid)
        if parentid:
            print("parent id: ",parentid)
            print(self.tree1.item(iid)['text'])
            path="dataFace/"+str(self.tree1.item(parentid)['text'])+"/"+str(self.tree1.item(iid)['text'])
            print(path)
            res=cv2.imread(path,1)
            while(True):
                cv2.imshow('image',res)
                k=cv2.waitKey(10 & 0xff)
                if k==27 or k==ord('q'):
                    break
            cv2.destroyAllWindows() 
        else:
            print("Düzenleme Penceresi Açılacak")
            


if __name__ == "__main__":
    app=App()
    print("Personel Takip Programı Başlatıldı.\nresizable Disabled.")
    app.resizable(False,False) 
    app.eval('tk::PlaceWindow . center')
    app.mainloop()