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
    

    """def treeView(self):
        style=ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        self.tree1=ttk.Treeview(self.second_frame)
        self.tree1["columns"]=("one","two","three","four","five","six")
        self.tree1.heading("#0",text="No",anchor=tk.W)
        self.tree1.column("#0",width=40)
        self.tree1.heading("one", text="Ad",anchor=tk.W)
        self.tree1.heading("two", text="Soyad",anchor=tk.W)
        self.tree1.heading("three", text="Telefon",anchor=tk.W)
        self.tree1.heading("four", text="E-posta",anchor=tk.W)
        self.tree1.heading("six", text="Departman",anchor=tk.W)
        rows=functions.kliste()
        kid={}
        for row in rows:
            print("for")
        self.folder=self.tree1.insert("",3,text="Folder 1",values=("23-Jun-17 11:05","File Folder",""))
        self.tree1.insert("",2,text="text_file.txt",values=("23-jun-17 11:25","TXT File","1 KB"))
        self.tree1.insert(self.folder,"end",text="photo1.jpg",values=("23-jun-17 11:28","PNG File","2.86 KB"))
        #self.tree1.insert(folder,"end","",text="photo1.jpg",values=("23-jun-17 11:28","PNG File","2.86 KB"))
        self.tree1.grid(row=1,column=0,padx=(30,30),pady=0,sticky="n")
        """

    """def viewer(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 15)) 
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        self.tree = ttk.Treeview(self.second_frame,columns=('U_Id','U_ad','U_soyad','U_telefon','U_eposta','D_ID'), show='headings',height=15,style="mystyle.Treeview")
        rows=functions.kliste()
        for row in rows:
            self.tree.insert("", tk.END, values=row)       
        self.tree.bind("<Double-1>",self.doubleclick)
        self.tree.column("#1",anchor=tk.CENTER,stretch=tk.NO,width=40)
        self.tree.heading("#1", text="No")
        self.tree.column("#2",anchor=tk.CENTER,stretch=tk.NO,width=100)
        self.tree.heading("#2", text="Ad")
        self.tree.column("#3",anchor=tk.CENTER,stretch=tk.NO,width=100)
        self.tree.heading("#3", text="Soyad")
        self.tree.column("#4",anchor=tk.CENTER,stretch=tk.NO,width=100)
        self.tree.heading("#4", text="Telefon")
        self.tree.column("#5",anchor=tk.CENTER,stretch=tk.NO,width=100)
        self.tree.heading("#5", text="E-Posta")
        self.tree.column("#6",anchor=tk.CENTER,stretch=tk.NO,width=150)
        self.tree.heading("#6", text="Departman Adı")
        self.tree.grid(row=1, column=0,padx=(30,30),pady=0,sticky="n")"""
