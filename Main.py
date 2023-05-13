""""
*****************************************************
*                   Ahmet Akkeçi                    *
*              Personel Takip Uygulaması            *
*                                                   *
*****************************************************
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Kütüphaneler #
import customtkinter
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image
from datetime import datetime, timezone
from CTkMessagebox import CTkMessagebox

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # fonksiyon import #
from scripts import Face_detect
from scripts import functions
from scripts import trainModel
from scripts import loadimages
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Window Başlangıç #
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.facedetectClass=Face_detect.FaceDetect()
        self.modelTrain=trainModel.TrainModel()
        customtkinter.set_default_color_theme('scripts/theme.json')
        self.title("Personel Takip Uygulaması")
        self.geometry("1155x792")
        self.iconbitmap(default="images/logo.ico")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Load Images#
        self.logo_image,self.large_test_image,self.image_icon_image,self.home_image, self.user_list_image, self.add_user_image, self.user_detect_image,self.refresh_image,self.adduser_CANCEL_image,self.info_image,self.userDelete_image=loadimages.loadimages()
        self.recentOnes=loadimages.loadimages2()   
        self.facelogo,self.instalogo,self.twlogo=loadimages.SocailMediaLogo()                         
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Navigation Bar Frame#
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=2)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Personel Takip", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=30, pady=20)
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=" Anasayfa",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", font=customtkinter.CTkFont(size=20),command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=" Kullanıcı Listesi",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.user_list_image, anchor="w",font=customtkinter.CTkFont(size=20), command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Son Hareketler",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.recentOnes, anchor="w",font=customtkinter.CTkFont(size=20), command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.theme_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Theme:", anchor="w",font=customtkinter.CTkFont(size=14))
        self.theme_label.grid(row=5, column=0, padx=30, pady=(0, 0),sticky="sw")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], width=200, font=customtkinter.CTkFont(size=14),
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=30, pady=0, sticky="sw")


        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Scaling:", anchor="w", font=customtkinter.CTkFont(size=14))
        self.scaling_label.grid(row=7, column=0, padx=30, pady=(0, 0),sticky="sw")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["90%", "100%", "110%", "120%","130%"], width=200,font=customtkinter.CTkFont(size=14),
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.set('100%')
        self.scaling_optionemenu.grid(row=8, column=0, padx=30, pady=(0, 10),sticky="sw")
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #First Frame#
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(8,weight=1)
        self.kSay=functions.KullaniciSay()
        self.labeltext=" "
        if self.kSay==-1:
            self.labeltext="Not Found Database"
        self.labeltext="  Sisteme Kayıtlı Kullanıcı Sayısı: "+str(self.kSay)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame,text_color="white", text="PERSONEL TAKİP SİSTEMİ ",font=customtkinter.CTkFont(size=30, weight="bold"), image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=0)
        self.label1=customtkinter.CTkLabel(self.home_frame,text=self.labeltext,font=customtkinter.CTkFont(size=25),text_color="#006BBB",image=self.info_image,compound="left")
        self.label1.grid_configure(row=2,column=0,padx=20,pady=(30,20))
        self.hakkindatxt="Personel Takip Sistemi ile personellerin işe başlama ve bitiş   saatlerini hızlı ve eksiksiz kayıt altına alabilirsiniz. \n "
        self.hakkindatxt+="Hata Oranı Düşük bir şekilde Yüz tanıma sistemi ile kolay ve hızlı işlem sunar. \n"
        self.hakkindatxt+="\n ~Ahmet Akkeçi~\n "
        self.widget=customtkinter.CTkFrame(self.home_frame,corner_radius=0)
        self.widget.grid_columnconfigure(3,weight=1)
        self.widget.grid_rowconfigure(0,weight=1)
        self.widget.grid(row=8,column=0,padx=10,pady=(20,20),sticky="s")
        self.textbox = customtkinter.CTkTextbox(self.home_frame, font=customtkinter.CTkFont(size=25))
        self.textbox.insert("0.0", self.hakkindatxt)
        self.textbox.configure(state="disabled") 
        self.textbox.grid(row=1, column=0, padx=(47, 47), pady=(0, 0), sticky="nsew")
        self.facelogobutton=customtkinter.CTkButton(self.widget,text="Facebook",image=self.facelogo,
                                                corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=20, weight="bold"),
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda: functions.socialmedia(1))
        self.instabutton=customtkinter.CTkButton(self.widget,text="İnstagram",image=self.instalogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=20, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda:functions.socialmedia(2))
        self.twlogobutton=customtkinter.CTkButton(self.widget,text="Twitter",image=self.twlogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=20, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda:functions.socialmedia(3))
        self.facelogobutton.grid(row=0,column=0,padx=5,pady=0)
        self.instabutton.grid(row=0,column=1,padx=5,pady=0)
        self.twlogobutton.grid(row=0,column=2,padx=5,pady=0)
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Second Frame#
        # create second frame  
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_rowconfigure(2, weight=1)
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame,text_color="white", text="Kullanıcı Listesi",font=customtkinter.CTkFont(size=30, weight="bold"), image=self.large_test_image)
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=0,sticky="n")

        #self.viewer()
        self.treeView()
        self.seconf_frame_buttonframe=customtkinter.CTkFrame(self.second_frame,corner_radius=0,fg_color="transparent")
        self.seconf_frame_buttonframe.grid(row=2,column=0,padx=(0,0),pady=(20,0),sticky="n")
        self.seconf_frame_buttonframe.grid_rowconfigure(0, weight=1)
        self.seconf_frame_buttonframe.grid_columnconfigure(3,weight=1)
        self.button_userDetect = customtkinter.CTkButton(self.seconf_frame_buttonframe, corner_radius=0, height=70, border_spacing=10, text="Kullanıcı Tanı",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.user_detect_image, anchor="w",font=customtkinter.CTkFont(size=18),command=self.DetectedFace)
        self.button_userDetect.grid(row=2, column=0, padx=(15,15))
        self.button_useredit =customtkinter.CTkButton(self.seconf_frame_buttonframe,corner_radius=0,height=70, border_spacing=10, text="Kullanıcı Ekle",
                                                        fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                                        image=self.add_user_image, anchor="w",font=customtkinter.CTkFont(size=18), command=self.frame3)
        self.button_useredit.grid(row=2, column=1,padx=(15,15))
        self.button_refresh =customtkinter.CTkButton(self.seconf_frame_buttonframe,corner_radius=0,height=70, border_spacing=10, text="Listeyi Güncelle",
                                                        fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                                        image=self.refresh_image, anchor="w",font=customtkinter.CTkFont(size=18),command=self.treeView)
        self.button_refresh.grid(row=2, column=2,padx=(15,15))
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                #Third Frame#
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.third_frame.grid_rowconfigure(4,weight=1)
        self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame,text_color="white", text="Yapılan İşlemler",font=customtkinter.CTkFont(size=30, weight="bold"), image=self.large_test_image)
        self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=0,sticky="n")
        self.LastProcessView()
        self.buttonframe=customtkinter.CTkFrame(self.third_frame,corner_radius=0,fg_color="transparent")
        self.buttonframe.grid_columnconfigure(3,weight=1)
        self.buttonframe.grid(row=2,column=0,padx=0,pady=15)
        self.button_refresh =customtkinter.CTkButton(self.buttonframe,corner_radius=0,height=70, border_spacing=10, text="Listeyi Güncelle",
                                                        fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                                        image=self.refresh_image, anchor="w",font=customtkinter.CTkFont(size=18),command=self.LastProcessView)
        self.button_refresh.grid(row=0, column=1,padx=(15,15),pady=0)
        self.buttonDelete=customtkinter.CTkButton(self.buttonframe,corner_radius=0,height=70, border_spacing=10, text="İşlemi Sil",
                                                  fg_color="transparent",text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                                  image=self.userDelete_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.processDelete)
        self.buttonDelete.grid(row=0,column=0,padx=(15,15),pady=0)
        



#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                #Fourth Frame#
        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self,corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=1)
        self.entries=[]
        self.fourth_frame_large_image_label = customtkinter.CTkLabel(self.fourth_frame,text_color="white", text="Yeni Personel Ekle",font=customtkinter.CTkFont(size=30, weight="bold"), image=self.large_test_image)
        self.fourth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10,sticky="n")
        self.txtframe_fourthframe=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")
        self.txtframe_fourthframe.grid_rowconfigure(7,weight=1)
        self.txtframe_fourthframe.grid_columnconfigure(2, weight=1)
        self.txtframe_fourthframe.grid(row=1,column=0,padx=0,pady=0,sticky=' ')
        self.labeltext=[" ","Personel Adı","Personel Soyad","Personel Telefon","Personel Eposta","Departman ID","Departman Name","Personel Sifre"]
        kid=functions.kIdFinder()+1
        for i in range(1,8):      
            self.navigation_label = customtkinter.CTkLabel(self.txtframe_fourthframe, text=self.labeltext[i],
                                                             font=customtkinter.CTkFont(size=18, weight="bold"))
            self.entries.append(customtkinter.CTkTextbox(self.txtframe_fourthframe,height=0.05, font=customtkinter.CTkFont(size=18)))
            self.navigation_label.grid(row=i, column=0, padx=(0,15), pady=10)  
            self.entries[-1].grid(row=i, column=1, padx=0, pady=10, sticky="ne")
        self.buttons_frame=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame.grid_columnconfigure(2,weight=1)
        self.buttons_frame.grid_rowconfigure(0,weight=1)
        self.buttons_frame.grid(row=2,column=0, padx=(10,10), pady=0)
        self.buttonOK=customtkinter.CTkButton(self.buttons_frame,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Ekle",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.add_user_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.adduser_OK)
        self.buttonOK.grid(row=0, column=0, padx=25, pady=10)    
        self.buttonCancel=customtkinter.CTkButton(self.buttons_frame,corner_radius=0,height=40, border_spacing=5, text="İptal Et",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_CANCEL_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.adduser_CANCEL)
        self.buttonCancel.grid(row=0, column=1, padx=25, pady=10)  
        self.entries[4].bind('<KeyPress>',self.onlyNumbers)
        self.entries[2].bind('<KeyPress>',self.onlyNumbers)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                #five Frame#
        # create five frame
        self.five_frame = customtkinter.CTkFrame(self,corner_radius=0, fg_color="transparent")
        self.five_frame.grid_columnconfigure(0, weight=1)
        self.five_frame.grid_rowconfigure(2,weight=1)
        self.entries1=[]
        self.five_frame_large_image_label = customtkinter.CTkLabel(self.five_frame,text_color="white", text="Personel Düzenle",font=customtkinter.CTkFont(size=30, weight="bold"), image=self.large_test_image)
        self.five_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10,sticky="n")
        self.txtframe_fiveframe=customtkinter.CTkFrame(self.five_frame,corner_radius=0,fg_color="transparent")
        self.txtframe_fiveframe.grid_rowconfigure(7,weight=1)
        self.txtframe_fiveframe.grid_columnconfigure(2, weight=1)
        self.txtframe_fiveframe.grid(row=1,column=0,padx=0,pady=0,sticky=' ')
        self.labeltext1=[" ","Personel ID","Personel Adı","Personel Soyad","Personel Telefon","Personel Eposta","Departman ID","Departman Name","Personel Sifre"]
        for i in range(1,9):
            self.navigation_label_fiveframe=customtkinter.CTkLabel(self.txtframe_fiveframe, text=self.labeltext1[i],
                                                             font=customtkinter.CTkFont(size=18, weight="bold"))
            self.entries1.append(customtkinter.CTkTextbox(self.txtframe_fiveframe,height=0.01, font=customtkinter.CTkFont(size=18)))
            self.navigation_label_fiveframe.grid(row=i, column=0, padx=(0,15), pady=10)  
            self.entries1[-1].grid(row=i, column=1, padx=0, pady=10, sticky="ne")
        self.buttons_frame_fiveframe=customtkinter.CTkFrame(self.five_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame_fiveframe.grid_columnconfigure(2,weight=1)
        self.buttons_frame_fiveframe.grid_rowconfigure(0,weight=1)
        self.buttons_frame_fiveframe.grid(row=2,column=0, padx=(10,10), pady=0)

        self.buttonOK1=customtkinter.CTkButton(self.buttons_frame_fiveframe,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Düzenle",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.add_user_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.userupdate)
        self.buttonOK1.grid(row=0, column=0, padx=25, pady=10)  
        self.buttonCancel1=customtkinter.CTkButton(self.buttons_frame_fiveframe,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Sil",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.userDelete_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.userDelete)
        self.buttonCancel1.grid(row=0, column=1, padx=25, pady=10)  
        self.entries1[3].bind('<KeyPress>',self.onlyNumbers)
        self.entries1[5].bind('<KeyPress>',self.onlyNumbers)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                #Home Frame#
        # select default frame
        self.select_frame_by_name("home")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Events Frame#
    def frame3(self):
        self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        self.frame_2_button.configure(text='Kullanıcı Ekle')
    
    def frame4(self):
        self.five_frame.grid(row=0,column=1,sticky="nsew")
        self.frame_2_button.configure(text='Kullanıcı Düzenle')
    
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        self.fourth_frame.grid_forget()
        self.five_frame.grid_forget()
        self.frame_2_button.configure(text="Kullanıcı Listesi")
        self.adduser_CANCEL()
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")
        self.kSay=functions.KullaniciSay()
        self.labeltext="Sisteme Kayıtlı Kullanıcı Sayısı: "+str(self.kSay)
        self.label1.configure(text=self.labeltext)

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def startFrame(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        yeniH=480*new_scaling_float
        yeniW=750*new_scaling_float
        yeniGeometry=str(int(yeniW))+"x"+str(int(yeniH))
        print("Resize new geometry: ",yeniGeometry)
        self.percent=int(new_scaling.replace("%",""))
        self.wm_geometry(yeniGeometry)
        
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        yeniH=720*new_scaling_float
        yeniW=1050*new_scaling_float
        yeniGeometry=str(int(yeniW))+"x"+str(int(yeniH))
        print("Resize new geometry: ",yeniGeometry)
        self.percent=int(new_scaling.replace("%",""))
        self.wm_geometry(yeniGeometry)
        
    def DetectedFace(self):
        ad,id=self.facedetectClass.main()
        if id==-1:
            print("Kimse Tanınmadı ! ")
            functions.messageBox("Kullanıcı tanıma","Kullanıcı Tanınamadı","warning",option=["Tamam"])
        else:
            print("id: ",ad," Ad: ",id)
            message=str(id)+" Numaralı Kullanıcı Tanındı. Ad: "+str(ad)
            functions.messageBox("Kullanıcı tanıma",message,"check",option=["Tamam"])
            msg=str(id)+" Numaralı "+str(ad)+" Kullanıcısı Giriş Yaptı"
            functions.bilgiEkle(msg,id)
            self.LastProcessView()
        self.facedetectClass.closeWindow()

    def adduser_OK(self):
        print("Kullanıcı ekleme kabul butonu")
        gettxt=[]
        for i in range(7):
            gettxt.append(self.entries[i].get("0.0","end-1c"))
        result=functions.kEkle(gettxt[0],gettxt[1],gettxt[2],gettxt[3],gettxt[4],gettxt[5],gettxt[6])
        if result == 1:
            kid=functions.kIdFinder()      
            functions.filedialog_show(kid)
        self.modelTrain.main()
        isimsoyisim=str(gettxt[0])+" "+str(gettxt[1])+" Kullanıcısı Eklendi İD Numarası: "+str(kid)
        functions.messageBox("Kullanıcı eklendi",isimsoyisim,icon="info",option=["OK"])
        self.adduser_CANCEL()
        self.treeView()

    def adduser_CANCEL(self):
        for i in range(7):
            self.entries[i].delete("0.0","end")

    def treeView(self):
        style=ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 15)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.configure("Treeview", background="#c9e0e2",foreground="black")
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        style.configure('Treeview', rowheight=40)
        self.tree=ttk.Treeview(self.second_frame,style="mystyle.Treeview",height=10)
        self.tree.bind('<Double-1>', self.DoubleClickTree)
        #self.tree.bind("<ButtonRelease-1>",self.dene) one click kodu + ya basarak aç kapa yapınca bozulursa aktif et
        self.tree["columns"]=("one","two","three","four","five","six")
        self.tree.heading("#0",text=" ",anchor=tk.W)
        self.tree.column("#0",width=110)
        self.tree.heading("one", text="Ad",anchor=tk.W)
        self.tree.column("one",width=155)
        self.tree.heading("two", text="Soyad",anchor=tk.W)
        self.tree.column("two",width=100)
        self.tree.heading("three", text="telefon",anchor=tk.W)
        self.tree.column("three",width=100)
        self.tree.heading("four", text="E-Posta",anchor=tk.W)
        self.tree.column("four",width=100)
        self.tree.heading("five", text="Depertman",anchor=tk.W)
        self.tree.column("five",width=120)
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
            ind[i]=self.tree.insert("",3,text=row[0],values=(row[1],row[2],row[3],row[4],row[5])) 
            list=[os.path.join(path,f) for f in os.listdir(path)]
            for p in list:
                al=p.split("\\")[1]
                dosya=os.stat(p)
                tip=al.split('.')[1]+" File"
                b=(dosya.st_size/1024)
                boyut=str(float("{:.2f}".format(b)))+"Kb"
                otarih=datetime.fromtimestamp(dosya.st_ctime, tz=timezone.utc).strftime('%Y-%m-%d %H:%M')
                self.tree.insert(ind[i],"end",text=al,values=(otarih,tip,boyut),tags="child")
        i+=1
        self.tree.tag_configure('child',background='#DFDFDF')
        
        self.tree.grid(row=1,column=0,padx=(70,70),pady=0,sticky="n")
        
    def DoubleClickTree(self,event):
        item=self.tree.selection()
        if len(item) != 1:
            functions.messageBox("Hata","Lütfen bir tane satır seçimi yapınız","warning",option=["Tamam"])
        else:
            iid=self.tree.selection()[0]
            parentid=self.tree.parent(iid)
            if parentid:
                path="dataFace/"+str(self.tree.item(parentid)['text'])+"/"+str(self.tree.item(iid)['text'])
                name=str(self.tree.item(parentid)['values'][0])+" "+str(self.tree.item(iid)['text'])
                functions.openPicture(path,name)
            else:
                self.OpenFrame4(event)

    def OpenFrame4(self,event):
        departmanrows=functions.departmanGetir()
        self.updateuser_Cancel()
        itema=self.tree.selection()
        al=self.tree.item(itema,'values')
        if len(itema) != 1:
            functions.messageBox("Hata","Lütfen bir tane satır seçimi yapınız","warning",option=["Tamam"])
        else :
            self.frame4()
            for i in range(5):
                if i == 4:
                    for row in departmanrows:
                        if self.tree.item(itema,"values")[4] in row:
                            self.entries1[i+1].insert("0.0",row[0])
                            break
                        elif self.tree.item(itema,"values")[4] == "Bilinmeyen Departman":
                            self.entries1[i+1].insert("0.0","0")
                            break
                else:
                    self.entries1[i+1].insert("0.0",self.tree.item(itema,"values")[i])
            self.entries1[0].insert("0.0",self.tree.item(itema,"text"))
            self.entries1[0].configure(state="disabled") 

    def userupdate(self):
        gettxtupdate=[]
        for i in range(8):
            gettxtupdate.append(self.entries1[i].get("0.0","end-1c"))
        message=str(gettxtupdate[0])+" ID numaralı kullanıcı güncellenmek üzere devam etmek istiyor musunuz?"
        response=functions.messageBox("Kullanıcı Güncelle",message,"question",option=["Hayır","Evet"])
        if response=="Evet":
            result=functions.kUpdate(gettxtupdate[0],gettxtupdate[1],gettxtupdate[2],gettxtupdate[3],gettxtupdate[4],gettxtupdate[5],gettxtupdate[6],gettxtupdate[7])
            if result==-1:
                print("Hatalı Giris")
                return
            message=str(gettxtupdate[0])+" ID numaralı kullanıcı güncellendi."
            functions.messageBox("Kullanıcı Güncelle",message,"info",option=["OK"])
            self.updateuser_Cancel()
            self.select_frame_by_name("frame_2")
            self.treeView()

    def updateuser_Cancel(self):
        for i in range(8):
            self.entries1[i].delete("0.0","end")

    def userDelete(self):
        delid=int(self.entries1[0].get("0.0","end-1c"))
        message=str(delid)+" ID numaralı kullanıcı silinecek, Emin misiniz?"
        response=functions.messageBox("Kullanıcı Sil",message,"question",option=["Hayır","Evet"])
        if response=="Evet":
            functions.kDel(delid)
            message=str(delid)+" ID numaralı Kullanıcı silindi!"
            functions.messageBox("Kullanıcı Sil",message,"info",option=["Tamam"])
            self.updateuser_Cancel()
            self.select_frame_by_name("frame_2")
            self.treeView()

    def processDelete(self):
        item=self.treeProcess.selection()
        if len(item) != 1:
            functions.messageBox("Hata","Lütfen bir tane satır seçimi yapınız","warning",option=["Tamam"])
        else:
            item=self.treeProcess.selection()
            id=self.treeProcess.selection()[0]
            Processid=self.treeProcess.item(id)["text"]
            message=f"{Processid} Numaralı işlem silinecek Devam etmek istiyor musunuz?"
            response=functions.messageBox("İşlem Sil",message,"question",option=["Hayır","Evet"])
            if response=="Evet":
                sonuc=functions.bilgisil(Processid)
                if sonuc==1:
                    message=f"{Processid} numaralı işlem veritabanından silindi."
                    functions.messageBox("İşlem Sil",message,"info",option=["Tamam"])
            self.LastProcessView()

    def LastProcessView(self):
        style=ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 15)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.configure("Treeview", background="#c9e0e2",foreground="black")
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        style.configure('Treeview', rowheight=40)
        self.treeProcess=ttk.Treeview(self.third_frame,style="mystyle.Treeview",height=10)
        self.treeProcess.bind('<Double-1>', self.ProcessViewDoubleClick)
        self.treeProcess["columns"]=("one","two","three","four")
        self.treeProcess.heading("#0",text=" ",anchor=tk.W)
        self.treeProcess.column("#0",width=70)
        self.treeProcess.heading("one", text="islem",anchor=tk.W)
        self.treeProcess.column("one",width=200)
        self.treeProcess.heading("two", text="saat",anchor=tk.W)
        self.treeProcess.column("two",width=80)
        self.treeProcess.heading("three", text="tarih",anchor=tk.W)
        self.treeProcess.column("three",width=100)
        self.treeProcess.heading("four", text="Kullanıcı",anchor=tk.W)
        self.treeProcess.column("four",width=150)
        rows=functions.Pliste()
        for row in rows: 
            self.treeProcess.insert("",3,text=row[0],values=(row[1],row[2],row[3],row[4]))
        self.treeProcess.grid(row=1,column=0,padx=(70,70),pady=0,sticky="n")

    def ProcessViewDoubleClick(self,event):
        item=self.treeProcess.selection()
        if len(item) != 1:
            functions.messageBox("Hata","Lütfen bir tane satır seçimi yapınız","warning",option=["Tamam"])
        else:
            iid=self.treeProcess.selection()[0]
            message=str(self.treeProcess.item(iid)['values'][3])+" Adlı "+str(self.treeProcess.item(iid)['values'][0])+" Tarih/Saat: "+str(self.treeProcess.item(iid)['values'][2])+"/"+str(self.treeProcess.item(iid)['values'][1])
            functions.messageBox("İşlem",message,"info",option=['OK'])

    def onlyNumbers(self,event):
        v=event.char
        try:
            v=int(v)
        except ValueError:
            if v!="\x08" and v!="":
                return "break"

if __name__ == "__main__":
    app = App()
    print("Personel Takip Programı Başlatıldı.\nresizable Disabled.")
    app.resizable(False,False) 
    app.eval('tk::PlaceWindow . center')
    app.mainloop()