import cv2,os,csv,time
from PIL import Image,ImageDraw,ImageFont
import numpy as np
class FaceDetect:
    def __init__(self):
        super().__init__()
        self.csvpath="dataFace/dataBase.csv"
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.cascadePath="Cascades/haarcascade_frontalface_default.xml"
        self.font=cv2.FONT_HERSHEY_SIMPLEX
        self.color = (255,0,0)
        self.device=0
        #self.device="face_test.mp4"
    def readCSV(self):
        self.names={}
        print("Reading CSV File...")
        if os.path.exists(self.csvpath):
            self.f=open(self.csvpath,mode='r')
        else:
            print("CSV NO FOUND!")
            print("Please Create a CSV File! You can sse train.py file")
            print("Terminating...")
            exit()           
        with self.f as csv_file:
            self.csv_reader=csv.reader(csv_file,delimiter=',')
            for row in self.csv_reader:
                if len(row) == 0:
                    continue
                if row[1] == ' ':
                    row[1]='Noname'
                self.names[str(row[0])]=str(row[1])
        self.f.close()
        print("Read Csv File!")
        return self.names
    def print_utf8_text(self,image,xy,text,color):
        fontName='FreeSerif.ttf'
        font=ImageFont.load_default()
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)
        draw.text((xy[0],xy[1]),text,font=font,
                fill=(color[0],color[1],color[2],0))
        image = np.array(img_pil)
        return image
    def main(self):
        self.kontrol =0
        self.recognizer.read('Train/train.yml')
        faceCascade = cv2.CascadeClassifier(self.cascadePath)
        id = 0
        names = self.readCSV()
        cam = cv2.VideoCapture(self.device)
        cam.set(3,1000)
        cam.set(4,800)
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)
        while(True):
            ret,img=cam.read()
            if not ret:
                cam=cv2.VideoCapture(self.device)
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
                id,uyum = self.recognizer.predict(gray[y:y+h, x:x+w])
                if(uyum<70):      
                    ad=id
                    id = names[str(id)]
                    uyum=f"Uyum Oranı: {round(uyum,0)}%"
                    print(f"\n Name: {id} {uyum}")
                    img=self.print_utf8_text(img,(x+5,y-25),str(id),self.color)
                    time.sleep(0.03)
                    self.kontrol=1
                    cv2.imwrite("../controlFace/set"+str(ad)+".jpg",img)
                    #cv2.putText(img,str(uyum),(x+5,y+h+25),font,1,(0,255,0),1)
            if self.kontrol==1:
                return id,ad
            cv2.imshow("Frame",img)
            k=cv2.waitKey(10 & 0xff)
            if k==27 or k==ord('q'):
                id = -1
                ad = -1
                print("\n [INFO]: Memory Clearing!")
                print("[INFO]: Program Terminating...")
                cam.release()
                cv2.destroyAllWindows()    
                return id,ad
