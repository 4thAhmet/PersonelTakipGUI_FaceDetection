#--------------------------------------------------------------------------------------------------------------------#
                            #                #
import cv2,os
import numpy as np
from PIL import Image


class TrainModel:
    def __init__(self):
        super().__init__()    
        self.recognizer=cv2.face.LBPHFaceRecognizer_create()
        self.detector=cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

    def getImagesAndLabels(self,path):
        self.dirPath = [os.path.join(path,f) for f in os.listdir(path)]
        self.ornekler=[]
        self.ids=[]
        for dir in self.dirPath:  
            if os.path.isfile(dir):
                break
            imagepaths=[os.path.join(dir,f) for f in os.listdir(dir)]
            id=int(os.path.split(dir)[-1].split(".")[0])
            for imagepath in imagepaths:
                PIL_img = Image.open(imagepath).convert('L')
                img_numpy = np.array(PIL_img,'uint8')
                faces= self.detector.detectMultiScale(img_numpy)
                for(x,y,w,h) in faces:
                    self.ornekler.append(img_numpy[y:y+h,x:x+w])
                    self.ids.append(id)
        return self.ornekler,self.ids
    
    def main(self):
        self.path='dataFace'
        print("\n [INFO]: Faces are being trained. Wait a few seconds...")
        self.faces,self.ids=self.getImagesAndLabels(self.path)
        self.recognizer.train(self.faces,np.array(self.ids))
        self.recognizer.write('Train/train.yml')
        print(f"\n[INFO]: {len(np.unique(self.ids))} face trained.")

#--------------------------------------------------------------------------------------------------------------------#
                            # End #