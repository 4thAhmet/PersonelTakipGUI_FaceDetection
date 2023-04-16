#--------------------------------------------------------------------------------------------------------------------#
                            # Kütüphaneler #
import cv2,os,csv
import numpy as np
from PIL import Image,ImageDraw,ImageFont
#from deepface import DeepFace  --> DeepFace Kontrol Edilecek


#--------------------------------------------------------------------------------------------------------------------#
                            # Global Değişkenler #
csvpath='dataFace/dataBase.csv'
recognizer = cv2.face.LBPHFaceRecognizer_create()
cascadePath="Cascades/haarcascade_frontalface_default.xml"
font=cv2.FONT_HERSHEY_SIMPLEX
color = (255,0,0)
#controlpath='controlFace/0.jpg'
device="face_test.mp4" # Video ismi veya Kamera için 0 yaz.


#--------------------------------------------------------------------------------------------------------------------#
                            # Fonksiyonlar #
def readCSV():
    names={}
    print("Reading CSV File...")
    if os.path.exists(csvpath):
        f=open(csvpath,mode='r')
    else:
        print("CSV NO FOUND!")
        print("Please Create a CSV File! You can sse train.py file")
        print("Terminating...")
        exit()
    with f as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count= 0
        for row in csv_reader:
            if len(row) == 0:
                continue
            if row[1] == ' ':
                row[1]='Noname'
            names[str(row[0])]=str(row[1])
            line_count+=1
    f.close()
    print("Read Csv File!")
    return names

"""def DeepfaceControl(cntrlpath,frompath):
    print("Deepface")
    pathlist=[os.path.join(frompath,f) for f in os.listdir(frompath)]
    for p in pathlist:
        result = DeepFace.verify(img1_path=controlpath,img2_path=p)
        if result['verified'] == False :
            return 
"""
def print_utf8_text(image,xy,text,color):
    fontName='FreeSerif.ttf'
    #font = ImageFont.truetype(fontName,24)
    font=ImageFont.load_default()
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    draw.text((xy[0],xy[1]),text,font=font,
              fill=(color[0],color[1],color[2],0))
    image = np.array(img_pil)
    return image


#--------------------------------------------------------------------------------------------------------------------#
                            # Main Fonksiyon #
if __name__=="__main__":
    recognizer.read('Train/train.yml')
    faceCascade = cv2.CascadeClassifier(cascadePath)
    id = 0
    names = readCSV()
    cam = cv2.VideoCapture(device)
    cam.set(3,1000)
    cam.set(4,800)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    while(True):
        ret,img=cam.read()
        if not ret:
            cam=cv2.VideoCapture(device)
            ret,img=cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize=(int(minW),int(minH)),
        )
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,uyum = recognizer.predict(gray[y:y+h, x:x+w])
            if(uyum<70):      
                #cv2.imwrite("controlFace/"+str(id)+".jpg",img)
                pth='dataFace/'+str(id)
                ad=id
                id = names[str(id)]
                uyum=f"Uyum Oranı: {round(uyum,0)}%"
                print(f"\n Name: {id} {uyum}")
                img=print_utf8_text(img,(x+5,y-25),str(id),color) 
                #cv2.putText(img,str(uyum),(x+5,y+h+25),font,1,(0,255,0),1)
        cv2.imshow("Frame",img)
        k=cv2.waitKey(10 & 0xff)
        if k==27 or k==ord('q'):
            break
    print("\n [INFO]: Memory Clearing!")
    print("[INFO]: Program Terminating...")
    cam.release()
    cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------------------------------------#
                            # END #

                            # Doğrulanan kişileri 2. Algoritma ile kontrol et 
                            # Doğrulanmayan kişilerin En yakın olduğu kişileri bul
                            # GUI girişini yap.
                            # Gui tasarımını yap.