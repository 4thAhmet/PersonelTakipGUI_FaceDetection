import customtkinter
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image

image_path=os.path.join("./images")
def loadimages():
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                        #Load Images#
        # load images with light and dark mode image
    logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(65, 65))
    large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
    image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(50, 50))
    home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home.png")),
                                            dark_image=Image.open(os.path.join(image_path, "home.png")), size=(50, 50))
    user_list_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "userlist.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "userlist.png")), size=(50, 50))
    add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add-user.png")),
                                                dark_image=Image.open(os.path.join(image_path, "add-user.png")), size=(50, 50))
    user_detect_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"face-detection.png")),
                                                      dark_image=Image.open(os.path.join(image_path,"face-detection.png")), size=(50,50))
    refresh_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"refresh.png")),
                                            dark_image=Image.open(os.path.join(image_path,"refresh.png")),size=(50,50))
    adduser_CANCEL_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"cancel.png")),
                                                         dark_image=Image.open(os.path.join(image_path,"cancel.png")),size=(50,50))
    info_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"info.png")),
                                               dark_image=Image.open(os.path.join(image_path,"info.png")), size=(30,30))
    deleteuser_image=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path,"removeuser.png")),
                                            dark_image=Image.open(os.path.join(image_path,"removeuser.png")), size=(50,50))
    return logo_image,large_test_image,image_icon_image,home_image,user_list_image,add_user_image,user_detect_image,refresh_image,adduser_CANCEL_image,info_image,deleteuser_image
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
def loadimages2():
    recentOnes = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "recent.png")),
                                        dark_image=Image.open(os.path.join(image_path, "recent.png")), size=(50, 50))
    return recentOnes
def SocailMediaLogo():
    facelogo=customtkinter.CTkImage(light_image=Image.open("images/f.png"),dark_image=Image.open("images/f.png"),size=(70,70))
    instalogo=customtkinter.CTkImage(light_image=Image.open("images/i.png"),dark_image=Image.open("images/i.png"),size=(70,70))
    twlogo=customtkinter.CTkImage(light_image=Image.open("images/t.png"),dark_image=Image.open("images/t.png"),size=(70,70))
    return facelogo,instalogo,twlogo
def sliderImage():
    rightarrow=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "right-arrow.png")),
                                            dark_image=Image.open(os.path.join(image_path, "right-arrow.png")), size=(25, 25))
    leftarrow=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "left-arrow.png")),
                                            dark_image=Image.open(os.path.join(image_path, "left-arrow.png")), size=(25, 25))
    img1= customtkinter.CTkImage(Image.open(os.path.join(image_path, "slide.png")),size=(700,450))
    img2= customtkinter.CTkImage(Image.open(os.path.join(image_path, "slide1.png")),size=(700,450))
    img3= customtkinter.CTkImage(Image.open(os.path.join(image_path, "slide2.png")),size=(700,450))
    img4= customtkinter.CTkImage(Image.open(os.path.join(image_path, "slide3.png")),size=(700,450))
    return rightarrow,leftarrow,img1,img2,img3,img4

