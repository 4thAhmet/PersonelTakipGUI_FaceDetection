from deepface import DeepFace
import cv2,os,sys

class deepFace:
    def __init__(self):
        super().__init__()
        self.path="dataFace"
        self.pathlist=[os.path.join(self.path,f) for f in os.listdir(self.path)]
    def RundeepFace(self,id):
        newpath="controlFace/set"+str(id)
        self.path=self.path+"/"+str(id)
        self.pathlist=[os.path.join(self.path,f) for f in os.listdir(self.path)]
        self.pathlistnew=[os.path.join(newpath,f) for f in os.listdir(newpath)]
        for p in self.pathlist:
            for p1 in self.pathlistnew:
                result=DeepFace.verify(img1_path=p,img2_path=p1)
                print(result['verified'],"\n")
