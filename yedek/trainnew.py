#--------------------------------------------------------------------------------------------------------------------#
                            # Kütüphaneler #
import cv2,os,csv
import numpy as np
from PIL import Image

#--------------------------------------------------------------------------------------------------------------------#
                            # Global Değişkenler #
path='dataFace'
csvName="dataFace/dataBase.csv"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')


#--------------------------------------------------------------------------------------------------------------------#
                            # Fonksiyonlar #
def addCsv(ids):
    if os.path.exists(csvName):
        f=open(csvName,mode='w')
    else :
        f=open(csvName,mode='x')
    with f as new_file:
        writer=csv.writer(new_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONE)
        for id in ids:
            writer.writerow([id,f'ID: {id}'])
    f.close()

def getImagesAndLabels(path):  
    dirPath = [os.path.join(path,f) for f in os.listdir(path)]
    ornekler=[]
    ids=[]
    for dir in dirPath:         
        if os.path.isfile(dir):
            break
        imagepaths=[os.path.join(dir,f) for f in os.listdir(dir)]
        id=int(os.path.split(dir)[-1].split(".")[0])
        for imagepath in imagepaths:
            PIL_img = Image.open(imagepath).convert('L')
            img_numpy = np.array(PIL_img,'uint8')
            faces= detector.detectMultiScale(img_numpy)
            for(x,y,w,h) in faces:
                ornekler.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
    return ornekler,ids

#--------------------------------------------------------------------------------------------------------------------#
                            # Main Fonksiyon #
if __name__ =="__main__":
    print("\n [INFO]: Faces are being trained. Wait a few seconds...")
    faces,ids=getImagesAndLabels(path)
    recognizer.train(faces,np.array(ids))
    recognizer.write('Train/train.yml')
    print(f"\n[INFO]: {len(np.unique(ids))} face trained. Add to Csv...")
    csvid=[]
    for no in ids:
        if not (no in csvid):
            csvid.append(no)
    addCsv(csvid)
    print(f"\n[INFO]: {len(csvid)} Added to Csv File. Terminating...")
    print("--------------")
    print(csvid)
    print("--------------")

#--------------------------------------------------------------------------------------------------------------------#
                            # End #