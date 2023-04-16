from deepface import DeepFace
import cv2,os,sys

path=sys.argv[1]
pathlist=[os.path.join(path,f) for f in os.listdir(path)]
for p in pathlist:
    result=DeepFace.verify(img1_path='controlFace/0.jpg',img2_path=p)
    print(p," icin Sonuc: ",result['verified'],"\n")
