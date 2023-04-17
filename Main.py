#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
                            # Kütüphaneler #
import customtkinter
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image
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
        self.geometry("700x480")
        self.iconbitmap(default="images/logo1.ico")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Load Images#
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.user_list_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "list-light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "list-dark.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.user_detect_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"face-detection-dark.png")),
                                                      dark_image=Image.open(os.path.join(image_path,"face-detection-light.png")), size=(20,20))
        self.user_edit_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"edituser-dark.png")),
                                                    dark_image=Image.open(os.path.join(image_path,"edituser-light.png")),size=(20,20))
        self.refresh_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"refresh-dark.png")),
                                                    dark_image=Image.open(os.path.join(image_path,"refresh-light.png")),size=(20,20))
        self.adduser_OK_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"add-user-dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path,"add-user-light.png")),size=(20,20))
        self.adduser_CANCEL_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"cancel-dark.png")),
                                                         dark_image=Image.open(os.path.join(image_path,"cancel-light.png")),size=(20,20))
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Navigation Bar Frame#
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Personel Takip", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=30, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=" Anasayfa",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=" Kullanıcı Listesi",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.user_list_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=0, sticky="s")


        self.scaling_label = customtkinter.CTkLabel(self.navigation_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(0, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.set('100%')
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(0, 10))
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
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="PERSONEL TAKİP SİSTEMİ ",font=customtkinter.CTkFont(size=25, weight="bold"), image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=0)
        self.label1=customtkinter.CTkLabel(self.home_frame,text=self.labeltext,font=customtkinter.CTkFont(size=18))
        self.label1.grid_configure(row=2,column=0,padx=20)
        self.hakkindatxt="Personel Takip Sistemi ile personellerin işe başlama ve bitiş   saatlerini hızlı ve eksiksiz kayıt altına alabilirsiniz. \n "
        self.hakkindatxt+="Hata Oranı Düşük bir şekilde Yüz tanıma sistemi ile kolay ve hızlı işlem sunar. \n"
        self.hakkindatxt+="\n ~Ahmet Akkeçi~\n "
        self.widget=customtkinter.CTkFrame(self.home_frame)
        self.widget.grid(row=3,column=0,padx=10,pady=20)
        self.textbox = customtkinter.CTkTextbox(self.home_frame, font=customtkinter.CTkFont(size=18))
        self.textbox.insert("0.0", self.hakkindatxt)
        self.textbox.configure(state="disabled") 
        self.textbox.grid(row=1, column=0, padx=(47, 47), pady=(0, 0), sticky="nsew")
        self.facelogo=customtkinter.CTkImage(light_image=Image.open("images/fbeyaz.png"),dark_image=Image.open("images/f.png"),size=(50,50))
        self.facelogobutton=customtkinter.CTkButton(self.widget,text="Facebook",image=self.facelogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=15, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda: functions.socialmedia(1))
        self.facelogobutton.grid(row=3,column=0,padx=(5,0),pady=0)
        self.instalogo=customtkinter.CTkImage(light_image=Image.open("images/ibeyaz.png"),dark_image=Image.open("images/i.png"),size=(50,50))
        self.instabutton=customtkinter.CTkButton(self.widget,text="İnstagram",image=self.instalogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=15, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda:functions.socialmedia(2))
        self.instabutton.grid(row=3,column=1,padx=(5,0),pady=0)

        self.twlogo=customtkinter.CTkImage(light_image=Image.open("images/tbeyaz.png"),dark_image=Image.open("images/t.png"),size=(50,50))
        self.twlogobutton=customtkinter.CTkButton(self.widget,text="Twitter",image=self.twlogo,
                                                    corner_radius=0, height=20, border_spacing=5,font=customtkinter.CTkFont(size=15, weight="bold"),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w",command=lambda:functions.socialmedia(3))
        self.twlogobutton.grid(row=3,column=2,padx=(5,0),pady=0)
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Second Frame#
        # create second frame  
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="Yuz Algılama ve Kullanıcı Listesi",font=customtkinter.CTkFont(size=25, weight="bold"), image=self.large_test_image)
        self.second_frame_large_image_label.grid(row=0, column=0, padx=10, pady=0)

        self.viewer()
        self.seconf_frame_buttonframe=customtkinter.CTkFrame(self.second_frame,corner_radius=0,fg_color="transparent")
        self.seconf_frame_buttonframe.grid(row=2,column=0,padx=(20,0),pady=0,sticky="nsew")

        self.button_userDetect = customtkinter.CTkButton(self.seconf_frame_buttonframe, corner_radius=0, height=40, border_spacing=10, text="Kullanıcı Tanı",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.user_detect_image, anchor="w",command=self.DetectedFace)
        self.button_userDetect.grid(row=2, column=1, padx=(20,0))
        self.button_useredit =customtkinter.CTkButton(self.seconf_frame_buttonframe,corner_radius=0,height=40, border_spacing=10, text="Kullanıcı Ekle",
                                                        fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                                        image=self.user_edit_image, anchor="w", command=self.frame3)
        self.button_useredit.grid(row=2, column=2)
        self.button_refresh =customtkinter.CTkButton(self.seconf_frame_buttonframe,corner_radius=0,height=40, border_spacing=10, text="Listeyi Güncelle",
                                                        fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                                        image=self.refresh_image, anchor="w",command=self.viewer)
        self.button_refresh.grid(row=2, column=3,sticky="")
        
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
                                                             font=customtkinter.CTkFont(size=25, weight="bold"))
        self.labelheader.grid(row=0,column=0,padx=(110,0),pady=0)
        self.labelheader1 = customtkinter.CTkLabel(self.fourth_frame, text="onel Ekleme",
                                                             font=customtkinter.CTkFont(size=25, weight="bold"))
        self.labelheader1.grid(row=0,column=1,padx=(0,80),pady=0,)
        self.labeltext=[" ","Personel ID","Personel Adı","Personel Soyad","Personel Telefon","Personel Eposta","Departman ID","Departman Name","Personel Sifre"]
        for i in range(1,9):
            self.f=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")  
            self.f.grid(row=i, column=0, padx=0,pady=0)         
            self.navigation_frame_label = customtkinter.CTkLabel(self.f, text=self.labeltext[i],
                                                             font=customtkinter.CTkFont(size=13, weight="bold"))
            self.entries.append(customtkinter.CTkTextbox(self.fourth_frame,height=0.01, font=customtkinter.CTkFont(size=13)))
            self.navigation_frame_label.grid(row=0, column=0, padx=5, pady=10)  
            self.entries[-1].grid(row=i, column=1, padx=0, pady=10, sticky="nsew")

        self.buttons_frame=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame.grid(row=10,column=1, padx=(10,10), pady=0)
        self.buttons_frame1=customtkinter.CTkFrame(self.fourth_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame1.grid(row=10,column=0, padx=(10,10), pady=0)
        self.buttonOK=customtkinter.CTkButton(self.buttons_frame,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Ekle",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_OK_image,anchor="w",command=self.adduser_OK)
        self.buttonOK.grid(row=9, column=0, padx=10, pady=10)    

        self.buttonCancel=customtkinter.CTkButton(self.buttons_frame1,corner_radius=0,height=40, border_spacing=5, text="İptal Et",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_CANCEL_image,anchor="w",command=self.adduser_CANCEL)
        self.buttonCancel.grid(row=9, column=0, padx=10, pady=10)  
        self.buttonOK.place(relx=0.5,rely=0.1,anchor="center")   
        self.buttonCancel.place(relx=0.9, rely=0.1,anchor="center") 
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
                                                             font=customtkinter.CTkFont(size=13, weight="bold"))
            self.entries1.append(customtkinter.CTkTextbox(self.five_frame,height=0.01, font=customtkinter.CTkFont(size=13)))
            self.navigation_frame_label1.grid(row=0, column=0, padx=5, pady=10)  
            self.entries1[-1].grid(row=i, column=1, padx=0, pady=10, sticky="nsew")

        self.buttons_frame1=customtkinter.CTkFrame(self.five_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame1.grid(row=10,column=1, padx=(10,10), pady=0)
        self.buttons_frame11=customtkinter.CTkFrame(self.five_frame,corner_radius=0,fg_color="transparent")
        self.buttons_frame11.grid(row=10,column=0, padx=(10,10), pady=0)
        self.buttonOK=customtkinter.CTkButton(self.buttons_frame1,corner_radius=0,height=40, border_spacing=5, text="Kullanıcı Düzenle",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_OK_image,anchor="w",command=self.userupdate)
        self.buttonOK.grid(row=9, column=0, padx=10, pady=10)    

        self.buttonCancel=customtkinter.CTkButton(self.buttons_frame11,corner_radius=0,height=40, border_spacing=5, text="İptal Et",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_CANCEL_image,anchor="w",command=self.adduser_CANCEL)
        self.buttonCancel.grid(row=9, column=0, padx=10, pady=10)  
        self.buttonOK.place(relx=0.5,rely=0.1,anchor="center")   
        self.buttonCancel.place(relx=0.9, rely=0.1,anchor="center") 
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

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        yeniH=480*new_scaling_float
        yeniW=700*new_scaling_float
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

    def adduser_CANCEL(self):
        for i in range(8):
            self.entries[i].delete("0.0","end")

    def viewer(self):
        self.tree = ttk.Treeview(self.second_frame,columns=('U_Id','U_ad','U_soyad','U_telefon','U_eposta','D_ID'), show='headings',height=10)
        rows=functions.kliste()
        for row in rows:
            print(row) 
            self.tree.insert("", tk.END, values=row) 
        self.tree.bind("<Double-1>",self.doubleclick)
        self.tree.column("#1",anchor=tk.CENTER,stretch=tk.NO,width=40)
        self.tree.heading("#1", text="No")
        self.tree.column("#2",anchor=tk.CENTER,stretch=tk.NO,width=75)
        self.tree.heading("#2", text="Ad")
        self.tree.column("#3",anchor=tk.CENTER,stretch=tk.NO,width=75)
        self.tree.heading("#3", text="Soyad")
        self.tree.column("#4",anchor=tk.CENTER,stretch=tk.NO,width=75)
        self.tree.heading("#4", text="Telefon")
        self.tree.column("#5",anchor=tk.CENTER,stretch=tk.NO,width=75)
        self.tree.heading("#5", text="E-Posta")
        self.tree.column("#6",anchor=tk.CENTER,stretch=tk.NO,width=70)
        self.tree.heading("#6", text="Departman Adı")
        self.tree.grid(row=1, column=0,padx=(30,30),pady=0)

    def doubleclick(self,event):
        item=self.tree.selection()
        print(len(item))
        if len(item) != 1:
            print("Bir tane seçim yapınız!")
        else :
            print("you clicked on ",self.tree.item(item,"values")[0])
            self.frame4()
            for i in range(7):
                if i==6:
                    self.entries1[i+1].insert("0.0",self.tree.item(item,"values")[i]) 
                else:
                    self.entries1[i].insert("0.0",self.tree.item(item,"values")[i])
            self.entries1[0].configure(state="disabled") 

    def userupdate(self):
        gettxtupdate=[]
        for i in range(8):
            gettxtupdate.append(self.entries1[i].get("0.0","end-1c"))
        result=functions.kUpdate(gettxtupdate[0],gettxtupdate[1],gettxtupdate[2],gettxtupdate[3],gettxtupdate[4],gettxtupdate[5],gettxtupdate[6],gettxtupdate[7])
        if result==-1:
            print("Hatalı Giris")
             
if __name__ == "__main__":
    app = App()
    print("Personel Takip Programı Başlatıldı.\nresizable Disabled.")
    app.resizable(False,False) 
    app.eval('tk::PlaceWindow . center')
    app.mainloop()