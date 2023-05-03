""" !!!!!!!!!!!!! USER ID OTAMATİK ARTAN YAPILACAK ARA BOŞLUKLAR OPTİMİZE EDİLECEK !!!!!!!!!!!!!!!!
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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # fonksiyon import #
from scripts import Face_detect
from scripts import functions
from scripts import trainModel
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Window Başlangıç #
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.facedetectClass=Face_detect.FaceDetect()
        self.modelTrain=trainModel.TrainModel()
        customtkinter.set_default_color_theme('scripts/theme.json')
        self.title("Personel Takip Uygulaması")
        self.geometry("1050x720")
        self.iconbitmap(default="images/logo.ico")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Load Images#
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(65, 65))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(50, 50))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home.png")), size=(50, 50))
        self.user_list_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "userlist.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "userlist.png")), size=(50, 50))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add-user.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add-user.png")), size=(50, 50))
        self.user_detect_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"face-detection.png")),
                                                      dark_image=Image.open(os.path.join(image_path,"face-detection.png")), size=(50,50))
        self.user_edit_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"edituser-dark.png")),
                                                    dark_image=Image.open(os.path.join(image_path,"edituser-light.png")),size=(50,50))
        self.refresh_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"refresh.png")),
                                                    dark_image=Image.open(os.path.join(image_path,"refresh.png")),size=(50,50))
        self.adduser_CANCEL_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"cancel-dark.png")),
                                                         dark_image=Image.open(os.path.join(image_path,"cancel-light.png")),size=(50,50))
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

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",font=customtkinter.CTkFont(size=20), command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.theme_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Theme:", anchor="w",font=customtkinter.CTkFont(size=14))
        self.theme_label.grid(row=5, column=0, padx=30, pady=(0, 0),sticky="sw")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], width=200, font=customtkinter.CTkFont(size=14),
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=30, pady=0, sticky="sw")


        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Scaling:", anchor="w", font=customtkinter.CTkFont(size=14))
        self.scaling_label.grid(row=7, column=0, padx=30, pady=(0, 0),sticky="sw")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["70%","80%", "90%", "100%", "110%", "120%","130%"], width=200,font=customtkinter.CTkFont(size=14),
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.set('100%')
        self.scaling_optionemenu.grid(row=8, column=0, padx=30, pady=(0, 10),sticky="sw")
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #First Frame#
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.kSay=functions.KullaniciSay()
        self.labeltext=" "
        if self.kSay==-1:
            self.labeltext="Not Found Database"
        self.labeltext="Sisteme Kayıtlı Kullanıcı Sayısı: "+str(self.kSay)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="PERSONEL TAKİP SİSTEMİ ",font=customtkinter.CTkFont(size=30, weight="bold"), image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=0)
        self.label1=customtkinter.CTkLabel(self.home_frame,text=self.labeltext,font=customtkinter.CTkFont(size=25),fg_color="#00bbc9")
        self.label1.grid_configure(row=2,column=0,padx=20,pady=(30,20))
        self.hakkindatxt="Personel Takip Sistemi ile personellerin işe başlama ve bitiş   saatlerini hızlı ve eksiksiz kayıt altına alabilirsiniz. \n "
        self.hakkindatxt+="Hata Oranı Düşük bir şekilde Yüz tanıma sistemi ile kolay ve hızlı işlem sunar. \n"
        self.hakkindatxt+="\n ~Ahmet Akkeçi~\n "
        self.widget=customtkinter.CTkFrame(self.home_frame)
        self.widget.grid(row=3,column=0,padx=10,pady=20)
        self.textbox = customtkinter.CTkTextbox(self.home_frame, font=customtkinter.CTkFont(size=25))
        self.textbox.insert("0.0", self.hakkindatxt)
        self.textbox.configure(state="disabled") 
        self.textbox.grid(row=1, column=0, padx=(47, 47), pady=(0, 0), sticky="nsew")
        self.facelogo=customtkinter.CTkImage(light_image=Image.open("images/f.png"),dark_image=Image.open("images/f.png"),size=(70,70))
        self.facelogobutton=customtkinter.CTkButton(self.widget,text="Facebook",image=self.facelogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=20, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda: functions.socialmedia(1))
        self.facelogobutton.grid(row=3,column=0,padx=(5,0),pady=0)
        self.instalogo=customtkinter.CTkImage(light_image=Image.open("images/i.png"),dark_image=Image.open("images/i.png"),size=(70,70))
        self.instabutton=customtkinter.CTkButton(self.widget,text="İnstagram",image=self.instalogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=20, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda:functions.socialmedia(2))
        self.instabutton.grid(row=3,column=1,padx=(5,0),pady=0)

        self.twlogo=customtkinter.CTkImage(light_image=Image.open("images/t.png"),dark_image=Image.open("images/t.png"),size=(70,70))
        self.twlogobutton=customtkinter.CTkButton(self.widget,text="Twitter",image=self.twlogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=20, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda:functions.socialmedia(3))
        self.twlogobutton.grid(row=3,column=2,padx=(5,0),pady=0)
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Second Frame#
        # create second frame  
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_rowconfigure(2, weight=1)
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="Kullanıcı Listesi",font=customtkinter.CTkFont(size=30, weight="bold"), image=self.large_test_image)
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

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                #Fourth Frame#
        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self,corner_radius=0, fg_color="transparent")
        self.entries=[]
        self.labelheader = customtkinter.CTkLabel(self.fourth_frame, text="Yeni Pers",
                                                             font=customtkinter.CTkFont(size=30, weight="bold"))
        self.labelheader.grid(row=0,column=0,padx=(110,0),pady=0)
        self.labelheader1 = customtkinter.CTkLabel(self.fourth_frame, text="onel Ekleme",
                                                             font=customtkinter.CTkFont(size=30, weight="bold"))
        self.labelheader1.grid(row=0,column=1,padx=(0,80),pady=0,)
        self.labeltext=[" ","Personel ID","Personel Adı","Personel Soyad","Personel Telefon","Personel Eposta","Departman ID","Departman Name","Personel Sifre"]
        for i in range(1,9):
            self.f=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")  
            self.f.grid(row=i, column=0, padx=0,pady=0)         
            self.navigation_frame_label = customtkinter.CTkLabel(self.f, text=self.labeltext[i],
                                                             font=customtkinter.CTkFont(size=18, weight="bold"))
            self.entries.append(customtkinter.CTkTextbox(self.fourth_frame,height=0.01, font=customtkinter.CTkFont(size=18)))
            self.navigation_frame_label.grid(row=0, column=0, padx=5, pady=10)  
            self.entries[-1].grid(row=i, column=1, padx=0, pady=10, sticky="nsew")

        self.buttons_frame=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame.grid(row=10,column=1, padx=(10,10), pady=0)
        self.buttons_frame1=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame1.grid(row=10,column=0, padx=(10,10), pady=0)
        self.buttonOK=customtkinter.CTkButton(self.buttons_frame,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Ekle",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.add_user_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.adduser_OK)
        self.buttonOK.grid(row=9, column=0, padx=10, pady=10)    

        self.buttonCancel=customtkinter.CTkButton(self.buttons_frame1,corner_radius=0,height=40, border_spacing=5, text="İptal Et",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_CANCEL_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.adduser_CANCEL)
        self.buttonCancel.grid(row=9, column=0, padx=10, pady=10)  
        self.buttonOK.place(relx=0.5,rely=0.1,anchor="center")   
        self.buttonCancel.place(relx=0.75, rely=0.1,anchor="center") 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                #five Frame#
        # create five frame
        self.five_frame = customtkinter.CTkFrame(self,corner_radius=0, fg_color="transparent")
        self.entries1=[]
        self.labelheader1 = customtkinter.CTkLabel(self.five_frame, text="Personel Düzenle",
                                                             font=customtkinter.CTkFont(size=25, weight="bold"))
        self.labelheader1.grid(row=0,column=0,padx=(0,0),pady=0)
        self.labeltext1=[" ","Personel ID","Personel Adı","Personel Soyad","Personel Telefon","Personel Eposta","Departman ID","Departman Name","Personel Sifre"]
        for i in range(1,9):
            self.f1=customtkinter.CTkFrame(self.five_frame,corner_radius=0,fg_color="transparent")  
            self.f1.grid(row=i, column=0, padx=0,pady=0)         
            self.navigation_frame_label1 = customtkinter.CTkLabel(self.f1, text=self.labeltext1[i],
                                                             font=customtkinter.CTkFont(size=18, weight="bold"))
            self.entries1.append(customtkinter.CTkTextbox(self.five_frame,height=0.01, font=customtkinter.CTkFont(size=18)))
            self.navigation_frame_label1.grid(row=0, column=0, padx=5, pady=10)  
            self.entries1[-1].grid(row=i, column=1, padx=0, pady=10, sticky="nsew")

        self.buttons_frame1=customtkinter.CTkFrame(self.five_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame1.grid(row=10,column=1, padx=(10,10), pady=0)
        self.buttons_frame11=customtkinter.CTkFrame(self.five_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame11.grid(row=10,column=0, padx=(10,10), pady=0)
        self.buttonOK=customtkinter.CTkButton(self.buttons_frame1,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Düzenle",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.add_user_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.userupdate)
        self.buttonOK.grid(row=9, column=0, padx=10, pady=10)  

        self.buttonCancel=customtkinter.CTkButton(self.buttons_frame11,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Sil",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_CANCEL_image,anchor="w",font=customtkinter.CTkFont(size=18),command=self.userDelete)
        self.buttonCancel.grid(row=9, column=0, padx=0, pady=10)  
        self.buttonOK.place(relx=0.1,rely=0.1,anchor="w")   
        self.buttonCancel.place(relx=0.25, rely=0.1,anchor="w") 
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
        
    def User_Delete(self,id):
        functions.kSil(id)
        self.scrollable_frame_switches.pop()
        self.scrollable()
        print(id,"'li Kullanıcı Silindi.")

    def DetectedFace(self):
        id,ad=self.facedetectClass.main()
        if id==-1:
            print("Kimse Tanınmadı ! ")
        else:
            print("id: ",ad," Ad: ",id)
        self.facedetectClass.closeWindow()

    def adduser_OK(self):
        print("Kullanıcı ekleme kabul butonu")
        gettxt=[]
        for i in range(8):
            gettxt.append(self.entries[i].get("0.0","end-1c"))
        result=functions.kEkle(gettxt[0],gettxt[1],gettxt[2],gettxt[3],gettxt[4],gettxt[5],gettxt[6],gettxt[7])
        if result == 1:      
            functions.filedialog_show(gettxt[0])
        self.modelTrain.main()
        self.adduser_CANCEL()
        self.viewer()

    def adduser_CANCEL(self):
        for i in range(8):
            self.entries[i].delete("0.0","end")

#------------------------------------------------------------------------------------------------------------------------------
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
            print("Bir tane seçim yapınız!")
        else:
            iid=self.tree.selection()[0]
            parentid=self.tree.parent(iid)
            if parentid:
                path="dataFace/"+str(self.tree.item(parentid)['text'])+"/"+str(self.tree.item(iid)['text'])
                name=str(self.tree.item(parentid)['values'][0])+" "+str(self.tree.item(iid)['text'])
                functions.openPicture(path,name)
            else:
                self.OpenFrame4(event)

#-------------------------------------------------------------------------------------------------------------------------------

    def OpenFrame4(self,event):
        self.entries1[0].configure(state="normal") 
        self.updateuser_Cancel()
        itema=self.tree.selection()
        al=self.tree.item(itema,'values')
        if len(itema) != 1:
            print("Bir tane seçim yapınız!")
        else :
            self.frame4()
            for i in range(5):
                self.entries1[i+1].insert("0.0",self.tree.item(itema,"values")[i])
            self.entries1[0].insert("0.0",self.tree.item(itema,"text"))
            self.entries1[0].configure(state="disabled") 

    def userupdate(self):
        gettxtupdate=[]
        for i in range(8):
            gettxtupdate.append(self.entries1[i].get("0.0","end-1c"))
        result=functions.kUpdate(gettxtupdate[0],gettxtupdate[1],gettxtupdate[2],gettxtupdate[3],gettxtupdate[4],gettxtupdate[5],gettxtupdate[6],gettxtupdate[7])
        if result==-1:
            print("Hatalı Giris")

    def updateuser_Cancel(self):
        for i in range(8):
            self.entries1[i].delete("0.0","end")

    def userDelete(self):
        delid=int(self.entries1[0].get("0.0","end-1c"))
        functions.kDel(delid)
        self.updateuser_Cancel()
        self.select_frame_by_name("frame_2")
        self.viewer()

if __name__ == "__main__":
    app = App()
    print("Personel Takip Programı Başlatıldı.\nresizable Disabled.")
    app.resizable(False,False) 
    app.eval('tk::PlaceWindow . center')
    app.mainloop()