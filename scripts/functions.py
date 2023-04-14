import os,csv

# Kayıtlı kullanıcı sayısını bulan fonksiyon#
def KullaniciSay():
        count=0
        csvpath="dataFace/dataBase.csv"
        if os.path.exists(csvpath):
            f=open(csvpath,mode='r')
        else:
            return -1
        with f as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if len(row) == 0:
                    continue
                count+=1
        f.close()
        return count

#Kayıtlı kullanıcıların id ve numarasını dizi olarak geri döndüren fonksiyon#
def Kliste():
        klistid=[]
        klistname=[]
        csvpath="dataFace/dataBase.csv"
        if os.path.exists(csvpath):
            f=open(csvpath,mode='r')
        else:
            return klistid,klistname
        with f as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                if len(row) == 0:
                    continue
                else:
                    klistid.append(row[0])
                    klistname.append(row[1])
        f.close()
        return klistid,klistname


def calistir(self):
    os.system("python Face_Detect.py")
    