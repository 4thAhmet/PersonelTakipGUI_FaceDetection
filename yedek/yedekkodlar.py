 """def userlist(self):
        self.sayac=1
        self.usertxt =""
        self.count=0
        self.userlistid,self.userlistname=functions.Kliste()
        print("userlist ve name: ")
        print("----------------")
        print(self.userlistid)
        print(self.userlistname)
        print("-------------------")
        self.scrollable_frame_switches.clear()
        self.btnname={}
        self.btnid=[]
        for user in self.userlistid:
            def action(x=user):
                return self.User_Delete(x)
            self.usertxt=str(user)+"\t"+str(self.userlistname[self.count])
            self.count+=1
            self.label=customtkinter.CTkLabel(master=self.scrollable_frame,text=self.usertxt,font=customtkinter.CTkFont(size=18),anchor='center')
            self.label.grid(row=self.sayac,column=0,padx=0, pady=(0,0))
            self.btnname[user]=customtkinter.CTkButton(master=self.scrollable_frame,corner_radius=0,height=20, border_spacing=5, text="",
                                              fg_color="transparent", text_color=("gray10","gray90"),hover_color=("gray70","gray30"),
                                              image=self.adduser_CANCEL_image,anchor="c",command=action)
            self.btnname[user].grid(row=self.sayac,column=1,padx=0,pady=0)
            self.scrollable_frame_switches.append(self.label)
            self.scrollable_frame_switches.append(self.btnname)
            self.sayac+=1
            self.usertxt=""
            """

    """def scrollable(self):

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.second_frame, label_text="Kayıtlı Kullanıcı Listesi")
        self.scrollable_frame.grid(row=1, column=0, padx=(30, 30), pady=(0, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame_switches = []
        self.headerlabel=customtkinter.CTkLabel(master=self.scrollable_frame,text="\tID NO \t KULLANICI ADI \t",text_color="red",font=customtkinter.CTkFont(size=18))
        self.headerlabel.grid(row=0,column=0,padx=0, pady=(0,0))
        self.headerlabel=customtkinter.CTkLabel(master=self.scrollable_frame,text="Kullanıcı Sil",text_color="red",compound='right',font=customtkinter.CTkFont(size=18),anchor='center')
        self.headerlabel.grid(row=0,column=1,padx=(0,0), pady=0)
        self.scrollable_frame_switches.append(self.headerlabel)
        self.userlist()
        self.usertxt=""
        self.sayac=1
        self.count=0"""
    